class Player:
    def __init__(self, player_name, used_words):
        self.player_name = player_name
        self.used_words = used_words

    def get_words_used(self):
        return len(self.used_words)

    def add_word_to_used(self, word):
        self.used_words.append(word)

    def is_already_used(self, word):
        return word in self.used_words

    def __repr__(self):
        return f"Ваше имя: {self.player_name}\nВы использовали слова: {self.used_words}"
