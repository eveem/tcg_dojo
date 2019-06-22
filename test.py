import unittest
from player import Player

class PlayerTest(unittest.TestCase):    
    def test_draw_success(self):
        p = Player()
        p.draw()
        self.assertEqual(len(p.hand), 1)

    def test_can_draw_hand_is_full(self):
        p = Player()
        p.hand = [1, 2, 3, 4, 5]
        p.draw()
        p.draw()
        p.draw()
        p.draw()
        self.assertEqual(len(p.hand), 5)
    
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

    def test_is_end_turn_empty_hand(self):
        p = Player()
        p.hand = []
        self.assertEqual(p.is_end_turn(), True)

    def test_is_end_turn_empty_can_not_play_card(self):
        p = Player()
        p.hand = [6]
        p.mana = 3
        self.assertEqual(p.is_end_turn(), True)

    def test_is_die_health_zero(self):
        p = Player()
        p.health = 0
        self.assertEqual(p.is_die(), True)

    def test_is_die_health_below_zero(self):
        p = Player()
        p.health = -1
        self.assertEqual(p.is_die(), True)

    def test_is_die_health_more_than_zero(self):
        p = Player()
        p.health = 1
        self.assertEqual(p.is_die(), False)

    def test_number_of_card_in_deck(self):
        p = Player()
        self.assertEqual(p.number_of_card_left(), 20)
    
    def test_number_of_card_in_deck_empty(self):
        p = Player()
        for i in range(0, 20):
            p.draw()
        self.assertEqual(p.number_of_card_left(), 0)

    def test_number_of_card_in_deck_five_left(self):
        p = Player()
        for i in range(0, 15):
            p.draw()
        self.assertEqual(p.number_of_card_left(), 5)

if __name__ == '__main__':
    unittest.main()