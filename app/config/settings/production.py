from .base import *

DEBUG = False

production_secrets = json.load(open(os.path.join(SECRET_ROOT, 'production.json')))
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = production_secrets['DATABASES']

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = production_secrets['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = production_secrets['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = production_secrets['AWS_STORAGE_BUCKET_NAME']

AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'
