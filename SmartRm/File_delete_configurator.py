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
import Regular
import Logger
import logging
import Config_parser

# тут обрабатывать декораторы dry-run + i,v,f
# redo and refactor all the code

# rename here deleted file to the id
# -i - confirm every your deletion / restore


class FileDeleteConfigurator(object):
    def __init__(self, argparser, paths):
        self.argparser = argparser

        self.dry_run = False
        self.silent = False
        self.interactive = False
        self.verbose = False
        self.force = False

        if argparser.args.interactive:  # if there is no interactive, ask only if you have no roots
            self.interactive = True  # if there are many files, ask for every file
        if argparser.args.silent:
            self.silent = True
        if argparser.args.force:
            self.force = True
        if argparser.args.verbose:
            self.verbose = True
        if argparser.args.dryrun:
            self.dry_run = True

        self.exit_codes = {
            'success': 0,
            'conflict': 1,
            'error': 2,
            'no_file': 3
        }

        # ???????
        # make this config as default and make load (right path) in the setup.py
        # load txt version as a user config after

        user_txt_path = 'SmartRm/Configure.txt'  # put this into setup.py
        try:
            self.config = json.load(open('SmartRm/Configure.json', 'r')) # put this into setup.py
        except ExeptionListener.FileDoesNotExistException as ex:
            # logging.error(ex)  # check if this works before constructor
            print ex
            sys.exit(self.exit_codes['no_file'])

        self.logger = Logger.Logger(self.config['trash_logging_path'], self.silent)

        try:
            self.config_parser = Config_parser.ConfParser(user_txt_path)
        except ExeptionListener.FileDoesNotExistException as ex:
            # logging.error(ex)
            print ex
            sys.exit(self.exit_codes['no_file'])

        self.change_configure_by_user_config()  # change config by the txt file
        self.change_configure()  # change config by the parsed command line

        try:
            # if critical - exit
            # if not critical - default settings(work in exceptionListener)
            self.trash = Trash.Trash(self.config['path'], self.config['trash_log_path'],
                                     self.config['trash_log_path_txt'],
                                     self.config['policy_time'], self.config['policy_size'], self.config['max_size'],
                                     self.config['current_size'], self.config['max_capacity'], self.config['max_time'])
        except ExeptionListener.FileDoesNotExistException as ex:
            # do not so broad exception
            # do closer exception
            logging.error('Unable to load trash')
            logging.error(ex)
            sys.exit(self.exit_codes['error'])
        try:
            self.smartrm = Smart_rm.SmartRm(self.config['path'])
        except ExeptionListener.FileDoesNotExistException as ex:
            logging.error('Unable to load smart rm')
            logging.error(ex)
            sys.exit(self.exit_codes['error'])

        self.paths = paths

    def define_action(self):
        logging.info('Define action')
        if self.argparser.args.remove is not None:
            if self.interactive:
                self.ask_for_confirmation()
            for item in self.paths:
                exists = self.check_file_path(item)
                if not exists:
                    logging.error('File % does not exist', item)
                else:
                    access = self.check_access(item)
                    if access == self.exit_codes['error']:
                        logging.error('Item {file} is a system unit'.format(file=item))
                    else:
                        # remove all the check to the trash or to the smart rm
                        self.trash.log_writer.create_file_dict(item, self.dry_run)
                        item = self.rename_file_name_to_id(item, self.dry_run)
                        self.smartrm.remove_to_trash_file(item, self.dry_run)

            self.trash.log_writer.write_to_json()
            self.trash.log_writer.write_to_txt()

        elif self.argparser.args.remove_regular is not None:
            # do here regular check
            for element in self.paths:
                if self.interactive:
                    self.ask_for_confirmation()
                items = Regular.define_regular_path(element)
                for item in items:
                    exists = self.check_file_path(item)
                    if not exists:
                        logging.error('File {file} does not exist'.format(file=item))
                        # exception
                    else:
                        access = self.check_access(item)
                        if access == self.exit_codes['error']:
                            logging.error('Item {file} is a system unit'.format(file=item))
                            # exception
                        else:
                            self.trash.log_writer.create_file_dict(item, self.dry_run)
                            item = self.rename_file_name_to_id(item, self.dry_run)
                            self.smartrm.remove_to_trash_file(item, self.dry_run)

                self.trash.log_writer.write_to_json()
                self.trash.log_writer.write_to_txt()

        elif self.argparser.args.clean is not None:
            if self.interactive:
                self.ask_for_confirmation()
            self.trash.delete_automatically(self.dry_run)

        elif self.argparser.args.restore is not None:
            if self.interactive:
                self.ask_for_confirmation()
            for item in self.paths:
                self.trash.restore_trash_manually(item, self.dry_run)  # проверить на правильность путей

        elif self.argparser.args.restore_all is not None:
            if self.interactive:
                self.ask_for_confirmation()
            self.trash.restore_trash_automatically(self.dry_run)

        elif self.argparser.args.remove_from_trash is not None:
            if self.interactive:
                self.ask_for_confirmation()
            for item in self.paths:
                self.trash.delete_manually(item)  # проверить на правильность путей

        elif self.argparser.args.show_trash is not None:
            if self.interactive:
                self.ask_for_confirmation()
            self.trash.watch_trash(self.dry_run)

        elif self.argparser.args.show_config is not None:
            if self.interactive:
                self.ask_for_confirmation()
            if self.dry_run:
                print 'show config'
            else:
                pprint.pprint(self.config)

    def check_file_path(self, path):
        if not self.silent:
            logging.info('Check if the path is correct')
        # if the file is already not existing for the delete function or the file exists for restore
        if os.path.exists(path):
            return True
        else:
            return False

# remove this thing to smart rm or to the trash
    def rename_file_name_to_id(self, path, dry_run):  # works
        logging.info('Rename item with id')
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
        answer = raw_input('Are you sure? [y/n]\n')
        if answer == 'n' or answer == 'N':
            if self.silent:
                print('Operation canceled')
            sys.exit(self.exit_codes['success'])
        elif answer != 'y' and answer != 'n' and answer != 'N' and answer != 'Y':
            self.ask_for_confirmation()

    def check_access(self, path):
        logging.info('Check {file} access'.format(file=path))
        if os.access(path, os.R_OK):
            return self.exit_codes['success']
        else:
            logging.error('This is a system unit')
            # raise system directory exception
            # write this in logger
            return self.exit_codes['error']

    def change_configure(self):  # works
        if self.argparser.args.configs is not None:
            for config in self.argparser.args.configs:
                arr = config.split('=')
                if arr[0] in self.config.keys:
                    self.config[arr[0]] = arr[1]

    def change_configure_by_user_config(self):
        for key in self.config.keys():
            try:
                if self.config_parser.dict[key] is not None:
                    self.config[key] = self.config_parser.dict[key]
            except ExeptionListener.WrongItemException as ex:
                logging.ERROR(ex)
