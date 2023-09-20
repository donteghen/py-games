"""Collatz Sequence, by Al Sweigart al@inventwithpython.com
Generates numbers for the Collatz sequence, given a starting number.
More info at: https://en.wikipedia.org/wiki/Collatz_conjecture
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, math"""

import sys, time, pprint

print('''Collatz Sequence, or, the 3n + 1 Problem
By Al Sweigart al@inventwithpython.com
The Collatz sequence is a sequence of numbers produced from a starting
number n, following three rules:
1) If n is even, the next number n is n / 2.
2) If n is odd, the next number n is n * 3 + 1.
3) If n is 1, stop. Otherwise, repeat.
It is generally thought, but so far not mathematically proven, that
every starting number eventually terminates at 1.
''')

print('Enter a starting number (greater than 0) for the number of values to represent the sequence or QUIT:')
while True:
    response = input('> ')
    if (not response.isdecimal()) and response != 'QUIT':
       print('Invalid input! Please try again')
       continue
    elif response.isdecimal() and int(response) == 0:
       print('Please enter a number greater that 0!')
       continue
    elif response == 'QUIT':
       print('Had enough fun? Well see tou next time')
       sys.exit()
    else:
       response = int(response)
       break
sequence = [response]    
while response != 1:
    isEven = response % 2 == 0
    if (isEven):
       response = response // 2
    else:
       response = (response * 3) + 1
    sequence.append(response)
print('\n\n Here is the generated sequence\n')   
time.sleep(0.1)
pprint.pprint(sequence)


