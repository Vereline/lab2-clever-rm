#! usr/bin/env python
# -*- coding: utf-8 -*-

import shutil  #  Contains functions for operating files
import os  # imports the os
import json


def remove_to_trash(path):
    print 'trying to move file'

    try:
        config = json.load(open('CleverRm/Configure.json', 'r'))
        trash_path = config['path']

        shutil.move(path, trash_path)
        print 'succeed'
    except:
        print 'something is going wrong'


def remove_directly(path):
    return None


def clean_trash():
    return None


def watch_trash():
    config = json.load(open('CleverRm/Configure.json', 'r'))
    trash_path = config['path']

    file_list = os.listdir(trash_path)
    if not file_list:
        print 'trash bucket is empty'
    else:
        for item in file_list:
            print item


def restore_trash(path):
    return None


def check_politics(path):
    config = json.load(open('CleverRm/Configure.json', 'r'))
    politics = config['politics']

    if politics == 'time':
        print 'time'
    elif politics == 'size':
        print 'size'
    elif politics == 'combined':
        print 'combined'
