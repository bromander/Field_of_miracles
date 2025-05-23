import random
import os
import time
from files import save_and_open_playerdata as saop
clear = lambda:os.system('cls')
from colorama import init, Fore
init(autoreset=True)


def collecting_players():
    players = []
    colih = ''

    clear()

    while True:
        try:
            colih = int(input('Введите кол-во игроков: \n>> '))
        except ValueError:
            print(Fore.RED + '[ERROR] Введите цифру!!!')
        else:
            break


    for i in range(0, colih):
        clear()
        saop.print_player_list(players)
        while True:
            name = str(input(f'Игрок {i+1}, введите своё имя: \n>> '))

            if name == ' ' or name == '':
                print(Fore.RED + '[ERROR] Введите имя!!!')
            else:
                players.append(name)
                break

    clear()
    saop.print_player_list(players)
    print('Загрузка...')
    time.sleep(0.5)



    return players

def player_move(players, now, IsGuess):
    if IsGuess:
        print(f'\nСнова ходит игрок {players[now]}\n')
    else:
        now += 1
        if now >= len(players):
            now = 0
        print(f'\nХодит игрок {players[now]}\n')


    return now

if __name__ == '__main__':
    now = 0
    while True:
        ise = str(input('True of False?(1 or 0): '))
        if ise == '1':
            now = player_move(['player1', 'player2', 'player3'], now, True)
        else:
            now = player_move(['player1', 'player2', 'player3'], now, False)
        print(f'{now} - now')