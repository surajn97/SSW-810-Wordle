from unittest import result
import HW03_Suraj_Nair_ui as ui
import HW03_Suraj_Nair_dictionary as dictionary


def game_greetings(attempts):
    '''Basic Greetings before the game begins'''
    print('\n***** WORDLE *****\n')
    print(f'Guess the WORDLE in {attempts} tries.')
    print('Each guess must be a valid 5 letter word. Hit the enter button to submit.')
    print('After each guess, the color of the letters will change to show how close your guess was to the word.\n')
    print(ui.print_green('Green') +
          ' color shows letter is in the word and in the correct spot.')
    print(ui.print_yellow('Yellow') +
          ' color shows letter is in the word but in the wrong spot.')
    print(ui.print_red('Red')+' color shows letter is not in the word in any spot.\n')


def game_loop(attempts):
    '''Gives user x amount of attempts to guess the hidden word'''
    # Hidden word
    game_word, valid_words = dictionary.load_dictionary()
    game_word = 'BARRY'
    game_word = list(game_word.upper())
    guess = False
    # List of words entered by the user
    attempted_words = []
    for i in range(attempts):
        # Get Input from user and split the word into letters
        user_input = ui.get_user_input(
            i+1, attempts, attempted_words, valid_words)
        # Update the list of attempted words for future comparison
        attempted_words.append(user_input)
        user_input = list(user_input)
        # Create a temporary copy of the hidden word to manipulate
        temp_game_word = game_word.copy()
        # Compare the user word to the game word and check if user won
        if compare_word(user_input, temp_game_word):
            guess = True
            break
    if guess:
        print('You guessed the word correctly!!')
    else:
        print(f"The word was {''.join(game_word)}")
        print('Better luck next time!')
    print('Press enter to exit or guess another word')
    game_loop(6)


def compare_word(user_word, game_word):
    '''Compares the user input word with the hidden word and returns true if both are equal'''
    correct = 0
    result = ['']*len(game_word)
    for i in range(len(user_word)):
        if game_word[i] == user_word[i]:
            result[i] = ui.print_green(user_word[i])
            user_word[i] = game_word[i] = '#'
            correct += 1

    if correct == len(game_word):
        output = ''.join(result)
        print(eval(f"f'{output}'"))
        return True

    for i, letter in enumerate(user_word):
        if letter == '#':
            continue
        if letter in game_word:
            result[i] = ui.print_yellow(letter + '`')
            # Clear the letter so it's not searched again
            game_word[game_word.index(letter)] = '#'
        else:
            result[i] = ui.print_red(letter + '"')
        # Check if the word was correct
    output = ''.join(result)
    print(eval(f"f'{output}'"))
    return False


def main():
    total_attempts = 6
    game_greetings(total_attempts)
    game_loop(total_attempts)


if __name__ == "__main__":
    main()
