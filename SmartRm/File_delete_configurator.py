#! usr/bin/env python
# -*- coding: utf-8 -*-

import json
import argparse
from argparse import *
import Smart_rm
import shutil         #Contains functions for operating files
import os         #imports the os
import sys
import Logwriter
import Argparser
import Trash
import re
import ExeptionListener
import pprint

# тут обрабатывать декораторы dry-run + i,v,f
# redo and refactor all the code

# rename here deleted file to the id
# -i - confirm every your deletion / restore

class File_delete_configurator():
    def __init__(self, argparser, paths):
        self.argparser = argparser
        self.config = json.load(open('SmartRm/Configure.json', 'r'))
        self.trash = Trash.Trash(self.config['path'], self.config['trash_log_path'], self.config['trash_log_path_txt'], self.config['politics_time'],self.config['politics_size'], self.config['max_capacity'], self.config['max_time'])
        self.smartrm = Smart_rm.Smart_rm(self.config['path'])
        self.exit_codes = {
             'success': 0,
             'conflict': 1,
             'error': 2,
             'no_file': 3
        }
        self.dry_run = False
        self.silent = False
        self.interactive = False
        self.verbose = False
        self.force = False
        if argparser.args.interactive:  # если нету интерэктив, спрашиваем только если прав не хватает
            self.interactive = True
        if argparser.args.silent:
            self.silent = True
        if argparser.args.force:
            self.force = True
        if argparser.args.verbose:
            self.verbose = True
        if argparser.args.dryrun:
            self.dry_run = True

        self.paths = paths

    def define_action(self):
        if self.argparser.args.remove is not None:
            for item in self.paths:
                # check if this file exists
                # . . .
                self.trash.log_writer.write_file_dict(item)
                self.rename_file_name_to_id(item)
                self.smartrm.remove_to_trash_file(item, self.dry_run)

        elif self.argparser.args.remove_regular is not None:
            pass
        elif self.argparser.args.clean is not None:
            self.trash.delete_automatically()

        elif self.argparser.args.restore is not None:
            for item in self.paths:
                self.trash.restore_trash_manually(item) # проверить на правильность путей

        elif self.argparser.args.remove_from_trash is not None:
            for item in self.paths:
                self.trash.delete_manually(item) # проверить на правильность путей

        elif self.argparser.args.show_trash is not None:
            self.trash.watch_trash()

        elif self.argparser.args.show_config is not None:
            #print self.config
            pprint.pprint(self.config)

        elif self.argparser.args.change_config is not None:  # deletion with one-time configs
            pass



    def check_file_path(self, path):
        try:
        # if the file is already doesnt exist
            pass

        except:
            ExeptionListener.ExceptionListener.check_if_exists()
        # ...

    def find_all_files_by_bit_mask(self):
        pass # find all *.txt files, as example

    def find_all_files_by_regular(self):
        pass  # find all [1*].txt files, as
        

    def rename_file_name_to_id(self, path):
        id =self.trash.log_writer.get_id_path(path)
        index = 0
        for i in reversed(range(len(path))):
            if path[i] == '/':
                index = i
                break
        dirname = path[:(index+1)] + id

        os.rename(path, dirname)
        pass

    def ask_for_confirmation(self):
        answer = input("Are you sure? [y/n]\n")
        if answer == "n" or answer == "N":
            print("Operation canceled")
            sys.exit(self.exit_codes['success'])
        elif answer != "y" and answer != "n" and answer != "N" and answer != "Y":
            self.ask_for_confirmation()

    def check_access(self, path):
        if os.access(path, os.R_OK):
            return self.exit_codes['success']
        else:
            # raise system directory exception
            return self.exit_codes['error']