import dj_database_url
from .base import *
from dotenv import load_dotenv
from datetime import timedelta
from decouple import config

load_dotenv()

SECRET_KEY="django-insecure-i3518xh534trgj8z%dbs+jnxi)s=y-xe75q7im1iil$3!u0$v^"


DEBUG = False


ADMINS = [
('Olawae Afuye', 'hello@pacific-professional.com.ng'),
]


ALLOWED_HOSTS = ["*"]


INTERNAL_IPS = ["127.0.0.1",
                'chrome-extension://fhbjgbiflinjbdggehcddcbncdddomop']




USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_ALL_ORIGINS = True

               

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "pg1",  # set in docker-compose.yml
        "PORT": 5432,  # default postgres port
    }
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'SIGNING_KEY': os.getenv("SECRET_KEY"),

}
