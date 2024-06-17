# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Installation instructions:
- Run the hangman.py script
  
## Usage instructions
- Enter a letters to reveal the word
- You have a limited number of guesses before HANGMAN!!!
  
## File structure of the project
- 1 script

## License information
Open to all 

## My Learnings from the Project
Check out project_learnings.py for example code of the learnings below.

- **BREAK DOWN PROBLEMS**: No matter how simple or complex a problem might seem, break it down into smaller, manageable parts. This approach made it easier to start working on a solution.

- **PRIORITISE WORKING CODE**: First, write code that works. Once it functions correctly, focus on optimising and making it leaner.

- **PLAN AHEAD**: Thinking ahead and understanding upcoming tasks can help solve current problems more effectively. Reading ahead in Milestone 4 helped me tackle challenges more efficiently.

- **EXPECT THE UNEXPECTED**: Challenges were unpredictable. For example, creating a successful while loop was easier than initialising the `word_guessed` variable, which was contrary to my initial expectations.

- **UNDERSTAND CLASSES AND FUNCTIONS**: When working with classes and functions, create examples to understand their behaviour. This practice helps me in debugging more complex code. I learned to solve problems by following the flow of information through variables and functions in the class.

- **USE BREAK STATEMENTS FOR TESTING**: Break statements can isolate problems, making it easier to test specific parts of the code. For example, in Milestone 4, I used break statements to test the `check_guess()` function efficiently by stopping after four guesses.

- **UTILISE IN-PLACE OPERATORS**: Use in-place operators like `-=` to update variables correctly. For instance, `self.num_lives -= 1` reduces the value by 1 and updates it in place.

- **SIMPLIFY CONDITIONS**: Simplify multiple `IF` statements where possible. For example, combining  `IF` conditions in the `check_guess()`

- **REFERENCE SELF VARIABLES CORRECTLY**: Correctly reference `self` variable from the `__init__()` method when defining new methods. Initially, I struggled with this syntax, often missing the self parameter (e.g., `check_guess(self)` vs. `check_guess()`).This ensures that variables defined in the `__init__()` method are accessed correctly.

- **CONSIDER DATA STRUCTURES**: Think about the data structures being used. For example, creating the `word_guessed` variable with the `set()` function extracts unique letters in one line of code, which is more efficient than using a separate function.

- **LEVERAGE EXISTING FUNCTIONS**: Often, there were pre-built functions in Python created by other developers that can were very useful. Researching these functions saved time and effort.















