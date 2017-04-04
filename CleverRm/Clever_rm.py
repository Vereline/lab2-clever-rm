#! usr/bin/env python
# -*- coding: utf-8 -*-

import shutil  #  Contains functions for operating files
import os  # imports the os


def simple_move(path):
    print("trying to move file")
    try:
        path2 = unicode('testbucket')  # move this thing to confg file
        shutil.move(path, path2)
        print('succeed')
    except:
        s = os.path.abspath(os.curdir)
        print s
        print os.getcwd()
        print os.listdir(os.curdir)
        print os.listdir(os.getcwd())
        print ('something is going wrong')


def watch_trash():
    path = unicode('testbucket')
    filelist = os.listdir(path)
    if not filelist:
        print 'the trash bucket is empty'
    else:
        for item in filelist:
            print item

