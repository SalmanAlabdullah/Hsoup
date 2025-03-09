from sum import sum
import unittest

class testsum(unittest.TestCase):
    def test(self):
        self.assertEqual(('the result is : ', 5), sum(1,4))

if __name__ == '__main__':
    unittest.main()