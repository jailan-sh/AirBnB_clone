#!/usr/bin/python3
"""
tests for class Review
"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """ unittest for city """
    def test_no_args(self):
        self.assertEqual(Review, type(Review()))
    def test_def_value(self):
        """ test values"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
