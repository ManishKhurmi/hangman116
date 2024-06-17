# Project Learnings with Examples
##################################################################################################################################
# Milestone 5: Writing quality doc strings 
# Exaplain what the code is doing in layman terms 

# Incorrect: Docstring is too vague
def play_game(word_list):
    '''
    Creates the logic for the game. 

    Attributes:
    word_list (list): A list of words from which the game will randomly choose one for the player to guess. 
                      For example, ['mango', 'lychee', 'banana'].
    '''

# Correct: Explains in a few sentences what this code does with game context 
def play_game(word_list):
    '''
    Execute the main game loop for Hangman.

    This function intialises the Hangman game with a given list of words and a fixed number of lives. It continously 
    prompts the player for guesses and provides feedback on their progress. The game ends when the player either 
    guesses all the letters in the word or runs out of lives.


    Attributes:
    word_list (list): A list of words from which the game will randomly choose one for the player to guess. 
                      For example, ['mango', 'lychee', 'banana'].
    '''

##################################################################################################################################
# Milestone 5: Updating variables correctly using "-="

# Incorrect: updating num_letters by subtracting 1 without assignment
    # It only performs the subtraction without storing the result.
def check_guess(self, guess):
    '''
    This function checks if the guess is in the randomly generated word.
    '''
    guess = guess.lower()
    
    if guess in self.word:
        print(f'Good guess! {guess} is in the word')
        for letter in self.word:
            if letter == guess:
                self.word_guessed[self.word.index(letter)] = guess
        self.num_letters - 1 
    else:
        self.num_lives = self.num_lives - 1 
        print(f'Sorry, {guess} is not in the word')
        print(f'You have {self.num_lives} lives left')


# Correct: Using -= to update num_letteres and num_lives
# correctly decrements the value of self.num_letters and updates the instance variable.
def check_guess(self, guess):

    guess = guess.lower() 
    
    if guess in self.word: 
        print(f'Good guess! {guess} is in the word')
        for letter in self.word:
            if letter == guess:
                self.word_guessed[self.word.index(letter)] = guess
        self.num_letters -= 1 
    else: 
        
        self.num_lives -= 1
        print(f'Sorry, {guess} is not in the word')
        print(f'You have {self.num_lives} lives left')
##################################################################################################################################
# Milestone 5: missing a break statement & correctly passing through 'self' in functions inside a class that use the class' initialised variables
    # ask_for_input method is missing a break statement at the end of the method definition to break out of the loop for when the user inputs a letter which is suitable for the game.
    # missing 'self' reference in the ask_for_input(self). This means that variables inside the __init__() cannot be accessed correctly.

# Incorrect use of break statement in ask_for_input()
# Having no break statement mean't that the while loop would go on forever, this made testing the function slower.
def ask_for_input():
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

# Correct passing of 'self' in the fuction definition and the use of break statement 
def ask_for_input(self):
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
##################################################################################################################################
# Milestone 5: simplify condions where possible 

# Incorrect Method: Using multiple if statements can lead to redundant checks and unclear logic. 
# For example, checking if game.num_lives == 0 and if game.num_lives > 0 separately can cause confusion and unnecessary processing.
# Correct Method: Using elif and else ensures that only one condition is checked and executed in each iteration of the loop, which simplifies the logic and improves readability.
    # Lay Example: 
    # Incorrect Method:
        # Imagine you're running a game, and you have several checkpoints to see if the game is over.
        # You keep checking, "Did the player lose?" and "Is the player still playing?" separately.
        # This can be confusing and make your game code messy because you're repeatedly asking similar questions.
    # Correct Method:
        # Instead, you should use a clearer way to check conditions.
        # First, ask "Did the player lose?" If yes, you stop the game right away.
        # If the player didn't lose, then ask "Did the player win?" If yes, you stop the game.
        # Only if the player hasn't lost or won, you keep the game going.
        # This way, you're only checking one thing at a time, making it easier to understand and more efficient.

# Incorrect: Redundant and unclear solutions
def play_game(word_list):

    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print('You lost!')
        if game.num_lives > 0:
            game.ask_for_input()
        if game.num_lives != 0 and game.num_letters == 0:
            print('Congratulations. You won the game!')
            break

# Correct: Simplified and clear conditions
while True:
    if game.num_lives == 0:
        print('You lost!')
        break
    elif game.num_letters == 0:
        print('Congratulations. You won the game!')
        break
    else:
        game.ask_for_input()
##################################################################################################################################
# Milestone 4: Noticing the data structures used and applying appropriate functions to them 
# num_letters: this has to be a all unique characters so I'll want a data structure which can easily perform this, a set can only have unique characters so I'll use that

# Incorrect: creating a for loop to create the word_guessed variable
# Create ['_','_','_','_','_'] from 'apples'
word = 'apples'
#def func(word):
num_letters = []

for i in word:
    num_letters.append('_')
num_letters

# Correct: using the set() at it extracts the unique elements from a list 
num_letters = len(set(word))
num_letters

##################################################################################################################################
# Milestone 2: Printing variables with messages when testing code
# Helps to break down a problem and the message helps to stay motivated on the problem

# print word_list along with a helpful error message
word = 'laptop'
print(f'Succefully prints word: {word}')