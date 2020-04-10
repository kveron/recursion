from simple_recursion import *
from unittest import TestCase


class FibonacciTestCase(TestCase):
    def setUp(self):
        self.fibonacci_test_data = [
            [1, 1], [2, 1], [3, 2], [4, 3],
            [5, 5], [6, 8], [7, 13], [8, 21],
            [9, 34], [10, 55], [11, 89], [12, 144]
        ]

    def test_first_fibonacci_number_is_1(self):
        x = find_fibonacci(1)
        self.assertEqual(1, x)

    def test_second_fibonacci_number_is_1(self):
        x = find_fibonacci(2)
        self.assertEqual(1, x)

    def test_5th_fibonacci_number_is_5(self):
        x = find_fibonacci(5)
        self.assertEqual(5, x)

    def test_30th_fibonacci_number_is_832040(self):
        x = find_fibonacci(30)
        self.assertEqual(832040, x)

    def test_fibonacci_test_data(self):
        for n, expected_number in self.fibonacci_test_data:
            actual_number = find_fibonacci(n)
            self.assertEqual(expected_number, actual_number)


class MaximumTestCase(TestCase):
    def test_maximum_number_is_92(self):
        x = maximum([92, 1, 2, 3, 4, 5, 6, 9, 11, 17, 0, 2, 7, 49, -17])
        self.assertEqual(92, x)

    def test_maximum_number_is_190(self):
        x = maximum([-347, 92, 190, 33, 64])
        self.assertEqual(190, x)

    def test_maximum_number_is_10(self):
        x = maximum([10, 9, 8, 3, 6])
        self.assertEqual(10, x)

    def test_maximum_number_is_192(self):
        x = maximum([192])
        self.assertEqual(192, x)

    def test_maximum_number_is_11(self):
        x = maximum([1, 2, 3, 4, 5, 6, 0, 10, 11, 11, 9, -9999999])
        self.assertEqual(11, x)


class FromAToBTestCase(TestCase):
    def test_from_a_to_b_with_positive_numbers(self):
        actual_list = from_a_to_b(0, 10, [])
        expected_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertListEqual(expected_list, actual_list)

    def test_from_a_to_b_with_negative_numbers(self):
        actual_list = from_a_to_b(-8, -5, [])
        expected_list = [-8, -7, -6, -5]
        self.assertListEqual(expected_list, actual_list)

    def test_from_a_to_b_with_mixed_numbers(self):
        actual_list = from_a_to_b(-3, 3, [])
        expected_list = [-3, -2, -1, 0, 1, 2, 3]
        self.assertListEqual(expected_list, actual_list)

    def test_from_a_to_b_with_wrong_numbers(self):
        actual_message = from_a_to_b(5, 0, [])
        expected_message = "a must be less than b"
        self.assertEqual(expected_message, actual_message)
