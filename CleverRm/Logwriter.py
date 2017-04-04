#! usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
from datetime import datetime


def write_json_log(file_path):
    print 'trying to write log'
    file_dict = {}
    path = os.path.abspath(file_path)
    date = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    name = os.path.split(file_path)
    file_dict["name"] = name[1]
    file_path["name_directory"] = name[0]
    file_dict["path"] = path
    file_dict["date"] = date
    filename = unicode(datetime.strftime(datetime.now(), "%Y.%m.%d"))
    json.dump(file_dict, open(filename, 'a'))
    print 'succeed'
