import random
from .card import Card

class AIdeck:

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


    def shuffle(self):
        random.shuffle(self._cards)

    def take_card(self):
        if len(self._cards):
            return self._cards.pop()

        self._cards = self._droppedCard
        self.shuffle()
        self._droppedCard = []
        return self._cards.pop()

    def drop_card(self, card):
        self._droppedCard.append(card)

