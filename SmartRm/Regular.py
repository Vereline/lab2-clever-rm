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


# is not need
class Regular(object):
    def __init__(self, dict):
        self.dry_run = False
        self.silent = False
        self.configure = {}  # сделать конфигурации на 1 раз, если передан параметр
