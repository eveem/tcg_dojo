import unittest
from player import Player

class PlayerTest(unittest.TestCase):    
    def test_draw_success(self):
        p = Player()
        self.assertEqual(type(p.draw()), int)

    def test_can_draw_hand_is_full(self):
        p = Player()
        p.hand = [1, 2, 3, 4, 5]
        self.assertEqual(p.can_draw(), False)
    
    def test_can_draw_hand_is_not_full(self):
        p = Player()
        p.hand = [1, 2, 3, 4]
        self.assertEqual(p.can_draw(), True)

    def test_deck_empty(self):
        p = Player()
        p.deck = {}
        self.assertEqual(p.is_deck_empty(), True)

    def test_deck_not_empty(self):
        p = Player()
        p.deck = {1: 1}
        self.assertEqual(p.is_deck_empty(), False)

    def test_hand_empty(self):
        p = Player()
        p.hand = []
        self.assertEqual(p.is_hand_empty(), True)

    def test_hand_not_empty(self):
        p = Player()
        p.hand = [1]
        self.assertEqual(p.is_hand_empty(), False)

    def test_can_play_card(self):
        p = Player()
        p.hand = [5, 1, 2, 4]
        p.mana = 6
        self.assertEqual(p.can_play_card(), True)

    def test_can_not_play_card(self):
        p = Player()
        p.hand = [6]
        p.mana = 3
        self.assertEqual(p.can_play_card(), False)

if __name__ == '__main__':
    unittest.main()