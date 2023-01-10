import inspect
import logging

import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]

        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('C:/Users/niran/PycharmProjects/python_Coursera/com_CE_Report/logfile.log')

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.INFO)

        #logger.debug("A debug statment is executed")
        #logger.info("Information statement")
        #logger.warning("something is in warning mode")
        #logger.error("A major error has happening")
        #logger.critical("critical issue")
        return logger

