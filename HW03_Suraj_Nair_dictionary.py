import random
import os.path


class Dictionary:
    def __init__(self) -> None:
        self.valid_words = []
        self.words = []

    def check_file_exists(self, file_path) -> bool:
        '''Check if the dictionary file exists'''
        return os.path.exists(file_path)

    def load_dictionary(self) -> str:
        try:
            '''Reads the words text file and returns a list of valid words along with a random word'''
            words_file = open("new_words.txt", "r")
        except FileNotFoundError:
            raise Exception("Error: File not found.  Aborting")
        except OSError:
            raise Exception("Error: OS error occurred trying to open")
        except Exception as err:
            raise Exception(f"Unexpected error opening is", repr(err))
        self.words = words_file.read().splitlines()
        words_file.close()
        if len(self.valid_words) == len(self.words):
            self.valid_words.clear()
        game_word = random.choice(self.words)
        while game_word in self.valid_words:
            game_word = random.choice(self.words)
        self.valid_words.append(game_word)
        return game_word

    def check_valid_word(self, word: str) -> bool:
        '''Compares the given word with the words list to check if it exists'''
        try:
            if not self.words or not word:
                return False
            return word.lower() in self.words
        except:
            raise Exception('Error: Word could not be checked')

    def __str__(self) -> str:
        return f'Total Words:{len(self.words)}\nValid Words:{len(self.valid_words)}'
