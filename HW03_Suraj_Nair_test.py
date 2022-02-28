import unittest
from unittest.mock import patch
import HW03_Suraj_Nair_ui as ui
import HW03_Suraj_Nair_dictionary as dictionary
import HW03_Suraj_Nair_wordle as wordle


class WordleTest (unittest.TestCase):

    words_list_resource = None

    @classmethod
    def setUpClass(cls):
        temp, cls.words_list_resource = dictionary.load_dictionary()

    @classmethod
    def tearDownClass(cls):
        cls.words_list_resource = None

    def test_compare_word_true(self) -> None:
        '''Test if two words are same or not'''
        t: wordle.Wordle = wordle.Wordle()
        self.assertTrue(t.compare_word('trial', 'trial'))

    def test_compare_word_false(self) -> None:
        '''Test if two words are same or not'''
        t: wordle.Wordle = wordle.Wordle()
        self.assertFalse(t.compare_word('hello', 'trial'))

    def test_check_if_dictionary_exists(self) -> None:
        '''Test if the word file exists'''
        self.assertTrue(dictionary.check_file_exists('words.txt'))

    def test_check_if_dictionary_loaded(self) -> None:
        '''Test if the word file is loaded correctly with a list of 5 letter words'''
        temp, words_list = dictionary.load_dictionary()
        self.assertTrue(len(words_list) != 0)
        self.assertTrue(not any(len(word) != 5 for word in words_list))

    def test_valid_dictionary_word_true(self) -> None:
        '''Check if a word is a valid dictionary word'''
        self.assertTrue(dictionary.check_valid_word(
            self.words_list_resource, 'arise'))

    def test_valid_dictionary_word_false(self) -> None:
        '''Check if a word is a valid dictionary word'''
        self.assertFalse(dictionary.check_valid_word(
            self.words_list_resource, 'asdfg'))

    @patch('builtins.input', side_effect=['Hello'])
    def test_get_user_input_true(self, mock_inputs) -> None:
        """Check if User Input is correct"""
        self.assertEqual(ui.get_user_input(
            1, 6, ['trial', 'arise', 'paper'], self.words_list_resource), (True, 'HELLO'))

    @patch('builtins.input', side_effect=['doctor'])
    def test_get_user_input_length_false(self, mock_inputs) -> None:
        """User Input should return false as it is a 6 letter word"""
        self.assertEqual(ui.get_user_input(
            1, 6, ['trial', 'arise', 'paper'], self.words_list_resource), (False, 'DOCTOR'))

    @patch('builtins.input', side_effect=['asdfg'])
    def test_get_user_input_valid_false(self, mock_inputs) -> None:
        """User Input should return false as it is not a valid word"""
        self.assertEqual(ui.get_user_input(
            1, 6, ['trial', 'arise', 'paper'], self.words_list_resource), (False, 'ASDFG'))

    def test_user_input_check_true(self) -> None:
        '''Check if a word satisfies all conditions'''
        self.assertTrue(ui.user_input_validation('hello', ['trial', 'arise', 'paper'],
                                                 self.words_list_resource))

    def test_user_input_check_false(self) -> None:
        '''Should fail as the word is in attempted words'''
        self.assertFalse(ui.user_input_validation('trial', ['trial', 'arise', 'paper'],
                                                  self.words_list_resource))

    def test_user_input_check_false_length(self) -> None:
        '''Should fail as the word is not 5 letter'''
        self.assertFalse(ui.user_input_validation('doctor', ['trial', 'arise', 'paper'],
                                                  self.words_list_resource))

    def test_user_input_check_false_alpha(self) -> None:
        '''Should fail as the word is not strictly alphabets'''
        self.assertFalse(ui.user_input_validation('a@s8t', ['trial', 'arise', 'paper'],
                                                  self.words_list_resource))


if __name__ == '__main__':
    unittest.main()
