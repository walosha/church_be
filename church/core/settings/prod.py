import os
import dj_database_url
from .base import *
from dotenv import load_dotenv
from datetime import timedelta
from decouple import config

load_dotenv()


SECRET_KEY = "9jsgjkww9982827272i3518xh534trgj8z%dbs+jnxi)s=y-xe75q7im1iil$3!u0$v^"


DEBUG = True


ADMINS = [
    ('Olawae Afuye', 'hello@pacific-professional.com.ng'),
]


ALLOWED_HOSTS = [
    "*"
]


INTERNAL_IPS = ["127.0.0.1"]

REDIS_URL = config("REDIS_URL", default="redis://127.0.0.1:6379")
CACHES['default']['LOCATION'] = REDIS_URL
# CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]


USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_ALL_ORIGINS = True


DATABASES = {
    "default": dj_database_url.parse(
        config("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=False
    )
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'SIGNING_KEY': os.getenv("SECRET_KEY"),

}


# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
