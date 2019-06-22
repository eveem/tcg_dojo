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

if __name__ == '__main__':
    unittest.main()