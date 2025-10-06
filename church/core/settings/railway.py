import os
import dj_database_url
from .base import *
from datetime import timedelta

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 'django-insecure-railway-default-key-change-me')

DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# Database configuration with proper fallback
PGHOST = os.environ.get('PGHOST')
PGPORT = os.environ.get('PGPORT', '5432')
PGDATABASE = os.environ.get('PGDATABASE')
PGUSER = os.environ.get('PGUSER')
PGPASSWORD = os.environ.get('PGPASSWORD')

# Database Configuration
if all([PGHOST, PGDATABASE, PGUSER, PGPASSWORD]):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': PGDATABASE,
            'USER': PGUSER,
            'PASSWORD': PGPASSWORD,
            'HOST': PGHOST,
            'PORT': PGPORT,
            'CONN_MAX_AGE': 600,
            'OPTIONS': {
                'connect_timeout': 10,
            }
        }
    }
else:
    raise Exception(
        f"Database variables missing! PGHOST={PGHOST}, PGDATABASE={PGDATABASE}")

# Redis Cache
REDIS_URL = os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379')
if REDIS_URL:
    CACHES['default']['LOCATION'] = REDIS_URL

# Static files configuration
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# WhiteNoise for static files - IMPORTANT for serving Swagger UI
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# CORS - Allow all for testing (restrict in production)
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# Security Settings (only in production)
if not DEBUG:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Restrict CORS in production
    cors_origins = os.environ.get('CORS_ALLOWED_ORIGINS', '')
    if cors_origins:
        CORS_ALLOWED_ORIGINS = cors_origins.split(',')
        CORS_ALLOW_ALL_ORIGINS = False
else:
    # Development - still need proxy header for Railway
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'SIGNING_KEY': SECRET_KEY,
}

# Spectacular settings override for Railway
# At the end of railway.py
SPECTACULAR_SETTINGS.update({
    'SWAGGER_UI_DIST': 'https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0',
    'SWAGGER_UI_FAVICON_HREF': 'https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/favicon-32x32.png',
    'REDOC_DIST': 'https://cdn.jsdelivr.net/npm/redoc@2.1.3/bundles',
})
