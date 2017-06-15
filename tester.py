#! usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import shutil


class TestSMART(unittest.TestCase):

    def setUp(self):  # create files for tests, preprocessing
        os.mkdir("test_directory")

        files = ["1", "12", "123"]
        for file_ in files:
            with open("test_directory/%s.txt" % file_, "w"):
                pass

    def test_remove_files(self):
        pass

    def test_recover_files(self):
        pass

    def test_remove_by_regular(self):
        pass

    def test_recover_by_regular(self):
        pass

    def test_clean_trash(self):
        pass

    def test_recover_all_trash(self):
        pass

    def test_remove_from_trash(self):
        pass

    def test_remove_with_dry_run(self):
        pass

    def tearDown(self):
        # empty_trash(trash_path, info_path, dry, silent)
        if os.path.exists("test_directory"):
            shutil.rmtree("test_directory")

if __name__ == '__main__':
    unittest.main()
