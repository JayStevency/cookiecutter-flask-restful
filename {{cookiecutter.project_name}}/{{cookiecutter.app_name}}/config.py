"""Default configuration

Use env var to override
"""
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True
SECRET_KEY = os.getenv('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_AS_ASCII = False

JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
