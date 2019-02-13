from .base import *

DEBUG = True

dev_secrets = json.load(open(os.path.join(SECRET_ROOT, 'dev.json')))

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = dev_secrets['DATABASES']

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = dev_secrets['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = dev_secrets['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = dev_secrets['AWS_STORAGE_BUCKET_NAME']


INSTALLED_APPS += [
    'django_extensions',
]