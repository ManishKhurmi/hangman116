
# For testing: 
import milestone_2
# Giving values to the parameters 
word_list = milestone_2.word_list
word = milestone_2.random_word
 
print(f'This is my list of words: {word_list}')
print(f'This is the randomly generated word: {word}')

# ['mango', 'lychee', 'banana', 'blueberry', 'apple']

####################################################################################################################################
# Task 2
word = 'apple'

# Task 2: Create methods for running the checks 
def check_guess(guess):
    '''
    This function checks if the guess is in the randomly generated word.
    '''
    guess = guess.lower() # converts the guess into a lowercase
    if guess in word:
        print(f'Good guess! {guess} is in the word')

list_of_guesses = ['b']

# Attempt 2 for ask_for_input()
def ask_for_input():
    '''
    Asks for user their guess and prints a message on the outcome.
    '''
    while True: 
        guess = input('Guess a Letter:')
        
        if len(guess) != 1:
            print('Invalid letter. Please, enter a single alphabetical character')
        if guess.isalpha() is False: #if the guess is not a single alphabetical character
            print('Invalid letter. Please, enter a single alphabetical character')
        elif guess in list_of_guesses:
            print('You already tried that letter!')
        else: 
            check_guess(guess)

ask_for_input()
# Test with the following inputs: '1' , 'manish', 'b'

####################################################################################################################################




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

# word_guessed 
# word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. 
# For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. 
    # If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']

# IDEA creating the word_guessed parameter ['_','_','_','_','_']
word = ['apples']
word[0][0]
#def func(word):
word_guessed = []

for i in word[0]:
    word_guessed.append('_')
word_guessed

# getting to ['a', '_', '_', '_', '_']
if 'a' in 'apples':
    #print('pass')
    word_guessed[0] = 'a'

#word_guessed[0].append('m')
word_guessed

# Great, so now we need a way to find the position of 'a' which gives us the 0 value in word_guessed[0]
if 'p' in 'apples':
    
# first find me where p is in apples 
word = 'apple' 

for letter in word: 
    print(letter)

########
word = 'apples'
#def func(word):
word_guessed = []

for i in word:
    word_guessed.append('_')
word_guessed

# getting to ['a', '_', '_', '_', '_']
guess = 'a'

if guess in word:
    #print('pass')
    word_guessed[0] = guess

# how can we find the position of 'a' in apples?

for i in 'apples': 

# use this idea to find the position 
    # If you need access to the index as you iterate through the string, use enumerate():

word_enumerated = []

for index, letter in enumerate('apple'):
    word_enumerated.append(index)
    print(index)


word = 'apple'

letters_as_list = []
for letter in word: 
    letters_as_list.append(letter) 

# use the index method to the position of the letter in the word
myString = 'Position of a character'
myString.index('s')
2



# now we can update the ['_', '_', '_'] correctly 

########## SOLUTION ##################################################
# creating word_guessed list ['_', '_', '_', '_', '_']
word = 'apple'

word_guessed = []
for i in word: 
    word_guessed.append('_')
word_guessed

# now we have the position of the letter 
guess = 'a'
word.index(guess)

# Updating to get to ['a', '_', '_', '_', '_']
if guess in word:
    # update the word_guessed list 
    word_guessed[word.index(guess)] = guess

word_guessed 
######################################################################


# where is 'm' in mango? 

# use rfing method, problem with this is that it will not work for words that have duplicate letters e.g. apples
#string = 'Geeks'
#letter = 'e'
#print(string.rfind(letter))


guess = 'm'

if 'm' in 'mango':
    print('has letter')
else:
    print('letter not there')

# now that the we know the letter is there we need to update the word_guessed with the letter 
word_guessed[0] = 'm'

word_guessed



# we need to map the word to numbers


# iterate through each letter, see if the letter is there, then update the list if it is there
for letter in word[0]: 
    if letter in word[0]:
        print('has letter')

    print(i)



#func(word)

# now if the player guesses the letter 'm' fill in the space 


# Now update with the guess 

if 'a' in word[0]:
    print('pass') # instead of pass use this to update a list 
else:
    print('fail')

word_guessed
word = 'mango'
enumerate(word)

word 

print(mango_enumerated)


# Testing the class 
Hangman(word_list = ['mango', 'lychee', 'banana', 'blueberry', 'apple'], number_of_lives = 5)




################################################################################################################
################################### SCRATCH WORK ###############################################################
################################################################################################################
# Testing 
guess = 'manish'

if len(guess) != 1:
    print('Invalid letter. Please, enter a single alphabetical character')
else: 
    print('pass')
if guess.isalpha() is False:
    print('Invalid letter. Please, enter a single alphabetical character')
else: 
    print('pass')

    
if len(guess) != 1 and guess.isalpha() is False: #if the guess is not a single alphabetical character
    print('Invalid letter. Please, enter a single alphabetical character')
else:
    print('pass')




def ask_for_input():
    '''
    Asks for user their guess and prints a message on the outcome.
    '''
    while True: 
        guess = input('Guess a Letter:')

        if len(guess) == 1 and guess.isalpha() == True:
            print('Good guess!')
            break
        elif guess in list_of_guesses:
            print('You already tried that letter!')
        else: 
            print('Invalid letter. Please, enter a single alphabetical character')
    else:
        check_guess(guess)
     # call the check_guess function outside of the while loop 
    check_guess(guess)
    
ask_for_input()

list_of_guesses = ['a', 'b']
guess = 'a'

if guess in list_of_guesses:
    print('You already tried that letter!')



#Step 3




