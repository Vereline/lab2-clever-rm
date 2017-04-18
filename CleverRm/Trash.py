#! usr/bin/env python
# -*- coding: utf-8 -*-


import shutil         # Contains functions for operating files
import os         # imports the os
import Logwriter
from datetime import datetime

class Trash():
    def __init__(self, path_trash, path_log_j, path_log_t, p, s, cap, t):
        self.path = path_trash
        self.log_writer = Logwriter.Logwriter(path_log_j, path_log_t)
        self.politics = p
        self.size = s
        self.capacity = cap
        self.time = t

    def delete_automatically(self):  # not checked(means clean trash)
        # delete the whole trash
        # os.access  - check the access!!!!(права доступа)
        d = os.listdir(self.path)
        for item in d:
            subpath = os.path.join(self.path, item)  # формирование адреса
            if item == 'Trash_log':
                continue
            elif os.path.isdir(subpath):
                shutil.rmtree(subpath)
            elif not os.path.isdir(subpath):
                os.remove(subpath)
        clean_json = open(self.log_writer.file_dict_path, 'w')
        clean_json.close()
        clean_txt = open(self.log_writer.file_dict_path_txt, 'w')
        clean_txt.close()

    def delete_manually(self, path):  # not checked
        # delete one file manually
        file_id = self.log_writer.get_id(path)
        clean_path = self.get_path_by_id(file_id, self.path)

        if os.path.isdir(clean_path):
            shutil.rmtree(clean_path)
        elif not os.path.isdir(clean_path):
            os.remove(clean_path)

    def get_path_by_id(self, file_id, path):  # not checked
        d = os.listdir(path)
        for item in d:
            subpath = os.path.join(path, item)  # формирование адреса
            if file_id in subpath:
                return subpath
            else:
                if os.path.isdir(subpath):
                    return self.get_path_by_id(file_id, subpath)
                elif not os.path.isdir(subpath):
                    continue

    def watch_trash(self):  # not checked
        if self.log_writer.file_dict_arr is [] or self.log_writer.file_dict_arr is None:
            print 'trash bucket is empty'
        else:
            txt_file = open(self.log_writer.file_dict_path_txt, 'r')
            print txt_file
        # file_list = json.load(open(self.trash_log_path, 'r'))
        # if not file_list:
        #     print 'trash bucket is empty'
        # else:
        #     for item in file_list:  # check this
        #         print item['name']  # check this
        #         # file_list = os.listdir(self.trash_path)

    def restore_trash_automatically(self):  # not done
        # restore the the whole trash
        self.rename_all_directory_content(self.path)
        allfiles = os.listdir(self.path)
        for f in allfiles:
            if not os.path.isdir(self.path+f):
                new_name = self.log_writer.get_name(f)
        return None

    def rename_all_directory_content(self, path):  # not checked

        if not os.path.isdir(path):
            name = os.path.split(path)
            newname = self.log_writer.get_name(name[1])
            os.rename(path, name[0]+newname)

        elif os.path.isdir(path):
            index = 0
            for i in reversed(range(len(path))):
                if path[i] == '/':
                    index = i
                    break
            dirname = path[index + 1:]
            d = os.listdir(path)
            print d
            for item in d:
                subpath = os.path.join(path, item)  # формирование адреса
                if os.path.isdir(subpath):
                    self.rename_all_directory_content(subpath)
                    #subfile = self.write_file_dict(subpath)

                elif not os.path.isdir(subpath):
                    self.rename_all_directory_content(subpath)
                    #subdict = self.write_file_dict(subpath)
            newname = self.log_writer.get_name(dirname)
            os.rename(path, path[:path.__sizeof__() - (index+1)]+newname)


    def restore_trash_manually(self, path):  # not checked
        # restore one file in the trash
        file_id = self.log_writer.get_id(path)
        clean_path = self.get_path_by_id(file_id, self.path)
        destination_path = self.log_writer.get_path(file_id)
        new_name = self.log_writer.get_name(file_id)

        index = 0
        for i in reversed(range(len(clean_path))):
            if path[i] == '/':
                index = i
                break
        dirname = path[:len(clean_path) - index] + new_name

        shutil.move(dirname, destination_path)
        self.log_writer.delete_elem_by_id(file_id)
        return None

    def check_politics(self):
        # config = json.load(open('CleverRm/Configure.json', 'r'))
        # politics = config['politics']
        if politics == 'time':
            print 'time'
        elif politics == 'size':
            print 'size'
        elif politics == 'combined':
            print 'combined'

    def check_date(self, path):
        name = os.path.split(path)
        if name[1] != '':
            file_id = self.log_writer.get_id(name[1])
            file_date = self.log_writer.get_date(file_id)
            cur_date = datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M:%S')
            years = ((int)(file_date[0]+file_date[1]) - (int)(cur_date[0]+cur_date[1]))
            months = ((int)(file_date[4] + file_date[5]) - (int)(cur_date[4] + cur_date[5]))
            days = ((int)(file_date[7] + file_date[8]) - (int)(cur_date[7] + cur_date[8]))
            days_common = years*365+months*30+days
        return days_common

    def check_size(self):
        return None