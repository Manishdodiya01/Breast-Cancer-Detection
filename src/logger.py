# logger.py
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# exception.py
class MLProjectException(Exception):
    pass
