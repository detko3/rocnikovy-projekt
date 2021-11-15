from .player import Player
from .table import Table
from .deck import Deck

class Game:

    def __init__(self):
        self.table = Table()
        self.deck = Deck()
        self.player = Player(self.deck, self.table)

    def start(self):
        while(True):
            self.table.show_table()
            self.player.take_card()
            self.player.show_hand()
            print("MOVE: 0 - drop, 1 - create set, 2 - add to set")
            move = int(input("move: "))
            if move == 0:
                if self.player.drop_card():
                    break
            elif move == 1:
                self.player.create_set()
            elif move == 2:
                self.player.add_to_set()
            else:
                print("Wrong value! try again")
