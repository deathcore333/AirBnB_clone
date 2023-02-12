#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
from datetime import datetime
import inspect
import models
import unittest


BaseModel = models.base_model.BaseModel


class TestBaseModelDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    all_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('.....  For BaseModel Class  .....')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nBaseModel Class of Models Module\n'
        actual = models.base_model.__doc__
        self.assertEqual(expected, actual)

    def test_all_function_docs(self):
        """... tests for ALL DOCS for all funcions in db_storage file"""
        all_functions = TestBaseModelDocs.all_funcs
        for function in all_functions:
            self.assertIsNotNone(function[1].__doc__)

    def test_pep8_base_model(self):
        """... base_model.py conforms to PEP8 Style"""
        pep8style = pep8.StyleGuide(quiet=True)
        errors = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_file_is_executable(self):
        """... tests if file has correct permissions so user can execute"""
        file_stat = stat('models/base_model.py')
        permissions = str(oct(file_stat[0]))
        actual = int(permissions[5:-2]) >= 5
        self.assertTrue(actual)

