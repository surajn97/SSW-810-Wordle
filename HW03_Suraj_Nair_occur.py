from collections import defaultdict
from functools import reduce
import csv
import HW03_Suraj_Nair_dictionary as dictionary
import HW03_Suraj_Nair_utility as utility


class Occurence:
    def __init__(self) -> None:
        self.letter_freq = defaultdict(lambda: [0, 0, 0, 0, 0])

    def get_occurence_frequency(self, words: list) -> None:
        '''Gets the frequency of all the letters in the list of words'''
        if not words or len(words) == 0:
            raise Exception("Error: Invalid words list")
        for word in words:
            for i, letter in enumerate(word.lower()):
                self.letter_freq[letter][i] += 1
        for key in self.letter_freq.keys():
            for i, val in enumerate(self.letter_freq[key]):
                self.letter_freq[key][i] = round(
                    val/len(words), 3)

    def write_to_csv(self) -> None:
        '''Writes the frequency to the file'''
        try:
            with open('letterFrequency.csv', 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile, delimiter=',')
                for key, val in sorted(self.letter_freq.items()):
                    csv_writer.writerow(
                        [key, val[0], val[1], val[2], val[3], val[4]])
                print('Done')
        except FileNotFoundError:
            raise Exception("Error: File not found.  Aborting")
        except OSError:
            raise Exception("Error: OS error occurred trying to open")
        except Exception as err:
            raise Exception(f"Unexpected error opening is", repr(err))

    def convert_list_to_tuple(self, dictionary: dict) -> dict:
        for key in dictionary:
            dictionary[key] = tuple(dictionary[key])
        return dictionary

    def get_dict_from_file(self) -> dict:
        '''Reads the frequency from the file'''
        try:
            freq_dict = {}
            with open('letterFrequency.csv', 'r', newline='') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',')
                for row in csv_reader:
                    freq_dict[row[0]] = (
                        row[1], row[2], row[3], row[4], row[5])
            return freq_dict
        except FileNotFoundError:
            raise Exception("Error: File not found.  Aborting")
        except OSError:
            raise Exception("Error: OS error occurred trying to open")
        except Exception as err:
            raise Exception(f"Unexpected error opening is", repr(err))

    def get_word_freq_weight(self, word: str, freq_dict: dict) -> float:
        '''Calculates the weight of word based on letter frequency'''
        weight = 1
        for i, letter in enumerate(word.lower()):
            weight *= freq_dict[letter][i]
        return weight

    def get_words_weight(self, words: list, freq_dict: dict) -> dict:
        weight_dict = {}
        for word in words:
            word = word.lower()
            weight_dict[word] = self.get_word_freq_weight(word, freq_dict)

        sorted_weight = sorted(weight_dict.items(), key=lambda x: x[1])
        try:
            with open('wordRank.csv', 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile, delimiter=',')
                for i, val in enumerate(sorted_weight):
                    csv_writer.writerow(
                        [i+1, val[0], val[1]])
                print('Done')
        except FileNotFoundError:
            raise Exception("Error: File not found.  Aborting")
        except OSError:
            raise Exception("Error: OS error occurred trying to open")
        except Exception as err:
            raise Exception(f"Unexpected error opening is", repr(err))


if __name__ == "__main__":
    utility.load_dictionary()
    dicti = dictionary.Dictionary()
    dicti.load_dictionary()
    occ = Occurence()
    occ.get_occurence_frequency(dicti.words)
    occ.write_to_csv()
    new_dict = occ.convert_list_to_tuple(occ.letter_freq)
    occ.get_words_weight(dicti.words, new_dict)
