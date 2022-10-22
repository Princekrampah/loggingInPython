import logging


info_log = logging.info("Info log")
warning_log = logging.warning("Warning log")
error_log = logging.error("Error log")
debug_log = logging.debug("Debug log")
critical_log = logging.critical("Critical log")


# output format is 
# severity_level : root : message
# the root is the default logger(later on we'll log at it)
# this format can be modified to include line number of the code
# and timestamps

# th info and debug does will not get logged since, the logger
# only logs messages with severity of warning and above
