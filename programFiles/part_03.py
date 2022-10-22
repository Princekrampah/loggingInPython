import logging

# using writing log to a file

logging.basicConfig(format="""Severity Level: %(levelname)s
Message: %(message)s 
Time executed: %(asctime)s
Log created at: %(created)f
On line: %(lineno)d 
Process Name: %(processName)s
Thread: %(thread)d
Thread Name: %(threadName)s \n\n""", 
                    datefmt='%y-%d-%b at %H:%M:%S', filename="log_info.log", filemode="w")


# filename = The file to write to
# filemode = The mode in which to open the file a => append mode(default mode)
# format = The format of the message
logging.warning("This is a warning log to a file")