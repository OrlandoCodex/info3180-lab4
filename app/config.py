import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER','./uploads')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgres://').replace('postgres://', 'postgresql://lab4_user:Password1@localhost/lab4')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed)