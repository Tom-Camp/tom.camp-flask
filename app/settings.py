import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key-please-change")
FLASK_DEBUG = os.environ.get("DEBUG", True)
