import unittest
import guessinggame


class TestGuessingGame(unittest.TestCase):
    def test_input(self):
        result = guessinggame.run_guess(5, 5)
        self.assertTrue(result)
        # self.assertEqual(result, True) # above better.

    def test_input_wrong_guess(self):
        result = guessinggame.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = guessinggame.run_guess(11, 5)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = guessinggame.run_guess('11', 5)
        self.assertEqual(result, TypeError)


if __name__ == '__main__':
    unittest.main()
