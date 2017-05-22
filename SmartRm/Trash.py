#! usr/bin/env python
# -*- coding: utf-8 -*-


import shutil         # Contains functions for operating files
import os         # imports the os
import Logwriter
from datetime import datetime


# new procedure if trash does not exist ( create new trash)

class Trash(object):
    def __init__(self, path_trash, path_log_j, path_log_t, policy_time, policy_size, size, cur_size, capacity, time):
        self.path = path_trash
        self.log_writer = Logwriter.Logwriter(path_log_j, path_log_t)
        self.policy_time = policy_time
        self.policy_size = policy_size
        self.max_size = size
        self.cur_size = cur_size
        self.max_capacity = capacity  # the max quantity of files in trash
        self.max_time = time

    def delete_automatically(self, dry_run):  # works
        # delete the whole trash
        if dry_run:
            print 'clean trash'
        else:
            d = os.listdir(self.path)
            for item in d:
                subpath = os.path.join(self.path, item)  # form the address
                dict_contains = False
                for _dict in self.log_writer.file_dict_arr:
                    if _dict['id'] == item:
                        dict_contains = True
                        break

                if dict_contains:
                    if os.path.isdir(subpath):
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
            subpath = os.path.join(path, item)  # form the address
            if file_id in subpath:
                return subpath

    def watch_trash(self, dry_run):  # works
        if dry_run:
            print 'show trash'
        else:
            if self.log_writer.file_dict_arr is [] or self.log_writer.file_dict_arr is None or self.log_writer.file_dict_arr.__len__() == 0:
                print 'trash bucket is empty'
            else:
                txt_file = open(self.log_writer.file_dict_path_txt, 'r')
                print(txt_file.read())

    def restore_trash_automatically(self):  # not done
        # restore the the whole trash
        # the same strategy as delete
        self.rename_all_directory_content(self.path)
        allfiles = os.listdir(self.path)
        for f in allfiles:
            if not os.path.isdir(self.path+f):
                new_name = self.log_writer.get_name(f)
        return None

    # def rename_all_directory_content(self, path):  # not checked
    #
    #     if not os.path.isdir(path):
    #         name = os.path.split(path)
    #         new_name = self.log_writer.get_name(name[1])
    #         os.rename(path, name[0]+new_name)
    #     elif os.path.isdir(path):
    #         index = 0
    #         for i in reversed(range(len(path))):
    #             if path[i] == '/':
    #                 index = i
    #                 break
    #         dir_name = path[index + 1:]
    #         new_name = self.log_writer.get_name(dir_name)
    #         os.rename(path, path[:path.__sizeof__() - (index+1)]+new_name)

    def restore_trash_manually(self, path, dry_run):  # works
        # restore one file in the trash
        # check if the path already exists
        file_id = self.log_writer.get_id(path)
        clean_path = self.get_path_by_id(file_id, self.path)
        destination_path = self.log_writer.get_path(file_id)
        new_name = self.log_writer.get_name(file_id)

        index = 0
        for i in reversed(range(len(clean_path))):
            if clean_path[i] == '/':
                index = i
                break
        dirname = clean_path[:(index+1)] + new_name
        if dry_run:
            print 'rename file and move to original directory'
            print 'clean record from json'
        else:
            os.rename(clean_path, dirname)
            shutil.move(dirname, destination_path)
            self.log_writer.delete_elem_by_id(file_id)
            self.log_writer.write_to_json()
            self.log_writer.write_to_txt()
        return None

    def check_policy(self, path):  # not checked(redo to check the whole bucket)
        if self.policy_time:
            confirm = self.check_date_if_overflow(path)
            if confirm:
                self.delete_manually(path)
        elif self.policy_size:
            print 'size'

    def count_days(self, path):
        name = os.path.split(path)
        if name[1] != '':
            file_id = self.log_writer.get_id(name[1])
            file_date = self.log_writer.get_date(file_id)
            cur_date = datetime.date.today()
            file_date = file_date.split('-')
            date_a = datetime.date(int(file_date[0]), int(file_date[1]), int(file_date[2]))

            days = cur_date - date_a
            days = str(days).split()[0]
        return days

    def check_date_if_overflow(self, path):
        time = self.count_days(path)
        if time > self.max_time:
            return True
        else:
            return False

    def check_size(self):
        return None