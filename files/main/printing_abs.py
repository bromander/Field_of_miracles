import time
from colorama import init, Fore
init(autoreset=True)

def loading(list_of_choosed_letters):
    indxs = list(list_of_choosed_letters.keys())
    abs_list = []

    for i in range(len(list_of_choosed_letters)):

        if list_of_choosed_letters[indxs[i]] == '0':
            abs_list.append("?")

        elif list_of_choosed_letters[indxs[i]] == '2':
            abs_list.append("✗")

        elif list_of_choosed_letters[indxs[i]] == '1':
            abs_list.append("✓")


    list_of_choosed_letters = list(list_of_choosed_letters.keys())
    time.sleep(0.2)
    print(f'\n{' '.join(list_of_choosed_letters[0: 8])}\n{' '.join(abs_list[0: 8])}\n\n'
          f'{' '.join(list_of_choosed_letters[8: 16])}\n{' '.join(abs_list[8: 16])}\n\n'
          f'{' '.join(list_of_choosed_letters[16: 24])}\n{' '.join(abs_list[16: 24])}\n\n'
          f'{' '.join(list_of_choosed_letters[24: 32])}\n{' '.join(abs_list[24: 32])}')
    time.sleep(0.2)
    return abs_list


if __name__ == '__main__':
    list_of_choosed_letters = {'а': '0', 'б': '0', 'в': '0', 'г': '0', 'д': '0',
                               'е': '0', 'ж': '0', 'з': '0', 'и': '0', 'й': '0',
                               'к': '0', 'л': '0', 'м': '0', 'н': '0', 'о': '0',
                               'п': '0', 'р': '0', 'с': '0', 'т': '0', 'у': '0',
                               'ф': '0', 'х': '0', 'ц': '0', 'ч': '0', 'ш': '0',
                               'щ': '0', 'ъ': '0', 'ы': '0', 'ь': '0', 'э': '0',
                               'ю': '0', 'я': '0'}


    while True:
        loading(list_of_choosed_letters)
        n = str(input('>> '))
        m = str(input('>> '))
        list_of_choosed_letters[n] = m
        loading(list_of_choosed_letters)