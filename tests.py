import unittest
import sys
from inchatgram import choice

class TestChoiceMethods(unittest.TestCase):

    def test_choice(self):
        self.assertEqual(choice('y'), True)
        self.assertEqual(choice('n'), False)

if __name__ == "__main__":
    unittest.main()