import unittest
import fib

class FibTest(unittest.TestCase):
    def test_fib_n_is_0(self):
        self.assertEqual(fib.fib(0), 1)

    def test_fib_n_is_1(self):
        self.assertEqual(fib.fib(1), 1)

    def test_fib_n_is_4(self):
        self.assertEqual(fib.fib(4), 5)

    def test_fib_n_is_10(self):
        self.assertEqual(fib.fib(10), 89)
