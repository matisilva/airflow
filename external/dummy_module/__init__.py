import logging
import time
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def dummy_function(argument):
    """
    Example function that will be performed in a virtual environment.
    """
    for _ in range(len(argument)):
        logger.debug(argument)
    logger.info("Sleeping")
    time.sleep(int(2))
    logger.info("Done")
    return argument