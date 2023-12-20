import logging
from json import JSONDecodeError
import httpx
from databases import Database
from app.config import config

logger = logging.getLogger(__name__)


class APIResponseError(Exception):
    pass
