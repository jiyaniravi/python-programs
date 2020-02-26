"""
Module contains unit test cases for cap.py
"""
import unittest
import cap

class TestCap(unittest.TestCase):
    """
    Class contains unit test cases for cap.py
    """
    def test_one_word(self):
        """
        Should return true if word capitalized properly.
        """

        text = "hi"
        result = cap.cap_text(text)
        self.assertEqual(result, 'Hi')

    def test_multiple_words(self):
        """
        Should return true if words capitalized properly.
        """

        text = "hi world"
        result = cap.cap_text(text)
        self.assertEqual(result, 'Hi world')

if __name__ == "__main__":
    unittest.main()