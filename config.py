import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    HOST = os.environ.get('HOST')
    PORT = os.environ.get('PORT')
    DEBUG = True if os.environ.get('FLASK_ENV') == 'development' else False
