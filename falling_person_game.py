"""
Created on Sat Jun 27 11:59:10 2020
@author: danielpelnar
"""
import graphic_1


# Creating a game called Falling Person. Modification of the hangman game.
#   The program 'thinks of' a word, the user is guessing.
#   8 gueesses max
#   By guessing the secret word, you save the falling person. 
#   We will separate this problem into subproblems.

# Outline:
# 1] Load words which will be available to the program.
# 2] Choose one word at random (secret word).
# 3] Have we guessed all the letters of the given secret word?
# 4] Get a string of letters which have already been guessed.
# 5] Get letters that can still be used.
# 6] Is the letter a correct guess?
# 7] Graphical illustration of the number of guesses left.
# 8] Putting it all together as one function.
# 9] Play the game!


# 1]
def load_words():
    '''
    Returns words.txt
    ''' 
    with open('words.txt', 'r') as file:  
        line = file.readline() 
    word_list = line.split() 
    return word_list

# 2]    
def choose_word(word_list):
    '''    
    Input: a list of words
    Returns one word at random with equal probability.  
    '''
    import random
    random_word = random.choice(word_list) 
    return random_word

wordList = load_words() 
secret_word = choose_word(wordList)

# 3]
def isWordGuessed(secret_word, guessed_letters_list):
    '''
    secret_word: The word that user is trying to guess.
    guessed_letters_list: A list of already guessed letters.
    Returns True if ALL the letters in secret_word are in guessed_letters_list,
    and False otherwise.
    '''
    placeholder = ''
    for letter in secret_word:
        if letter in guessed_letters_list:
            placeholder += letter
    return secret_word == placeholder

# 4]
def getGuessedWord(secret_word, guessed_letters_list):
    '''
    secret_word: The word that user is trying to guess.
    guessed_letters_list: A list of already guessed letters.
    Returns a string comprised of letters and underscores.
    Underscores represent letters that have not been guessed yet.
    '''
    creating_secret_word = ''
    for letter in secret_word:
        if letter in guessed_letters_list:
            creating_secret_word += letter
        else:
            creating_secret_word += '_ '
    return creating_secret_word

# 5]
def getAvailableLetters(guessed_letters_list):
    '''
    guessed_letters_list: A list of already guessed letters.
    Returns a string of letters that are still available.
    '''
    import string
    alphabet_string = string.ascii_lowercase   
    not_guessed = ''
    for letter in alphabet_string:
        if letter not in guessed_letters_list:
            not_guessed += letter
    return not_guessed

# 6]
def goodGuess(guess, secret_word):
    '''
    guess: a string letter  (guessed letter)
    secret_word: The word that user is trying to guess.
    Returns True if secret_word contains the guessed letter
    '''
    if guess in secret_word:
        return True
    else:
        return False
   
# 7]
# Import any graphic you want.         
falling_person = graphic_1.pics

# 8]    
def falling_person_game():
    '''
    Starts the game.
    A person has jumped from a building. Your job is to save him/her. 
    Save that poor person by guessing the secret word.
    You have 8 guesses.
    Better not fail!
    '''
    print('-----------')
    print('Welcome to the Falling Person game!')
    wordList = load_words() 
    secret_word = choose_word(wordList)
    guessed_letters_list = []
    guesses_left = 8
    repeated_guesses = []
    print('I am thinking of a word that is {} letters long.'.format(len(secret_word)))
    
    while True:
        print('-----------')
        print('You have {} guesses left.'.format(guesses_left))
        print(falling_person[8-guesses_left])
        print('Available letters:', getAvailableLetters(guessed_letters_list))
        guess = input('Please guess a letter:')
        guess = guess.lower()  
        if guess in getAvailableLetters(guessed_letters_list) and goodGuess(guess, secret_word):
            guessed_letters_list.append(guess)
            print('Good guess:', 
                  getGuessedWord(secret_word, guessed_letters_list))
        elif guess in guessed_letters_list:
            print("You have already guessed that letter. Try again:", 
                  getGuessedWord(secret_word, guessed_letters_list))
        else:
            print('That letter is not in my word:', 
                  getGuessedWord(secret_word, guessed_letters_list))
            if guess not in repeated_guesses:
                guesses_left -= 1
            repeated_guesses.append(guess)        

        if isWordGuessed(secret_word, guessed_letters_list):
            print('-----------')
            print('Congratulations, you saved the person :)')
            print(falling_person[9])
            break
        elif guesses_left == 0:
            print('-----------')
            print('You ran out of guesses. The word was {}.'.format(secret_word))
            print('R.I.P :(')
            print(falling_person[8])
            break


# 9] PLAY THE GAME!            
if __name__ == '__main__':
    falling_person_game()




