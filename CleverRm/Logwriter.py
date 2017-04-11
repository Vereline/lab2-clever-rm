#! usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
from datetime import datetime


class Logwriter():
    def __init__(self, path):
        self.file_dict = {}
        self.file_dict_path = path

    def create_file_dict(self, path):
        self.file_dict = self.write_json_log(path)

    def write_json_log(self, path):
        file_dict = {}
        file_dict['path'] = path
        file_dict['id'] = str(path.__hash__())
        file_dict['date'] = datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M:%S')
        file_dict['size'] = os.path.getsize(path)
        if not os.path.isdir(path):
            name = os.path.split(path)
            file_dict['name'] = name[1]
            return file_dict
        elif os.path.isdir(path):
            file_list = []
            tree = os.walk(path)
            for d in tree:
                if len(d[1]) != 0:
                    for dir in d[1]:
                        subpath_d = os.path.join(d[0], dir)  # формирование адреса
                        subdict = self.write_json_log(subpath_d)
                        file_list.append(subdict)
                if len([d[2]]) != 0:
                    for f in d[2]:
                        subpath_f = os.path.join(d[0], f)  # формирование адреса
                        subfile = self.write_json_log(subpath_f)
                        file_list.append(subfile)
            # for d, dirs, files in os.walk(path):
            #     for dir in dirs:
            #         file_path = os.path.join(d, dir)  # формирование адреса
            #         subdict = self.write_json_log(file_path)
            #         file_list.append(subdict)

            # for d, dirs, files in os.walk(path):
            #     for f in files:
            #         file_path = os.path.join(d, f)  # формирование адреса
            #         subdict = self.write_json_log(file_path)
            #         file_list.append(subdict)

            # for d, dirs, files in os.walk(path):
            #     for f in files:
            #         file_path = os.path.join(d, f)  # формирование адреса
            #         subdict = self.write_json_log(file_path)
            #         file_list.append(subdict)

                    # path_f.append(path)  # добавление адреса в список
            # names = os.listdir(path)
            # for name in names:
            #     name_dict = write_json_log(self, name)
            #     file_list.append(name_dict)
            file_dict['content'] = file_list
        return file_dict
    # def write_json_log(self, file_path):
    #     print 'trying to write log'
    #     file_dict = {}
    #
    #     path = os.path.abspath(file_path)
    #     date = datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M:%S')
    #     name = os.path.split(file_path)
    #     file_size = os.path.getsize(file_path)
    #
    #     file_dict['name'] = name[1]
    #     file_dict['path'] = path
    #     file_dict['date'] = date
    #     file_dict['size'] = file_size
    #     file_dict['name_and_path'] = os.path.split(file_path)
    #
    #     filename = unicode(datetime.strftime(datetime.now(), '%Y.%m.%d'))
    #
    #     json.dump(file_dict, open(filename, 'a'))
    #     print 'succeed'
    #
    # # make restructure of this function, in order not to repeat json func
    # def write_txt_log(self, file_path):
    #     print 'trying to write log'
    #     file_dict = {}
    #
    #     path = os.path.abspath(file_path)
    #     date = datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M:%S')
    #     name = os.path.split(file_path)
    #     file_size = os.path.getsize(file_path)
    #
    #     file_dict['name'] = name[1]
    #     file_dict['path'] = path
    #     file_dict['date'] = date
    #     file_dict['size'] = file_size
    #     file_dict['name_and_path'] = os.path.split(file_path)
    #
    #     filename = unicode(datetime.strftime(datetime.now(), '%Y.%m.%d'))
    #
    #     txt_file = open(filename+'.txt', 'w')
    #     for item in file_dict.values():
    #         txt_file.write(str(item)+'\n')
    #     txt_file.close()
    #     print 'succeed'
