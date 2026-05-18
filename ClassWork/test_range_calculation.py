from unittest import TestCase

import range_calculation

class TestFindingTheLargest(TestCase):

    def test_that_finding_the_largest_exists(self):
        range_calculation.finding_the_largest([2, 5, 7, 9, 20])

    def test_that_finding_the_largest_returns_the_correct_value(self):
        actual = range_calculation.finding_the_largest([2, 5, 7, 9, 20])
        expected = 20
        self.assertEqual(actual, expected)


class TestFindingTheSmallest(TestCase):

    def test_that_finding_the_smallest_exists(self):
        range_calculation.finding_the_smallest([2, 5, 7, 9, 20])

    def test_that_finding_the_smallest_returns_the_correct_value(self):
        actual = range_calculation.finding_the_smallest([2, 5, 7, 9, 20])
        expected = 2
        self.assertEqual(actual, expected)

class TestCalculatingTheRange(TestCase):

    def test_that_calculating_the_range_exists(self):
        range_calculation.calculating_the_range()

    def test_that_calculating_the_range_returns_the_correct_value(self):
        actual = range_calculation.calculating_the_range()
        expected = 18
        self.assertEqual(actual, expected)
