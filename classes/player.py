# from .deck import Deck


class Player:

    def __init__(self, deck, table):
        self._table = table
        self._deck = deck
        self._hand = []
        self.moves = 0
        self.fill_hand()

    def fill_hand(self):
        for i in range (0, 14):
            self._hand.append(self._deck.take_card())

    def drop_card(self):
        index = int(input("index: "))
        if index >= len(self._hand) > 0:
            self._deck.drop_card(len(self._hand) - 1)
        self._deck.drop_card(self._hand.pop(index))

        """ked je prazdna koniec hry"""
        if len(self._hand):
            return False
        return True


    def take_card(self):
        self._hand.append(self._deck.take_card)

    def create_set(self):
        print("create set")

    def add_to_set(self):

        print("add to set")

    def show_hand(self):
        print("HAND: ", end ="")
        for card in self._hand:
            print(card.to_string(), end =", ")

