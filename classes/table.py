

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
            return self._check_and_add(len(self._table) - 1, card)

        return self._check_and_add(index, card)


    def _check_and_add(self, index, card) -> bool:
        self._jokerTurn = False
        if not len(self._table):
            return False

        if index >= len(self._table):
            index = len(self._table) - 1

        """je postupka"""
        isforward = self._add_to_forward(index, card)
        if isforward:
            return True
        """je pair"""
        ispair = self._add_to_pair(index, card)
        if ispair:
            return True

        return False

    def _add_to_forward(self, index, card):
        cards = self._table[index]
        symbol = ""
        counter = -1
        values = []
        jokerNum = 0

        for i in range(0, len(cards)):
            c = cards[i]
            """karta je zolik"""
            if c.value == 0:
                jokerNum += 1
                if counter != - 1:
                    counter += 1
                    values.append(counter)
            else:
                """prva karta s hodnotou"""
                if counter == -1:
                    counter = c.value
                    for j in range(0, i):
                        values.append(counter - i + j)
                    values.append(counter)
                    symbol = c.symbol
                else:
                    counter += 1
                    """nie som postupka """
                    if symbol != c.symbol:
                        return False
                    else:
                        if counter == 14 and c.value != 1:
                            return False
                        elif counter != 14 and counter != c.value:
                            return False
                        else:
                            values.append(counter)

        # print(values)

        """nie je postupka"""
        if values[0] < 1:
            return False
        """nie je postupka"""
        if values[len(values) - 1] > 14:
            return False

        """karta je zolik"""
        if card.value == 0:
            if jokerNum > 2:
                return False
            if values[len(values) - 1] < 13:
                cards.append(card)
                return True
            else:
                cards.insert(0, card)
                return True
        else:
            """zly symbol"""
            if card.symbol != symbol:
                return False

        for i in range(0, len(values)):
            """mozem zamenit za zolika"""
            if card.value == values[i] and cards[i].value == 0:
                cards[i] = card
                self._jokerTurn = True
                return True
            else:
                """pridat na zaciatok"""
                if i == 0 and values[i] != 1 and card.value == values[i] - 1:
                    cards.insert(0, card)
                    return True
                """mozem pridat na koniec"""
                lastI = len(values) - 1
                if i == lastI:
                    if values[lastI] == 13 and card.value == 1:
                        cards.append(card)
                        return True
                    elif card.value == values[lastI] + 1:
                        cards.append(card)
                        return True

        return False

    def _add_to_pair(self, index, card):
        cards = self._table[index]
        joker_num = 0

        """kariet je viac nez 3"""
        if len(cards) > 3:
            return False
        """som zolik"""
        if card.value == 0:
            for c in cards:
                if c.value == 0:
                    joker_num += 1
                    if joker_num >= 2:
                        return False
            cards.append(card)
            return True

        """znak sa uz nachadza alebo ine cislo"""
        for c in cards:
            if c.symbol == card.symbol:
                return False
            elif c.value != 0 and c.value != card.value:
                return False

        """ak ma zolika vymen"""
        for i  in range(0, len(cards)):
            if cards[i].value == 0:
                cards[i] = card
                self._jokerTurn = True
                return True

        cards.append(card)
        return True

    def get_joker_turn(self):
        return self._jokerTurn

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