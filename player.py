from random import choice

class Player:

    def __init__(self):
        self.deck = {0: 2, 1: 2, 2: 3, 3: 4, 4: 3, 5: 2, 6: 2, 7: 1, 8: 1}
        self.hand = []
        self.bleeding = False

    def draw(self):
        card_cost = choice(list(self.deck.keys()))
        self.deck[card_cost] -= 1
        if self.deck[card_cost] == 0:
            self.deck.pop(card_cost)
        return card_cost

    def can_draw(self):
        if len(self.hand) < 5:
            return True
        return False


    
