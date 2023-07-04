import string
from random_word import RandomWords

# Write your code here
print('H A N G M A N')

lost_games = 0
won_games = 0

valid_menu_inputs = ['results', 'exit', 'play']

while True:
    # Opening up the menu for the user
    user_request = ''
    while user_request != 'play':
        print('\nType "play" to play the game, "results" to show the \
scoreboard, and "exit" to quit: ')
        user_request = input()
        if user_request == 'results':
            print(f"""You won: {won_games} times.
You lost: {lost_games} times.
            """)
        elif user_request == 'exit':
            break

    if user_request == 'exit':
        break

    # Creating the word for the user to guess
    r = RandomWords()
    correct_word = r.get_random_word()
    word_to_show = '-' * len(correct_word)
    attempts = 0
    guessed_letters = ''

    # Playing the guessing game with 8 attempts
    while attempts < 8:

        # Checking if input is correct (should only be one lower-case letter)
        checking = True
        while checking:
            print(f'\n{word_to_show}')
            print('Input a letter: ')
            letter = input()
            if len(letter) != 1:
                print('Please, input a single letter.')
            elif letter not in string.ascii_lowercase:
                print("Please, enter a lowercase letter from the English \
alphabet.")
            else:
                checking = False

        # Checking if letter is in <correct_word>
        # If letter has been guessed before
        if letter in guessed_letters:
            print("You've already guessed this letter.")
        # If guessed letter occurs in <correct_word>
        elif letter in correct_word and letter not in word_to_show:
            index_of_letter = correct_word.find(letter)
            while index_of_letter != -1:
                word_to_show = word_to_show[
                               :index_of_letter] + letter + word_to_show[
                                                            index_of_letter + 1:]
                index_of_letter = correct_word.find(letter, index_of_letter + 1)
        # Guessed letter doesn't appear in <correct_word>
        else:
            print("That letter doesn't appear in the word.")
            attempts = attempts + 1

        # The user guessed the entire word correctly
        if '-' not in word_to_show:
            print(f'You guessed the word {correct_word}!\nYou survived!')
            won_games = won_games + 1
            break

        # Updating <guessed_letters>
        if letter not in guessed_letters:
            guessed_letters = guessed_letters + letter

    # The user failed to guess <correct_word> with 8 attempts
    if attempts == 8:
        print(f'You lost!\nThe word was {correct_word}')
        lost_games = lost_games + 1
