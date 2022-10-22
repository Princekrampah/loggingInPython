import logging

logger = logging.getLogger("code_with_prince")
logger.warning("Warining message")


# by default the logger does not show the name of the logger
# as well as the severity level.

# configuring the format
logging.basicConfig(format="%(name)s - %(message)s - %(levelname)s")

logger.warning("Warning message 2")


# common way people also create loggers is by using __name__

logger2 = logging.getLogger(__name__)

