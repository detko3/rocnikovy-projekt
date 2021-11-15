
class Card:

    # spadesCards = ["🂡", "🂢", "🂣", "🂤", "🂥", "🂦", "🂧", "🂨", "🂩", "🂪", "🂫", "🂭", "🂮"]

    def __init__(self, value, symbol):
        self.value = value
        self.symbol = symbol
        # self.jokerValue = 0

        if self.value == 1:
            self.str = "A"
        elif self.value == 11:
            self.str = "J"
        elif self.value == 12:
            self.str = "Q"
        elif self.value == 13:
            self.str = "K"
        elif self.value == 0:
            self.str = "JOKER"
        else:
            self.str = value

    def to_string(self):
        return "{}{}".format(self.str, self.symbol)