

class Table:

    def __init__(self):
        self._table = []
        self._jokerTurn = False

    """pridaj novy set"""
    def add_new(self, cards):
        self._table.append(cards)

    """pridaj kartu k dakemu setu"""
    def add_to_existing(self, index, card) -> bool:
        if index >= len(self._table) > 0:
            index = len(self._table) - 1

        if self._add_to_forward(self._table[index], card):
            return True
        if self._add_to_pair(self._table[index], card):
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



    def show_table(self):
        print("TABLE: ")
        for i in range(0, len(self._table)):
            print("{}: ".format(i), end="")
            for card in self._table[i]:
                print(card.to_string(), end=", ")
            print()

    def table_to_string(self):
        result = []

        for cards in self._table:
            tmpSet = []
            for card in cards:
                tmpSet.append(card.to_string())
            result.append(' '.join(tmpSet) + "\n")

        return result