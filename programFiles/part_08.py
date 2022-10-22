import logging
import logging.config
import yaml

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

logger.warning("This is a warning message")
logger.debug("This is a debug message")
logger.error("This is a error message")