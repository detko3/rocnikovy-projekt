from unittest import TestCase, mock
from .AIplayer import AIplayer
from .AIdeck import AIdeck
from .AItable import AItable
from .card import Card
# from unittest.mock import MagicMock
from classes.player import print_cards

class TestAIplayer(TestCase):

    @mock.patch.object(AIplayer, '_hand', new_callable=mock.PropertyMock)
    @mock.patch.object(AIplayer, 'fill_hands', new_callable=mock.MagicMock)
    def test_drop_card(self, hand_mock: mock.PropertyMock, fill_hand_mock: mock.MagicMock):
        # hand_mock.return_value = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        fill_hand_mock.return_value = [
            Card(1, "♥"),
            Card(2, "♥"),
            Card(3, "♥"),
            Card(4, "♥"),
            Card(5, "♥"),
            Card(6, "♥"),
            Card(7, "♥"),
            Card(8, "♥"),
            Card(9, "♥"),
            Card(10, "♥"),
            Card(11, "♥"),
            Card(12, "♥"),
            Card(13, "♥"),
            Card(10, "♥"),
            Card(12, "♥")]
        player = AIplayer(AIdeck(), AItable())
        probabiloties1 = [0.8, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
        probabiloties2 = [0.8, 0.5, 0.7, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

        player.drop_card(probabiloties1)
        player.drop_card(probabiloties2)

        result = player.getHand()
        self.assertEqual(-1, result[0])
        self.assertEqual(-1, result[2])
        self.assertEqual(True, isinstance(result[1], Card))

    @mock.patch.object(AIplayer, '_hand', new_callable=mock.PropertyMock)
    @mock.patch.object(AIplayer, 'fill_hands', new_callable=mock.MagicMock)
    def test_create_set(self, hand_mock: mock.PropertyMock, fill_hand_mock: mock.MagicMock):
        table = AItable()
        player = AIplayer(AIdeck(), table)
        fill_hand_mock.return_value = [
            Card(1, "♥"),
            Card(2, "♥"),
            Card(4, "♠"),
            Card(3, "♥"),
            Card(5, "♥"),
            Card(6, "♠"),
            Card(7, "♥"),
            Card(8, "♣"),
            Card(9, "♥"),
            Card(10, "♥"),
            Card(11, "♥"),
            Card(12, "♥"),
            Card(10, "♠"),
            Card(10, "♦"),
            Card(10, "♣")
            ]

        probabiloties = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.5, 0.5, 0.7, 0.5, 0.5, 0.5]

        res = player.create_new_set(probabiloties)
        result = player.getHand()
        self.assertTrue(res)
        self.assertEqual(-1, result[14])
        self.assertEqual(-1, result[13])
        self.assertEqual(-1, result[12])
        self.assertEqual(-1, result[11])
        self.assertEqual(-1, result[10])
        self.assertEqual(-1, result[9])
        self.assertEqual(2, len(table.get_table()))

        # player.show_hand()

        probabilities2 = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.5, 0.5, 0.7, 0.5, 0.5, 0.5]
        res2 =  player.create_new_set(probabilities2)
        self.assertTrue(res2)
        self.assertEqual(-1, result[0])
        self.assertEqual(-1, result[1])
        self.assertEqual(-1, result[3])

        # print(player.getHand())
        # player.show_hand()
        # table.show_table()


    @mock.patch.object(AIplayer, '_hand', new_callable=mock.PropertyMock)
    @mock.patch.object(AIplayer, 'fill_hands', new_callable=mock.MagicMock)
    def test_create_set2(self, hand_mock: mock.PropertyMock, fill_hand_mock: mock.MagicMock):
        table = AItable()
        player = AIplayer(AIdeck(), table)
        fill_hand_mock.return_value = [
            Card(1, "♥"),
            Card(2, "♥"),
            Card(4, "♠"),
            Card(4, "♥"),
            Card(5, "♥"),
            Card(6, "♠"),
            Card(7, "♥"),
            Card(8, "♣"),
            Card(9, "♥"),
            Card(10, "♥"),
            Card(11, "♥"),
            Card(12, "♥"),
            Card(10, "♠"),
            Card(10, "♦"),
            Card(1, "♣")
        ]

        probabilities = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.5, 0.5, 0.7, 0.5, 0.5, 0.5]

        res = player.create_new_set(probabilities)
        result = player.getHand()

        for resCard in result:
            self.assertEqual(True, isinstance(resCard, Card))
            self.assertEqual(0, len(table.get_table()))
            self.assertFalse(res)


    @mock.patch.object(AItable, '_table', new_callable=mock.PropertyMock)
    def test_add_to_set(self,  table_mock: mock.PropertyMock):
        table = AItable()

        table_mock.return_value = [
            [Card(10, "♠"), Card(10, "♦"), Card(10, "♣")],
            [Card(5, "♥"), Card(6, "♥"), Card(7, "♥")]
        ]

        res1 = table.add_card_to_table(Card(10, "♥"))
        res2 = table.add_card_to_table(Card(3, "♥"))
        res3 = table.add_card_to_table(Card(4, "♥"))
        res4 = table.add_card_to_table(Card(8, "♥"))
        res5 = table.add_card_to_table(Card(10, "♥"))

        self.assertTrue(res1)
        self.assertFalse(res2)
        self.assertTrue(res3)
        self.assertTrue(res4)
        self.assertFalse(res5)

        table.show_table()
