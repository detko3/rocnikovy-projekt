# from classes.Card import Card
from classes.deck import Deck

if __name__ == '__main__':
    # card = Card(1, "♠")
    # print(card.to_string())
    deck = Deck()
    deck.shuffle()
    deck.show_deck()
    deck.take_card()
    deck.show_deck()