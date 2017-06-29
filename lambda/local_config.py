import os

REGION = os.environ['REGION']
CHEF_SERVER_URL = os.environ['CHEF_SERVER_URL']
USERNAME = os.environ['USERNAME']
S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
S3_KEY_NAME = os.environ['S3_KEY_NAME']
VERIFY_SSL = 'VERIFY_SSL' in os.environ and os.environ['VERIFY_SSL'] == '1'
DEBUG = 'DEBUG' in os.environ and os.environ['DEBUG'] == '1'
