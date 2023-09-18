"""Caesar Cipher, by Donald Teghen donaldteghen@gmail.com
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
More info at: https://en.wikipedia.org/wiki/Caesar_cipher
View this code at https://learnwithdonny.com/mini-games/caeser-cipher
Tags: short, beginner, cryptography, math"""

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.

# Every possible symbol that can be encrypted/decrypted:
# (!) You can add numbers and punctuation marks to encrypt those
# symbols as well.
SYMBOLS = ''

print('Caesar Cipher, by Donald Teghen donaldteghen@gmail.com')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

#get 
# Get the symbol from the user or let to opt for default symbol based on the english alphabet
while True:
    ensymbols = input('Please enter the encryption symbols or "D" for the default (ABCDEFGHIJKLMNOPQRSTUVWXYZ)> ')
    if len(ensymbols) == 0:
        continue
    elif ensymbols == 'D' or ensymbols == 'd':
        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        break
    else:
        SYMBOLS = ensymbols.strip().upper()
        break
print('\nKeep your symbol and key jealously and don\'t share them unless neccessary.\n')

# Let the user enter if they are encrypting or decrypting:
while True:  # Keep asking until the user enters EC or DC.
    print('What is your operation (EC)encryption or (DC)decryption?')
    response = input('> ').lower()
    if response.startswith('e') or response.startswith('E') or response == 'EC':
        print('Your are starting an encryption operation!')
        mode = 'encrypt'
        break
    elif response.startswith('d') or response.startswith('D') or response == 'DC':
        print('Your are starting an decryption operation!')
        mode = 'decrypt'
        break
    print('Please select between EC & DC.')

# Let the user enter the key to use:
while True:  # Keep asking until the user enters a valid key.
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# Let the user enter the message to encrypt/decrypt:
print('Enter the message to {}.'.format(mode))
message = input('> ')

# Caesar cipher only works on uppercase letters:
message = message.upper()

# Stores the encrypted/decrypted form of the message:
translated = ''

# Encrypt/decrypt each symbol in the message:
for symbol in message:
    if symbol in SYMBOLS:
        # Get the encrypted (or decrypted) number for this symbol.
        num = SYMBOLS.find(symbol)  # Get the number of the symbol.
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # Handle the wrap-around if num is larger than the length of
        # SYMBOLS or less than 0:
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # Add encrypted/decrypted number's symbol to translated:
        translated = translated + SYMBOLS[num].lower()
    else:
        # Just add the symbol without encrypting/decrypting:
        translated = translated + symbol

# Display the encrypted/decrypted string to the screen:
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
    if mode == 'encrypt':
        print('You can paste it anywhere you want or paste here when its time to {} again!'.format('decript'))
    else:
        print('You can paste it anywhere you want')
except:
    pass  # Do nothing if pyperclip wasn't installed.