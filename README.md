# Falling Man game
A program written in Python that lets you play a variation of the popular Hangman game. For more information about this game, go to this wikipedia page: https://en.wikipedia.org/wiki/Hangman_(game)
\
\
This repository contains:
\
1] words.txt  (words that can be used in the game)\
2] falling_person_game.py\
3] graphic_1.py
\
\
How to Play the Game:
\
In the game, the program provides a secret word randomly chosen from words.txt. The user is guessing the secret word by inputting letters.
\
1] Download all the 3 files in one folder and execute falling_person_game.py\
2] You will be asked to guess a letter in the console.\
3] You have 8 guesses. Guesses are subtracted ONLY for an incorrect guess; if you accidentlly input a letter you have already tried, a guess is not subtracted.\
4] You win if you guess the secret word before you have used up all your guesses.
\
\
How the Code Works:
\
In order to avoid a large chunk of disorganized code, the problem was solved by dividing it into subproblems. A solution to each subproblem was coded and functionalized. In total, there are 6 helping functions. Then a final function: falling_person_game() was defined which put together all the helping functions.  
\
\
Making it Run Faster:
\
I would be happy for any pull request which would make the code more efficient. I would be also glad for any suggestion on how to improve it in any way.\
You can commit your own graphics.
\
\
Author:
\
Daniel Pelnar
\
\
Credit:
\
A variation of this game was inspired by MIT assignment from this course:\
MITx -  6.00.1x Introduction to Computer Science and Programming Using Python

