#! usr/bin/env python
# -*- coding: utf-8 -*-

import json
import argparse
from argparse import *
import Clever_rm
import shutil         #Contains functions for operating files
import os         #imports the os
import Logwriter
import Argparser


def main():
    argparser = Argparser.Argparser()
    cmd = argparser.define_command_line()
    outlist = argparser.create_outlist(argparser.args, cmd)
#    print outlist

    if outlist[0][0] == 'remove':
        # original logwriter is in trash
        config = json.load(open('CleverRm/Configure.json', 'r'))
        lo = Logwriter.Logwriter(config['trash_log_path'], config['trash_log_path_txt'])
        lo.create_file_dict(outlist[1][0])
        lo_id = lo.get_id('filefile')
        print lo_id
        # print lo.file_dict
        # for y in lo.file_dict:
        #     if type(y) == type(list):
        #         for i in y:
        #             print i
        #             print('\n')
        #     print '%s - %s' % (y, lo.file_dict[y])  # Вывод на экран
        # smart_rm = Clever_rm.Clever_rm()
        # if not outlist[1][1]:
        #     smart_rm.remove_to_trash_file(outlist[1][0])

    # parser = add_parser()
    # args = parser.parse_args()
    #
    # # how to control namespaces???
    #
    # if args.show_trash:
    #     Clever_rm.watch_trash()
    #
    #
    #             # if args.cleverrm:
                #     this_path = unicode(os.path.abspath(args.path))
                #     Logwriter.write_json_log(this_path)
                #     Clever_rm.simple_move(this_path)
                # elif args.lstrash:
                #     Clever_rm.watch_trash()


if __name__ == '__main__':
    main()

