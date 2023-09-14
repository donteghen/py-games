"""Bagels,by Donald Teghen donald.teghen@gmail.com
A deductive logic game where you must guess a number based on clues.
This code is available at https://learningwithdonny.com/mini-games/bagels
A version of this game is featured in the book "Invent Your Own
Tags: short, game, puzzle"""              

import random

NUM_DIGITS = 2  # (!) Try setting this to 1 or 10.
MAX_GUESSES = 3  # (!) Try setting this to 1 or 100.

def main():
    global NUM_DIGITS, MAX_GUESSES
    print('''\n\n
    Bagels, a deductive logic game.
   by Donald Teghen donald.teghen@gmail.com
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:
    Pico => One digit is correct but in the wrong position.
    Fermi => One digit is correct and in the right position.
    Bagels => No digit is correct.
    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.\n\n'''.format(NUM_DIGITS))

    while True:  # Main game loop.
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            if guess == secretNum:
                break  # They're correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))
        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no) or (setting) to increase the guess number size and max number of guesses')
        inp = input(' > ').lower()
        if inp == 'settings':
            NUM_DIGITS= int(input('Enter guess number length: '))
            MAX_GUESSES = int(input('Enter max quess: '))
        elif inp == 'no' or inp.startswith('n'):
            print('you entered : {} so game is exiting...'.format(inp)) 
            break         
    print('Thanks for playing!')

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secretNum:
        return 'You got it!'

    clues = []  

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()