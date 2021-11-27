from classes.card import Card
from classes.deck import Deck
from classes.player import Player
from classes.player import print_cards
from classes.table import Table
from classes.game import Game

def test1():
    deck = Deck()
    table = Table()
    player = Player(deck, table)

    cards1 = [Card(12, "♥"), Card(13, "♥"), Card(1, "♥")]
    cards2 = [Card(1, "♥"), Card(2, "♥"), Card(3, "♥")]
    cards3 = [Card(0, ""), Card(1, "♥"), Card(2, "♥")]
    cards4 = [Card(1, "♥"), Card(0, ""), Card(3, "♥")]
    cards5 = [Card(13, "♥"), Card(1, "♥"), Card(0, "")]
    cards6 = [Card(0, ""), Card(0, ""), Card(2, "♥")]
    cards7 = [Card(13, "♥"), Card(0, ""), Card(0, "")]
    # print_cards(cards1)
    print(player.check_valid_cards(cards1))
    print(player.check_valid_cards(cards2))
    print(player.check_valid_cards(cards3))
    print(player.check_valid_cards(cards4))
    print(player.check_valid_cards(cards5))
    print(player.check_valid_cards(cards6))
    print(player.check_valid_cards(cards7))


if __name__ == '__main__':
    # card = Card(1, "♠")
    # print(card.to_string())
    # test1()

    game = Game()
    game.start()