# author: Lyric Marner
# date: July 22, 2021

from random import randint

# --------------- # Section 1 # --------------- #
# ---------- # Part 1 # ---------- #

print('----- Section 1 -----'.center(25))
print('--- Part 1 ---'.center(25))

# Conditions & Conditionals

# 1 - Conditions
print('\n' + 'Task 1' + '\n')
# Part 1 is focused on getting input from the user and comparing that input in various ways.
#
# Instructions:
#   a. Prompt input in the form of a float from the user and save to four variables: a, b, c, and d.
#       --> a has been done for you already. Feel free to change the prompt if you wish.
#   b. Print the results of the following comparisons. Number 1 has been done for you.
#       1. a == b
#       2. a == b == c
#       3. a > b > c
#       4. a < b < c < d
#       5. a != b == c != d
#       6. a >= b >= c == d
#       7. a <= b > c <= d
#
# WRITE CODE BELOW #
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
d = float(input('d = '))
print()

print('a == b |', a == b)
print('a == b == c|', a == b == c)
print('a > b > c |', a > b > c)
print('a < b < c < d |', a < b < c < d)
print('a != b == c != d |', a != b == c != d)
print('a >= b >= c == d', a >= b >= c == d)
print('a <= b > c <= d', a <= b > c <= d)
print()
# To make it faster you can copy and paste the equations. 
# Test your code out to see if it looks the way it should.
# I solved this by copying and pasting the equations into my code and then tested it by running the code and entering different numbers to see if it worked with all sorts of number combinations. 


# 2 - if Statements (ONLY USE if STATEMENTS)
print('\n' + 'Task 2' + '\n')
# Instructions:
#   a. Prompt input from the user in the form of a word, and save to a variable. Do this twice. It has been done
#       for the first word, you must do the second one yourself.
#
#   b. Write the following conditionals using ONLY if Statements:
#       1. Compare the words to see if they are the same. If so, print that they are the same.
#
#       2. Compare the words to see if they aren't the same. If so, print that they are not the same.
#
#       3. Compare the words to see if word1 is alphabetically lower (less than) than word2. If so, print that
#           the first word appears before the second word.
#
#       4. Compare the words to see if word1 is alphabetically higher (greater than) than word2. If so, print that
#           the first word appears after the second word.
#
# WRITE CODE BELOW #
word1 = input('enter a word: ')
word2 = input('enter another word: ')

if word1 == word2:
    print(word1, 'and', word2, 'are the same!')

if word1 != word2: 
    print(word1, 'and', word2, 'are not the same.')

if word1 < word2:
    print('The first word,', word1, ', appears before the second word,', word2)

if word1 > word2:
    print('The first word,', word1, ', appears before the second word,', word2)
# Refer back to the list of comparison operators if you forget what they are.
# Add a comma in your string before it ends and before the other one starts so you can separate the word that the variable will insert into the sentence. 

# 3 - if-elif-else Statements
print('\n' + 'Task 3' + '\n')
# Instructions:
#   a. Using the randint function, roll two six sided dice. One dice has been rolled for you already.
#
#   b. Write the following using if-elif-else Statements:
#       1. If both dice are the same value, print 'Doubles!' followed by the two numbers. However, if the numbers
#           are both ones, print 'Snake Eyes!' instead.
#
#       2. If both dice are even, print 'Evens!' followed by the two numbers.
#
#       3. If both dice are odd, print 'Odds!' followed by the two numbers.
#
#       4. If the sum of the values of the dice are greater than 6, print 'Win!'
#
#       5. Otherwise, print 'Lose!'
#
# WRITE CODE BELOW #
dice1 = randint(1,6)
dice2 = randint(1,6)

for i in range(1):
    if dice1 == dice2:
        print('Doubles!', dice1,',', dice2)

    elif dice1 == dice2 == 1:
        print('Snake Eyes!')

    elif dice1 == dice2 % 2 == 0:
        print('Evens', dice1,',', dice2)

    elif dice1 == dice2 % 2 == 1:
        print('Odds!', dice1,',', dice2)

    elif dice1 + dice2 > 6:
        print('Win!')
    
    else:
        print('Lose!')
# Remember to keep the if, elif, and the else sections apart so it's easier to see if you have any mistakes. 
# Make sure to indent the code when it's needed or else the data won't run correctly. 


