"""Caesar Cipher Hacker, by Donald Teghen donaldteghen@gmail.com
This programs hacks messages encrypted with the Caesar cipher by doing
a brute force attack against every possible key.
More info at:
https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher
This code is available at  https://learnwithdonny.com/mini-games/caeser-hacker
Tags: tiny, beginner, cryptography, math"""

import time
print('\n\n Caesar Cipher Hacker, by Donald Teghen donaldteghen@gmail.com \n\n')
print('\nIdeally, your are expected to know the encryption sysbols used during encoding, else the result might be beyond weird 🤓!\n')

# Every possible symbol that can be encrypted/decrypted:
# (This must match the SYMBOLS used when encrypting the message.)
SYMBOLS = ''

# Get the sysmbols
while True:
    ensymbols = input('Please enter the encryption symbols > ')
    if len(ensymbols) == 0:
        continue
    else:
        SYMBOLS = ensymbols.strip().upper()
        break
# Let the user specify the message to hack:
print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ')
message = message.upper()
time.sleep(5)
print('Decription start for the message:  {}'.format(message))

for key in range(len(SYMBOLS)):  # Loop through every possible key.
    translated = ''

    # Decrypt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)  # Get the number of the symbol.
            num = num - key  # Decrypt the number.

            # Handle the wrap-around if num is less than 0:
            if num < 0:
                num = num + len(SYMBOLS)

            # Add decrypted number's symbol to translated:
            translated = translated + SYMBOLS[num]
        else:
            # Just add the symbol without decrypting:
            translated = translated + symbol

    # Display the key being tested, along with its decrypted text:
    print('Key #{}: {}'.format(key, translated))