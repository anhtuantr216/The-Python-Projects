# Game 3 cay

import random 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':1, 'Queen':2, 'King':3, 'Ace':1}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has:' + deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
    def adjust_value(self):
        while self.value > 10:
            self.value -= 10
        return self.value


def display_card(player, dealer):
    print("\nDealer's Hand:")
    for i in dealer.cards:
        print(i)
    print("Dealer's Hand =", dealer.adjust_value())
    print("\nPlayer's Hand:")
    for i in player.cards:
        print(i)
    print("Player's Hand =", player.adjust_value())


total = 100
while True:
    print("Welcome to the casino. Let's play 3 cay!")
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    while True:
        try:
            bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if bet > total:
                print("Sorry, year bet can't exceed", total)
            else:
                break
    
    display_card(player_hand, dealer_hand)

    if player_hand.value > dealer_hand.value:
        print("You win!")
        total += bet
    elif player_hand.value < dealer_hand.value:
        print("Dealer win!")
        total -= bet
    else:
        print('Draw')

    if total > 0:
        print("\nPlayer's winnings stand at", total)
    else:
        print("\nYou have losen all of your chips.")
        break

    new_game = input("Would you like to play anather hand? Enter 'y' or 'n' ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing!")
        break





