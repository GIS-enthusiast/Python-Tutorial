import unittest
import main9


class TestMain(unittest.TestCase):
    def test_do_stuff(self):  # name of function in main9
        test_param = 10
        result = main9.do_stuff(test_param)
        self.assertEqual(result, 15)


unittest.main()
