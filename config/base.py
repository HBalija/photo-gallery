# flake8: noqa
from .env import ENV_BOOL, ENV_STR, ABS_PATH

DEBUG = ENV_BOOL('DEBUG', False)
SECRET_KEY = ENV_STR('SECRET_KEY')
