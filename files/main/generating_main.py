from urllib.request import Request, urlopen
import json
import random
import time
from english_words import get_english_words_set
from deep_translator import GoogleTranslator

def choosing_word():
    word = get_english_words_set(['web2'], lower=True)
    word = list(word)
    word = random.choice(word)
    return word


def getting_word_definition():
    while True:
        try:
            word = choosing_word()
            URLS = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
            req = Request(
                url=URLS,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            webpage = urlopen(req).read()
        except:
            pass
        else:
            break

    description = ((((((json.loads(webpage))[0])['meanings'])[0])['definitions'])[0])['definition'].replace('(general) ', '')
    description = GoogleTranslator(source='auto', target='russian').translate(description)
    word = GoogleTranslator(source='auto', target='russian').translate(word)


    return description, word


def main():
    unfilled_word = []
    description, word = getting_word_definition()

    word = word.replace('.', '')
    word = word.replace(',', '')
    word = word.replace('ё', 'е')
    word = word.replace(' ', '')
    word = word.lower()

    for i in list(word):
        unfilled_word.append('_')
    return description, word, unfilled_word