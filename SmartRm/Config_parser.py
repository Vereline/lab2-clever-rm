#! usr/bin/env python
# -*- coding: utf-8 -*-


import ConfigParser
import logging

class ConfParser(object):
    def __init__(self, path):
        self.parser = ConfigParser.ConfigParser()
        self.dict = {}
        self.parser.read(path)
        self.sections = self.parser.sections()

    def define_config_section(self, section):
        options = self.parser.options(section)
        for option in options:
            try:
                self.dict[option] = self.parser.get(section, option)
                if self.dict[option] == -1:
                    logging.DEBUG("skip: %s" % option)
                    # DebugPrint("skip: %s" % option)
            except():
                logging.ERROR("exception on %s!" % option)
                # print("exception on %s!" % option)
                self.dict[option] = None
