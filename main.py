#!/bin/python3

# print an introduction
print('Hi, my name is Forrest and I\'m learning to code.')
# display ASCII art
print('''''''''             ccee88oo
         C8O8O8Q8PoOb o8oo
       dOB69QO8PdUOpugoO9bD
     CgggbU8OU qOp qOdoUOdcb
       6OuU  /p u gcoUodpP
           \\\//  /douUP
             \\\////
             |||/\\
             |||\/
             |||||
       .....//||||\....''''''''''')
# empty line for formatting
print('')

# more information about me
print('I live in Seattle.')
# display ASCII art
print('''''''''''''''''''''''''''''''''                     *
                     :
                     |
                     |
                     |
                    :|:
                    |||
               _____|||_____
              /=============\\
          ---<~~~~~~~~~~~~~~~>---
              \-------------/
               \___________/
                 \||:::||/
                  ||:::||
                  ||:::||
                  ||:::||
                  ||ooo||
                  ||___||
                  ||:::||
                  ||:::||
                  ||:::||
                  ||:::||
                  ||:::||
                 /||:::||\\
                / ||:::|| \\
               /  ||:::||  \\
              /   ||:::||   \\
          ___/____||:::||____\\____
         /~~~~~~~~~~~~~~~~~~~~~~~~\\
        /   |~~~~~~~~|  _____      \\
        |   |________| |  |  |     | 
________|___|________|_|__|__|_____|________''''''''''''''''''''')
# empty line for formatting
print('')

# define variable 'born'
# prompt user for input
born=input('What year were you born? ')
# convert user input into whole integer numbers
born=int(born)
# calculate how old the user will be in 2025 given their input
age=(2025-born)
# show the user how old they will be in 2025
print'In the year 2025, you will be' ,age, 'years old.'
# empty line for formatting
print('')

# define 'dogage'
dogage=(age*7)
# show the user how old they will be in 2025 in dog years
print'If you were a dog, you would be' ,dogage, 'years old!'
# display ASCII art
print('''Q____/
||||''''')