#! usr/bin/env python
# -*- coding: utf-8 -*-

import shutil  #  Contains functions for operating files
import os  # imports the os
import json

class Clever_rm():
    def __init__(self):
        self.config = json.load(open('CleverRm/Configure.json', 'r'))
        self.trash_path = self.config['path']

    def remove_to_trash_file(self, path):
        #  print 'trying to move file'
        try:
            shutil.move(path, self.trash_path)
            print 'succeed'
        except:
            print 'something is going wrong'

    def remove_to_trash_directory(self, path):
        #  print 'trying to move file'
        try:
            shutil.move(path, self.trash_path)
            print 'succeed'
        except:
            print 'something is going wrong'

    def remove_directly(self, path):
        return None

    def clean_trash(self):
        return None

    def watch_trash(self):
        file_list = os.listdir(self.trash_path)
        if not file_list:
            print 'trash bucket is empty'
        else:
            for item in file_list:
                print item

    def restore_trash(path):
        return None

    def check_politics(path):
        config = json.load(open('CleverRm/Configure.json', 'r'))
        # politics = config['politics']
        #
        # if politics == 'time':
        #     print 'time'
        # elif politics == 'size':
        #     print 'size'
        # elif politics == 'combined':
        #     print 'combined'
