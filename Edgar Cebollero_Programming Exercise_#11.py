#Using the Deck object presented in Section 11.5, write a game program that deals a Poker hand of five cards.
#Then prompt the user to enter a series of numbers (for example: 1, 3, 5) that selects cards to be replaced during a draw phrase.
#Then print the result of drawing the new cards. You should have at least two functions, but you can have more.

from random import shuffle

#Deck class for cards
class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = [f"{rank} of {suit}" for suit in self.suits for rank in self.ranks]
        self.shuffle()

    def shuffle(self):
        shuffle(self.cards)

    def deal(self, num):
        dealt_cards = self.cards[:num]
        self.cards = self.cards[num:]
        return dealt_cards

#Function to display card hand
def display_hand(hand):
    for i, card in enumerate(hand, start=1):
        print(f"{i}: {card}")
    print()

#Function to handle new cards drawn
def draw_cards(deck, hand):

    indices_to_replace = input(
        "Enter the numbers of cards to replace (e.g., 1 3 5), or press Enter to keep all: "
    ).strip()

    if indices_to_replace:
        indices = [int(x) - 1 for x in indices_to_replace.split() if x.isdigit()]
        for i in indices:
            if 0 <= i < len(hand):
                hand[i] = deck.deal(1)[0]
    return hand

#Function for main card game
print("Welcome to Luigi's Casino, today you'll be playing cards, good luck!")
def play_poker_hand():
    deck = Deck()
    hand = deck.deal(5)

    print("Here's your initial hand:")
    display_hand(hand)  #Show initial hand once

    #Draw phase
    hand = draw_cards(deck, hand)

    print("Here's your final hand:")
    display_hand(hand)


if __name__ == "__main__":
    play_poker_hand()
