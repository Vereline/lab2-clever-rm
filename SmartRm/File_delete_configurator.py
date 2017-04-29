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
    def __init__(self, dict):
        # self.trash = Trash.Trash("add here arguments")
        # self.smartrm = Smart_rm.Smart_rm("add here arguments")
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
        if dict.get('-i') != None:
            self.interactive = True
        if dict.get('-s') != None:
            self.silent = True
        if dict.get('-f') != None:
            self.force = True
        if dict.get('-v') != None:
            self.verbose = True
        if dict.get('-d') != None:
            self.dry_run = True


        #     dict = {'key': 'r'}
        # file_list = []
        # file_path = None

        self.dict = dict

    def make_list(self):
        self.path = self.dict.get('r')
        print self.path
        # ...

    def check_file_path(self, path):

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
