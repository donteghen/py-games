"""Countdown, by Donald Teghen donaldteghen@gmail.com
Show a countdown timer animation using a seven-segment display.
Press Ctrl-C to stop.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
Requires sevseg.py to be in the same folder.
This code is available at https://learnwithdonny.com/mini-games/countdown
Tags: tiny, artistic"""


def addmodule():
    '''Determines if the sevseg module exits in the sys path, if no adds it'''
    try:
        sys.path.index(ADDED_PATH_TO_SEVSEG_MODULE) # this will throw a ValueError which is handled below
    except ValueError:
        print('Seven segment module isn\'t present in the list of system path. Let add that..')
        sys.path.append(ADDED_PATH_TO_SEVSEG_MODULE)
        time.sleep(1)
        print('Cutom module succefuly added')
        pass
    return

def removemodule():
    try:
        index = sys.path.index(ADDED_PATH_TO_SEVSEG_MODULE) # this will throw a ValueError which is handled below
        if index:
            print('Removing custom module from path...')            
            sys.path.remove(ADDED_PATH_TO_SEVSEG_MODULE)
            time.sleep(1)
            print('Removed successfully')
    except ValueError:
        print('Custom module wasn\'t added!')
        
    return  

ADDED_PATH_TO_SEVSEG_MODULE = '/Users/donaldteghen/Desktop/py-small-projects/seven-segment'
try:
    import sys, time
    addmodule()
    import sevseg  # Imports our sevseg.py program.

    # (!) Change this to any number of seconds:
    secondsLeft = 3


    while True:  # Main program loop.
        # Clear the screen by printing several newlines:
        print('\n' * 60)

        # Get the hours/minutes/seconds from secondsLeft:
        # For example: 7265 is 2 hours, 1 minute, 5 seconds.
        # So 7265 // 3600 is 2 hours:
        hours = str(secondsLeft // 3600)
        # And 7265 % 3600 is 65, and 65 // 60 is 1 minute:
        minutes = str((secondsLeft % 3600) // 60)
        # And 7265 % 60 is 5 seconds:
        seconds = str(secondsLeft % 60)

        # Get the digit strings from the sevseg module:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Display the digits:
        print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)

        if secondsLeft == 0:
            print()
            print('    * * * * BOOM * * * *')
            break

        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1)  # Insert a one-second pause.
        secondsLeft -= 1
    removemodule()
except Exception as e:
    if isinstance(e, ValueError):
        print('Seven segment module isn\'t present in the list of system path, please add that explicitly, then try again')
    elif isinstance(e, ModuleNotFoundError):
        print('Module not found!') 
    elif isinstance(e, KeyboardInterrupt):
        print('Countdown, by Donald Teghen donaldteghen@gmail.com') 
    sys.exit()  # When Ctrl-C is pressed, end the program.)


 
