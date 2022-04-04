import HW03_Suraj_Nair_ui as userinterface
import HW03_Suraj_Nair_dictionary as dictionary
import HW03_Suraj_Nair_logging as logger
import HW03_Suraj_Nair_utility as utility
import HW03_Suraj_Nair_word_finder as wordFinder


class Wordle:
    def __init__(self, is_automated: bool = False, number_of_automated_games: int = 1) -> None:
        self.log = logger.Logger()
        self.dicti = dictionary.Dictionary()
        self.util = utility.Utility()
        # Create new Word file with 5 letter words
        self.util.load_dictionary()
        # Reads the new Word file with 5 letter words
        self.dicti.load_dictionary()
        self.ui = userinterface.Ui()
        self.is_automated = is_automated
        self.word_finder = wordFinder.WordFinder()
        self.number_of_automated_games = number_of_automated_games
        self.bad_letters = set()
        self.good_letters = set()
        self.correct_letters = set()

    def game_greetings(self, attempts: int) -> None:
        '''Basic Greetings before the game begins'''
        print('\n***** WORDLE *****\n')
        print(f'Guess the WORDLE in {attempts} tries.')
        print('Each guess must be a valid 5 letter word. Hit the enter button to submit.')
        print('After each guess, the color of the letters will change to show how close your guess was to the word.\n')
        print(self.ui.print_green('Green') +
              ' color shows letter is in the word and in the correct spot.')
        print(self.ui.print_yellow('Yellow') +
              ' color shows letter is in the word but in the wrong spot.')
        print(self.ui.print_red('Red') +
              ' color shows letter is not in the word in any spot.\n')

    def game_loop(self, attempts: int) -> tuple[int, bool, bool]:
        '''Gives user x amount of attempts to guess the hidden word'''
        try:
            # Hidden word
            game_word = self.dicti.get_game_word()
            self.log.write_log(f'Selected Word: {game_word}\n')
            guess = False
            # List of words entered by the user
            attempted_words = []
            success_attempt = 0
            for i in range(attempts):
                # Get Input from user and split the word into letters
                if self.is_automated:
                    automated_word = self.word_finder.find_word_automated(
                        list(self.good_letters), list(
                            self.correct_letters), list(self.bad_letters))
                    print(automated_word)
                    self.word_finder
                    user_input, validity = self.ui.get_user_input_recur(
                        i+1, attempts, attempted_words, self.dicti, self.log, self.is_automated, automated_word)
                else:
                    user_input, validity = self.ui.get_user_input_recur(
                        i+1, attempts, attempted_words, self.dicti, self.log, self.is_automated)
                # Quit game if validity is 2
                if validity == 2:
                    return success_attempt, guess, True
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
                self.log.write_log('You guessed the word correctly!!\n')
            else:
                print(f"The word was {''.join(game_word)}")
                print('Better luck next time!')
                self.log.write_log('Better luck next time!\n')
            print('Press enter to exit or guess another word')
            return success_attempt, guess, False
        except Exception as e:
            print(e)
            return 0, False, True

    def compare_word(self, user_word: str, game_word: str) -> bool:
        '''Compares the user input word with the hidden word and returns true if both are equal'''
        try:
            correct = 0
            user_word = list(user_word.upper())
            game_word = list(game_word.upper())
            result = ['']*len(game_word)

            # build good. bad, correct letter list

            for i, letter in enumerate(user_word):
                if letter == game_word[i]:
                    self.correct_letters.add((letter, i))
                if letter in game_word:
                    self.good_letters.add(letter)
                else:
                    self.bad_letters.add(letter)

            for i in range(len(user_word)):
                if game_word[i] == user_word[i]:
                    result[i] = self.ui.print_green(user_word[i])
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
                    result[i] = self.ui.print_yellow(letter + '`')
                    # Clear the letter so it's not searched again
                    game_word[game_word.index(letter)] = '#'
                else:
                    result[i] = self.ui.print_red(letter + '"')
                # Check if the word was correct
            output = ''.join(result)
            print(eval(f"f'{output}'"))
            return False
        except:
            raise Exception("Error: Could not compare words")

    def game_statistics(self, number_of_games: int, win_percent: int, guess_distribuition: list) -> None:
        '''Game statistics info'''
        print('\n***** Game Statistics *****\n')
        self.log.write_log('***** Game Statistics *****\n')
        print(f'{number_of_games} Games Played')
        self.log.write_log(f'{number_of_games} Games Played\n')
        print(f'{win_percent:.2f}% Win Rate')
        self.log.write_log(f'{win_percent:.2f}% Win Rate\n')
        print('Guess Distribution:')
        self.log.write_log('Guess Distribution:\n')
        for i, dist in enumerate(guess_distribuition):
            print(f'{i+1}: {dist}')
            self.log.write_log(f'{i+1}: {dist}\n')

    def start_game(self) -> None:
        total_attempts = 6
        self.game_greetings(total_attempts)
        num_of_games, win_count = 0, 0
        game_distribuiton = [0]*6
        while True:
            if self.is_automated and num_of_games == self.number_of_automated_games:
                break
            # Re-initialize word finder, good letters, bad letters and correct letters
            self.word_finder = wordFinder.WordFinder()
            self.good_letters = set()
            self.bad_letters = set()
            self.correct_letters = set()

            self.log.write_log(f"Game #{num_of_games+1}\n")
            success, win, should_quit = self.game_loop(total_attempts)
            if should_quit:
                break
            if win:
                win_count += 1
                game_distribuiton[success] += 1
            num_of_games += 1
            self.game_statistics(num_of_games, (win_count /
                                                num_of_games)*100, game_distribuiton)

    def __str__(self) -> str:
        return 'Main Game Object'


if __name__ == "__main__":
    game = Wordle()
    game.start_game()
