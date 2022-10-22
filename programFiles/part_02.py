import logging

# using basicConfig

# how to configure the logging: The basicConfig() is called each time the program
# runs: 

#### 1. formatting the output 

# logging.basicConfig()
# logging.warning("Warning message")

#### 2. formatting the output format

# logging.basicConfig(format="%(name)s - %(message)s - %(levelname)s")
# logging.warning("Warning message")

# logging.basicConfig(format="%(process)d - %(message)s - %(levelname)s")
# logging.warning("Warning message")

# logging.basicConfig(format="%(asctime)s - %(message)s - %(levelname)s")
# logging.warning("Warning message")

# logging.basicConfig(format="%(asctime)s - %(message)s - %(levelname)s", datefmt='%y-%d-%b at %H:%M:%S')
# logging.warning("Warning message")

logging.basicConfig(format="""
Severity Level: %(levelname)s
Message: %(message)s 
Time executed: %(asctime)s
Log created at: %(created)f
On line: %(lineno)d 
Process Name: %(processName)s
Thread: %(thread)d
Thread Name: %(threadName)s""", 
                    datefmt='%y-%d-%b at %H:%M:%S')
logging.warning("Warning message")

# logging.basicConfig(level=logging.INFO)
# logging.info("Info log")





