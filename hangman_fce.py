#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:59:10 2020

@author: danielpelnar
"""

# Creating a game called Hangman
# The program 'thinks of' a word, the user is guessing.
# 8 gueesses max
# We will separate this problem into subproblems.

# Outline:
# 1] Loads words which will be available to the program
# 2] Choose one word at random. This is the secret word that user is trying to guess.
# 3] Have we guessed all the letters of the given secret word?
# 4] Get a string of letters which have already been guessed
# 5] Get letters that can still be used
# 6] Is the letter a correct guess?
# 7] Graphical illustration of nomber of guesses left
# 8] Putting it all together into one function
# 9] Play the game!


# 1]
def load_words():
    '''
    Returns a list of valid words.
    ''' 
    with open('words.txt', 'r') as file:  # words.txt contains ONE line of words.
        line = file.readline() 
    
    word_list = line.split() # Creates a list of words by splitting the string by space.
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
hanger=['''
             _____
            |     |
                  |
                  |
                  |
                 _|_''', '''
             _____
            |     |
            O     |
                  |
                  |
                 _|_''', '''
             _____
            |     |
            O     |
            |     |
                  |
                 _|_''',
                  '''
             _____
            |     |
            O     |
            |     |
            |     |
                 _|_''','''
             _____
            |     |
            O     |
            |     |
            |     |
                 _|_''', '''
             _____
            |     |
            O     |
           /|     |
            |     |
                 _|_''', '''
             _____
            |     |
            O     |
           /|\    |
            |     |
                 _|_''', ''' 
             _____
            |     |
            O     |
           /|\    |
            |     |
           /     _|_''', '''
             _____
            |     |
            O     |
           /|\    |
            |     |
           / \   _|_''','''
   ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
   ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆    

                \O/      
      ~WINNER~   |   ~WINNER~        
                 |    
                / \ 
   ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
   ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆''']
   
# 8]    
def hangman_fce():
    '''
    Starts up an interactive game of Hangman.
    '''
    print('-----------')
    print('Welcome to the game, Hangman!')
    wordList = load_words() 
    secret_word = choose_word(wordList)
    guessed_letters_list = []
    guesses_left = 8
    repeated_guesses = []
    print('I am thinking of a word that is {} letters long.'.format(len(secret_word)))
    
    while True:
        print('-----------')
        print('You have {} guesses left.'.format(guesses_left))
        print(hanger[8-guesses_left])
        print('Available letters:', getAvailableLetters(guessed_letters_list))
        guess = input('Please guess a letter:')
        guess = guess.lower()  
        if guess in getAvailableLetters(guessed_letters_list) and goodGuess(guess, secret_word):
            guessed_letters_list.append(guess)
            print('Good guess:', 
                  getGuessedWord(secret_word, guessed_letters_list))
        elif guess in guessed_letters_list:
            print("Oops! You've already guessed that letter:", 
                  getGuessedWord(secret_word, guessed_letters_list))
        else:
            print('Oops! That letter is not in my word:', 
                  getGuessedWord(secret_word, guessed_letters_list))
            if guess not in repeated_guesses:
                guesses_left -= 1
            repeated_guesses.append(guess)        

        if isWordGuessed(secret_word, guessed_letters_list):
            print('-----------')
            print('Congratulations, you won!')
            print(hanger[9])
            break
        elif guesses_left == 0:
            print('-----------')
            print('Sorry, you ran out of guesses. The word was {}.'.format(secret_word))
            print(hanger[8])
            break


# 9]
hangman_fce()


    