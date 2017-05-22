#! usr/bin/env python
# -*- coding: utf-8 -*-

import json
import Smart_rm
import shutil         #Contains functions for operating files
import os
import sys
import Logwriter
import Argparser
import Trash
import re
import ExeptionListener
import pprint

# тут обрабатывать декораторы dry-run + i,v,f
# redo and refactor all the code

# rename here deleted file to the id
# -i - confirm every your deletion / restore


class File_delete_configurator():
    def __init__(self, argparser, paths):
        self.argparser = argparser
        self.config = json.load(open('SmartRm/Configure.json', 'r'))
        self.change_configure()
        self.trash = Trash.Trash(self.config['path'], self.config['trash_log_path'], self.config['trash_log_path_txt'],
                                 self.config['policy_time'], self.config['policy_size'], self.config['max_size'],
                                 self.config['current_size'], self.config['max_capacity'], self.config['max_time'])
        self.smartrm = Smart_rm.SmartRm(self.config['path'])
        self.exit_codes = {
             'success': 0,
             'conflict': 1,
             'error': 2,
             'no_file': 3
        }

        self.dry_run = False
        self.silent = False
        self.interactive = False
        self.verbose = False
        self.force = False

        if argparser.args.interactive:  # если нету интерэктив, спрашиваем только если прав не хватает
            self.interactive = True
        if argparser.args.silent:
            self.silent = True
        if argparser.args.force:
            self.force = True
        if argparser.args.verbose:
            self.verbose = True
        if argparser.args.dryrun:
            self.dry_run = True

        self.paths = paths

    def define_action(self):
        if self.argparser.args.remove is not None:
            for item in self.paths:
                exists = self.check_file_path(item)
                if not exists:
                    pass
                    # exception
                access = self.check_access(item)
                if access == self.exit_codes['error']:
                    pass
                    # exception
                self.trash.log_writer.create_file_dict(item, self.dry_run)
                item = self.rename_file_name_to_id(item, self.dry_run)
                self.smartrm.remove_to_trash_file(item, self.dry_run)

            self.trash.log_writer.write_to_json()
            self.trash.log_writer.write_to_txt()

        elif self.argparser.args.remove_regular is not None:
            # do here regular check

            for item in self.paths:
                exists = self.check_file_path(item)
                if not exists:
                    pass
                    # exception
                access = self.check_access(item)
                if access == self.exit_codes['error']:
                    pass
                    # exception
                self.trash.log_writer.create_file_dict(item, self.dry_run)
                item = self.rename_file_name_to_id(item, self.dry_run)
                self.smartrm.remove_to_trash_file(item, self.dry_run)

            self.trash.log_writer.write_to_json()
            self.trash.log_writer.write_to_txt()
            pass

        elif self.argparser.args.clean is not None:
            self.trash.delete_automatically(self.dry_run)

        elif self.argparser.args.restore is not None:
            for item in self.paths:
                self.trash.restore_trash_manually(item, self.dry_run)  # проверить на правильность путей

        elif self.argparser.args.restore_all is not None:
            # for item in self.paths:
            #     self.trash.restore_trash_manually(item)  # проверить на правильность путей
            #
            pass

        elif self.argparser.args.remove_from_trash is not None:
            for item in self.paths:
                self.trash.delete_manually(item)  # проверить на правильность путей

        elif self.argparser.args.show_trash is not None:
            self.trash.watch_trash(self.dry_run)

        elif self.argparser.args.show_config is not None:
            # print self.config
            pprint.pprint(self.config)

    def check_file_path(self, path):
        # if the file is already not existing for the delete function or the file exists for restore
        if os.path.exists(path):
            return True
        else:
            return False

    def rename_file_name_to_id(self, path, dry_run):  # works
        _id = self.trash.log_writer.get_id_path(path)
        index = 0
        for i in reversed(range(len(path))):
            if path[i] == '/':
                index = i
                break

        directory_name = path[:(index+1)] + _id
        if dry_run:
            print 'rename file name to id'
        else:
            os.rename(path, directory_name)
        return directory_name

    def ask_for_confirmation(self):
        answer = input('Are you sure? [y/n]\n')
        if answer == 'n' or answer == 'N':
            print('Operation canceled')
            sys.exit(self.exit_codes['success'])
        elif answer != 'y' and answer != 'n' and answer != 'N' and answer != 'Y':
            self.ask_for_confirmation()

    def check_access(self, path):
        if os.access(path, os.R_OK):
            return self.exit_codes['success']
        else:
            # raise system directory exception
            # write this in logger
            return self.exit_codes['error']

    def change_configure(self):  # works
        if self.argparser.args.configs is not None:
            for config in self.argparser.args.configs:
                arr = config.split('=')
                if arr[0] in self.config.keys:
                    self.config[arr[0]] = arr[1]
