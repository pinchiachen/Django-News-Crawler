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

本程式資料庫預設使用 Heroku 上的 PostgreSQL，在你的 Heroku 專案安裝好 PostgreSQL 後，進入你的 PostgreSQL 頁面 Settings 裡面點選 View Credentials 按鈕，將裡面各種參數填入 settings.py 裡的 DATABASE 區塊。

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

也可以使用自動抓取環境變數的方式如下，但此方式無法在本地端使用。

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}
```

> 在本地運行

- 手動執行 crawler.py，將爬取下來的資料存入資料庫以供前端頁面使用，並執行專案即可。

> 在 Heroku 上運行

- 將程式碼部屬成功後，記得手動啟動 worker，爬蟲檔才會自動執行。

