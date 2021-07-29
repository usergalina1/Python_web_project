import unittest


class MyTestCase1(unittest.TestCase):
    # Create python function that performs the following action:
    def test_two_secvence(self):

        # 1) takes 2 lists as input
        list1 =[1,3,5,7]
        list2 =[7,1,5,3]
   #     list2 =[1,3,5,7]

# 2) checks if the lists have same members, regardless of order
        result1 = sorted(list1)
        result2 = sorted(list2)
        self.assertEqual(result1, result2, 'Something wrong with your lists')

# 3) does not effect the original order within either list
        print(result1, result2)

# 4) return True if the lists have the same members

        self.assertListEqual(result1, result2, "Sorry,  lists are not a  twins")

# or False if they have different members
        self.assertFalse(result1 != result2, "They are different")