import os

class Config:
    # Secret key for securing sessions and other cryptographic functions
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key'

    # Database configuration
    DATABASE_HOST = 'localhost'
    DATABASE_USER = 'root'
    DATABASE_PASSWORD = ''
    DATABASE_NAME = 'elako_db'
    DATABASE_PORT = 3308

    # Other application-specific configuration settings
    DEBUG = False
