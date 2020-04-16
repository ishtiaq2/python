import unittest
import test_module

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = test_module.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = test_module.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()


# the second test will fail, so you have to update your cap_text function
# if you want to capitalize the first letter of each word OR
# change the test, assertEqual to 'Monty python'
