import unittest
from mylist import *
from stack import *

class TestLinkedStack(unittest.TestCase):
    def test_init(self):
        """
        Check that the fields are right for an empty stack.
        """
        stack = LinkedStack()
        self.assertTrue(stack.isEmpty(), "The stack is not empty.")
        self.assertEqual(stack._size, 0, "The size is not 0.")
        self.assertIsNone(stack._top, "The top of the stack is not None.")
        self.assertEqual(str(stack), "empty stack", "The string representation of an empty stack failed.")

    def test_peek_empty(self):
        """
        Peek an empty stack. Check the size and str and returned value (None).
        """
        stack = LinkedStack()
        peeked = stack.peek()
        self.assertIsNone(peeked, "Peeking an empty stack does not return None.")
        self.assertEqual(stack._size, 0, "The size is not 0.")
        self.assertEqual(str(stack), "empty stack", "The string representation of an empty stack failed.")

    def test_pop_empty(self):
        """
        Pop an empty stack. Check the size and str and returned value (None).
        """
        stack = LinkedStack()
        self.assertIsNone(stack.pop(), "Popping an empty stack failed to return None.")
        self.assertEqual(stack._size, 0, "The size is not 0.")
        self.assertEqual(str(stack), "empty stack", "The string representation of an empty stack failed.")


    def test_push_only(self):
        """
        Push an item onto an empty stack. Check the size and str.
        """
        stack = LinkedStack()
        stack.push("A")
        self.assertEqual(stack._size, 1, "The size failed to increment.")
        self.assertEqual(str(stack), "top --> A", "The string representation after push is wrong.")

    def test_push(self):
        """
        Push a few items onto a stack. Check the size and str.
        """
        stack = LinkedStack()
        stack.push("A")
        stack.push("B")
        stack.push("C")
        self.assertEqual(stack._size, 3, "The size failed to increment.")
        self.assertEqual(str(stack), "top --> C B A", "The string representation after push is wrong.")

    def test_peek(self):
        """
        Push a few items onto a stack. Peek it. Check the size and str returned value (last item pushed).
        """
        stack = LinkedStack()
        stack.push("A")
        stack.push("B")
        stack.push("C")
        self.assertEqual(stack.peek(), "C", "Peeking stack failed to return last item.")
        self.assertEqual(stack._size, 3, "The size accidentally incremented after peek.")
        self.assertEqual(str(stack), "top --> C B A", "The string representation after peek is wrong.")

    def test_pop(self):
        """
        Push a few items onto a stack. Pop it. Check the size and str returned value (last item pushed).
        """
        stack = LinkedStack()
        stack.push("A")
        stack.push("B")
        stack.push("C")
        popped_value = stack.pop()
        self.assertEqual(popped_value, "C", "The popped value was not the proper item in the stack.")
        self.assertEqual(stack._size, 2, "The size did not decrease by 1 after peek.")
        self.assertEqual(str(stack), "top --> B A", "The string representation of a stack is wrong after popping.")

if __name__ == "__main__":
    unittest.main()