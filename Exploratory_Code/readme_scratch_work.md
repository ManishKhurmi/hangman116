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

# General learnings from the project 
- Research functions in python, more often than not with this project there was a useful function created by another developer
- No matter how simple or complex a problem might be, break it down until I can start.
- Write code that works and then focus on making it leaner. 
- What I found challenging was often not comparable and specific to me. For example creating a succcessful while loop was a lot easier than initalising the word_guessed variable, however my expectations were the opposite.
- When dealing with  classes and functions in classes, create examples to understand the behaviour of the code. This has been a helpful first step to solving a bug in more complex code. - Here I learn't how to solve problems when calling classes by following the flow of information :variables and functions in the class.
- Break statements can help with testing as they can isolate the problem up to the bug in a code. For example In milestone 4, to test the check_guess() function I created break statements to run when the user inputed 4 guesses, this helped me to test the IF statements I created for the function more efficiently.
- Using in-place operators '-= 1' to correctly update num_lives. Here '-=' us used to reduce the value by 1 and update it in place
- simplifying multiple IF statements where possible e.g. combining IF statements in the check_guess() function for checking if the guess is an alphabetical letter and a single letter.
- Refrencing self variables from the __init__() of classes correctly. I learn't how to correctly use self variables in defining new methods to build the class. The syntex was initially challenging as I would often miss defining self in the method e.g. check_guess() vs check_guess(self) making sure that the flow of information makes sense.
- Passing the 'self' variable  in the ask_for_input(), done correctly: ask_for_input(self). This means that variables inside the __init__() of the Hangman class were not being accessed correctly. This improved my understanding of working with variables defined within the classes and the flow of information when using classes and defining methids inside classes.
- The absence of a BREAK statement in ask_for_input() made testing the function slower. 
- Thinking of what data structures I'm working with can helped to writing leaner code and solving the problem faster problem faster. An example here was creating the word_guessed variable in milestone 4, where I used the set() function as I needed a data structure where only the unique letters of a word were extracted, the set() does exacly this and helped to create the variable in just one line of code. My initial approach used a function to create this variable which wasn't ideal as I was creating the initial variables for the class inside the class' __init__(),  although this approach is possible, it's not needed here given that there was a defining word_guessed without needing a seperate function.
- Thinking ahead at what I need to do can help in solving a problem for example reading ahead for tasks in milestone 4 helped to solve.