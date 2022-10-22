from cgitb import handler
import logging

# handlers can be configured to send messages to a variaty of places
# from files to http or email addresses

# You can also create more than one handler in your code and have
# it send data to more than just a single location


# here is a program that create two handlers, one for handling erros and the
# for warnings

# create a custome logger object
logger = logging.getLogger(__name__)


# create handlers
s_handler = logging.StreamHandler()
f_handler = logging.FileHandler("handler_logs.log")

# set levels for handlers
s_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# create handler formatters
s_format = logging.Formatter("%(name)s - %(message)s - %(levelname)s")
f_format = logging.Formatter("%(name)s - %(message)s - %(levelname)s - %(asctime)s - %(lineno)d")

# set the formatters values
s_handler.setFormatter(s_format)
f_handler.setFormatter(f_format)

# add the handler to the logger
logger.addHandler(s_handler)
logger.addHandler(f_handler)


# log some info
logger.error("This is an error message")
logger.warning("This is a warning message")
