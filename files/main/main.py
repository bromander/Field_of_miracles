import generating_main as gm
import colecting_letters as cl
import printing_abs as pabs
import checking as check
import choose_player  as cp
from files import save_and_open_playerdata as saop
import os
from colorama import init, Fore
init(autoreset=True)

clear = lambda:os.system('cls')


clear()
print(Fore.LIGHTBLUE_EX + 'Загрузка...')


def starting():
    IsGuess = False
    now = -1

    list_of_choosed_letters = {}

    for i in range(ord('а'), ord('я') + 1):
        list_of_choosed_letters[chr(i)] = '0'

    description, word, unfilled_word = gm.main()

    players = cp.collecting_players()

    clear()
    print(Fore.LIGHTBLUE_EX + f'Колличество букв: {len(word)}')
    print(f"\n {" ".join(unfilled_word)}")

    while True:
        pabs.loading(list_of_choosed_letters)
        now = cp.player_move(players, now, IsGuess)
        list_of_choosed_letters, unfilled_word, IsGuess = cl.get_letter(word, unfilled_word, list_of_choosed_letters)
        print(f"\n {" ".join(unfilled_word)}\n")

        if check.check(word, list_of_choosed_letters):
            clear()
            print(f'Поздравляем, {players[now]}, вы выиграли!')
            saop.save_playerlst(players, players[now])
            if check.continue_game():
                starting()
            else:
                clear()
                exit()

starting()