# Pseudocode for wordle

# SET attempts to 6
# SET game_word to SONAR
# For each attempt
#     SET correct to 0
#     SET user_input to blank
#     While user_input is not 5 characters or user_input is not a unique word or user_input is not alphabets
#         Get Input from User
#     For each letter in user_input
#         If letter is in game_word
#             If user_input letter is game_word letter
#                 Print letter is in correct position
#                 Increment correct by 1
#             Else
#                 Print letter is in the word but not in correct position
#             Update game_word letter to '#'
#         Else
#             Print letter is not in word
#     If correct is equal to length of game_word
#         Print You win and quit the game
    

# ANSII Codes for colors
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

# Number of attempts
attempts = 6

# Hidden word
game_word = list('SONAR'.upper())

# List of words entered by the user
attempted_words = []

print('\n***** WORDLE *****\n')
print(f'Guess the WORDLE in {attempts} tries.')
print('Each guess must be a valid 5 letter word. Hit the enter button to submit.')
print('After each guess, the color of the letters will change to show how close your guess was to the word.\n')
print(f'{OKGREEN}Green{ENDC} color shows letter is in the word and in the correct spot.')
print(f'{WARNING}Yellow{ENDC} color shows letter is in the word but in the wrong spot.')
print(f'{FAIL}Red{ENDC} color shows letter is not in the word in any spot.\n')

# Loop for attempts
for i in range(attempts):
    correct = 0
    user_input = ''

    # Keep getting input from user until it's a unique 5 letter word
    while not user_input.isalpha() or len(user_input) != 5 or user_input in attempted_words:
        print(f'Attempt {i+1} / {attempts} --> Please Enter a 5 letter unique word:')
        user_input = input().strip().upper()

    # Add the new word to attempt list
    attempted_words.append(user_input)

    # Split the word into letters
    user_input = list(user_input)
    output = ''
    #Create a temporary copy of the hidden word to manipulate
    temp_game_word = game_word.copy()
    # Loop each letter to compare
    for y,letter in enumerate(user_input):
        if letter in temp_game_word:
            if user_input[y] == temp_game_word[y]:
                output += '{OKGREEN}' + letter + '{ENDC}'
                correct += 1
            else:
                output += '{WARNING}' + letter + '{ENDC}'
            # Clear the letter so it's not searched again
            temp_game_word[temp_game_word.index(letter)]='#'
        else:
            output += '{FAIL}' + letter + '{ENDC}'

        # Check if the word was correct
        if correct == len(game_word):
            print(eval(f"f'{output}'"))
            print('You guessed the word correctly!!')
            quit()

    print(eval(f"f'{output}'"))

print('Better luck next time!')