from unittest import TestCase

import count_of_most_occuring

class TestMostOccuringCount(TestCase):

    def test_that_most_occuring_count_exists(self):
        count_of_most_occuring.most_occurring_count([1, 5, 5, 6, 4])

    def test_that_most_occuring_count_returns_the_correct_value(self):
        actual = count_of_most_occuring.most_occurring_count([1, 5, 5, 6, 4])
        expected = 2
        self.assertEqual(actual, expected)
