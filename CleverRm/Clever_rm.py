#! usr/bin/env python
# -*- coding: utf-8 -*-

import shutil         #Contains functions for operating files
import os         #imports the os



def SimpleMove(path):
    print("trying to move file")
    try:
        path2 = unicode('~/Рабочий стол/Python projects/lab2/CleverRm/testbucket/', 'utf-8') # move this thing to confg file
        shutil.move(path, path2)
        print('succeed')
    except:
        print ('something is going wrong')

