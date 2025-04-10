import os
import sys
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, render_template
from loguru import logger

from app.static.files.quotes import quotes

logger.remove()

logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO",
)

logger.add(
    "logs/error.log",
    rotation="10 MB",
    retention="1 week",
    level="ERROR",
    backtrace=True,
    diagnose=True,
)

logger.add("logs/app.log", rotation="100 MB", retention="10 days", level="DEBUG")


def create_app(test_config=None):
    load_dotenv()

    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile("settings.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route("/")
    def index():
        date = datetime.now().strftime("%Y")
        content: dict = {
            "date": date,
            "title": "Home",
            "quote": quotes[0],
        }
        return render_template("index.html", **content)

    return app


if __name__ == "__main__":
    app = create_app()
    environment = os.getenv("FLASK_ENV", "development")
    app.run()
