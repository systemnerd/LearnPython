import logging

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s:%(message)s',
                    filename='logs.txt')
logger = logging.getLogger(__name__)

logger.info("This is an INFO message")
logger.warning("Warning message")
logger.warning("Another message")
