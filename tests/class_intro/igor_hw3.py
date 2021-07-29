import unittest
from unittest import skip


def input_numeric(value):

    input_a = value
    print(type(input_a), input_a)

    if type(input_a) is int:
        result = [int(x) for x in str(input_a)]
        print("The list from number is " + str(result))


    elif type(input_a) is float:
        res = sorted(str(value))
        res.pop(0)
        print(res)
        print("The list from number is " + str(res))

    elif type(input_a) is list:
        res = (str(input_a))
        print(res)


    elif type(input_a) is not int:
        print (input_a)
        raise TypeError('It is not a digits')




class MyTestCase(unittest.TestCase):

    def test_numeric_input(self):
        value = 7153
        input_numeric(value)
        self.assertTrue(type(value), int)

    def test_convert_in_list_integers(self):
        value = 0.0056
        print("The original number is " + str(value))
        input_numeric(value)

    def test_text(self):
        value = "abvgd"
        print("The original value is " + str(value))
        input_numeric(value)
        self.assertRaises(TypeError)


    def test_list(self):
        try:
            value = ['sss', 13, 12, 14]
            print("The original value is " + str(value))
            input_numeric(value)
        except TypeError:

            print(value)
        return False


        self.assertRaises(TypeError)

            # return True

if __name__ == '__main__':
    unittest.main()
