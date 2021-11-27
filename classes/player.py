# from .deck import Deck
from .card import Card


def print_cards(cards):
    for card in cards:
        print(card.to_string(), end=" ")
    print()


class Player:

    def __init__(self, deck, table):
        self._table = table
        self._deck = deck
        self._hand = []
        self.moves = 0
        self.fill_hand()
        self._first_move = False  #TODO nastavit na True
        self._clean_fwd = False

    def fill_hand(self):
        for i in range (0, 14):
            self._hand.append(self._deck.take_card())

    # def test_hand(self):


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
        self._hand.append(self._deck.take_card())

    def create_set(self):
        if len(self._hand) < 4:
            print("lack of cards")
            return
        """2D pole indexov vylozenych kariet"""
        sets = []
        """2D pole vylozenych karty"""
        cardSets = []
        indexes = []
        while(True):
            lst = [int(item) for item in input("Enter the set: ").split()]
            if len(lst):
                if self._check_valid_input(lst, indexes):
                    sets.append(lst)
                    cardSet = []
                    for index in lst:
                        indexes.append(index)
                        cardSet.append(self._hand[index])
                    cardSets.append(cardSet)
            else:
                break

        if self._first_move:
            print("first move")
            score = 0
            validCards = []
            validIndexes = []
            """ak je validna pridaj do [] a pripocitaj score"""
            for i in range(0, len(cardSets)):
            # for cards in cardSets:
                res = self.check_valid_cards(cardSets[i])
                if res != -1:
                    validCards.append(cardSets[i])
                    validIndexes.append(sets[i])
                    score += res

            if (score >= 51 and self._clean_fwd):
                for cards in validCards:
                    """vyloz karty na stol"""
                    self._table.add_new(cards)
                """odstran karty z ruky"""
                for indexes in validIndexes:
                    for index in indexes:
                        self._hand.pop(index)
                self._first_move = False
            else:
                print("bodov < 51 alebo nie je cista postupka")
                self._clean_fwd = False

        else:
            validIndexes = []
            for i in range(0, len(cardSets)):
                if self.check_valid_cards(cardSets[i]) != -1:
                    self._table.add_new(cardSets[i])
                    for set in sets[i]:
                        validIndexes.append(set)
                    # validIndexes.append(sets[i])

            for index in sorted(validIndexes, reverse=True):
                del self._hand[index]


    def _check_valid_input(self, lst, indexes):
        if (len(lst) < 3):
            print("to short")
            return False

        myIndexes = indexes.copy()
        for index in lst:
            if index in myIndexes:
                print("card already used {}".format(index))
                return False
            elif index >= len(self._hand) or index < 0:
                print("card doesn't exist {}".format(index))
                return False
            else:
                myIndexes.append(index)

        return True

    def check_valid_cards(self, cards):
        if self._first_move:
            forward = self._is_clean_forward(cards)
        else:
            forward = self._is_forward(cards)

        if forward != -1:
            return forward

        pair = self._is_pair(cards)
        if pair != -1:
            return pair
        else:
            print("invalid pair/forward ", end="")
            print_cards(cards)
        return -1

    def _is_forward(self, cards):
        result = 0
        jokers_num = 0
        symbol = ""
        counter = -1
        for card in cards:
            """obsahuje max 2 zolikov"""
            if card.value == 0:
                jokers_num += 1
                if jokers_num > 2:
                    return -1
                """zolik nie je na zaciatku"""
                if counter != -1:
                    counter += 1
                """zolik na konci po Acku"""
                if counter > 14:
                    return -1
            else:
                """maju rovnaky symbol"""
                if symbol == "":
                    symbol = card.symbol
                elif card.symbol != symbol:
                    return -1
                """skontroluj hodnoty"""
                if counter == -1:
                    """zolik predbehol 1ku"""
                    if jokers_num > 0 and card.value == 1:
                        return -1
                    if jokers_num > 1 and card.value == 2:
                        return -1
                    counter = card.value
                else:
                    counter += 1
                    if counter != 14 and card.value != counter:
                        return -1
                    """Acko na konci"""
                    if counter == 14 and card.value != 1:
                        return -1
                """spocitaj skore"""
                if counter >= 10:
                    result += 10
                else:
                    result += card.value
        return result


    def _is_clean_forward(self, cards):
        isClean = True
        fwdRes = self._is_forward(cards)
        if fwdRes != -1:
            for card in cards:
                if card.value == 0:
                    isClean = False

            if isClean:
                self._clean_fwd = True
        return fwdRes

    def _is_pair(self, cards):
        result = 0
        symbols = []
        value = -1
        joker_num = 0
        for card in cards:
            """su max 2 ja zolikovia"""
            if card.value == 0:
                joker_num += 1
                if joker_num > 2:
                    return -1
            else:
                """maju rozny symbol"""
                if card.symbol in symbols:
                    return -1
                """maju rovnaku hodnotu"""
                if value == -1:
                    value = card.value
                elif card.value != value:
                    return -1
                symbols.append(card.symbol)
                """ak je Acko tak 10b"""
                if card.value == 1:
                    result += 10
                elif card.value >= 10:
                    result += 10
                else:
                    result += card.value
        return result


    def add_to_set(self):

        print("add to set")

    def show_hand(self):
        print("HAND: ", end ="")
        for i in range(0, len(self._hand)):
        # for card in self._hand:
            print("{} ({})".format(i, self._hand[i].to_string()), end =", ")
        print()

    def show_custom_hand(self):
        print("CUSTOM HAND: ")
        jokers = []
        heart = []
        spade = []
        diamond = []
        club = []
        for i in range(0,len(self._hand)):
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

        hand = [jokers, heart, spade, diamond, club]
        for h in hand:
            if len(h):
                print("    ", end="")
                h.sort(key=lambda item: item[1].value)
                for item in h:
                    print("{} ({})".format(item[0], item[1].to_string()), end=", ")
                print()

    def hand_size(self):
        return len(self._hand)

