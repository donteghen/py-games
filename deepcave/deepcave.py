"""Deep Cave, by by Donald Teghen donaldteghen@gmail.com
An animation of a deep cave that goes forever into the earth.
This code is available at https://learnwithdonny.com/mini-games/deepcave
Tags: tiny, beginner, scrolling, artistic"""

def display(lw, gap, rw):
    print(('#' * lw) + (' ' * gap) + ('#' * rw))
    # Check for Ctrl-C press during the brief pause:
    try:
        time.sleep(SPEED)
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.

import random, sys, time, os

# Set up the constants:
WIDTH, HEIGHT = os.get_terminal_size()  # (!) Try changing this to 10 or 30.
SPEED = 0.1  # (!) Try changing this to 0 or 1.0.

print('Deep Cave, by by Donald Teghen donaldteghen@gmail.com')
print('Press Ctrl-C to stop.')
print('\n\nHight way to hell about to beggin!\n\n')
time.sleep(1)

GAPWIDTH = 10
leftWidth = WIDTH//2 - GAPWIDTH//2

# Initially dive to the right 
for x in range(1, 11):
    if x == 11: 
        initial = False           
        break
    leftWidth += 1
    rightWidth = WIDTH - GAPWIDTH - leftWidth - 1
    display(leftWidth, GAPWIDTH, rightWidth)

#The alternative zigzag tuneling starts
while True:
    # Display the tunnel segment:
    rightWidth = WIDTH - GAPWIDTH - leftWidth
    display(leftWidth, GAPWIDTH, rightWidth)

    # Tuneling left        
    for x in range(1, 21) :
        if x == 20:            
            break
        leftWidth -= 1
        rightWidth += 1
        display(leftWidth, GAPWIDTH, rightWidth)

    # Tuneling left  
    for x in range(1, 21) :
        if x == 20:            
            break
        leftWidth += 1
        rightWidth -= 1
        display(leftWidth, GAPWIDTH, rightWidth) 

    ''' Uncomment this section and comment the above section to get a different experience'''       
    # diceRoll = random.randint(1, 6)
    # if diceRoll == 1 and leftWidth > 1:
    #     leftWidth = leftWidth - 1  # Decrease left side width.
    # elif diceRoll == 2 and leftWidth + GAPWIDTH < WIDTH - 1:
    #     leftWidth = leftWidth + 1  # Increase left side width.
    # else:
    #     pass  # Do nothing; no change in left side width.