import HW03_Suraj_Nair_dictionary as dictionary


def get_user_input_recur(attempt_no: int, total_attempts: int, attempted_words: list, valid_dictionary_words: list) -> str:
    '''Gets input word from user until valid'''
    valid = False
    # Keep getting input from user until it's a unique 5 letter word
    while not valid:
        valid, word = get_user_input(attempt_no, total_attempts,
                                     attempted_words, valid_dictionary_words)
    return word


def get_user_input(attempt_no: int, total_attempts: int, attempted_words: list, valid_dictionary_words: list) -> tuple[bool, str]:
    '''Gets input word from user'''
    print(
        f'Attempt {attempt_no} / {total_attempts} --> Please enter a 5 letter word:')
    user_input = input().strip().upper()
    if not user_input:
        print('Exiting game!')
        quit()
    valid = user_input_validation(
        user_input, attempted_words, valid_dictionary_words)
    return valid, user_input


def user_input_validation(user_input, attempted_words, valid_dictionary_words):
    if not user_input.isalpha():
        print("Only alphabets are allowed")
        return False
    if len(user_input) != 5:
        print('Only 5 letter words are allowed')
        return False
    if user_input in attempted_words:
        print(f'{user_input} has already been tried')
        return False
    if not dictionary.check_valid_word(valid_dictionary_words, user_input):
        print('Word is not a valid dictionary word')
        return False
    return True


def print_green(word: str):
    '''Returns a string with Green color code prepended'''
    return '\033[92m'+word+'\033[0m'


def print_red(word: str):
    '''Returns a string with Red color code prepended'''
    return f'\033[91m{word}\033[0m'


def print_yellow(word: str):
    '''Returns a string with Yellow color code prepended'''
    return f'\033[93m{word}\033[0m'
