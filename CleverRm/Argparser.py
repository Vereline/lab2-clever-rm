#! usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from argparse import *
import Clever_rm
import shutil         #Contains functions for operating files
import os         #imports the os
import Logwriter


# print ("must write clever -rm")
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-cleverrm', '-myrm', help='This will be option removal', action="store_true")
    parser.add_argument('path', help='a path of file or directory to remove', type=lambda s: unicode(s, 'utf-8'))

    args = parser.parse_args()
    if args.cleverrm:
        this_path = unicode(os.path.abspath(args.path))
        Logwriter.write_json_log(this_path)
        Clever_rm.simple_move(this_path)

if __name__ == '__main__':
    main()
