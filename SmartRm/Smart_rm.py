#! usr/bin/env python
# -*- coding: utf-8 -*-

import shutil  #  Contains functions for operating files
import os  # imports the os
import json
import Logwriter
import ExeptionListener
import re


class SmartRm():
    def __init__(self, path):
        self.trash_path = path
        self.exeption_listener = ExeptionListener.ExceptionListener
        # self.config = json.load(open('SmartRm/Configure.json', 'r'))
        # self.trash_path = self.config['path']
        # self.trash_log_path = self.config['trash_log_path']
        # self.logwriter = Logwriter.Logwriter(self.trash_log_path)

    def remove_by_regular(self, path, dryrun):
        regular_arr = self.search_all_by_regular()
        for item in regular_arr:
            self.remove_to_trash_file(item, dryrun)
        pass

    def search_all_by_regular(self, path):
        pass

    def remove_to_trash_file(self, path, dryrun):
        #  print 'trying to move file'
        try:
            if dryrun == False:
                 shutil.move(path, self.trash_path)
            else:
                print 'remove file'
        #     if '*' or '?' in path:
        #        self.remove_by_regular(path)
            #print 'succeed'
        except:
            self.exeption_listener.check_capacity()
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
