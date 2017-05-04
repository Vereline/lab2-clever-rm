#! usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from argparse import *
import Smart_rm
import shutil         #Contains functions for operating files
import os         #imports the os
import Logwriter
import sys

class Argparser():
    def __init__(self, arguments_string=''):
        self.parser = self.add_parser()
        if arguments_string != '':
            splited_arguments_string = arguments_string.split(' ')
            self.args = self.parser.parse_args(splited_arguments_string)
        else:
            self.args = self.parser.parse_args()

    def add_parser(self):
        parser = argparse.ArgumentParser()
        # subparsers = parser.add_subparsers()
        # nargs поменять и см, как это правильно сделать
        parser.add_argument('-smrm', nargs='*', dest='remove', help='remove file or directory(also make a mask type as *.py)')
        parser.add_argument('-smrmr', nargs='*', dest='remove_regular', help='remove file or directory by regular expression')
        parser.add_argument('-smtrc', nargs='*', dest='clean', help='clean trash')
        parser.add_argument('-smtrr', nargs='*', dest='restore', help='restore trash')
        parser.add_argument('-smtrrm', nargs='*', dest='remove_from_tras', help='remove from trash')
        parser.add_argument('-smtrs', nargs='*', dest='show_trash', help='show trash')
        parser.add_argument('-smcs', nargs='*', dest='show_config', help='show config')
        parser.add_argument('-smcc', nargs='*', dest='change_config', help='change config and delete')  # только для 1 запуска

        # интерактивно спрашивает, хочешь удалить или нет
        parser.add_argument('-i', '-interactive', dest='interactive', action='store_true', help='interactive mode')
        parser.add_argument('-f', '-force', dest='force', action='store_true', help='force mode')  # ничего не спрашивает
        parser.add_argument('-v', '-verbose', dest='verbose', action='store_true', help='verbose mode')  # отображает состояние текущее программы(противоположно сайленту)
        parser.add_argument('-s', '-silent', dest='silent', action='store_true', help='silent mode')
        parser.add_argument('-d', '-dryrun', dest='dryrun', action='store_true', help='dry-run mode')

        parser.add_argument('path', nargs='*', help='path of file or directory')

        # -smrm - remove
        # -smrmr - remove regular
        # -smtrc - trash clean
        # -smtrr - trash restore
        # -smtrs - trash show
        # -smcs  - config show
        # -smcc  - config change
        #
        # -i - interactive
        # -v - verbose
        # -f - force
        # -s - silent
        # -d - dryrun
        #
        # path - path of file/directory

        # remove files
        # parser_remove = subparsers.add_parser('remove')
        #
        # parser_remove.add_argument('-i', nargs='+')
        # parser_remove.add_argument('-f', nargs='+')
        # parser_remove.add_argument('-v', nargs='+')
        # parser_remove.add_argument('path', nargs='*')
        #
        # parser_trash = subparsers.add_parser('trash')
        # trash_subparsers = parser_trash.add_subparsers()
        #
        # # cleaning trash
        # parser_clean_trash = trash_subparsers.add_parser('clean')
        # parser_clean_trash.add_argument('-i', nargs='+')
        # parser_clean_trash.add_argument('-f', nargs='+')
        # parser_clean_trash.add_argument('-v', nargs='+')
        # parser_clean_trash.add_argument('path', nargs='*')
        #
        # # restore trash
        # parser_restore_trash = trash_subparsers.add_parser('restore')
        # parser_restore_trash.add_argument('-i', nargs='+')
        # parser_restore_trash.add_argument('-f', nargs='+')
        # parser_restore_trash.add_argument('-v', nargs='+')
        # parser_restore_trash.add_argument('path', nargs='*')
        #
        # # show trash
        # parser_trash_show = trash_subparsers.add_parser('show')
        # parser_trash_show.add_argument('show_trash')
        #
        # # configure files
        # parser_configure = subparsers.add_parser('configure')
        # parser_configure_subparsers = parser_configure.add_subparsers()
        #
        # parser_configure_show = parser_configure_subparsers.add_parser('show')
        # parser_configure_show.add_argument('show_options ', nargs='+', choices=['path', 'capacity', 'position'])
        #
        # parser_configure_setter = parser_configure_subparsers.add_parser('setter')
        # parser_configure_setter.add_argument('set_options', nargs='+')+

        return parser

    def define_command_line(self):
        command = sys.argv
        command.pop(0)
        return command

    def define_path(self, rm_file):
        if rm_file.find('/') == -1:
            path = os.path.abspath(rm_file)
            # path = os.path.abspath(os.getcwd()+'/()'.format(rm_file))
        else:
            path = os.path.abspath(os.path.expanduser(rm_file))
        return path

    def create_outlist(self, args, command):
        outlist = []
        for item in args.path:
            outlist.append(self.define_path(item))
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

    # def get_files_arguments(self, args):
    #     rm_files = []
    #
    #     if args.i:
    #         for rm_file in args.i:
    #             path = self.define_path(rm_file)
    #             rm_files.append(path)
    #             rm_files.append(os.path.isdir(path))
    #             rm_files.append('-i')
    #     if args.f:
    #         for rm_file in args.f:
    #             path = self.define_path(rm_file)
    #             rm_files.append(path)
    #             rm_files.append(os.path.isdir(path))
    #             rm_files.append('-f')
    #     if args.v:
    #         for rm_file in args.v:
    #             path = self.define_path(rm_file)
    #             rm_files.append(path)
    #             rm_files.append(os.path.isdir(path))
    #             rm_files.append('-v')
    #
    #     return rm_files
    #     # if args.f:
    #     #     for path in args.f:
    #     #         try:
    #     #             file_path = os.path.abspath(path)
    #     #             Logwriter.write_json_log(file_path)
    #     #             Logwriter.write_txt_log(file_path)
    #     #             Clever_rm.remove_to_trash(file_path)
    #     #         except:
    #     #             print 'error, no such file or directory'
    #     # if args.i:
    #     #     for path in args.f:
    #     #         try:
    #     #             answer = raw_input('Do you want to delete ' + path + '?')
    #     #             if 'Yes' in answer or 'YES' in answer or 'yes' in answer:
    #     #                 file_path = os.path.abspath(path)
    #     #                 Logwriter.write_json_log(file_path)
    #     #                 Logwriter.write_txt_log(file_path)
    #     #                 Clever_rm.remove_to_trash(file_path)
    #     #             elif 'No' in answer or 'NO' in answer or 'no' in answer:
    #     #                 continue
    #     #             else:
    #     #                 print 'did not understand the input'
    #     #         except:
    #     #             print 'error, no such file or directory'
