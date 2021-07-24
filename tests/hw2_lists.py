import unittest

#Homework 1
#Create python function that performs the following action:
#1) takes 2 lists as input
#2) checks if the lists have same members, regardless of order
#3) does not effect the original order within either list
#4) return True if the lists have the same members
#or False if they have different members
#Example:
#[1,3,5,7] AND [7,1,5,3]  ->  True
#['a', 'b', 'c'] AND ['a', 'b', 'd'] -> False
#[9,8,7,6,5] AND [9,8,7,6] -> False
#Part 2:
#Test your function using a unittest.TestCase class
#Create at least 2 negative test cases, and at least 6 total test cases.
#Hint:
 #       self.assertEqual(a,d)
  #      self.assertListEqual(a,d)
   #     self.assertTrue(a==d)

   #Ellie
    # 1) takes 2 lists as input
def compare_lists(list1, list2):
    if type(list1) != list and type(list2) != list:
        raise TypeError("The data type of one or both of the inputs is not a list.")

    # ls1 = []
    # for item in list1:
    #     ls1.append(str(item))
    # ls2 = []
    # for item in list2:
    #     ls2.append(str(item))

    ls2 = list(list2[::])
    for item in list1:
        try:
            idx = ls2.index(item)
        except ValueError:
            return False
        ls2.pop(idx)

    return len(ls2) == 0

    # return sorted(ls1) == sorted(ls2)


class ListCompareTests(unittest.TestCase):
    def test_same_lists(self):
        ls1 = [1, 3, 6, 2]
        ls2 = [1, 3, 6, 2]
        self.assertTrue(compare_lists(ls1, ls2))

    def test_different_lists(self):
        ls1 = [1, 3, 6, 2]
        ls2 = [9, 8, 2, 4]
        self.assertFalse(compare_lists(ls1, ls2))

    def test_different_lengths(self):
        ls1 = [1, 3, 6, 2]
        ls2 = [1, 3, 6, 2, 4]
        self.assertFalse(compare_lists(ls1, ls2))

    def test_duplicate_values(self):
        ls1 = [1, 3, 6, 2, 1]
        ls2 = [1, 3, 6, 2, 3]
        self.assertFalse(compare_lists(ls1, ls2))

    def test_different_order(self):
        ls1 = [1, 3, 5, 7]
        ls2 = [7, 1, 5, 3]
        self.assertTrue(compare_lists(ls1, ls2))

    def test_char_list(self):
        ls1 = ['a', 'b', 'c']
        ls2 = ['a', 'b', 'd']
        self.assertFalse(compare_lists(ls1, ls2))

    # @unittest.expectedFailure
    def test_mixed_lists(self):
        ls1 = [False, 33, 'word']
        ls2 = [33, 'word', False]
        self.assertTrue(compare_lists(ls1, ls2))

    def test_mixed_types(self):
        ls1 = [4, 5, 6]
        ls2 = ['4', '5', '6']
        self.assertFalse(compare_lists(ls1, ls2))

    def test_unexpected_data_types(self):
        word1 = "abcde"
        word2 = "decba"
        self.assertRaises(TypeError, lambda :compare_lists(word1, word2))

    def test_other_collection(self):
        ls1 = [1, 3, 5, 7]
        ls2 = (1, 3, 5, 7)
        self.assertTrue(compare_lists(ls1, ls2))

    def test_with_dups(self):
        ls1 = [1, 2, 3, 2]
        ls2 = [1, 2, 3]
   # my code
class TestCheckingLists(unittest.TestCase):
    def test_check_if_two_lists_equal(self):
        # 1) takes 2 lists as input
        list1 = [1,3,5,7]
        list2 = [7,1,5,3]
        # 2) checks if the lists have same members, regardless of order
        new_list1 = sorted(list1)
        new_list2 = sorted(list2)
        self.assertListEqual(new_list1, new_list2, "Lists are not equal")

    def test_if_lists_have_same_number_of_members(self):
        list1 = [1,3,5,7]
        list2 = [7,1,5,3]
        member_count1 = len(list1)
        member_count2 = len(list2)
        self.assertTrue(member_count1 == member_count2, "Number of members is different")

       # 3) does not effect the original order within either list
    def test_check_if_two_lists_not_equal(self):
        list1 = ['a', 'b', 'c']
        list2 = ['a', 'b', 'd']
        self.assertNotEqual(list1, list2, "Lists are equal")

       # 4) return True if the lists have the same members
       # or False if they have different members
    def test_check_if_2_lists_not_equal(self):
        list1 = [9,8,7,6,5]
        list2 = [9,8,7,6]
        self.assertFalse(list1 == list2, "Lists are equal")


