import logging
import datetime
import os

class Logger():
    def __init__(self, path):
        self.logger = logging.getLogger()

        if not self.check_file_path(path):
            f = open(path, 'w')
            f.close()
        #     pyrm.directory.create_directory(os.path.abspath(os.path.dirname(logger_config['log_file'])))

        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s %(levelname)s in \'%(module)s\' at line %(lineno)d: %(message)s',
                                           '%Y-%m-%d %H:%M:%S')
        self.fh = logging.FileHandler(path)
        self.fh.setLevel(logging.DEBUG)
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)

        self.logger.addHandler(ch)
        self.logger.debug('This is a test log message.')

    def check_file_path(self, path):
        # if the file is already not existing for the delete function or the file exists for restore
        if os.path.exists(path):
            return True
        else:
            return False
