

class AItable:

    _table = []

    def __init__(self):
        self._table = []
        # for i in range(0, 4):
        #     tmp = []
        #     for j in range(0, 15):
        #         tmp.append(-1)
        #     self._table.append(tmp)

    def add_card_to_table(self, card):
        for cards in self._table:
            if self._add_to_forward(cards, card):
                return True
            if self._add_to_pair(cards, card):
                return True
        return False


    def _add_to_pair(self, cards, card):
        if cards[0].value == cards[1].value:
            if len(cards) == 4:
                return False
            if card.value == cards[0].value:
                for tmpCard in cards:
                    if tmpCard.symbol == card.symbol:
                        return False
                cards.append(card)
                return True
        return False

    def _add_to_forward(self, cards, card):
        if cards[0].value + 1 == cards[1].value and cards[0].symbol == card.symbol:
            if card.value == 1:
                if cards[0].value == 2:
                    cards.insert(0, card)
                    return True
                if cards[len(cards) - 1].value == 13:
                    cards.append(card)
                    return True
            else:
                if card.value + 1 == cards[0].value:
                    cards.insert(0, card)
                    return True
                if cards[len(cards) - 1].value != 1 and cards[len(cards) - 1].value + 1 == card.value:
                    cards.append(card)
                    return True

        return False

    def add_set_to_table(self, cards):
        self._table.append(cards)

    def show_table(self):
        print("TABLE: ")
        for i in range(0, len(self._table)):
            print("{}: ".format(i), end="")
            for card in self._table[i]:
                print(card.to_string(), end=", ")
            print()

    def get_table(self):
        return self._table
