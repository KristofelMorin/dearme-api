"""Flask configuration variables."""
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

class Config(object):
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = os.environ.get("SECRET_KEY")
    FLASK_APP = os.environ.get("FLASK_APP")
    FLASK_ENV = os.environ.get("FLASK_ENV")

     
    basedir = os.path.abspath(os.path.dirname(__file__))
    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    SQLALCHEMY_ECHO= False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
