import os

REGION = os.environ['REGION']
CHEF_SERVER_URL = os.environ['CHEF_SERVER_URL']
USERNAME = os.environ['USERNAME']
VERIFY_SSL = os.environ['VERIFY_SSL'] == '1'
DEBUG = os.environ['DEBUG'] == '1'
