class BasicWord:
    def __init__(self, original_word, set_of_words):
        """
        Инициализирует параметры класса Слово
        :param original_word: исходное слово
        :param set_of_words: набор допустимых подслов
        """
        self.original_word = original_word
        self.set_of_words = set_of_words

    def word_in_set(self, user_input):
        """
        Проверка введенного слова пользователем на наличие в списке допустимых подслов
        :param user_input: слово вводимое пользователем
        :return: вернет True в случае если слово есть в списке
        """
        return user_input in self.set_of_words

    def counting_words(self):
        """
        Подсчитываем количество подслов
        :return: возвращает количество подслов в списке
        """
        return len(self.set_of_words)

    def __repr__(self):
        """
        Заглушка для отображения репрезентация
        :return: возвращает описание объекта в читаемом виде
        """
        return f"Основное слово -  {self.original_word} / Набор подслов - {self.set_of_words}"
