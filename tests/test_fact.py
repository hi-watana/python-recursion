import unittest
import fact

class FactTest(unittest.TestCase):
    def test_fact_n_is_0(self):
        self.assertEqual(fact.fact(0), 1)

    def test_fact_n_is_6(self):
        self.assertEqual(fact.fact(6), 720)

