#! usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

import shutil         #Contains functions for operating files
import os         #imports the os
import sys
import re
import logging

class Argparser(object):
    def __init__(self, arguments_string=''):
        self.parser = self.add_parser()
        if arguments_string != '':
            splited_arguments_string = arguments_string.split(' ')
            self.args = self.parser.parse_args(splited_arguments_string)
        else:
            self.args = self.parser.parse_args()

    def add_parser(self):
        parser = argparse.ArgumentParser()

        parser.add_argument('-smrm', nargs='*', dest='remove', help='remove file or directory')
        parser.add_argument('-smrmr', nargs='*', dest='remove_regular', help='remove file or directory by regular')
        parser.add_argument('-smtrc', nargs='*', dest='clean', help='clean trash')
        parser.add_argument('-smtrr', nargs='*', dest='restore', help='restore 1 item in trash')
        parser.add_argument('-smtrra', nargs='*', dest='restore_all', help='restore all items in trash')
        parser.add_argument('-smtrrm', nargs='*', dest='remove_from_trash', help='remove from trash')
        parser.add_argument('-smtrs', nargs='*', dest='show_trash', help='show trash')
        parser.add_argument('-smcs', nargs='*', dest='show_config', help='show config')

        # интерактивно спрашивает, удалить или нет
        parser.add_argument('-i', '-interactive', dest='interactive', action='store_true', help='interactive mode')
        parser.add_argument('-f', '-force', dest='force', action='store_true', help='force mode')  # ничего не спрашивает
        parser.add_argument('-v', '-verbose', dest='verbose', action='store_true', help='verbose mode')  # отображает состояние текущее программы(противоположно сайленту)
        parser.add_argument('-s', '-silent', dest='silent', action='store_true', help='silent mode')
        parser.add_argument('-d', '-dryrun', dest='dryrun', action='store_true', help='dry-run mode')

        parser.add_argument('path', nargs='*', help='path of file or directory')
        parser.add_argument('--configs', dest='configs', nargs='*', help='configurations for 1 run')  # только для 1 запуска

        # -smrm - remove
        # -smrmr - remove regular
        # -smtrc - trash clean
        # -smtrr - trash restore
        # -smtrs - trash show
        # -smcs  - config show
        #
        # -i - interactive
        # -v - verbose
        # -f - force
        # -s - silent
        # -d - dryrun
        #
        # path - path of file/directory
        # configs - change configs for 1 time

        return parser

    def define_command_line(self):
        return sys.argv[1:]

    def define_path(self, rm_file):
        if os.path.exists(rm_file):
            return os.path.abspath(os.path.expanduser(rm_file)) #  rm_file
        if rm_file.find('/') == -1:
            path = os.path.abspath(rm_file)
            # path = os.path.abspath(os.getcwd()+'/()'.format(rm_file))
        else:
            path = os.path.abspath(os.path.expanduser(rm_file))
        return path

    def create_outlist(self, args, command):
        outlist = []
        if args.remove_regular is not None:
            for item in args.remove_regular:
                outlist.append(item)
            for item in args.path:
                outlist.append(item)
        elif args.remove is not None:
            for item in args.remove:
                outlist.append(self.define_path(item))
            for item in args.path:
                outlist.append(self.define_path(item))
        elif args.restore is not None:
            for item in args.restore:
                outlist.append(item)
            for item in args.path:
                outlist.append(item)

        # outlist.append(command)
        # if args.remove:
        # # if command[0] == 'remove' or (command[0] == 'trash' and (command[1] == 'clean' or command[1] == 'restore')):
        #     outlist.append(self.get_files_arguments(args))
        # # elif command[0] == 'trash' and command[1] == 'show':
        # elif command[0] == '-smtrr' or command[0] == '-smtrc' or command[0] == '-smtrs' or command[0] == '-smcs':
        #     show_keys = []
        #     for show_key in args.show_trash:
        #         show_keys.append(show_key)
        #     outlist.append(show_keys)
        # elif command[0] == '-smcc':
        #     # if command[1] == 'setter':
        #         set_options = []
        #         for option in args.set_options:
        #             set_options.append(option)
        #         outlist.append(set_options)
        #      # else:
        #         # outlist.append(args.show_options)
        return outlist

