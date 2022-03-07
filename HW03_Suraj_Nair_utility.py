import os.path


def check_file_exists(file_path: str) -> bool:
    '''Check if the dictionary file exists'''
    return os.path.exists(file_path)


def load_dictionary() -> bool:
    '''Reads the words text file and creates a new file of 5 letter valid words'''
    try:
        words_file = open("words.txt", "r")
    except FileNotFoundError:
        raise Exception("Error: File not found.  Aborting")
    except OSError:
        raise Exception("Error: OS error occurred trying to open")
    except Exception as err:
        raise Exception(f"Unexpected error opening is", repr(err))
    words = words_file.read().splitlines()
    filtered_words = list(filter(lambda x: len(x) == 5, words))
    words_file.close()
    new_file = open('new_words.txt', 'w')
    new_file.write("\n".join(filtered_words))
    new_file.close()
    return True
