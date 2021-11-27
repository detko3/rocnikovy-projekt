

class Table:

    def __init__(self):
        self._table = []
        self.jokerTurn = False

    """pridaj novy set"""
    def add_new(self, cards):
        self._table.append(cards)
        # return self._check_and_add_new()
        #TODO if its first check 51 and cista postupka

        # self._table.append(cards)

    """pridaj kartu k dakemu setu"""
    def add_to_existing(self, index, card) -> bool:
        if index >= len(self._table) > 0:
            return self._check_and_add(len(self._table) - 1, card)

        return self._check_and_add(index, card)

    # def _check_and_add_new(self, cards):
    #     #zatial ratam s tym ze to je dobre
    #     self._table.append(cards)
    #     #moj fancy strom
    #     return True

    def _check_and_add(self, index, card) -> bool:
        if not len(self._table):
            return False

        if index >= len(self._table):
            index = len(self._table) - 1

        #TODO je JOKER

        #TODO if forward add and sava value
        isforward = self._add_to_forward(index, card)
        if isforward:
            return True

        #TODO je trojica/pairs
        ispair = self._add_to_pair(index, card)
        if ispair:
            return True

        return False

    def _add_to_forward(self, index, card):
        cards = self._table[index]
        """nesmu byt vsetky 3 rovnake mozu byt max 2 zoliky"""
        if cards[0].value == cards[1].value and cards[1] == cards[2]:
            return False

        """karta ma iny symbol"""
        for c in cards:
            if c.symbol != card.symbol:
                return False

        # TODO karta je Acko dat use case ci sa da dat na zaciatok alebo koniec moze mat hodnotu 1/14

        """kartu viem ulozit dopredu"""
        for i in range(0,3):
            if cards[i].value != 0 and card.value + i + 1 == cards[i].value:
                cards.insert(0, card)
                return True

        """kartu vieme pridat na koniec"""
        for i in range(0, 3):
            if cards[len(cards) - 1 - i].value != 0 and cards[len(cards) - 1 - i].value + 1 + i == card.value:
                cards.append(card)
                return True

        """karta moze byt zamenena s zolikom"""
        for i in range(0,len(cards)):
            """karta je zolik"""
            if cards[i].value == 0:
                """karta nie je posledna"""
                if i < len(cards) - 1:
                    """nasledujuca karta nie je zolik"""
                    if cards[i + 1].value != 0:
                        if cards[i + 1].value == card.value + 1:
                            cards[i] = card
                            self.jokerTurn = True
                            return True
                        """nasledujuca karta je zolik"""
                    else:
                        """karta je prva"""
                        if i == 0:
                            if cards[i + 2].value == card.value + 2:
                                cards[i] = card
                                self.jokerTurn = True
                                return True
                            """karta nie je prva"""
                        else:
                            if cards[i - 1].value == card.value - 1:
                                cards[i] = card
                                self.jokerTurn = True
                                return True
                    """karta je posledna"""
                else:
                    """predosla je zolik"""
                    if cards[i - 1].value == 0:
                        if cards[i - 2].value + 2 == card.value:
                            cards[i] = card
                            self.jokerTurn = True
                            return True
                        """predosla nie je zolik"""
                    else:
                        if cards[i - 1].value + 1 == card.value:
                            cards[i] = card
                            self.jokerTurn = True
                            return True

        return False

    def _add_to_pair(self, index, card):
        cards = self._table[index]

        """znak sa uz nachadza alebo ine cislo"""
        for c in cards:
            if c.symbol == card.symbol:
                return False
            elif c.value != 0 and c.value != card.value:
                return False

        # TODO som zolik chcem pridat a nie zamenit

        """ak ma zolika vymen"""
        for i  in range(0, len(cards)):
            if cards[i].value == 0:
                cards[i] = card
                self.jokerTurn = True
                return True

        cards.append(card)

    def show_table(self):
        print("TABLE: ")
        for i in range(0, len(self._table)):
            print("{}: ".format(i), end="")
            for card in self._table[i]:
                print(card.to_string(), end=", ")
            print()

