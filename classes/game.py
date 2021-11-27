from .player import Player
from .table import Table
from .deck import Deck

class Game:

    def __init__(self):
        self.table = Table()
        self.deck = Deck()
        self.player = Player(self.deck, self.table)

    def start(self):
        while(self.player.hand_size()):
            print("--- NEXT MOVE ---")
            self.player.take_card()
            while(True):
                print("-----------------")
                self.table.show_table()
                self.player.show_hand()
                self.player.show_custom_hand()
                print("MOVES: 0 - drop, 1 - create set, 2 - add to set")
                # try:
                move = int(input("move: "))
                # except:
                #     print("Wrong input")
                if move == 0:
                    self.player.drop_card()
                    break
                elif move == 1:
                    self.player.create_set()
                elif move == 2:
                    self.player.add_to_set()
                else:
                    print("Wrong value! try again")

