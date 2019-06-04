# Django News Crawler

This is a Django based web with crawler collecting news from nba.udn.com.

## Built With

- Python
- Django
- Django REST Framework
- Beautiful Soup
- PostgreSQL
- Bootstrap
- Schedule
- Heroku

## How To Use

本程式資料庫預設使用 Heroku 上的 PostgreSQL，申請完後記得將你的 PostgreSQL 頁面 Settings 裡面點選 View Credentials 按鈕，將裡面各種參數填入 settings.py 裡的 DATABASE 區塊。

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'YOUR_Database',
        'USER': 'YOUR_USER',
        'PASSWORD': 'YOUR_PASSWORD',
        'HOST': 'YOUR_HOST',
        'PORT': 'YOUR_PORT',

    }
}
```

>在本地運行

-手動執行 crawler.py，將爬取下來的資料存入資料庫以供前端頁面使用。

>在 Heroku 上運行

-將程式碼部屬成功後，記得手動啟動 worker，爬蟲檔才會自動執行。

