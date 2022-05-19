import inspect
import logging


class BaseClass:

    def getLogger(self):
        # Creating an object
        # __name__ capturing file name
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # File location
        fileHandler = logging.FileHandler("logfile.log")
        # Format
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

        # Conection with fileHandler
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        # Determining at which level we want to show our log information
        logger.setLevel(logging.INFO)
        return logger
