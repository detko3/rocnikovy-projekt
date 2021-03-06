from classes.card import Card
from classes.deck import Deck
from classes.player import Player
from classes.player import print_cards
from classes.table import Table
from classes.game import Game
from classes.myTest import createCustom

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
    cards8 = [Card(1, "♥"), Card(0, ""), Card(0, "")]
    cards9 = [Card(0, ""), Card(1, "♥"), Card(0, "")]
    # print_cards(cards1)
    print(player.check_valid_cards(cards1))
    print(player.check_valid_cards(cards2))
    print(player.check_valid_cards(cards3))
    print(player.check_valid_cards(cards4))
    print(player.check_valid_cards(cards5))
    print(player.check_valid_cards(cards6))
    print(player.check_valid_cards(cards7))
    print(player.check_valid_cards(cards8))
    print(player.check_valid_cards(cards9))


def test2():
    table = Table()
    cards1 = [Card(0, ""), Card(12, "♥"), Card(13, "♥")]
    cards2 = [Card(0, ""), Card(0, ""), Card(1, "♥")]

    table.add_new(cards1)
    table.add_new(cards2)

    table.show_table()

    assert table.add_to_existing(0, Card(11, "♦")) == False
    assert table.add_to_existing(0, Card(10, "♥"))  == True
    assert table.add_to_existing(0, Card(11, "♥")) == True
    assert table.add_to_existing(0, Card(0, "")) == True
    assert table.add_to_existing(0, Card(1, "♥")) == True
    assert table.add_to_existing(0, Card(8, "♥")) == True

    assert table.add_to_existing(1, Card(0, "")) == False
    assert table.add_to_existing(1, Card(2, "♥")) == False
    assert table.add_to_existing(1, Card(1, "♦")) == True
    assert table.add_to_existing(1, Card(1, "♦")) == False
    assert table.add_to_existing(1, Card(1, "♣")) == True
    assert table.add_to_existing(1, Card(1, "♠")) == True
    assert table.add_to_existing(1, Card(0, "")) == False

    table.show_table()

def test3():
    cards = []
    for i in range(3,6):
        cards.append(Card(i, "♥"))
    cards.append(Card(1, "♥"))
    cards.append(Card(8, "♥"))
    cards.append(Card(0, ""))
    cards.append(Card(0, ""))
    # cards.append(Card(3, "♥"))
    created = createCustom(cards)
    for item in created:
        print_cards(item)

if __name__ == '__main__':
    # card = Card(1, "♠")
    # print(card.to_string())
    # test1()
    # test2()
    test3()

    # game = Game()
    # game.start()