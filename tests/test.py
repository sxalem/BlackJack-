from blackjack.deck import Card, Deck, Hand
from blackjack.game import BlackJackGame


def test_card():
    card = Card("hearts", {"rank": "A", "value": 11})
    assert card.suit == "hearts", "Expected suit to be 'hearts'"
    assert card.rank["rank"] == "A", "Expected rank to be 'A'"
    assert card.value == 11, "Expected value to be 11"
    assert str(card) == "A of hearts", "Expected string representation to be 'A of hearts'"


def test_deck():
    deck = Deck()
    assert len(deck.cards) == 52, "Expected deck to have 52 cards"

    original_order = deck.cards.copy()
    deck.shuffle()
    assert deck.cards != original_order, "Expected deck to be shuffled"

    dealt_cards = deck.deal(2)
    assert len(dealt_cards) == 2, "Expected to deal 2 cards"
    assert len(deck.cards) == 50, "Expected deck to have 50 cards after dealing 2"


def test_hand():
    hand = Hand()
    assert len(hand.cards) == 0, "Expected empty hand"

    deck = Deck()
    hand.add_card(deck.deal(1))
    assert len(hand.cards) == 1, "Expected hand to have 1 card"

    hand.add_card(deck.deal(1))
    assert hand.calculate_value() > 0, "Expected non-zero hand value"

    hand.add_card([Card("hearts", {"rank": "A", "value": 11})])
    assert hand.calculate_value() <= 21, "Expected hand value to be at most 21"


def test_blackjack_game():
    game = BlackJackGame()
    assert not game.game_over, "Expected game to not be over initially"

    game.deal_initial_cards()
    assert len(game.player_hand.cards) == 2, "Expected player hand to have 2 cards"
    assert len(game.dealer_hand.cards) == 2, "Expected dealer hand to have 2 cards"

    player_value = game.player_hand.calculate_value()
    dealer_value = game.dealer_hand.calculate_value()
    assert player_value > 0, "Expected non-zero player hand value"
    assert dealer_value > 0, "Expected non-zero dealer hand value"


# Running all tests
def run_tests():
    test_card()
    test_deck()
    test_hand()
    test_blackjack_game()
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
