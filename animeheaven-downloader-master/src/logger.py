from datetime import datetime
import os

from . import config


class Logger:
    __LOG_PATH = config.LOG_PATH


    def __init__(self, verbose=True):
        self.__verbose = verbose
        self.__logs = self.__exists( self.__LOG_PATH )
        self.__today = datetime.today()

    def info(self, msg:str):
        self.__log(msg, 'Info')

    def error(self, msg:str):
        self.__log(msg, 'Error')

    
    def __log(self, msg:str, msg_type:str):
        log = self.__get_logfile()
        now = datetime.today().strftime('%d-%m-%Y %H:%M:%S %p')

        with open(log, 'a') as logger:
            msg = f'[{now} : {msg_type:5}] {msg}'
            # show in terminal if verbose
            if self.__verbose:
                print(msg)
            logger.writelines(msg + '\n')

    def __get_logfile(self) -> str:
        # group logs by current day
        log = self.__today.strftime('%d-%m-%Y.log')
        return f'{self.__logs}/{log}'

    def __exists(self, directory:str) -> str:
        if not os.path.isdir(directory):
            os.makedirs(directory)
        return f'{os.path.dirname( os.path.abspath(directory) )}/{directory.split("/")[-1]}'
