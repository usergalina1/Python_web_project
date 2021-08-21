import unittest


def find_sum(number1, number2) -> float:
    if number1 == None:
        number1 = 0
    if number2 == None:
        number2 = 0
    if type(number1) == str:
        raise ValueError('Please put integers')
    return number1 + number2


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        my_name: str = "Galina Demysheva"
        age: int = 51
        height: float = 170.0

        name_length = len(my_name) - 1
        # name_length * 2 < 51
        # name_length < 51 / 2

        self.assertTrue(name_length * 2 < age)

        self.assertLess(name_length, age / 2)

    def test_positive_valid_sum(self):
        self.assertEqual(10, find_sum(7, 3))

    def test_adding_negative_numbers(self):
        self.assertEqual(-3, find_sum(-5, 2))

    def test_none_input(self):
        self.assertEqual(5, find_sum(5, None))

    def test_negative_char_input(self):
        self.assertRaises(ValueError, lambda: find_sum('a', 'x'))

    def test_negative_char_number_input(self):
        self.assertRaises(TypeError, lambda: find_sum(4, 'x'))
