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


player_name = 'Alex'
used_words = ["братишка", "писюшка"]

player_one = Player(player_name, used_words)
print(player_one)
print(player_one.get_words_used())
print(player_one.is_already_used("писюшка"))

player_one.add_word_to_used('аркашка')
print(player_one)
