import logging


def test_loggingDemo():
    # Creating an object
    # __name__ capturing file name
    logger = logging.getLogger(__name__)

    # File location
    fileHandler = logging.FileHandler("logfile.log")
    # Format
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

    # Conection with fileHandler
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler) # filehandler object

    # Determining at which level we want to show our log information
    logger.setLevel(logging.CRITICAL)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    # para señalar la situación pero que no falle la ejecución
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happen")
    logger.critical("Critical issue")