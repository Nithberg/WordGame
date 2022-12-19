class BasicWord:
    def __init__(self, original_word, set_of_words):
        '''
        Инициализирует значения
        :param original_word: исходное слово
        :param set_of_words: набор допустимых подслов
        '''
        self.original_word = original_word
        self.set_of_words = set_of_words

    def word_in_set(self, user_input):
        return user_input in self.set_of_words

    def counting_words(self):
        return len(self.set_of_words)

    def __repr__(self):
        return f"Основное слово -  {self.original_word} / Набор подслов - {self.set_of_words}"


data = {
    "original_word": "питон",
    "set_of_words": ["пони", "тон", "ион", "опт", "пот", "тип", "топ", "пион", "понт"]
}

get_words = BasicWord(data.get("original_word"), data.get("set_of_words"))
print(get_words)

user_input = "пионпп"
print(get_words.word_in_set(user_input))
print(get_words.counting_words())
