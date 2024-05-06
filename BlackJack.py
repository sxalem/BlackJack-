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

class BlackJackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand(is_dealer=True)
        self.game_over = False
    
    def deal_initial_cards(self):
        self.player_hand.add_card(self.deck.deal(2))
        self.dealer_hand.add_card(self.deck.deal(2))
    
    def player_turn(self):
        while True:
            self.player_hand.display()
            choice = input("Would you like to 'hit' or 'stand'? ").strip().lower()
            
            if choice in ["h", "hit"]:
                self.player_hand.add_card(self.deck.deal(1))
                if self.player_hand.calculate_value() > 21:
                    print("Busted! You went over 21.")
                    self.game_over = True
                    break
            elif choice in ["s", "stand"]:
                break
            else:
                print("Invalid choice. Please choose 'hit' or 'stand'.")
    
    def dealer_turn(self):
        while self.dealer_hand.calculate_value() < 17:
            self.dealer_hand.add_card(self.deck.deal(1))
    
    def determine_winner(self):
        player_value = self.player_hand.calculate_value()
        dealer_value = self.dealer_hand.calculate_value()

        self.dealer_hand.display(reveal_dealer=True)

        if dealer_value > 21:
            print("Dealer busted! You win!")
        elif player_value > 21:
            print("You busted! Dealer wins.")
        elif dealer_value == player_value:
            print("It's a tie!")
        elif player_value > dealer_value:
            print("You win!")
        else:
            print("Dealer wins.")

    def play(self):
        self.deal_initial_cards()

        if self.dealer_hand.is_blackjack():
            self.dealer_hand.display(reveal_dealer=True)
            if self.player_hand.is_blackjack():
                print("Both dealer and player have blackjack. It's a tie!")
            else:
                print("Dealer has blackjack. Dealer wins.")
            self.game_over = True
        
        if not self.game_over:
            self.player_turn()
        
        if not self.game_over:
            self.dealer_turn()
        
        if not self.game_over:
            self.determine_winner()

        print("\nThanks for playing!")
