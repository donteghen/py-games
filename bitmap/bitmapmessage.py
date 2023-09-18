"""Bitmap Message, by Donald donaldteghen@gmail.com
Displays a text message according to the provided bitmap image.
This code is available at https://learnwithdonny.com/mini-games/bitmapmessage
Tags: tiny, beginner, artistic"""

import  sys

message = input('Enter name for bitmap > ')
spaces = input('Enter a special for spaces. Here are your options: (s : space | d for dash | + for plus) >')
empty = '💔'
if message == ' ' or len(message) == 0: 
    sys.exit()
if (spaces == 's'): 
    empty = ' ' 
elif spaces == 'd':
    empty = '-' 
elif spaces == '+':
    empty = '+'
bitmap = open('bitmap.txt', mode='r', encoding='utf-8').readlines()
_bitmap = []
for line in bitmap:
    _line = ''
    for i, bit in enumerate(line):
        if bit == ' ':
            _line += empty
        else:
            _line += message[i % len(message)]
    _line += '\n'        
    _bitmap.append(_line)        
              
f = open('bitmapresult.txt', mode='w', encoding='utf-8')
f.writelines(_bitmap)
f.close()