from HW03_Suraj_Nair_dictionary import Dictionary
from HW03_Suraj_Nair_logging import Logger


class Ui:
    def __init__(self) -> None:
        self.latest_typed_word = ''

    def get_user_input_recur(self, attempt_no: int, total_attempts: int, attempted_words: list, dictionary: Dictionary, logger) -> str:
        '''Gets input word from user until valid'''
        try:
            valid = 0  # 0 - False, 1- True, 2- Exit
            # Keep getting input from user until it's a unique 5 letter word
            while valid == 0:
                valid, word = self.get_user_input(attempt_no, total_attempts,
                                                  attempted_words, dictionary, logger)
            return word, valid
        except Exception as e:
            raise Exception(e)

    def get_user_input(self, attempt_no: int, total_attempts: int, attempted_words: list, dictionary: Dictionary, logger: Logger) -> tuple[bool, str]:
        '''Gets input word from user'''
        try:
            print(
                f'Attempt {attempt_no} / {total_attempts} --> Please enter a 5 letter word:')
            user_input = input().strip().upper()
            self.latest_typed_word = user_input
            if not user_input:
                print('Exiting game!')
                logger.write_log('User Exited the game\n')
                logger.close_log()
                return 2, ''
            valid = self.user_input_validation(
                user_input, attempted_words, dictionary)
            if valid:
                logger.write_log(f'User Input #{attempt_no}: {user_input}\n')
            else:
                logger.write_log(
                    f'Invalid User Input #{attempt_no}: {user_input}\n')
            return int(valid), user_input
        except Exception as e:
            raise Exception(e)

    def user_input_validation(self, user_input: str, attempted_words: list, dictionary: Dictionary) -> bool:
        if not user_input.isalpha():
            print("Only alphabets are allowed")
            return False
        if len(user_input) != 5:
            print('Only 5 letter words are allowed')
            return False
        if user_input in attempted_words:
            print(f'{user_input} has already been tried')
            return False
        if not dictionary.check_valid_word(user_input):
            print('Word is not a valid dictionary word')
            return False
        return True

    def print_green(self, word: str):
        '''Returns a string with Green color code prepended'''
        return '\033[92m'+word+'\033[0m'

    def print_red(self, word: str):
        '''Returns a string with Red color code prepended'''
        return f'\033[91m{word}\033[0m'

    def print_yellow(self, word: str):
        '''Returns a string with Yellow color code prepended'''
        return f'\033[93m{word}\033[0m'

    def __str__(self) -> str:
        return f'Last user input: {self.latest_typed_word}'
