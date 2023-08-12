#!/usr/bin/python3
"""
tests for class State
"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """ unittest for state """
    def test_no_args(self):
        self.assertEqual(State, type(State()))
    def test_def_value(self):
        """ test values"""
        state = State()
        self.assertEqual(state.name, "")
