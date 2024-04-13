import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mySecretKey'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
