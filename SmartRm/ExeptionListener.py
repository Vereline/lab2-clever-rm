#! usr/bin/env python
# -*- coding: utf-8 -*-

class ExceptionListener():

    def __init__(self):
        self.exception = ''

    def check_size(path):
        print 'size of file is bigger than the size of trash'
        #  if the size of file is bigger than the size of trash
        return None

    def check_if_exists(path):
        print 'this file does not exist'
        #  if the size of file is bigger than the size of trash
        return None


    def check_is_system_directory(path):
        print 'deleted file or directory is system'
        #  if the deleted file or directory is system
        return None

    def check_capacity(path):
        #  if the trash is full/else(not enough disk space)
        print 'not enough disk space'
        return None

    def check_quantity_of_files(path):
        #  checks if the quantity of files is big/bigger than in config
        print 'too many files in trash'
        return None

    def check_cycles(path):
        print 'cycles detected'
        return None

    def check_if_conflict(path):
        # if in restore path this file already exists
        print 'conflict is detected'
        return None

