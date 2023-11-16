import os

class Config:
    # Secret key for securing sessions and other cryptographic functions
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key'

    # Database configuration
    DATABASE_HOST = 'y5svr1t2r5xudqeq.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
    DATABASE_USER = 'xkwo0puwn8wpp11p'
    DATABASE_PASSWORD = 'mfbjl6adjf3btrxg'
    DATABASE_NAME = 'lxm14898h1ry2khd'
    DATABASE_PORT = 3306

    # Other application-specific configuration settings
    DEBUG = False
