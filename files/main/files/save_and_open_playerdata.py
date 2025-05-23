import json
from colorama import init, Fore
init(autoreset=True)

json_file = 'files\\playerData.json'

def open_playerlst():
    with open(json_file, "r") as js:
        js = json.load(js)
    return js


def save_playerlst(players, winner):
    content = open_playerlst()

    for i in players:
        if i not in content['playerscore']:
            content['playerscore'][i] = 0

    try:
        content['playerscore'][winner] += 1
    except:
        content['playerscore'][winner] = 1

    with open(json_file, "w") as js:
        json.dump(content, js)


def print_player_list(players):
    print('\n')


    with open(json_file, "r") as js:
        js = json.load(js)

    for i in players:
        if i not in js['playerscore']:
            js['playerscore'][i] = 0

    for i in range(0, len(js['playerscore'].keys())):
        playername = list(js['playerscore'].keys())[i]
        playerscore = js['playerscore'][list(js['playerscore'])[i]]
        if playername in players:
            print(Fore.LIGHTBLUE_EX + f'Игрок: {playername}, {playerscore} баллов')

    print('\n')


def clear_json():
    content = {'playerscore':{}}

    with open(json_file, "w") as js:
        json.dump(content, js)