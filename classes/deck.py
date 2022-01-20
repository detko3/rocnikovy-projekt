import random
from .card import Card


class Deck:

    def __init__(self):
        self._cards = []
        self._droppedCard = []
        self.fill_cards()
        self.shuffle()

    def fill_cards(self):
        self._cards = []
        self._droppedCard = []

        for i in range(0, 2):
            for symbol in ["♠", "♣", "♥", "♦"]:
                for value in range(1, 14):
                    self._cards.append(Card(value, symbol))

        for i in range(0, 5):
            self._cards.append(Card(0, ""))

    def shuffle(self):
        random.shuffle(self._cards)

    def take_card(self):
        if len(self._cards):
            return self._cards.pop()

        # otazka ci miesat karty
        # self._droppedCard.reverse()
        self._cards = self._droppedCard
        self.shuffle()
        self._droppedCard = []
        return self._cards.pop()


    def drop_card(self, card):
        self._droppedCard.append(card)

    def show_deck(self):
        for card in self._cards:
            print(card.to_string(), end =", ")
        print()

    def dropped_cards_to_string(self):
        result = []
        for card in self._droppedCard:
            result.append(card.to_string())

        return ' '.join(result)