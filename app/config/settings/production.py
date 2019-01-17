from .base import *

DEBUG = False

production_secrets = json.load(open(os.path.join(SECRET_ROOT, 'production.json')))
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = production_secrets['DATABASES']

DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'

AWS_ACCESS_KEY_ID = production_secrets['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = production_secrets['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = production_secrets['AWS_STORAGE_BUCKET_NAME']
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'

ALLOWED_HOSTS = [
    '.elasticbeanstalk.com',
    'monglab.com',
    'www.monglab.com',
    'api.monglab.com',
    'localhost',
]

# Log

LOG_DIR = os.path.join(ROOT_DIR, '.log')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)

LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(levelname)s] %(name)s (%(asctime)s)\n\t%(message)s'
        },
    },
    'handlers': {
        'file_error': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'formatter': 'default',
            'maxBytes': 1048576,
            'backupCount': 10,
        },
        'file_info': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'filename': os.path.join(LOG_DIR, 'info.log'),
            'formatter': 'default',
            'maxBytes': 1048576,
            'backupCount': 10,
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file_error', 'file_info', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
