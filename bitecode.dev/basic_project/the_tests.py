import unittest
#Import the code we need to test:
from the_code_to_test import add

#create a class that inherits from Testcase. This is necessary for unittest to detect it as a test, and to provide methods like self.asserEqual
class TestAddFunction(unittest.TestCase):
    def test_add_integers(self):
        result = add(1, 2)
        self.assertEqual(result, 3)
        result = add(1, -2)
        self.assertEqual(result, -1)
    
    def test_add_strings(self):
        result = add ("1", "2")
        self.assertEqual(result, "12")

    def test_add_floats(self):
        result = add(0.1, 0.2)
        self.assertEqual(result, 0.3)

    def test_add_mixed_types(self):
        add(1, "2")

if __name__ == "__main__":
    unittest.main()

