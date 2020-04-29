#!/bin/python3

# import randint for generating random numbers later on
from random import randint

# let the player choose rock, paper, or scissors
player = input('rock (r), paper (p), or scissor (s)?')
# print ascii art depending on the player's choice
if player == 'r':
    print('O', end=' ')
elif player == 'p':
    print('__', end=' ')
else:
    print('8<', end=' ')
# if the player doesn't choose rock(r), paper(p), or scissor(s), the selection will default to scissor

# print out "vs" in between the player and computer choices
print('vs', end=' ')

# randomly generate the computer's choice
chosen = randint(1, 3)

# print ascii art depending on the computer's choice
if chosen == 1:
    computer = 'r'
    print('O')
elif chosen == 2:
    computer = 'p'
    print('__')
else:
    computer = 's'
    print('>8')

# if the player and computer choose the same thing, display the result: DRAW
if player == computer:
    print('DRAW!')

# define outcomes for different outcomes
elif player == 'r' and computer == 'p':
    print('Computer wins!')

elif player == 'r' and computer == 's':
    print('Player wins!')

elif player == 'p' and computer == 'r':
    print('Player wins!')

elif player == 'p' and computer == 's':
    print('Computer wins!')

elif player == 's' and computer == 'r':
    print('Computer wins!')

elif player == 's' and computer == 'p':
    print('Player wins!')