from player import Player

def show_detail(player):
    print('--------------------------')
    print(f'|        Player {player.pid}        |')
    print('--------------------------')
    print(f'  Health    : {player.health}')
    print(f'  Hand      : {player.hand}')
    print(f'  Card left : {player.number_of_card_left()}')
    print(f'  Mana      : {player.mana}')

def action():
    print('--------------------------')
    print('|    Choose something    |')
    print('--------------------------')
    print('  (1) Play any card')
    print('  (2) End turn?')
    print('  Enter your choice : ', end='')

def switch(me, op):
    return op, me

if __name__ == "__main__":
    players = []
    players.append(Player(1))
    players.append(Player(2))

    for player in players:
        player.initial_hand()

    me = 0
    op = 1

    while True:
        show_detail(players[me])
        c = 0
        while True:
            action()
            c = input()
            if c == '1':
                break
            if c == '2' or players[me].is_end_turn():
                me, op = switch(me, op)
                break
            else:
                print("\n      Can't do that !")
