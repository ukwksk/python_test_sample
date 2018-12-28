# -*- coding: utf-8 -*-
import unittest

from src import add


class AddTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_fail(self):
        self.assertEqual(add(1, 2), 5)
