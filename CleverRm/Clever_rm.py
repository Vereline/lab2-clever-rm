#! usr/bin/env python
# -*- coding: utf-8 -*-

import shutil  #  Contains functions for operating files
import os  # imports the os
import json
import Logwriter


class Clever_rm():
    def __init__(self):
        self.config = json.load(open('CleverRm/Configure.json', 'r'))
        self.trash_path = self.config['path']
        self.trash_log_path = self.config['trash_log_path']
        self.logwriter = Logwriter.Logwriter(self.trash_log_path)

    # def remove_to_trash_file(self, path):
    #     #  print 'trying to move file'
    #     try:
    #         shutil.move(path, self.trash_path)
    #         log_writer = Logwriter.Logwriter(self.trash_log_path)
    #
    #         print 'succeed'
    #     except:
    #         print 'something is going wrong'
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


