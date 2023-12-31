"""Blackjack, by Donald Teghen donaldteghen@gmail.com
The classic card game also known as 21. (This version doesn't have
splitting or insurance.)
More info at: https://en.wikipedia.org/wiki/Blackjack
This code is available at https://learningwithdonny.com/mini-games/balckjack
Tags: large, game, card game"""

import random, sys

# Set up the constants:
HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.
# (A list of chr codes is at https://inventwithpython.com/charactermap)
BACKSIDE = 'backside'

print('''
Blackjack, by Donald Teghen donaldteghen@gmail.com
      
Rules:
      
- Try to get as close to 21 without going over.
- Kings, Queens, and Jacks are worth 10 points.
- Aces are worth 1 or 11 points.
- Cards 2 through 10 are worth their face value.
- (H)it to take another card.
- (S)tand to stop taking cards.
- On your first play, you can (D)ouble down to increase your bet but must hit exactly one more time before standing.
- In case of a tie, the bet is returned to the player.
- The dealer stops hitting at 17.
''')
print('\n\n')


def main():
    money, MIN_AMOUNT, MAX_AMOUNT, MIN_BET = 0, 5000, 50000, 500, 
    while True: # amount deposiit loop
        amount = input('Topup your balance in multiples of 500 ie(500, 1000, 1500, ..., 50000) >')
        if not amount.isdecimal():
            print('Invalid input! try again')
            continue
        if MIN_AMOUNT <= int(amount) <= MAX_AMOUNT:
            money = int(amount)
            break
        if int(amount) < MIN_AMOUNT or int(amount) > MAX_AMOUNT:
            print('\nInvalid amount enter! Please enter a minimum of {} and maximum of {}\n'.format(MIN_AMOUNT, MAX_AMOUNT))
            continue
    while True: #main loop
    # check if the player has ran out money
        if money <= 0:
            print('You\'re out')
            print('Alhamdulillah! you aren\'t playing with real money')
            print('Eyvallah for the time spent!')
            sys.exit()
        #let the player enter their bet for rount 1
        print('Standing', money) 
        bet =  getBet(money)   

        #give the dealer and player 2 cards from the deck each
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        #handle player actions:
        print('Your bet is: ', bet)
        while True: # keep looping until player stands or busts(went over 21)
            displayHands(playerHand, dealerHand, False)
            print()

            #check if player has bust
            if getHandValue(playerHand) > 21:
                break
            # get the player's move either H, S or D
            move = getMove(playerHand, money - bet)
            
            #handle player actions:
            if move == 'D':
                # player is doubling down, they can increase their bet:
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}'.format(bet))
                print('Current bet is: {}'.format(bet))

            if move in ('H', 'D'):
                # Hit / double down takes another card
                newCard = deck.pop()
                rank, suit = newCard
                print('You draw a {} of {}'.format(rank, suit))
                playerHand.append(newCard)
                if getHandValue(playerHand) > 21:
                    # player has busted
                    continue
            if move in ('S', 'D'):
                #stand / doubling down stops the players turn 
                break   
        # Handle the dealer's actions
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # The dealer hits
                print('Dealer hits...')    
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break # Dealer has busted
                input('Press Enter to continue...')
                print('\n\n')

        # Show the final hands
        displayHands(playerHand, dealerHand, True)        

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        #handle whether the player won, lost or tied
        if dealerValue > 21:
            print('Dealer busts! You win ${}'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You Lost!')
            money -= bet
        elif playerValue > dealerValue:
            print('You won ${}'.format(bet))   
            money += bet  
        elif playerValue == dealerValue:
            print('It\'s a tie, the bet is returned to you')
        input('Press Enter to continue...')
        print('\n\n')


def getBet(maxbet):
    '''Ask the player how much they want to bet for this round'''
    while True: # keep asking until valid input id entered
        print('How much do you want to bet? (1--{}) or QUIT'.format(maxbet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing')
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 < bet <= maxbet:
            return bet    

def getHandValue(cards):
    ''' Return the value of the cards. face cards are worth 10, aces are worth 11 or 1 (This finctionpicks the most suitable ace value)'''
    value = 0
    numberOfAces = 0
    #Add the value for the non-ace cards:
    for card in cards:
        rank = card[0] # card is tuple like (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'): # worth 10 points
            value += 10
        else:
            value += int(rank)  # worth rank number
    # add the values for the aces
    value += numberOfAces
    for i in range(numberOfAces):
        # if another 10 can be added without busting, do so
        if value + 10 <= 21:
            value += 10 
    return value        

def getDeck():
    '''Return a list of (rank , suit) tuples for all 52 cards'''
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  
        for rank in ['J', 'K', 'Q']:
            deck.append((rank, suit)) 
    random.shuffle(deck)
    return deck
                   
def displayHands(playerHand, dealerHand, showDelaerHand):
    '''Show the player's card. Hide the dealer's first card if showDealerHand is False'''
    print()
    if showDelaerHand:
        print('DEALER: ', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')  
        # Hide the delaer's first card
        displayCards([BACKSIDE] + dealerHand[1:])  
    #show player's cards:
    print('PLAYER: ', getHandValue(playerHand))
    displayCards(playerHand)   


def displayCards(cards):
    '''Display all the cards in the card list'''
    rows = ['', '', '', ''] # The text to be display on each row

    for i, card in enumerate(cards):
        rows[0] += ' ___ ' # Print the top line of the card
        if card == BACKSIDE:
            # print a card's back
            rows[1] += '|##|'
            rows[2] += '|###|'
            rows[3] += '|_##|'
        else:
            # Print the card's front:
            rank, suit = card
            rows[1] += '|{}  |'.format(rank.ljust(2)) 
            rows[2] += '| {} |'.format(suit)  
            rows[3] += '|_ {}|'.format(rank.rjust(2))
    #print each row on screen        
    for row in rows:
        print(row)


def getMove(playerHand, money):
    """Asks the player for their move, and returns 'H' for hit, 'S' for
    stand, and 'D' for double down."""
    while True:  # Keep looping until the player enters a correct move.
        # Determine what moves the player can make:
        moves = ['(H)it', '(S)tand']

        # The player can double down on their first move, which we can
        # tell because they'll have exactly two cards:
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Get the player's move:
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move  # Player has entered a valid move.
        if move == 'D' and '(D)ouble down' in moves:
            return move  # Player has entered a valid move.


 # If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()