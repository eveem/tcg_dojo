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

if __name__ == "__main__":
    player_1 = Player(1)
    player_1.draw()
    player_1.draw()
    player_1.draw()
    show_detail(player_1)

    while True:
        action()
        c = input()
        if c == '1' or c == '2':
            print(c)
            break
        else:
            print("\n      Can't do that !")


