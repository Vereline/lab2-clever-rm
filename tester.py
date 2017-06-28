#! usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import shutil
from smartrm.Trash import *
from smartrm.Smart_rm import *
from smartrm.File_delete_configurator import DEFAULT_CONFIG
import smartrm.Argparser
import smartrm.File_delete_configurator
import smartrm.Logger

EXIT_CODES = {
            'success': 0,
            'conflict': 1,
            'error': 2,
            'no_file': 3}


class TestSMART(unittest.TestCase):

    def setUp(self):  # create files for tests, preprocessing
        os.mkdir('test_directory')

        files = ['1', '12', '123']
        for file_ in files:
            with open('test_directory/%s' % file_, 'w'):
                pass
        more_files = ['abcd', 'abcde', 'abcdef']
        for file_ in more_files:
            with open('%s' % file_, 'w'):
                pass
        self.question_for_true = self.q_true
        self.question_for_false = self.q_false

    def q_true(self, string):
        return True

    def q_false(self, string):
        return False

    def test_remove_files(self):
        trash = Trash(DEFAULT_CONFIG['path'], DEFAULT_CONFIG['trash_log_path'],
                      DEFAULT_CONFIG['trash_log_path_txt'],
                      DEFAULT_CONFIG['policy_time'], DEFAULT_CONFIG['policy_size'], DEFAULT_CONFIG['max_size'],
                      DEFAULT_CONFIG['current_size'], DEFAULT_CONFIG['max_capacity'], DEFAULT_CONFIG['max_time'], self.question_for_true)

        smartrm = SmartRm(DEFAULT_CONFIG['path'], self.question_for_true)
        path = os.path.abspath('test_directory/1')
        smartrm.operate_with_removal(path, EXIT_CODES, trash, dry_run=False, verbose=False)
        self.assertFalse(os.path.exists(path))
        self.assertTrue(not os.path.exists(path))
        # self.assertFalse(os.path.isfile())
        pass

    def test_recover_files(self):
        trash = Trash(DEFAULT_CONFIG['path'], DEFAULT_CONFIG['trash_log_path'],
                      DEFAULT_CONFIG['trash_log_path_txt'],
                      DEFAULT_CONFIG['policy_time'], DEFAULT_CONFIG['policy_size'], DEFAULT_CONFIG['max_size'],
                      DEFAULT_CONFIG['current_size'], DEFAULT_CONFIG['max_capacity'], DEFAULT_CONFIG['max_time'], self.question_for_true)

        smartrm = SmartRm(DEFAULT_CONFIG['path'], self.question_for_true)
        path = os.path.abspath('test_directory/1')
        smartrm.operate_with_removal(path, EXIT_CODES, trash, dry_run=False, verbose=False)
        trash.restore_trash_manually('1', dry_run=False, verbose=False)
        self.assertFalse(not os.path.exists(path))
        self.assertTrue(os.path.exists(path))

        pass

    def test_remove_by_regular(self):
        trash = Trash(DEFAULT_CONFIG['path'], DEFAULT_CONFIG['trash_log_path'],
                      DEFAULT_CONFIG['trash_log_path_txt'],
                      DEFAULT_CONFIG['policy_time'], DEFAULT_CONFIG['policy_size'], DEFAULT_CONFIG['max_size'],
                      DEFAULT_CONFIG['current_size'], DEFAULT_CONFIG['max_capacity'], DEFAULT_CONFIG['max_time'], self.question_for_true)

        smartrm = SmartRm(DEFAULT_CONFIG['path'], self.question_for_true)
        path = '^abcd'
        interactive = False
        smartrm.operate_with_regex_removal(path, interactive, trash, EXIT_CODES, dry_run=False, verbose=False)
        self.assertFalse(os.path.exists(os.path.abspath('abcd')))
        self.assertFalse(os.path.exists(os.path.abspath('abcde')))
        self.assertFalse(os.path.exists(os.path.abspath('abccdef')))

        self.assertTrue(not os.path.exists(os.path.abspath('abcd')))
        self.assertTrue(not os.path.exists(os.path.abspath('abcde')))
        self.assertTrue(not os.path.exists(os.path.abspath('abcdef')))
        # self.assertTrue(not os.path.exists(path))
        # self.assertFalse(os.path.isfile())
        pass

    def test_recover_by_regular(self):
        trash = Trash(DEFAULT_CONFIG['path'], DEFAULT_CONFIG['trash_log_path'],
                      DEFAULT_CONFIG['trash_log_path_txt'],
                      DEFAULT_CONFIG['policy_time'], DEFAULT_CONFIG['policy_size'], DEFAULT_CONFIG['max_size'],
                      DEFAULT_CONFIG['current_size'], DEFAULT_CONFIG['max_capacity'], DEFAULT_CONFIG['max_time'], self.question_for_true)

        smartrm = SmartRm(DEFAULT_CONFIG['path'], self.question_for_true)
        path = '^abcd'
        interactive = False
        smartrm.operate_with_regex_removal(path, interactive, trash, EXIT_CODES, dry_run=False, verbose=False)
        trash.restore_by_regular(path, dry_run=False, interactive=False, verbose=True)
        self.assertFalse(not os.path.exists(os.path.abspath('abcd')))
        self.assertFalse(not os.path.exists(os.path.abspath('abcde')))
        self.assertFalse(not os.path.exists(os.path.abspath('abcdef')))

        self.assertTrue(os.path.exists(os.path.abspath('abcd')))
        self.assertTrue(os.path.exists(os.path.abspath('abcde')))
        self.assertTrue(os.path.exists(os.path.abspath('abcdef')))
        # self.assertTrue(not os.path.exists(path))
        # self.assertFalse(os.path.isfile())

    def test_remove_directory(self):
        trash = Trash(DEFAULT_CONFIG['path'], DEFAULT_CONFIG['trash_log_path'],
                      DEFAULT_CONFIG['trash_log_path_txt'],
                      DEFAULT_CONFIG['policy_time'], DEFAULT_CONFIG['policy_size'], DEFAULT_CONFIG['max_size'],
                      DEFAULT_CONFIG['current_size'], DEFAULT_CONFIG['max_capacity'], DEFAULT_CONFIG['max_time'], self.question_for_true)

        smartrm = SmartRm(DEFAULT_CONFIG['path'], self.question_for_true)
        path = os.path.abspath('test_directory')
        smartrm.operate_with_removal(path, EXIT_CODES, trash, dry_run=False, verbose=False)
        self.assertFalse(os.path.exists(path))
        self.assertTrue(not os.path.exists(path))

    def test_remove_with_dry_run(self):
        trash = Trash(DEFAULT_CONFIG['path'], DEFAULT_CONFIG['trash_log_path'],
                      DEFAULT_CONFIG['trash_log_path_txt'],
                      DEFAULT_CONFIG['policy_time'], DEFAULT_CONFIG['policy_size'], DEFAULT_CONFIG['max_size'],
                      DEFAULT_CONFIG['current_size'], DEFAULT_CONFIG['max_capacity'], DEFAULT_CONFIG['max_time'], self.question_for_true)

        smartrm = SmartRm(DEFAULT_CONFIG['path'], self.question_for_true)
        path = os.path.abspath('test_directory/1')
        smartrm.operate_with_removal(path, EXIT_CODES, trash, dry_run=True, verbose=False)
        self.assertFalse(not os.path.exists(path))
        self.assertTrue(os.path.exists(path))

    def test_restore_with_dry_run(self):
        trash = Trash(DEFAULT_CONFIG['path'], DEFAULT_CONFIG['trash_log_path'],
                      DEFAULT_CONFIG['trash_log_path_txt'],
                      DEFAULT_CONFIG['policy_time'], DEFAULT_CONFIG['policy_size'], DEFAULT_CONFIG['max_size'],
                      DEFAULT_CONFIG['current_size'], DEFAULT_CONFIG['max_capacity'], DEFAULT_CONFIG['max_time'], self.question_for_true)

        smartrm = SmartRm(DEFAULT_CONFIG['path'], self.question_for_true)
        path = os.path.abspath('test_directory/123')
        smartrm.operate_with_removal(path, EXIT_CODES, trash, dry_run=False, verbose=False)
        trash.restore_trash_manually('123', dry_run=True, verbose=False)
        self.assertFalse(os.path.exists(path))
        self.assertTrue(not os.path.exists(path))

    def test_default_configures(self):
        txt_path = '/home/vereline/Configure.txt'
        json_path = '/home/vereline/Configure.json'
        if os.path.exists(txt_path):
            os.remove(txt_path)
        if os.path.exists(json_path):
            os.remove(json_path)

        argparser = smartrm.Argparser.Argparser()
        conf = smartrm.File_delete_configurator.FileDeleteConfigurator(argparser, paths='')

        self.assertFalse(not os.path.exists(txt_path))
        self.assertTrue(os.path.exists(txt_path))
        self.assertFalse(not os.path.exists(json_path))
        self.assertTrue(os.path.exists(json_path))

    def test_trash_creation(self):
        path = DEFAULT_CONFIG['path']
        if os.path.exists(path):
            shutil.rmtree(path)
        trash = Trash(DEFAULT_CONFIG['path'], DEFAULT_CONFIG['trash_log_path'],
                      DEFAULT_CONFIG['trash_log_path_txt'],
                      DEFAULT_CONFIG['policy_time'], DEFAULT_CONFIG['policy_size'], DEFAULT_CONFIG['max_size'],
                      DEFAULT_CONFIG['current_size'], DEFAULT_CONFIG['max_capacity'], DEFAULT_CONFIG['max_time'], self.question_for_true)

        self.assertFalse(not os.path.exists(path))
        self.assertTrue(os.path.exists(path))

    def test_trash_restore_conflict(self):
        trash = Trash(DEFAULT_CONFIG['path'], DEFAULT_CONFIG['trash_log_path'],
                      DEFAULT_CONFIG['trash_log_path_txt'],
                      DEFAULT_CONFIG['policy_time'], DEFAULT_CONFIG['policy_size'], DEFAULT_CONFIG['max_size'],
                      DEFAULT_CONFIG['current_size'], DEFAULT_CONFIG['max_capacity'], DEFAULT_CONFIG['max_time'], self.question_for_true)
        smartrm = SmartRm(DEFAULT_CONFIG['path'], self.question_for_true)
        path = os.path.abspath('abcd')
        smartrm.operate_with_removal(path, EXIT_CODES, trash, dry_run=False, verbose=False)
        file = open('abcd', 'w')
        file.close()
        smartrm.operate_with_removal(path, EXIT_CODES, trash, dry_run=False, verbose=False)
        files_ids = trash.search_for_all_files_with_this_name('abcd')
        trash.restore_trash_manually('abcd', dry_run=False, verbose=False)
        exists = False
        for new_path in files_ids:
            new_path = path + '_' + new_path
            if os.path.exists(new_path):
                exists = True

        self.assertFalse(not os.path.exists(path))
        self.assertTrue(os.path.exists(path))
        self.assertFalse(not exists)
        self.assertTrue(exists)

    def test_trash_remove_conflict(self):
        trash = Trash(DEFAULT_CONFIG['path'], DEFAULT_CONFIG['trash_log_path'],
                      DEFAULT_CONFIG['trash_log_path_txt'],
                      DEFAULT_CONFIG['policy_time'], DEFAULT_CONFIG['policy_size'], DEFAULT_CONFIG['max_size'],
                      DEFAULT_CONFIG['current_size'], DEFAULT_CONFIG['max_capacity'], DEFAULT_CONFIG['max_time'], self.question_for_true)
        smartrm = SmartRm(DEFAULT_CONFIG['path'], self.question_for_true)
        path = os.path.abspath('abcd')
        smartrm.operate_with_removal(path, EXIT_CODES, trash, dry_run=False, verbose=False)
        file_ = open('abcd', 'w')
        file_.close()
        smartrm.operate_with_removal(path, EXIT_CODES, trash, dry_run=False, verbose=False)
        files_ids = trash.search_for_all_files_with_this_name('abcd')
        trash.delete_manually('abcd', dry_run=False, verbose=False)
        for file_id in files_ids:
            for elem in trash.log_writer.file_dict_arr:
                self.assertNotEqual(file_id, elem['id'])

    def test_logging_file_creation(self):
        path = DEFAULT_CONFIG['trash_logging_path']
        if os.path.exists(path):
            os.remove(path)

        logger = smartrm.Logger.Logger(path, silent=True)
        self.assertFalse(not os.path.exists(path))
        self.assertTrue(os.path.exists(path))

    def tearDown(self):
        # empty_trash(trash_path, info_path, dry, silent)
        if os.path.exists('test_directory'):
            shutil.rmtree('test_directory')
        if os.path.exists('abcd'):
            os.remove('abcd')
        if os.path.exists('abcde'):
            os.remove('abcde')
        if os.path.exists('abcdef'):
            os.remove('abcdef')


if __name__ == '__main__':
    unittest.main()
