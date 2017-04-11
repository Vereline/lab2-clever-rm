#! usr/bin/env python
# -*- coding: utf-8 -*-


from argparse import *
import shutil         #Contains functions for operating files
import os         #imports the os


class Trash():
    def __init__(self, path):
        self.path = path

    def delete_automatically(self):
        # delete the whole trash
        return None

    def delete_manually(self, path):
        # delete one file manually
        return None

    def clean_trash(self):
        return None

    def watch_trash(self):
        return None
        # file_list = json.load(open(self.trash_log_path, 'r'))
        # if not file_list:
        #     print 'trash bucket is empty'
        # else:
        #     for item in file_list:  # check this
        #         print item['name']  # check this
        #         # file_list = os.listdir(self.trash_path)

    def restore_trash_automatically(self):
        # restore the the whole trash
        return None

    def restore_trash_manually(self, path):
        # restore one file in the trash
        return None

    def check_politics(self):
        # config = json.load(open('CleverRm/Configure.json', 'r'))
        # politics = config['politics']
        if politics == 'time':
            print 'time'
        elif politics == 'size':
            print 'size'
        elif politics == 'combined':
            print 'combined'
