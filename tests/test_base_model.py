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


