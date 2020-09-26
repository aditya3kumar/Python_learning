import pytest
import logging

def test_loggingdemo():
    logger=logging.getLogger(__name__) # here we taking object of log and  in argument it passed the file name for the file which generate the log
    fileHandler=logging.FileHandler('logfile1.log') # here we doing the log file where all logs will generate
    formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    #logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler.setFormatter(formatter) #sets the format in filehandler
    logger.addHandler(fileHandler) #create filehandler object
    logger.setLevel(logging.DEBUG) # sets the priority level of log

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

    return logger
