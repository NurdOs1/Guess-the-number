import unittest

from guess_number import generate_number, check_guess


class TestGuessNumber(unittest.TestCase):

    def test_generate_number(self):
        number = generate_number()
        self.assertTrue(1 <= number <= 100)

    def test_check_guess_less(self):
        result = check_guess(50, 100)
        self.assertEqual(result, "less")

    def test_check_guess_greater(self):
        result = check_guess(150, 100)
        self.assertEqual(result, "greater")

    def test_check_guess_equal(self):
        result = check_guess(100, 100)
        self.assertEqual(result, "equal")


if __name__ == "__main__":
    unittest.main()
