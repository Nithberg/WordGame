import json
import random
from classes.BasicWord import BasicWord

DATA_SOURCE = "data_words.json"


def load_data(path):
    with open(path) as file:
        return json.load(file)


data_words = load_data(DATA_SOURCE)


def get_random_word():
    words = []

    for value in data_words:
        words.append(BasicWord(
            value["word"],
            value["subwords"]
        ))
    random.shuffle(words)

    for word in words:
        get_word = word

    print(f"Составьте {len(get_word.set_of_words)} слов из слова {get_word.original_word.upper()}")



get_random_word()
