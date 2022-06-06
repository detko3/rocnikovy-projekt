from .card import Card
from .myTest import createCustom, filterCards, filterCardsNotFirst
from classes.player import print_cards

class AIplayer:

    _hand = []

    def __init__(self, deck, table):
        self._table = table
        self._deck = deck
        self._hand = []
        self.moves = 0
        self.fill_hands()
        self._first_move = True
        self._has_changed = True
        self._custom = []
        self._score  = 0


    def fill_hands(self):
        for i in range(0, 14):
            self._hand.append(self._deck.take_card())
        self._hand.append(-1)
        self._has_changed = True


    def drop_card(self, probability):
        position = -1
        value = -1
        for i in range(0, 15):
            if isinstance(self._hand[i], Card) and probability[i] > value:
                value = probability[i]
                position = i

        self._deck.drop_card(self._hand[position])
        self._hand[position] = -1

    def take_card(self):
        for i in range(0, 15):
            if not isinstance(self._hand[i], Card):
                self._hand[i] = self._deck.take_card()
                break
        self._has_changed = True

    def add_card(self, probability):
        position = -1
        value = -1
        for i in range(0, 15):
            if isinstance(self._hand[i], Card) and probability[i] > value:
                value = probability[i]
                position = i
        if self._table.add_card_to_table(self._hand[position]):
            self._hand[position] = -1
            return True
        return False

    def create_new_set(self, probability):
        prob = []
        # hand without -1 cards
        cards = []
        for i in range(0, 15):
            if isinstance(self._hand[i], Card):
                cards.append(self._hand[i])
                prob.append(probability[i])

        if self._has_changed:
            self._custom = createCustom(cards)
            self._has_changed = False

        if self._first_move:
            setToCreate = filterCards(self._custom, cards, prob)
            """vyloz karty odstran ich z ruky bude pole poli ak je prazdne vrati false"""
            if len(setToCreate) == 0:
                return False

            for setToCreateCards in setToCreate:
                self._table.add_set_to_table(setToCreateCards)
                #remove cards from hand
                self.remove_from_hand(setToCreateCards)

            self._first_move = False
            self._has_changed = True
            return True
        else:
            setToCreate = filterCardsNotFirst(self._custom, cards, prob)
            """vyloz a odstran bude 3jica ak je prazdna vrati false"""
            if len(setToCreate) == 0:
                return False
            self.remove_from_hand(setToCreate)
            self._has_changed = True
            return True

    def remove_from_hand(self, cards):
        for card in cards:
            for i in range(0, 15):
                if isinstance(self._hand[i], Card):
                 if card.value == self._hand[i].value and card.symbol == self._hand[i].symbol:
                     self._deck.drop_card(self._hand[i])
                     self._hand[i] = -1

    def inc_score(self):
        self._score += 1

    def show_hand(self):
        print("HAND: ", end ="")
        for i in range(0, len(self._hand)):
        # for card in self._hand:
            if isinstance(self._hand[i], Card):
                print("{} ({})".format(i, self._hand[i].to_string()), end =", ")
            else:
                print("{}({})".format(i, -1), end=", ")
        print()


    def show_custom_hand(self):
        print("CUSTOM HAND: ")
        heart = []
        spade = []
        diamond = []
        club = []
        for i in range(0,len(self._hand)):
            if isinstance(self._hand[i], Card):
                card = (i, self._hand[i])
                if card[1].symbol == "♥":
                    heart.append(card)
                elif card[1].symbol == "♠":
                    spade.append(card)
                elif card[1].symbol == "♦":
                    diamond.append(card)
                elif card[1].symbol == "♣":
                    club.append(card)

        hand = [heart, spade, diamond, club]
        for h in hand:
            if len(h):
                print("    ", end="")
                h.sort(key=lambda item: item[1].value)
                for item in h:
                    print("{} ({})".format(item[0], item[1].to_string()), end=", ")
                print()

    def hand_size(self):
        return len(self._hand)

    def get_score(self):
        return self._score

    def getHand(self):
        return self._hand