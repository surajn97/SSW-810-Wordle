import random


def load_dictionary():
    '''Reads the words text file and returns a list of valid words along with a random word'''
    words_file = open("words.txt", "r")
    words = words_file.read().splitlines()
    filtered_words = list(filter(lambda x: len(x) == 5, words))
    words_file.close()
    return random.choice(filtered_words), filtered_words


def check_valid_word(words: list, word: str) -> bool:
    '''Compares the given word with the words list to check if it exists'''
    if not words or not word:
        return False
    return word.lower() in words
