# Hangman

This project implements the classic Hangman game.
Players should sequentially guess the letters in the word, one letter at a time,
which is randomly chosen by the program. If an attempt is successful, the letter 
is uncovered, otherwise, the player loses an attempt (the player haa 8 attempts 
to guess all letters that appear in the word). When the player runs out of 
attempts or guesses the word correctly, the game ends, and the player is 
prompted to try again, with a new word, or exit.

Things to take note of:
    - The player won't lose an attempt if they guessed a correct letter, or 
they suggested a letter that was previously suggested
    - It is able to handle wrong input
    - The player can play this game multiple times, and before each 
re-play, they can check their score (number of lost and won games)

# General Info

To learn more about this project, please visit 
[HyperSkill Website - Hangman](https://hyperskill.org/projects/69).

This project's difficulty has been labelled as __Easy__ where this is how 
HyperSkill describes each of its four available difficulty levels:

- __Easy Projects__ - if you're just starting
- __Medium Projects__ - to build upon the basics
- __Hard Projects__ - to practice all the basic concepts and learn new ones
- __Challenging Projects__ - to perfect your knowledge with challenging tasks

This Repository contains one .py file:

    code.py - Contains the code of the game

Project was built using python version 3.11.3

# How to Run

Download the code.py file to your local repository and open the project in your choice 
IDE and run the project.
