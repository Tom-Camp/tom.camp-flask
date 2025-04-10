import os
from distutils.util import strtobool

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key-please-change")
FLASK_DEBUG = bool(strtobool(os.environ.get("DEBUG", "true")))
