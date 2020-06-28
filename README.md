# hangman
A program written in Python that lets you play the popular Hangman game. For more information about this game, go to this wikipedia page: https://en.wikipedia.org/wiki/Hangman_(game)
\n
This repository contains:
1] words.txt  (words that will be used in the game)
2] hangman_fce.py  (Python file where all the code resides)
\n
How to Play the Game:
In the game, the program provides a secret word randomly chosen from words.txt. The user is guessing the secret word by inputting letters.\n 
1] Execute hangman_fce.py \n
2] You will be asked to guess a letter in the console.\n
3] You have 8 guesses. Guesses are subtracted ONLY for an incorrect guess; if you accidentlly input a letter you have already tried, a guess is not subtracted.\n
4] You win if you guess the secret word before you have used up all your guesses.\n
\n
How the Code Works:
In order to avoid a large chunk of disorganized code, the problem was solved by dividing it into subproblems. A solution to each subproblem was coded and functionalized. In total, there are 6 helping functions inside hangman_fce.py. Then a final function: hangman_fce() was defined which put together all the helping functions.  

Making it Run Faster:
I would be happy for any pull request which would make the code more efficient. I would be also glad for any suggestion on how to improve it in any way. 

Author:
Daniel Pelnar

Contributors:

