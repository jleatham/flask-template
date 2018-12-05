import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SS_ACCESS_TOKEN = os.environ.get('SMARTSHEET_TOKEN')
