import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = rank["value"]
    
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10},
        ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, count):
        return [self.cards.pop() for _ in range(count)]


class Hand:
    def __init__(self, is_dealer=False):
        self.cards = []
        self.is_dealer = is_dealer
    
    def add_card(self, new_cards):
        self.cards.extend(new_cards)
    
    def calculate_value(self):
        total_value = 0
        ace_count = 0
        
        for card in self.cards:
            total_value += card.value
            if card.rank["rank"] == "A":
                ace_count += 1
        
        while total_value > 21 and ace_count > 0:
            total_value -= 10
            ace_count -= 1
        
        return total_value
    
    def is_blackjack(self):
        return len(self.cards) == 2 and self.calculate_value() == 21
    
    def display(self, reveal_dealer=False):
        if self.is_dealer:
            print("Dealer's hand:")
            for index, card in enumerate(self.cards):
                if index == 0 and not reveal_dealer and not self.is_blackjack():
                    print("Hidden")
                else:
                    print(card)
            if reveal_dealer:
                print("Dealer's hand value:", self.calculate_value())
        else:
            print("Your hand:")
            for card in self.cards:
                print(card)
            print("Your hand value:", self.calculate_value())
