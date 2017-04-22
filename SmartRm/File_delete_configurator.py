#! usr/bin/env python
# -*- coding: utf-8 -*-

import json
import argparse
from argparse import *
import Smart_rm
import shutil         #Contains functions for operating files
import os         #imports the os
import Logwriter
import Argparser

# тут обрабатывать декораторы dry-run + i,v,f
#redo and refactor all the code

# rename here deleted file to the id

class File_delete_configurator():
    def __init__(self, dict):
        if dict.get('i') != None:
            dict = {'key': 'r'}
        file_list = []
        file_path = None
        self.dict = dict

    def make_list(self):
        self.path = self.dict.get('r')
        print self.path
        # ...

    def check_file_path(self, path):

            pass
        # ...

