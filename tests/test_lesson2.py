import unittest


class MyTestCase(unittest.TestCase):
    def test_reverse_string(self):
        sentence = "I am a happy person"
        expected = "Person happy a am I"

        ls_sentence = sentence.split()
        rv_list = list(reversed(ls_sentence))
        new_sentence = " ".join(rv_list)
        result = new_sentence[0].upper() + new_sentence[1:]

        #in one string:
      #  result = " ".join(list(reversed(sentence.split())))[0].upper() + \
       #          " ".join(list(reversed(sentence.split())))[1:]
        self.assertEqual(expected, result)


class TestReverseTheSentence(unittest.TestCase):
    def test_reverse_the_sentence(self):
        sentence = "I almost understood the topic"
        expected_result = "Topic the understood almost I"
        
        ls_sentence = sentence.split()
        new_reversed_ls_sentence = list(reversed(ls_sentence))
        actual_result = new_reversed_ls_sentence[0].capitalize() + " " + " ".join(new_reversed_ls_sentence[1:])
        self.assertEqual(expected_result, actual_result,
                         f"Actual result '{actual_result}' is not equal expected result '{expected_result}'.")