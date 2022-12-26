import json
import random
from classes.BasicWord import BasicWord

DATA_SOURCE = "data_words.json"


def load_data(path):
    with open(path) as file:
        return json.load(file)


data_words = load_data(DATA_SOURCE)


def get_random_word():
    random_words = random.choice(data_words)

    basic_word = BasicWord(random_words["word"], random_words["subwords"])

    return basic_word
