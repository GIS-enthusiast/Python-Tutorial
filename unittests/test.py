import unittest
import main


class TestMain(unittest.TestCase):
    def test_do_stuff(self):  # name of function in main9
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):  # name of function in main9
        test_param = 'jejweg'
        result = main.do_stuff(test_param)
        # or better, use assertIsInstance
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):  # name of function in main9
        test_param = [3, 4]
        result = main.do_stuff(test_param)
        # self.assertTrue(isinstance(result, TypeError))
        self.assertIsInstance(result, TypeError)

    def test_do_stuff4(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff5(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff6(self):
        test_param = 4
        result = main.do_stuff(test_param)
        self.assertEqual(result, 9)


unittest.main()
