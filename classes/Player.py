class Player:
    def __init__(self, player_name, used_words):
        """
        Инициализируем параметры класса Игрок
        :param player_name: вводимое имя пользователя
        :param used_words: используемые пользователем слова
        """
        self.player_name = player_name
        self.used_words = used_words

    def get_words_used(self):
        """
        Получаем количество использованых слов
        :return: возвращаем количество слов из списка
        """
        return len(self.used_words)

    def add_word_to_used(self, word):
        """
        Добавляем введенные пользователем слова в список использованых слов
        :param word:
        :return: ничего не возвращаем
        """
        self.used_words.append(word)

    def is_already_used(self, word):
        """
        Проверка использования данного слово
        :param word: введенное пользователем слово
        :return: возвращаем True если введенное пользователем слово уже было использованно и есть в списке слов
        """
        return word in self.used_words

    def __repr__(self):
        """
        Заглушка для отображения репрезентация
        :return: возвращает описание объекта в читаемом виде
        """
        return f"Ваше имя: {self.player_name}\nВы использовали слова: {self.used_words}"
