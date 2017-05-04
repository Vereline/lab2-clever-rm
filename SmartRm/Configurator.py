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
        self.dry_run = False
        self.silent = False
        self.configure = {}  # сделать конфигурации на 1 раз, если передан параметр


    # def configure_arguments(self, dict):
    #     if dict[0] == '-smrm' or dict[0] == '-smrmr':
    #         self.define_removal()
    #     elif dict[0] == '-smcc':
    #         self.define_change_configure()
    #     elif dict[0] == '-smcc':
    #         self.define_change_configure()
    #         # ...
    #     pass
    #
    # def define_dry_run(self):
    #     pass
    #
    # def define_removal(self):
    #     pass
    #
    # def define_restore(self):
    #     pass
    #
    # def define_watch_trash(self):
    #     pass
    #
    # def define_change_configure(self):
    #     pass
