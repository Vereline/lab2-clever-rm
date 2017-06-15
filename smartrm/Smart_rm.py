#! usr/bin/env python
# -*- coding: utf-8 -*-

import shutil  #  Contains functions for operating files
import os  # imports the os
import json
import Logwriter
import ExeptionListener
import re
import Logger
import logging


class SmartRm(object):
    def __init__(self, path):
        self.trash_path = path
        self.exception_listener = ExeptionListener.ExceptionListener

    def remove_to_trash_file(self, path, dry_run, verbose):  # works
        logging.info('Remove {path}'.format(path=path))
        try:
            if not dry_run:
                # head, tail = os.path.split(path)
                # new_path = os.path.join(self.trash_path, tail)
                shutil.move(path, self.trash_path)
                # return new_path
            else:
                print 'remove file'
            if verbose:
                print path + ' removed'
        except ExeptionListener.WrongItemException as ex:
            logging.error(ex.msg)
        except Exception as ex:
            logging.error(ex.message)

