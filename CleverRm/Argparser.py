#! usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from argparse import *
import Clever_rm
import shutil         #Contains functions for operating files
import os         #imports the os
import Logwriter


def add_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # remove files
    parser_remove = subparsers.add_parser('remove')

    parser_remove.add_argument('-i', nargs='+')
    parser_remove.add_argument('-f', nargs='+')
    parser_remove.add_argument('-v', nargs='+')
    parser_remove.add_argument('path', nargs='*')

    parser_trash = subparsers.add_parser('trash')
    trash_subparsers = parser_trash.add_subparsers()

    # cleaning trash
    parser_clean_trash = trash_subparsers.add_parser('clean')
    parser_clean_trash.add_argument('-i', nargs='+')
    parser_clean_trash.add_argument('-f', nargs='+')
    parser_clean_trash.add_argument('-v', nargs='+')
    parser_clean_trash.add_argument('path', nargs='*')

    # restore trash
    parser_restore_trash = trash_subparsers.add_parser('restore')
    parser_restore_trash.add_argument('-i', nargs='+')
    parser_restore_trash.add_argument('-f', nargs='+')
    parser_restore_trash.add_argument('-v', nargs='+')
    parser_restore_trash.add_argument('path', nargs='*')

    # show trash
    parser_trash_show = trash_subparsers.add_parser('show')
    parser_trash_show.add_argument('show_trash')

    # configure files
    parser_configure = subparsers.add_parser('configure')
    parser_configure_subparsers = parser_configure.add_subparsers()

    parser_configure_show = parser_configure_subparsers.add_parser('show')
    parser_configure_show.add_argument('show_options ', nargs='+')

    parser_configure_setter = parser_configure_subparsers.add_parser('setter')
    parser_configure_setter.add_argument('set_options', nargs='+')

    return parser

def main():

    parser = add_parser()
    args = parser.parse_args()

# how to control namespaces???

    if args.show_trash:
        Clever_rm.watch_trash()
    if args.f:
        for path in args.f:
            try:
                file_path = os.path.abspath(path)
                Logwriter.write_json_log(file_path)
                Logwriter.write_txt_log(file_path)
                Clever_rm.remove_to_trash(file_path)
            except:
                print 'error, no such file or directory'
    if args.i:
        for path in args.f:
            try:
                answer = raw_input('Do you want to delete '+path+'?')
                if 'Yes' in answer or 'YES' in answer or 'yes' in answer:
                    file_path = os.path.abspath(path)
                    Logwriter.write_json_log(file_path)
                    Logwriter.write_txt_log(file_path)
                    Clever_rm.remove_to_trash(file_path)
                elif 'No' in answer or 'NO' in answer or 'no' in answer:
                    continue
                else:
                    print 'did not understand the input'
            except:
                print 'error, no such file or directory'


    # if args.cleverrm:
    #     this_path = unicode(os.path.abspath(args.path))
    #     Logwriter.write_json_log(this_path)
    #     Clever_rm.simple_move(this_path)
    # elif args.lstrash:
    #     Clever_rm.watch_trash()

if __name__ == '__main__':
    main()


