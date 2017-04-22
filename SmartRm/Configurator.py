# обрабатывать тут все аргументы(кроме i , v, f)

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


class Configurator():
    def __init__(self, dict):
        if dict.get('i') != None:
            dict = {'key': 'r'}
        file_list = []
        file_path = None
        self.dict = dict

    def configure_arguments(self, dict):
        pass

    def define_dry_run(self):
        pass

    def define_removal(self):
        pass

    def define_restore(self):
        pass

    def define_watch_trash(self):
        pass

    def define_change_configure(self):
        pass
