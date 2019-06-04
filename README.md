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

本程式資料庫預設使用Heroku上的PostgreSQL，申請完後記得將你的PostgreSQL頁面setting裡面點選
View Credentials按鈕，將裡面各種參數填入settings.py裡的DATABASE區塊

'''
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
'''
