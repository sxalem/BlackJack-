from blackjack_project.deck import Deck, Hand


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
