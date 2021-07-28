# author: Lyric Marner
# date: july 22, 2021

# --------------- # Section 2 # --------------- #
# ---------- # Part 1 # ---------- #

print('----- Section 2 -----'.center(25))
print('--- Part 1 ---'.center(25))

# 2 - Palindrome
print('\n' + 'Task 1' + '\n')
#
# Background: A palindrome is a word that is the same if read forwards and backwards. Examples of palindromes include:
#   - mom
#   - dad
#   - radar
#   - deified
#
# Instructions
#   a. Prompt input from the user in the form of a word.
#   b. Determine if the word is a palindrome.
#       a. If so, print that the word is a palindrome.
#       b. Otherwise, print that the word is not a palindrome.

word = input('Enter a word: ')
word = word.lower
length = len(word)

for i in range(1):
    if length % 3 == 1: 
        print('This word is a palindrome!')
    else:
        print('This word is not a palindrome.')


# Make sure to add colons after your if statements so they run correctly. 

# 2 - for Loop Patterns
print('\n' + 'Task 2' + '\n')
#
#
# Instructions
#   a. Create at least two of the following patterns using for loops and conditionals. One has been done for you as an
#       example. You still have to do two more. You are free to choose which ones you do.
#   b. Use the symbol specified by the user.

# $$$$$ | i = 0
# $     | i = 1
# $     | i = 2
# $$$$$ | i = 3
# $     | i = 4
# $     | i = 5
# $$$$$ | i = 6

# When i is evenly divisible by 3 --> 5 symbols. Otherwise, 1 symbol.

s = input('>> symbol | ')

for i in range(7):
    if i % 3 == 0:
        print(s * 5)
    else:
        print(s)

print()
# 
s = input('Enter a symbol: ')

for i in range(6):
    if i == 5:
        print(s * 5)
    else: 
        print(s)

s = input('Enter a symbol: ')
for i in range(7):
    if i % 6 == 0:
        print(s * 4)
    else:
        print(s + ' ' * 3 + s)
# Write out the position of i for the patterns so it's easier to find the pattern that you can make code to.
# I used the addition symbol to add together the spaces and the singular symbols on each side to get the spaces within the pattern. 

print()

# ****  i = 0
# *   * i = 1 
# *   * i = 2
# *   * i = 3
# *   * i = 4
# *   * i = 5 
# ****  i = 6


# &      i = 0
# &      i = 1
# &      i = 2
# &      i = 3
# &      i = 4
# &&&&&  i = 5


# @   @    
# @   @   
#  @ @    
#   @      
#  @ @    
# @   @     
# @   @    


# -------
#      -
#     -
#    -
#   -
#  -
# -------
