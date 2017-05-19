import logging
import datetime

class Logger():
    def __init__(self, path):
        self.logger = logging.getLogger()
        # self.logger.setLevel(logging.DEBUG)
        # self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        # self.fh = logging.FileHandler(path+'log_filename.txt')
        # self.fh.setLevel(logging.DEBUG)
        # self.fh.setFormatter(self.formatter)
        # self.logger.addHandler(self.fh)
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.DEBUG)
        # ch.setFormatter(self.formatter)
        # self.logger.addHandler(ch)
        # self.logger.debug('This is a test log message.')


    def write_message(self):
        
        pass