import os
import time
from colorama import init, Fore
from files import save_and_open_playerdata as saop
init(autoreset=True)

def collect(word, letter, unfilled_word, list_of_choosed_letters):
    IsGuess = False
    clear = lambda: os.system('cls')

    word = list(word)
    now = 0

    clear()

    if letter in word:
        for i in word:
            if letter == i:
                unfilled_word.pop(now)
                unfilled_word.insert(now, letter)
            now += 1
        print(Fore.GREEN + 'Есть такая буква!')
        IsGuess = True
        list_of_choosed_letters[letter] = '1'
    else:
        print(Fore.RED + 'Такой буквы нет!')
        IsGuess = False
        list_of_choosed_letters[letter] = '2'

    time.sleep(0.2)

    return list_of_choosed_letters, unfilled_word, IsGuess

def get_letter(word, unfilled_word, list_of_choosed_letters):
    perm_one = False
    perm_two = False
    perm_three = False
    perm_four = False

    while True:

        time.sleep(0.2)
        print('Введите букву')
        letter = str(input('>> '))
        time.sleep(0.2)

        commands(letter, word)

        if len(letter) > 1:
            print(Fore.RED + '[ERROR] Нужно ввести одну букву!!!')
            continue
        else:
            perm_one = True

        if letter not in list_of_choosed_letters.keys():
            print(Fore.RED + '[ERROR] Нужно ввести букву русского алфавита!!!')
        else:
            perm_two = True

        if letter in list_of_choosed_letters.keys():
            if list_of_choosed_letters[letter] != "0":
                print(Fore.RED + '[ERROR] Вы уже вводили такую букву!!!')
            else:
                perm_three = True
        else:
            perm_three = True


        try:
            int(letter)
        except ValueError:
            perm_four = True
        else:
            print(Fore.RED + '[ERROR] Нужно ввести букву!!!')
            continue

        if perm_two and perm_one and perm_three and perm_four:
            break

    list_of_choosed_letters, unfilled_word, IsGuess = collect(word, letter, unfilled_word, list_of_choosed_letters)
    return list_of_choosed_letters, unfilled_word, IsGuess


def commands(text, word):
    if text == 'clear()':
        print('JSON был очищен!')
        saop.clear_json()
    elif text == 'getLetter()':
        print(f'Слово: {word}')
    elif text == 'allStat()':
        print(saop.open_playerlst())
