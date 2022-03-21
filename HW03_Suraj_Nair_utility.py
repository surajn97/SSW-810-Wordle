import os.path


class Utility:
    def __init__(self) -> None:
        self.words_file = None

    def check_file_exists(self, file_path: str) -> bool:
        '''Check if the dictionary file exists'''
        return os.path.exists(file_path)

    def load_dictionary(self) -> bool:
        '''Reads the words text file and creates a new file of 5 letter valid words'''
        try:
            self.words_file = open("words.txt", "r")
        except FileNotFoundError:
            raise Exception("Error: File not found.  Aborting")
        except OSError:
            raise Exception("Error: OS error occurred trying to open")
        except Exception as err:
            raise Exception(f"Unexpected error opening is", repr(err))
        words = self. words_file.read().splitlines()
        filtered_words = list(filter(lambda x: len(x) == 5, words))
        self.words_file.close()
        new_file = open('new_words.txt', 'w')
        new_file.write("\n".join(filtered_words))
        new_file.close()
        return True

    def __str__(self) -> str:
        if self.words_file:
            if self.words_file.closed:
                return 'File Status: Closed'
            else:
                return 'File Status: Open'
        else:
            return 'Words file not created yet'
