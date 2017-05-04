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

# тут обрабатывать декораторы dry-run + i,v,f
# redo and refactor all the code

# rename here deleted file to the id
# -i - confirm every your deletion / restore

class File_delete_configurator():
    def __init__(self, argparser, paths):
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
        pass


    def check_file_path(self, path):
        # if the file is already doesnt exist
            pass
        # ...

    def rename_file_name_to_id(self, path):
        pass

    def ask_for_confirmation(self):
        answer = input("Are you sure? [y/n]\n")
        if answer == "n" or answer == "N":
            print("Operation canceled")
            sys.exit(self.exit_codes['success'])
        elif answer != "y" and answer != "n" and answer != "N" and answer != "Y":
            self.ask_for_confirmation()
