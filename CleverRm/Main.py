#! usr/bin/env python
# -*- coding: utf-8 -*-

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
        smart_rm = Clever_rm.Clever_rm()
        if not outlist[1][1]:
            smart_rm.remove_to_trash_file(outlist[1][0])

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

