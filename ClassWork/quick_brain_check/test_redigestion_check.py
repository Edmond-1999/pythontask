from unittest import TestCase

import redigestion_check

class TestDigitAdder(TestCase):

    def test_that_digit_adder_exists(self):
        redigestion_check.digit_adder("a5b2c1")

    def test_that_digit_adder_gives_the_correct_value(self):
        actual = redigestion_check.digit_adder("a5b2c1")
        expected = 8
        self.assertEqual(actual, expected)

class TestCaseToggle(TestCase):

    def test_that_case_toggle_exists(self):
        redigestion_check.case_toggle("PyThOn")

    def test_that_case_toggle_gives_the_correct_value(self):
        actual = redigestion_check.case_toggle("PyThOn")
        expected = "pYtHoN"
        self.assertEqual(actual, expected)

class TestSpaceCompressor(TestCase):

    def test_that_space_compressor_exists(self):
        redigestion_check.space_compressor("Hello World !")

    def test_that_space_compressor_gives_the_correct_value(self):
        actual = redigestion_check.space_compressor("Hello World !")
        expected = "Hello-World-!"
        self.assertEqual(actual, expected)

class TestTripleThreat(TestCase):

    def test_that_triple_threat_exists(self):
        redigestion_check.triple_threat("code")

    def test_that_triple_threat_gives_the_correct_value(self):
        actual = redigestion_check.triple_threat("code")
        expected = "cccooodddeee"
        self.assertEqual(actual, expected)
