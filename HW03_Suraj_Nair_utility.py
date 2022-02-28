import os.path


def check_file_exists(file_path):
    '''Check if the dictionary file exists'''
    return os.path.exists(file_path)


def load_dictionary():
    '''Reads the words text file and creates a new file of 5 letter valid words'''
    if not check_file_exists('words.txt'):
        return False
    words_file = open("words.txt", "r")
    words = words_file.read().splitlines()
    filtered_words = list(filter(lambda x: len(x) == 5, words))
    words_file.close()
    new_file = open('new_words.txt', 'w')
    new_file.write("\n".join(filtered_words))
    new_file.close()
    return True
