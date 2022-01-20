from .player import Player
from .table import Table
from .deck import Deck

class Game:

    def __init__(self):
        self.table = Table()
        self.deck = Deck()
        self.player = Player(self.deck, self.table)

    def start(self):
        file = open("game.txt", "w")
        while(self.player.hand_size()):
            print("--- NEXT MOVE ---")
            self.player.take_card()
            self.player.inc_score()
            file.write(">next\n")
            self._write_states(file)
            while(True):
                print("-----------------")
                self.table.show_table()
                self.player.show_hand()
                self.player.show_custom_hand()
                print("MOVES: 0 - drop, 1 - create set, 2 - add to set")
                # try:
                move = int(input("move: "))
                # skusit odchytit konkretnu chybu
                # except:
                #     print("Wrong input")
                if move == 0:
                    if self.player.drop_card():
                        self._write_after_move(0, file)
                    break
                elif move == 1:
                    if self.player.create_set():
                        self._write_after_move(1, file)
                elif move == 2:
                    if self.player.add_to_set():
                        self._write_after_move(2, file)
                else:
                    print("Wrong value! try again")
        print("Congrat.. your score is: {}".format(self.player.get_score()))
        file.write(">score\n")
        file.write(str(self.player.get_score()) + "\n")
        file.close()


    def _write_states(self, file):
        file.write(">state\n")
        file.write(">dropped\n")
        file.write(self.deck.dropped_cards_to_string() + "\n")
        file.write(">table\n")
        file.writelines(self.table.table_to_string())
        file.write(">hand\n")
        file.write(self.player.hand_to_string() + "\n")

    def _write_after_move(self, move, file):
        file.write(">move\n")
        file.write(str(move) + "\n")
        self._write_states(file)

