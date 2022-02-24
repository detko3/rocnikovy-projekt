from .card import Card

class AIplayer:

    def __init__(self, deck, table):
        self._table = table
        self._deck = deck
        self._hand = []
        self.moves = 0
        self.fill_hand()
        self._first_move = True  # TODO nastavit na True
        self._clean_fwd = False
        self._score = 0


    def fill_hand(self):
        for i in range(0, 14):
            self._hand.append(self._deck.take_card())


    def drop_card(self):
        index = int(input("index: "))
        if index >= len(self._hand) > 0:
            self._deck.drop_card(len(self._hand) - 1)
        self._deck.drop_card(self._hand.pop(index))

        """ked je prazdna koniec hry"""
        # if len(self._hand) == 0:
        #     return False
        return True


    def take_card(self):
        self._hand.append(self._deck.take_card())


    def createCustom(self):
        jokers = []
        heart = []
        spade = []
        diamond = []
        club = []
        for i in range(0, len(self._hand)):
            card = (i, self._hand[i])
            if card[1].value == 0:
                jokers.append(card)
            elif card[1].symbol == "♥":
                heart.append(card)
            elif card[1].symbol == "♠":
                spade.append(card)
            elif card[1].symbol == "♦":
                diamond.append(card)
            elif card[1].symbol == "♣":
                club.append(card)

        for i in range(0, len(heart)):
            self.create_forward(heart[i], heart[i + 1: len(heart)])

    def create_forward(self, card, cards):
        return True