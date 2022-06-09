import copy

from classes.card import Card
from classes.deck import Deck
from classes.player import Player
from classes.player import print_cards
from classes.table import Table
from classes.game import Game
from classes.myTest import createCustom
from classes.myTest import removeFromSet
from classes.myTest import startCombinigSets, fillDict, cardsProbability
from classes.AItable import AItable
from classes.AIgame import AIgame

from classes.unitTests import TestAIplayer
import unittest

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
    for i in range(1,9):
        cards.append(Card(i, "♥"))
        # cards.append(Card(i, "♦"))
        # cards.append(Card(i, "♣"))
        # cards.append(Card(i, "♠"))
    # cards.append(Card(12, "♥"))
    # cards.append(Card(13, "♥"))
    # cards.append(Card(3, "♥"))
    created = createCustom(cards)
    for item in created:
        print_cards(item)

    print("----------------------")

    startCombinigSets(created, cards)

    # newS = removeFromSet(Card(1, "♥"), created)
    # for item in newS:
    #     print_cards(item)

def testDict():
    print("test Dict")
    cards = []
    for i in range(1, 6):
        cards.append(Card(i, "♥"))

    cards.append(Card(1, "♥"))
    cards.append(Card(9, "♥"))
    cards.append(Card(9, "♥"))
    cards.append(Card(1, "♠"))

    probs = [2, 3, 5, 1, 5, 1, 7, 2, 4]
    values = fillDict(cards, probs)
    print(values)

    newCards = [[Card(1, "♥"), Card(2, "♥"), Card(3, "♥")]]
    prob = cardsProbability(newCards, copy.deepcopy(values))
    print(prob)
    print(values)

def testAItable():
    table = AItable()
    cards = []
    cards.append(Card(1, "♥"))
    cards.append(Card(2, "♥"))
    cards.append(Card(3, "♥"))

    table.add_set_to_table(cards)
    table.show_table()

    assert table.add_card_to_table(Card(2, "♥")) == False
    assert table.add_card_to_table(Card(5, "♥")) == False
    assert table.add_card_to_table(Card(4, "♠")) == False
    assert table.add_card_to_table(Card(4, "♥")) == True

    cards = []
    cards.append(Card(11, "♠"))
    cards.append(Card(12, "♠"))
    cards.append(Card(13, "♠"))

    table.add_set_to_table(cards)
    table.show_table()

    assert table.add_card_to_table(Card(1, "♠")) == True
    assert table.add_card_to_table(Card(5, "♠")) == False
    assert table.add_card_to_table(Card(10, "♠")) == True

    cards = []
    cards.append(Card(6, "♥"))
    cards.append(Card(6, "♦"))
    cards.append(Card(6, "♠"))

    table.add_set_to_table(cards)
    table.show_table()

    assert table.add_card_to_table(Card(6, "♦")) == False
    assert table.add_card_to_table(Card(7, "♦")) == False
    assert table.add_card_to_table(Card(6, "♣")) == True

    table.show_table()


if __name__ == '__main__':
    # card = Card(1, "♠")
    # print(card.to_string())
    # test1()
    # test2()
    # test3()
    # testDict()
    # testAItable()

    game = Game()
    game.start()

    # aigame = AIgame()
    # aigame.start()

    # aiPlayerTest = unittest.TestLoader().loadTestsFromTestCase(TestAIplayer)
    # unittest.TextTestRunner().run(aiPlayerTest)