from unittest import result
import HW03_Suraj_Nair_ui as ui
import HW03_Suraj_Nair_dictionary as dictionary


class Wordle:
    def game_greetings(self, attempts: int):
        '''Basic Greetings before the game begins'''
        print('\n***** WORDLE *****\n')
        print(f'Guess the WORDLE in {attempts} tries.')
        print('Each guess must be a valid 5 letter word. Hit the enter button to submit.')
        print('After each guess, the color of the letters will change to show how close your guess was to the word.\n')
        print(ui.print_green('Green') +
              ' color shows letter is in the word and in the correct spot.')
        print(ui.print_yellow('Yellow') +
              ' color shows letter is in the word but in the wrong spot.')
        print(ui.print_red('Red') +
              ' color shows letter is not in the word in any spot.\n')



    def game_loop(self, attempts: int):
        '''Gives user x amount of attempts to guess the hidden word'''
        # Hidden word
        game_word, valid_words = dictionary.load_dictionary()
        print(game_word)
        guess = False
        # List of words entered by the user
        attempted_words = []
        success_attempt = 0
        for i in range(attempts):
            # Get Input from user and split the word into letters
            user_input = ui.get_user_input_recur(
                i+1, attempts, attempted_words, valid_words)
            # Update the list of attempted words for future comparison
            attempted_words.append(user_input)
            # Create a temporary copy of the hidden word to manipulate
            temp_game_word = game_word
            # Compare the user word to the game word and check if user won
            if self.compare_word(user_input, temp_game_word):
                guess = True
                success_attempt = i
                break
        if guess:
            print('You guessed the word correctly!!')
        else:
            print(f"The word was {''.join(game_word)}")
            print('Better luck next time!')
        print('Press enter to exit or guess another word')
        return success_attempt, guess


    def compare_word(self, user_word: str, game_word: str):
        '''Compares the user input word with the hidden word and returns true if both are equal'''
        correct = 0
        user_word = list(user_word.upper())
        game_word = list(game_word.upper())
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

    def game_statistics(self, number_of_games, win_percent, guess_distribuition):
        '''Game statistics info'''
        print('\n***** Game Statistics *****\n')
        print(f'{number_of_games} Games Played')
        print(f'{win_percent:.2f}% Win Rate')
        print('Guess Distribution:')
        for i, dist in enumerate(guess_distribuition):
            print(f'{i+1}: {dist}')


    def start_game(self):
        total_attempts = 6
        self.game_greetings(total_attempts)
        num_of_games, win_count = 0, 0
        game_distribuiton = [0]*6
        while True:
            success, win = self.game_loop(total_attempts)
            if win:
                win_count += 1
                game_distribuiton[success] += 1
            num_of_games += 1
            self.game_statistics(num_of_games, (win_count /
                                                num_of_games)*100, game_distribuiton)
            
if __name__ == "__main__":
    game = Wordle()
    game.start_game()
