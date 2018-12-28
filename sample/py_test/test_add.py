# -*- coding: utf-8 -*-
from src import add


def test_add():
    assert add(1, 2) == 3


def test_add_fail():
    assert add(1, 2) == 5
