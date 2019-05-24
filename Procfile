release: python nba_news/manage.py migrate
web: gunicorn --pythonpath nba_news nba_news.wsgi
worker python nba_news/crawler/nba_crawler.py
