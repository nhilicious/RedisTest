import os

from dotenv import load_dotenv

load_dotenv()


class ArangoConfig:
    CONNECTION_URL = os.environ.get("ARANGO_URL")
    USERNAME = os.environ.get("ARANGO_USERNAME")
    PASSWORD = os.environ.get("ARANGO_PASSWORD")
    DATABASE = os.environ.get("ARANGO_DATABASE")