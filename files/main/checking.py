from colorama import init, Fore
import os
init(autoreset=True)

clear = lambda:os.system('cls')


def check(word, list_of_choosed_letters):
    now = 0

    for i in list(word):
        if list_of_choosed_letters[i] == '1':
            now += 1
    if now == len(word):
        return True
    else:
        return False

def continue_game():
    print(Fore.YELLOW + '\nПродолжить игру? (Да/Нет)\n')
    while True:
        yesorno = str(input('>> '))
        if yesorno.lower() not in ['да', 'нет']:
            print(Fore.RED + '[ERROR] Да или Нет!!!')
        else:
            if yesorno.lower() == 'нет':
                return False
            else:
                return True

if __name__ == '__main__':
    list_of_choosed_letters =  {'а': '0', 'б': '0', 'в': '1', 'г': '0', 'д': '0',
                                'е': '0', 'ж': '0', 'з': '0', 'и': '0', 'й': '0',
                                'к': '0', 'л': '1', 'м': '0', 'н': '0', 'о': '1',
                                'п': '0', 'р': '0', 'с': '1', 'т': '2', 'у': '0',
                                'ф': '0', 'х': '0', 'ц': '0', 'ч': '0', 'ш': '0',
                                'щ': '0', 'ъ': '0', 'ы': '0', 'ь': '0', 'э': '0',
                                'ю': '0', 'я': '0'}

    print(check('слово', list_of_choosed_letters))