import inspect
import logging


class Baseclass:
    def getlogger(self):
        loggername=inspect.stack()[1][3] # this will give the file name where this method used by that file
        logger=logging.getLogger(loggername) # here we taking object of log and  in argument it passed the file name for the file which generate the log
        fileHandler=logging.FileHandler('Logfile.log') # here we doing the log file where all logs will generate
        formatter=logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
        #logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG) # sets the priority level of log

        return logger