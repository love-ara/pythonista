import unittest

from src.logistic_func import LogisticFunction


class TestLogisticFunction(unittest.TestCase):
    def setUp(self):
        self.logistic_fn = LogisticFunction()

    def test_calculate_below_50(self):
        self.assertEqual(9000, self.logistic_fn.calculate_payment(25))
        self.assertEqual(9800, self.logistic_fn.calculate_payment(30))
        self.assertEqual(11400, self.logistic_fn.calculate_payment(40))
        self.assertEqual(12840, self.logistic_fn.calculate_payment(49))

    def test_calculate_50_to_59(self):
        self.assertEqual(15000, self.logistic_fn.calculate_payment(50))
        self.assertEqual(16000, self.logistic_fn.calculate_payment(55))
        self.assertEqual(16800, self.logistic_fn.calculate_payment(59))

    def test_calculate_60_to_69(self):
        self.assertEqual(20500, self.logistic_fn.calculate_payment(62))
        self.assertEqual(21250, self.logistic_fn.calculate_payment(65))

    def test_calculate_70_and_above(self):
        self.assertEqual(40000, self.logistic_fn.calculate_payment(70))
        self.assertEqual(45000, self.logistic_fn.calculate_payment(80))
        self.assertEqual(50000, self.logistic_fn.calculate_payment(90))
        self.assertEqual(55000, self.logistic_fn.calculate_payment(100))

    def test_that_successful_deliveries_greater_than_100_throws_exception(self):
        self.assertRaises(ValueError, lambda: self.logistic_fn.calculate_payment(120))

    def test_negative_successful_delivery_provided_throws_exception(self):
        self.assertRaises(ValueError, lambda: self.logistic_fn.calculate_payment(-1))
