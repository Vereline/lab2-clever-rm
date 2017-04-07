#! usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
from datetime import datetime


def write_json_log(file_path):
    print 'trying to write log'
    file_dict = {}

    path = os.path.abspath(file_path)
    date = datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M:%S')
    name = os.path.split(file_path)
    file_size = os.path.getsize(file_path)

    file_dict['name'] = name[1]
    file_dict['path'] = path
    file_dict['date'] = date
    file_dict['size'] = file_size
    file_dict['name_and_path'] = os.path.split(file_path)

    filename = unicode(datetime.strftime(datetime.now(), '%Y.%m.%d'))

    json.dump(file_dict, open(filename, 'a'))
    print 'succeed'


# make restructure of this function, in order not to repeat json func
def write_txt_log(file_path):
    print 'trying to write log'
    file_dict = {}

    path = os.path.abspath(file_path)
    date = datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M:%S')
    name = os.path.split(file_path)
    file_size = os.path.getsize(file_path)

    file_dict['name'] = name[1]
    file_dict['path'] = path
    file_dict['date'] = date
    file_dict['size'] = file_size
    file_dict['name_and_path'] = os.path.split(file_path)

    filename = unicode(datetime.strftime(datetime.now(), '%Y.%m.%d'))

    txt_file = open(filename+'.txt', 'w')
    for item in file_dict.values():
        txt_file.write(str(item)+'\n')
    txt_file.close()
    print 'succeed'
