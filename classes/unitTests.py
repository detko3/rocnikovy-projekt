from unittest import TestCase, mock
from .AIplayer import AIplayer
from .AIdeck import AIdeck
from .AItable import AItable
from .card import Card
# from unittest.mock import MagicMock

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
        player = AIplayer(AIdeck(), AItable())
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
            Card(10, "♣")
            ]

        probabiloties = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

        player.create_new_set(probabiloties)
        print(player.getHand())

        pass

    def test_add_to_set(self):
        pass