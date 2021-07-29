import unittest

# Homework 1
# Using PyCharm create a new unittest.TestCase class to test the code within hw.py file (attached)
# Create at least 2 negative test cases, and at least 6 total test cases.
# If you are more advanced try testing using list/dict...
# We will learn about list/dict in the next session :)


def vowel_counter(word) -> int:
    count = 0
    if type(word) is list:
        for x in word:
            count += vowel_counter(x)
    elif type(word) is dict:
        for x, y in word.items():
            count += vowel_counter(x)
            count += vowel_counter(y)
    elif type(word) is not str:
        return count
    elif not word.isascii():
        raise ValueError("Sorry, non English words are not supported at this time")

    vowel = set("aeiou")

    for letter in word:
        if letter.lower() in vowel:
            count = count + 1

    return count

#Ellie's explanation of Homework
class TestVowelCount(unittest.TestCase):
    # positive smoke test
    def test_small_word(self):
        input = "dog"
        expected = 1
        actual = vowel_counter(input)
        self.assertEqual(expected, actual, "For some reason the test failed")

    def test_sentence(self):
        sentence = "It's a great Tuesday evening!"
        actual_count = vowel_counter(sentence)
        expected_count = 10
        self.assertTrue(expected_count == actual_count, f"The actual count of vowels {actual_count} in the input '{sentence}'"
                                                        f" did not match expected count {expected_count}.")

    #negative test
    def test_int_input(self):
        input = 266
        expected = 0
        actual = vowel_counter(input)
        self.assertEqual(expected,actual)

    #localization test
    def test_russian_word(self):
        word = "корова"
        self.assertRaises(ValueError, lambda : vowel_counter(word))

    #positive test
    def test_no_vowel_input(self):
        word = 'sdfghjLKJH'
        self.assertEqual(0, vowel_counter(word))

    # positive test
    def test_empty_input(self):
        word = ""
        self.assertEqual(0, vowel_counter(word))

    #negative test
    def test_object_input(self):
        obj = object()
        self.assertEqual(0, vowel_counter(obj))


# My Homework
class MyTestCase(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(5, vowel_counter("revolution"))

    def test_negative_digits(self):
        self.assertEqual(0, vowel_counter(0.38383))

    def test_count_vowels_true(self):
        vowels = vowel_counter("revolution")
        print(vowels)
        self.assertTrue(vowels)

    def test_negative_only_consonants(self):
        self.assertEqual(0, vowel_counter("rvltn"))

    def test_assert_false(self):
        a = vowel_counter('aoi')
        print(a)
        self.assertFalse(a == 0)

    def test_negative_only_chars(self):
        self.assertEqual(0, vowel_counter('=+!?><'))

    def test_negative_empty(self):
        self.assertEqual(0, vowel_counter(" "))

    def test_negative_string(self):
        self.assertEqual(6, vowel_counter("Galina Demysheva"))

    def test_negative_mix_of_chars(self):
        self.assertEqual(1, vowel_counter("1234@@##$%John"))

    def test_negative_foreign_chars(self):
        self.assertEqual(0, vowel_counter("Галина"))





if __name__ == '__main__':
    unittest.main()
