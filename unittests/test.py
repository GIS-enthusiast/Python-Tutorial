import unittest
import script


class TestMain(unittest.TestCase):
    def setUp(self):  # default method with unittest.
        print('about to test a function')
        # it runs this function before every unittest. you could use setUp to set up some default variables.

    def test_do_stuff(self):  # name of function in main9
        '''Hi! Comments can be added to tests so you can see them when running the tests.'''
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):  # name of function in main9
        test_param = 'jejweg'
        result = script.do_stuff(test_param)
        # or better, use assertIsInstance
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):  # name of function in main9
        test_param = [3, 4]
        result = script.do_stuff(test_param)
        # self.assertTrue(isinstance(result, TypeError))
        self.assertIsInstance(result, TypeError)

    def test_do_stuff4(self):
        test_param = None
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff5(self):
        test_param = ''
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff6(self):
        test_param = 4
        result = script.do_stuff(test_param)
        self.assertEqual(result, 9)

    def test_do_stuff7(self):
        test_param = 0
        result = script.do_stuff(test_param)
        self.assertEqual(result, 5)

    def tearDown(self):
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()
