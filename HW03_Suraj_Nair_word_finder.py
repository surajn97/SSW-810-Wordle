import HW03_Suraj_Nair_occur as occur
import HW03_Suraj_Nair_dictionary as dictionary
import HW03_Suraj_Nair_utility as utility


class Node:
    def __init__(self, value: any = None) -> None:
        self.val = value
        self.next_node = None


class WordFinder:

    def __init__(self) -> None:
        '''Creates word rank file'''
        self.util = utility.Utility()
        self.util.load_dictionary()
        self.dicti = dictionary.Dictionary()
        self.dicti.load_dictionary()
        self.occ = occur.Occurence()
        self.occ.get_occurence_frequency(self.dicti.words)
        self.occ.write_to_csv()
        self.new_dict = self.occ.convert_list_to_tuple(self.occ.letter_freq)
        word_rank = self.occ.get_words_weight(
            self.dicti.words, self.new_dict)
        self.word_rank_list = [x[0] for x in word_rank]

    def get_user_input(self):
        '''Gets user input'''

        good_letters, bad_letters, correct_letters = None,   None,  None
        good_words = input(
            'Please enter up to 5 Good letters (Press enter to ignore):\n')
        if len(good_words) > 0:
            while len(good_words) > 5 or not good_words.isalpha():
                good_words = input('Please enter up to 5 Good letters:\n')
            good_letters = list(good_words)

        bad_words = input(
            'Please enter Bad letters (Press enter to ignore):\n')
        if len(bad_words) > 0:
            while len(bad_words) == 0 or not bad_words.isalpha() or (good_letters and len(set(good_letters).intersection(set(bad_words))) != 0):
                bad_words = input('Please enter Bad letters:\n')
            bad_letters = list(bad_words)

        correct_letters = None
        correct_words = input(
            'Enter Correct letters with spaces for blanks (Press enter to ignore):\n')
        if len(correct_words) > 0:
            while len(correct_words) != 5 or not correct_words.replace(' ', '').isalpha() or (bad_letters and len(set(correct_words).intersection(set(bad_letters))) != 0):
                correct_words = input(
                    'Enter Correct letters with spaces for blanks:\n')
            correct_letters = []
            for i, letter in enumerate(correct_words):
                if letter != ' ':
                    correct_letters.append((letter, i))

        self.find_word(good_letters=good_letters, wrong_letters=bad_letters,
                       correct_letters_with_pos=correct_letters)

    def find_word(self, good_letters: list, correct_letters_with_pos: list = None, wrong_letters: list = None) -> list:
        '''Finds top possible words'''
        if good_letters != None or wrong_letters != None or correct_letters_with_pos != None:
            head = temp = Node()
            for word in self.word_rank_list:
                word = word.lower()
                if wrong_letters != None and any(x.lower() in word for x in wrong_letters):
                    continue
                if good_letters != None and any(x.lower() not in word for x in good_letters):
                    continue
                if correct_letters_with_pos != None:
                    flag = True
                    for letter, index in correct_letters_with_pos:
                        if word[index].lower() != letter:
                            flag = False
                            break
                    if flag:
                        temp.next_node = Node(word)
                        temp = temp.next_node
                else:
                    temp.next_node = Node(word)
                    temp = temp.next_node
            head = head.next_node
            if head:
                print('List of possible words:')
                total = 1
                while head:
                    print(f'{total}. {head.val}')
                    head = head.next_node
                    total += 1
            else:
                print('Could not find any suggestions')
        else:
            for i, word in enumerate(self.word_rank_list[:50]):
                print(f'{i+1}. {word}')


if __name__ == "__main__":
    finder = WordFinder()
    finder.get_user_input()
