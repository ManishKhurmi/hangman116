# After talking to Patrick 

# There is a way to initialise the variables without needing additional functions to be defined in the class 
import random

class Hangman:
    # Task 1
    def __init__(self, word_list, num_lives):
      
        self.word = random.choice(word_list) # random word picked from word_list 
        self.word_guessed = len(self.word) * ['_'] # a list of letters of the word with a '_' if the letter is not guessed
        # create the logic for each variable base
        self.num_letters = len(set(self.word))# the number of UNIQUE letters not guessed yet 
        self.num_lives = num_lives # the number of lives the player has at the start of the game 
        self.word_list = word_list # e.g. ['mango', 'lychee', 'banana', 'blueberry', 'apple']
        self.list_of_guesses = [] # a list of guesses that have already been tried 

    # Task 2
    def check_guess(self, guess):

        '''
        This function checks if the guess is in the randomly generated word.
        '''
        guess = guess.lower() # converts the guess into a lowercase
        
        if guess in self.word:
            print(f'Good guess! {guess} is in the word')
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[self.word.index(letter)] = guess
            self.num_letters - 1 
        else:
            # reduce the number of lives by 1 for every wrong guess
            self.num_lives = self.num_lives - 1 
            print(f'Sorry, {guess} is not in the word')
            print(f'You have {self.num_lives} lives left')

            
    # Task 2
    def ask_for_input(self):
        '''
        Asks for user their guess and prints a message on the outcome.
        '''
        while True: 
            guess = input('Guess a Letter:')
            
            if len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character')
            # elif guess.isalpha() is False: #if the guess is not a single alphabetical character
            #     print('Invalid letter. Please, enter a single alphabetical character')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            # For testing check_guess()
            # elif len(self.list_of_guesses) == 3: # For Testing only 
            #     break
            else: 
                self.list_of_guesses.append(guess) 
                self.check_guess(guess)
            
# Testing the game class 
game = Hangman(word_list= ['banana', 'apples'], num_lives= 5)
print(game.word)
game.ask_for_input()
game.num_letters
game.word
game.list_of_guesses

################################################################################################################
################################### SCRATCH WORK ###############################################################
################################################################################################################

game.word.index('p')
game.word_guessed

fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
x

word = 'apple'
word_guessed = len(word) * ['_']
word_guessed
guess = 'p'

#word.index(guess)
#word_guessed[word.index(guess)] = guess
word = 'apple'
word_guessed = len(word) * ['_']
guess = 'p'
num_letters = len(set(word))
num_letters

for letter in word:
    if letter == guess:
        word_guessed[word.index(letter)] = guess

word_guessed
num_letters = len(set(word))
num_letters - 1

def check_guess(self, guess):

    '''
    This function checks if the guess is in the randomly generated word.
    '''
    guess = guess.lower() # converts the guess into a lowercase
    
    if guess in self.word:
        print(f'Good guess! {guess} is in the word')
        for letter in word:
            if letter == guess:
                word_guessed[word.index(letter)] = guess
        num_letters - 1 
        

guess = 'a'
game.word
game.check_guess(guess = 'd')

# Example Class

class Car:

    def __init__(self, colour):
        self.colour = colour 
        self.list_of_guesses = []

    def ask_for_colour(self):     
        while True:
            guess = input('What colour car do you want?:')
            if guess.isalpha() is True:
                if guess in self.list_of_guesses:
                    print('you already tried that')
                else:
                    self.list_of_guesses.append(guess)
            else:
                print('Invalid input. Please enter a valid colour')
            continue_asking = input('Do you wamt tp keep guessing? (yes/no)').strip().lower()
            if continue_asking != 'yes':
                break


car = Car(colour= 'red')
car.ask_for_colour()
print("List of guesses", car.list_of_guesses)





game.ask_for_input()


word = 'apple'
guess = 'a'
list_of_guesses = ['a']

def check_guess(guess):
    '''
    This function checks if the guess is in the randomly generated word.
    '''
    guess = guess.lower() # converts the guess into a lowercase
    if guess in word:
        print(f'Good guess! {guess} is in the word')

# Task 2
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


# __init__() variables 
# creating word_guessed
word = 'apple'
len(word) * ['_']

# num_letters, here we want to count the unique characters only 
# makes sense to use a set() as a set only includes the unique characters 
# example 
word = 'apple'
set_1 = len(set(word))
set_1 # returns 4, for 4 unique characters in 'apple'
