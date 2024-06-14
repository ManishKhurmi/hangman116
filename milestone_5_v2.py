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
            self.num_letters -= 1 
        else:
            # reduce the number of lives by 1 for every wrong guess
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word')
            print(f'You have {self.num_lives} lives left')

            
    # Task 2
    def ask_for_input(self):
        '''
        Asks for user their guess and prints a message on the outcome.
        '''
        while True: 
            guess = input('Guess a Letter:')
            
            if len(guess) != 1 or not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else: 
                self.list_of_guesses.append(guess) 
                self.check_guess(guess)
                break

def play_game(word_list):

    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters == 0:
            print('Congratulations. You won the game!')
            break
        else:
            game.ask_for_input()

# Testing play_game()
play_game(word_list = ['apples', 'bananas'])


# learnings 
# input breaks for win and lost moments in the game
# learn't how to solve problems when calling classes by following the flow of information :variables and functions in the class.
# Using in-place operators '-= 1' to correctly update num_lives. Here '-=' us used to reduce the value by 1 and update it in place
# Proper Use of 'self'
    # Ensure all instance variable modifications and method calls within a class use self to refer to the instance correctly.
# combine checks for single alphabet 

