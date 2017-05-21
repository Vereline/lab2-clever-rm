#! usr/bin/env python
# -*- coding: utf-8 -*-

import shutil  #  Contains functions for operating files
import os  # imports the os
import json
import Logwriter
import ExeptionListener
import re


class SmartRm(object):
    def __init__(self, path):
        self.trash_path = path
        self.exception_listener = ExeptionListener.ExceptionListener
        # self.config = json.load(open('SmartRm/Configure.json', 'r'))
        # self.trash_path = self.config['path']
        # self.trash_log_path = self.config['trash_log_path']
        # self.logwriter = Logwriter.Logwriter(self.trash_log_path)

    # def remove_by_regular(self, path, dryrun):
    #     regular_arr = self.search_all_by_regular()
    #     for item in regular_arr:
    #         self.remove_to_trash_file(item, dryrun)
    #     pass
    #
    # def search_all_by_regular(self, path):
    #     pass

    def remove_to_trash_file(self, path, dry_run):  # works

        try:
            if not dry_run:
                # head, tail = os.path.split(path)
                # new_path = os.path.join(self.trash_path, tail)
                shutil.move(path, self.trash_path)
                # return new_path
            else:
                print 'remove file'
        except:
            self.exception_listener.check_capacity()
            # self.exeption_listener.check_cycles()
            # self.exeption_listener.check_if_conflict()
            # self.exeption_listener.check_is_system_directory()
            # self.exeption_listener.check_size()
            #print 'something is going wrong'
    #
    # def remove_to_trash_directory(self, path):
    #     #  print 'trying to move file'
    #     try:
    #         shutil.move(path, self.trash_path)
    #         print 'succeed'
    #     except:
    #         print 'something is going wrong'
    #
    # def remove_directly(self, path):
    #     return None
