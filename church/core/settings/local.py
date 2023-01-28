import dj_database_url
from .base import *
from dotenv import load_dotenv
from datetime import timedelta
from decouple import config


load_dotenv()


SECRET_KEY="django-insecure-i3518xh534trgj8z%dbs+jnxi)s=y-xe75q7im1iil$3!u0$v^"
DEBUG = True

ALLOWED_HOSTS = ["*"]


os.getenv
# SECURITY WARNING: don't run with debug turned on in production!

if DEBUG:
    import os  # only if you haven't already imported this
    import socket  # only if you haven't already imported this

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + '1' for ip in ips] + ['127.0.0.1', '10.0.2.2']

os.getenv('GOOGLE_SERVICE_ACCOUNT')

DATABASES = {
    "default": dj_database_url.config(default=config('DATABASE_URL'))
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'SIGNING_KEY': os.getenv("SECRET_KEY"),

}
