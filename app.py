from flask import Flask
from random import choice

app = Flask(__name__)

CARD_COST = {0: 2, 1: 2, 2: 3, 3: 4, 4: 3, 5: 2, 6: 2, 7: 1, 8: 1}

def draw(deck):
    card_cost = choice(list(deck.keys()))
    deck[card_cost] -= 1
    if deck[card_cost] == 0:
        deck.pop(card_cost)
    return card_cost
    
@app.route("/player1")
def player1():
    p1_deck = CARD_COST
    print(draw(p1_deck))
    return 'hello'

@app.route("/player2")
def player2():
    p2_deck = CARD_COST
    return 'hello'


if __name__ == "__main__":
    app.run()
