from .card import Card

class AIplayer:

    def __init__(self, deck, table):
        self._table = table
        self._deck = deck
        self._hand = []
        self.moves = 0
        self.fill_hand()
        self._first_move = True


    def fill_hand(self):
        for i in range(0, 14):
            self._hand.append(self._deck.take_card())
        self._hand.append(-1)


    def drop_card(self, probability):
        position = -1
        value = -1
        for i in range(0, 14):
            if isinstance(self._hand[i], Card) and probability[i] > value:
                value = probability[i]
                position = i

        self._deck.drop_card(self._hand[position])
        self._hand[position] = -1

    def take_card(self):
        for i in range(0, 14):
            if not isinstance(self._hand[i], Card):
                self._hand[i] = self._deck.take_card()
                break

    def add_card(self, probability):
        position = -1
        value = -1
        for i in range(0, 14):
            if isinstance(self._hand[i], Card) and probability[i] > value:
                value = probability[i]
                position = i
        if self._table.add_card_to_table(self._hand[position]):
            self._hand[position] = -1
            return True
        return False





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