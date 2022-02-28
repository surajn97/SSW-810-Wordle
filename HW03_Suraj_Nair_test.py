import unittest
from unittest.mock import patch
import HW03_Suraj_Nair_ui as ui
import HW03_Suraj_Nair_dictionary as dictionary
import HW03_Suraj_Nair_wordle as wordle
import HW03_Suraj_Nair_utility as utility
import HW03_Suraj_Nair_logging as logger


class WordleTest (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dic = dictionary.Dictionary()
        cls.dic.load_dictionary()
        cls.log = logger.Logger()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_log()

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
        self.assertTrue(self.dic.check_file_exists('words.txt'))

    def test_check_if_dictionary_loaded(self) -> None:
        '''Test if the word file is loaded correctly with a list of 5 letter words'''
        self.assertTrue(len(self.dic.words) != 0)
        self.assertTrue(not any(len(word) != 5 for word in self.dic.words))

    def test_valid_dictionary_word_true(self) -> None:
        '''Check if a word is a valid dictionary word'''
        self.assertTrue(self.dic.check_valid_word('arise'))

    def test_valid_dictionary_word_false(self) -> None:
        '''Check if a word is a valid dictionary word'''
        self.assertFalse(self.dic.check_valid_word('asdfg'))

    @patch('builtins.input', side_effect=['Hello'])
    def test_get_user_input_true(self, mock_inputs) -> None:
        """Check if User Input is correct"""
        self.assertEqual(ui.get_user_input(
            1, 6, ['trial', 'arise', 'paper'], self.dic, self.log), (True, 'HELLO'))

    @patch('builtins.input', side_effect=['doctor'])
    def test_get_user_input_length_false(self, mock_inputs) -> None:
        """User Input should return false as it is a 6 letter word"""
        self.assertEqual(ui.get_user_input(
            1, 6, ['trial', 'arise', 'paper'], self.dic, self.log), (False, 'DOCTOR'))

    @patch('builtins.input', side_effect=['asdfg'])
    def test_get_user_input_valid_false(self, mock_inputs) -> None:
        """User Input should return false as it is not a valid word"""
        self.assertEqual(ui.get_user_input(
            1, 6, ['trial', 'arise', 'paper'], self.dic, self.log), (False, 'ASDFG'))

    def test_user_input_check_true(self) -> None:
        '''Check if a word satisfies all conditions'''
        self.assertTrue(ui.user_input_validation('hello', ['trial', 'arise', 'paper'],
                                                 self.dic))

    def test_user_input_check_false(self) -> None:
        '''Should fail as the word is in attempted words'''
        self.assertFalse(ui.user_input_validation('trial', ['trial', 'arise', 'paper'],
                                                  self.dic))

    def test_user_input_check_false_length(self) -> None:
        '''Should fail as the word is not 5 letter'''
        self.assertFalse(ui.user_input_validation('doctor', ['trial', 'arise', 'paper'],
                                                  self.dic))

    def test_user_input_check_false_alpha(self) -> None:
        '''Should fail as the word is not strictly alphabets'''
        self.assertFalse(ui.user_input_validation('a@s8t', ['trial', 'arise', 'paper'],
                                                  self.dic))

    def test_utility(self) -> None:
        '''Should Pass as the words.txt file exists and can create a new file'''
        self.assertTrue(utility.load_dictionary())

    @patch('random.choice')
    def test_check_game_word(self, mock_random):
        '''To check if hello has already been used as a game word, the function should return a new random word'''
        # Set Random choice to hello
        mock_random.return_value = ["hello", "fixed"]
        dic = dictionary.Dictionary()
        # Add hello to already used words list
        dic.valid_words.append('hello')
        self.assertNotEqual(dic.load_dictionary(), 'hello')


if __name__ == '__main__':
    unittest.main()
