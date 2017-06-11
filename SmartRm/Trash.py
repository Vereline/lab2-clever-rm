#! usr/bin/env python
# -*- coding: utf-8 -*-


import shutil         # Contains functions for operating files
import os         # imports the os
import Logwriter
from datetime import datetime
import logging

# new procedure if trash does not exist ( create new trash)


class Trash(object):
    def __init__(self, path_trash, path_log_j, path_log_t, policy_time, policy_size, size, cur_size, capacity, time):
        self.path = path_trash
        if not os.path.exists(self.path):
            logging.info('Create a new trash in the {path}'.format(path=self.path))
            os.makedirs(self.path)
        self.log_writer = Logwriter.Logwriter(path_log_j, path_log_t)
        self.policy_time = policy_time
        self.policy_size = policy_size
        self.max_size = size
        self.cur_size = cur_size
        self.max_capacity = capacity  # the max quantity of files in trash
        self.max_time = time

    def delete_automatically(self, dry_run):  # works
        # delete the whole trash
        logging.info("Clean the whole trash".format())
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
            logging.info("Clean information about files".format())
            clean_json = open(self.log_writer.file_dict_path, 'w')
            clean_json.close()
            clean_txt = open(self.log_writer.file_dict_path_txt, 'w')
            clean_txt.close()

    def delete_manually(self, path):  # not checked
        # delete one file manually
        file_id = self.log_writer.get_id(path)
        clean_path = self.get_path_by_id(file_id, self.path)

        if os.path.isdir(clean_path):
            logging.info("Remove directory".format())
            shutil.rmtree(clean_path)
        elif not os.path.isdir(clean_path):
            logging.info("Remove file".format())
            os.remove(clean_path)

    def get_path_by_id(self, file_id, path):  # not checked
        d = os.listdir(path)
        for item in d:
            subpath = os.path.join(path, item)  # form the address
            if file_id in subpath:
                return subpath

    def watch_trash(self, dry_run):  # works
        logging.info("Show trash".format())
        if dry_run:
            print 'show trash'
        else:
            if self.log_writer.file_dict_arr is [] or self.log_writer.file_dict_arr is None or self.log_writer.file_dict_arr.__len__() == 0:
                print 'trash bucket is empty'
            else:
                txt_file = open(self.log_writer.file_dict_path_txt, 'r')
                print(txt_file.read())

    def restore_trash_automatically(self, dry_run):  # not tested
        # restore the the whole trash
        logging.info("Restore the whole trash".format())

        if dry_run:
            print 'restore the whole trash'
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
                    subpath = os.path.split(subpath)  # ???
                    subpath = self.get_path_by_id(subpath[1], subpath[0])  # ???
                    logging.info("Restore file".format())
                    self.restore_trash_manually(subpath, dry_run)
                    # if os.path.isdir(subpath):
                    #     shutil.rmtree(subpath)
                    # elif not os.path.isdir(subpath):
                    #     os.remove(subpath)
            # with
            clean_json = open(self.log_writer.file_dict_path, 'w')
            clean_json.close()
            clean_txt = open(self.log_writer.file_dict_path_txt, 'w')
            clean_txt.close()

    def restore_trash_manually(self, path, dry_run, interactive):  # works
        # restore one file in the trash
        # check if the path already exists

        # находит первый попавшийся файл, но не ищет, есть ли еще, предотвратить политику конфликтов
        file_id = self.log_writer.get_id(path)
        # file_id = os.path.split(path)[1]
        clean_path = self.get_path_by_id(file_id, self.path)
        destination_path = self.log_writer.get_path(file_id)
        new_name = self.log_writer.get_name(file_id)
        logging.info("Operations with file {file}".format(file=new_name))
        index = 0
        for i in reversed(range(len(clean_path))):
            if clean_path[i] == '/':
                index = i
                break
        dirname = clean_path[:(index+1)] + new_name
        logging.info("Rename {file}".format(file=new_name))
        logging.info("Move to original directory {file}".format(file=new_name))
        # находит первый попавшийся файл, но не ищет, есть ли еще, предотвратить политику конфликтов
        # при восстановлении чтоб смотерл, а вдруг есть уже такой файл в директории выдавать предупреждение
        if os.path.exists(destination_path):
            logging.warning('Item with this name already exists.id will be added to real name')
            dirname += file_id
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

    def check_policy(self, path, dry_run):  # not checked(redo to check the whole bucket)
        logging.info("Check policies".format())
        if self.policy_time:
            confirm = self.check_date_if_overflow(path)
            if confirm:
                self.delete_manually(path)
        if self.policy_size:
            self.count_size(dry_run)
            pass

    def count_days(self, path):
        logging.info("Check the time policy".format())
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

    def check_size(self, dry_run):
        logging.info("Check the size policy".format())
        if self.max_size - self.count_size(dry_run) <= 0:
            if dry_run:
                print 'not enough trash space'
            else:
                self.delete_automatically(dry_run)

    def count_size(self, dry_run):  # not tested
        total_size = 0
        if dry_run:
            print 'count real size of the whole trash'
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
                        total_size += self.get_size(subpath)
                    elif not os.path.isdir(subpath):
                        total_size += os.path.getsize(subpath)

        return total_size

    def get_size(self, start_path='.'):
        logging.info("Get the size of file in the trash".format())
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    def search_for_all_files_with_this_name(self, name):
        files_id = []
        for file_dict in self.log_writer.file_dict_arr:
            if file_dict['name'] == name:
                files_id.append(file_dict['id'])

        return files_id
