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
        self._first_move = True  #TODO nastavit na True
        # self._clean_fwd = False
        self._score = 0

    def fill_hand(self):
        for i in range(0, 14):
            self._hand.append(self._deck.take_card())

    # def test_hand(self):


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

    def create_set(self):
        if len(self._hand) < 4:
            print("lack of cards")
            return False
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
                    for s in sets[i]:
                        validIndexes.append(s)
                    score += res

            if (score >= 51):
                for cards in validCards:
                    """vyloz karty na stol"""
                    self._table.add_new(cards)
                """odstran karty z ruky"""
                for index in sorted(validIndexes, reverse=True):
                    del self._hand[index]
                self._first_move = False
            else:
                print("bodov < 51 alebo nie je cista postupka")
                """invalidny tah"""
                return False

        else:
            validIndexes = []
            for i in range(0, len(cardSets)):
                if self.check_valid_cards(cardSets[i]) != -1:
                    self._table.add_new(cardSets[i])
                    for set in sets[i]:
                        validIndexes.append(set)
                    # validIndexes.append(sets[i])

            if len(validIndexes) == 0:
                """ak neodstranujem indexi nespravil som nic co by zmenilo stav"""
                return False

            for index in sorted(validIndexes, reverse=True):
                del self._hand[index]

        return True


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
        # if self._first_move:
        #     forward = self._is_clean_forward(cards)
        # else:
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
        symbol = cards[0].symbol
        first = cards[0].value
        result = first

        for i in range(1, len(cards)):
            if cards[i].value != cards[i - 1].value + 1 or cards[i].symbol != symbol:
                return -1
            if cards[i].value > 9:
                result += 10
            else:
                result += cards[i].value

        if first == 1 and cards[len(cards) - 1].value == 1:
            return -1

        if cards[len(cards) - 1].value == 1:
            result += 9

        return result

    def _is_pair(self, cards):
        symbols = [cards[0].symbol]
        first = cards[0].value
        result = first

        for i in range(1, len(cards)):
            if cards[i].symbol in symbols or cards[i].value != first:
                return -1
            symbols.append(cards[i].symbol)
            if cards[i].value > 9:
                result += 10
            else:
                result += cards[i].value

        if first == 1:
            result *= 10

        return result



    def add_to_set(self):
        if len(self._hand) < 2:
            print("invalid move remains last card")
            return False

        indexTable = int(input("Enter set from table: "))
        indexHand = int(input("Enter card: "))
        if self._table.add_to_existing(indexTable, self._hand[indexHand]):
            del self._hand[indexHand]
            # if self._table.get_joker_turn():
            #     self._hand.append(Card(0, ""))
        else:
            print("invalid move")
            return False

        return True


    def show_hand(self):
        print("HAND: ", end ="")
        for i in range(0, len(self._hand)):
        # for card in self._hand:
            print("{} ({})".format(i, self._hand[i].to_string()), end =", ")
        print()

    def show_custom_hand(self):
        print("CUSTOM HAND: ")
        # jokers = []
        heart = []
        spade = []
        diamond = []
        club = []
        for i in range(0,len(self._hand)):
            card = (i, self._hand[i])
            # if card[1].value == 0:
            #     jokers.append(card)
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

    def hand_to_string(self):
        result = []
        for card in self._hand:
            result.append(card.to_string())
        return ' '.join(result)

    def inc_score(self):
        self._score += 1

    def get_score(self):
        return self._score
