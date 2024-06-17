# For testing: 
import milestone_2 as milestone_2
# Giving values to the parameters 
word_list = milestone_2.word_list
word = milestone_2.random_word
 
print(f'This is my list of words: {word_list}')
print(f'This is the randomly generated word: {word}')

# ['mango', 'lychee', 'banana', 'blueberry', 'apple']
####################################################################################################################################
import random 

 # Task 1 
class Hangman:

    def __init__(self, word_list, number_of_lives):
      
        self.word = random.choice(word_list) # random word picked from word_list 
        self.word_guessed = word_guessed # a list of letters of the word with a '_' if the letter is not guessed
        # create the logic for each variable base
        self.num_letters = num_letters # the number of UNIQUE letters not guessed yet 
        self.num_lives = num_lives # the number of lives the player has at the start of the game 
        self.word_list = word_list
        self.list_of_guesses = list_of_guesses # a list of guesses that have already been tried 


# word_guessed variable

# creating word_guessed list ['_', '_', '_', '_', '_']
word = 'apple'

word_guessed = []
for i in word: 
    word_guessed.append('_')
word_guessed

# now we have the position of the letter 
guess = 'p'
word.index(guess)

# Updating to get to ['a', '_', '_', '_', '_']
if guess in word:
    # update the word_guessed list 
    word_guessed[word.index(guess)] = guess


for guess in word:

    if guess in word:
        # update the word_guessed list 
        word_guessed[word.index(guess)] = guess

word_guessed 

word_guessed = []
word = 'apple'
guess = 'p'

for i in word: 
    if guess in word:
        print('pass')
        word_guessed[word.index(guess)] = guess

if guess in word: 
    for guess in word:
        word_guessed[word.index(guess)] = guess

word_guessed

# Find multiple positions of letter in a string 

s = 'shak#spea#e'
c = '#'
print([pos for pos, char in enumerate(s) if char == c])

# Tailor to our project 
print([pos for pos, char in enumerate(word) if char == guess ])

position = [pos for pos, char in enumerate(word) if char == guess ]
position

for i in position:
    word_guessed

word_guessed

word.index(guess)


word_guessed[word.index(guess)] = guess

word_guessed 

word = 'apple'

######################
word = 'apple'

word_guessed = []
for i in word: 
    word_guessed.append('_')
word_guessed

guess = 'p'

# Position of where to update 'p' i.e. covers the case of multiple characters 
position = [pos for pos, char in enumerate(word) if char == guess ]

# [1, 2]
position

# update list word_guessed 

for i in position: 
    word_guessed[i] = guess 

word_guessed