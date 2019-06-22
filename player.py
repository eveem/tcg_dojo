from random import choice

class Player:

    def __init__(self, pid=0):
        self.pid = pid
        self.deck = {0: 2, 1: 2, 2: 3, 3: 4, 4: 3, 5: 2, 6: 2, 7: 1, 8: 1}
        self.hand = []
        self.bleeding = False
        self.health = 30
        self.mana = 1

    def draw(self):
        if not self.is_deck_empty():
            card_cost = choice(list(self.deck.keys()))
            self.deck[card_cost] -= 1
            if self.deck[card_cost] == 0:
                self.deck.pop(card_cost)
            
            if self.can_draw():
                self.hand.append(card_cost)

    def can_draw(self):
        if len(self.hand) < 5:
            return True
        return False

    def is_deck_empty(self):
        if len(self.deck) == 0:
            return True
        return False

    def is_hand_empty(self):
        return not bool(self.hand)

    def can_play_card(self):
        lowerest_card_in_hand = min(self.hand)
        if lowerest_card_in_hand > self.mana:
            return False
        return True

    def is_end_turn(self):
        if self.is_hand_empty() or not self.can_play_card():
            return True
        return False

    def is_die(self):
        if self.health < 1:
            return True
        return False
    
    def number_of_card_left(self):
        return sum(list(self.deck.values()))