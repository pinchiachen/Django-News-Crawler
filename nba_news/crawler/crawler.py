import os
import sys

from django.core.wsgi import get_wsgi_application

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nba_news.settings')
sys.path.append(PROJECT_DIR)

application = get_wsgi_application()

import time
import schedule
from news.models import *
import requests
from bs4 import BeautifulSoup



def news_crawler(pages: int = 10):
    print('-----Crawler Start-----')

    url_base = 'https://nba.udn.com'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}

    # 從焦點新聞首頁抓取詳細新聞頁面的URL，預設抓取10頁
    page_detail_url = []
    for i in range(pages):
        res = requests.get(url = 'https://nba.udn.com/nba/cate/6754/-1/newest/%d'%(i+1), headers = headers)
        soup = BeautifulSoup(res.text, features='lxml')
        news_list_body = soup.find(id = 'news_list_body')
        for ele in news_list_body.find_all('a'):
            page_detail_url.append(url_base + ele.get('href'))

    # 抓取詳細新聞頁面中的各項參數
    post_list = []
    for page_url in page_detail_url:

        # 新聞ID
        post_id = page_url.split('/')[-1]

        # 新聞來源URL
        post_source_url = page_url

        try:
            # 如果抓取的新聞ID已存在，則跳出此層迴圈(為了避免抓取重複新聞)
            if Post.objects.filter(id=post_id).exists():
                continue

            res = requests.get(url = page_url, headers = headers)
            soup = BeautifulSoup(res.text, features='lxml')
            story_body_content = soup.find(id = 'story_body_content')

            # 新聞標題
            post_title = story_body_content.find(class_ = 'story_art_title').text

            # 新聞發布日期
            post_date = story_body_content.find(class_ = 'shareBar__info--author').find('span').text

            # 新聞圖片
            post_image_url = story_body_content.find(class_ = 'photo_center photo-story').find('img')['data-src']

            # 新聞內文
            post_content = ''
            content = story_body_content.find_all('p')
            for ele in content[1::]:
                post_content += ele.text

            # 依表格規格建立相關資料
            post_list.append(Post(
                id = post_id,
                title = post_title,
                content = post_content,
                image_url = post_image_url,
                publish_date = post_date,
                source_url = post_source_url
            ))

            print(f'{post_id} {post_title} {post_date}')

        except Exception as e:
            print(e)
            continue

    print('-----Crawler End-----')

    # 將大量資料存入資料庫表格
    Post.objects.bulk_create(post_list)

    print('-----Data Saved Complete-----')


if __name__ == "__main__":
    news_crawler()

    print("schedule on")
    schedule.every(30).minutes.do(news_crawler)
    while True:
        print("waiting......")
        schedule.run_pending()
        time.sleep(1)






