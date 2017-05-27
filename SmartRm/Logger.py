import logging
import datetime
import os

class Logger():
    def __init__(self, path, silent):
        self.logger = logging.getLogger()

        if not check_file_path(path):
            f = open(path, 'w')
            f.close()
        #     pyrm.directory.create_directory(os.path.abspath(os.path.dirname(logger_config['log_file'])))

        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(levelname)s in \'%(module)s\' at line %(lineno)d: %(message)s',
                                      '%Y-%m-%d %H:%M:%S')
        fh = logging.FileHandler(path)
        fh.setLevel(logging.DEBUG)

        # if silent:
        #     self.fh.setLevel(logging.ERROR)

        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

        if silent:
            self.logger.setLevel(logging.ERROR)  # shows only error
            # self.logger.setLevel(logging.DEBUG)  # shows info and debug and error
            # ch.setLevel(logging.ERROR)

        logging.debug('This is a test log message.')


def check_file_path(path):
    # if the file is already not existing for the delete function or the file exists for restore
    if os.path.exists(path):
        return True
    else:
        return False
