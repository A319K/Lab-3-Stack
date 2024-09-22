# teststack.py
import unittest
from stack import MyStack

class TestMyStack(unittest.TestCase):
    def test_init(self):
        temp = MyStack()
        self.assertEqual(len(temp._array), 2)
        self.assertEqual(temp._array[0], None)
        self.assertEqual(temp._array[1], None)
        self.assertEqual(len(temp), 0)

    def test_is_empty(self):
        temp = MyStack()
        self.assertTrue(temp.is_empty())
        temp.push(5)
        self.assertFalse(temp.is_empty())

    def test_push(self):
        temp = MyStack()
        temp.push(5)
        self.assertEqual(temp.top(), 5)

    def test_pop(self):
        temp = MyStack()
        temp.push(5)
        self.assertEqual(temp.pop(), 5)
        self.assertTrue(temp.is_empty())

    def test_top(self):
        temp = MyStack()
        temp.push(5)
        self.assertEqual(temp.top(), 5)
        self.assertFalse(temp.is_empty())
        
if __name__ == '__main__':
    unittest.main()
