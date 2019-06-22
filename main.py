from player import Player

def show_detail(player):
    print('--------------------------')
    print(f'|        Player {player.pid}        |')
    print('--------------------------')
    print(f'  Health    : {player.health}')
    print(f'  Hand      : {player.hand}')
    print(f'  Card left : {player.number_of_card_left()}')
    print(f'  Mana      : {player.mana}')

def show_important_detail(player):
    print(f'  Your hand : {player.hand}')
    print(f'  Your mana : {player.mana}')

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

    turn_count = [0, 0]
    game = True
    while game:
        player = players[me]
        opponent = players[op]
        player.draw()
        turn_count[me] += 1
        player.mana = min(turn_count[me], 10)
        show_detail(player)
        c = 0
        while True:
            if player.is_end_turn():
                print("\n   Can't play anything")
                print("     Force end turn!")
                break
            
            action()
            
            c = int(input())
            if c == 1:
                print('  Choose card : ', end='')
                card = int(input())
                if card in player.hand and player.mana >= card:
                    player.deal_damage(card, opponent)
                    player.use_card(card)
                    print(f"\n  Player {player.pid} health : {opponent.health}")
                elif card not in player.hand:
                    print("\n  Don't have that card!")
                elif player.mana < card:
                    print("\n  Don't have enough mana!")
                show_important_detail(player)
            elif c == 2:
                break
            else:
                print("\n      Can't do that!")
            
            if opponent.is_die():
                print('\n--------------------------')
                print('|                        |')
                print(f'|     Player {player.pid} win !     |')
                print('|                        |')
                print('--------------------------')
                game = False
                break

        me, op = switch(me, op)
