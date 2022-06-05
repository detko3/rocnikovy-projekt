from .AIdeck import AIdeck
from .AIplayer import AIplayer
from .AItable import AItable

class AIgame:

    def __init__(self):
        self.table = AItable()
        self.deck = AIdeck()
        self.player = AIplayer(self.deck, self.table)

    def start(self):
        while (self.player.hand_size()):
            print("--- NEXT MOVE ---")
            self.player.take_card()
            self.player.inc_score()
            while (True):
                print("-----------------")
                self.table.show_table()
                self.player.show_hand()
                self.player.show_custom_hand()
                print("MOVES: 0 - drop, 1 - create set, 2 - add to set")
                move = int(input("move: "))
                if move == 0:
                    prob = [int(item) for item in input("Enter the probability: ").split()]
                    self.player.drop_card(prob)
                    break
                elif move == 1:
                    prob = [int(item) for item in input("Enter the probability: ").split()]
                    if self.player.create_new_set(prob):
                        print("vylozene")
                elif move == 2:
                    prob = [int(item) for item in input("Enter the probability: ").split()]
                    if self.player.add_card(prob):
                        print("prilzene")
                else:
                    print("Wrong value! try again")
        print("Congrat.. your score is: {}".format(self.player.get_score()))
