import random

class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9',
                  '10', 'Jack', 'Queen', 'King']
    
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])
    
    def __lt__(self,other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
    
class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label
    
class Time:
    """Represents the time of day.
    
    attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __lt__(self,other):
        t1 = self.hour, self.minute, self.second
        t2 = other.hour, other.minute, other.second
        return t1 < t2
    
    
#queen_of_diamonds = Card(1,12)
#print(queen_of_diamonds)
#four_of_spades = Card(3,4)
#print(four_of_spades)
#print(queen_of_diamonds < four_of_spades)
#midday = Time(12,0,0)
#print(midday)
#elevenses = Time(11,3,42)
#print(elevenses)
#print(midday < elevenses)
deck1 = Deck()
deck1.shuffle()
#print(deck1)
#print('***END***')
#deck1.sort()
#print(deck1)
hand = Hand('new hand')
#card = deck.pop_card()
#hand.add_card(deck1.pop_card())
#print(hand)
deck1.move_cards(hand, 3)
print(hand)