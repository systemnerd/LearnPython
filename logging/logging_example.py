import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(message)s')
logger = logging.getLogger('test_logger')

logger.info("This is an INFO message")
logger.warning("Warning message")
