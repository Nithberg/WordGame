from utils import *
from classes.Player import Player

player_name = input("Введите ваше имя: ")
used_words = []

player = Player(player_name, used_words)

print(f"Привет, {player.player_name}!")

word = get_random_word()
print(f"Составьте {word.counting_words()} слов из слова {word.original_word.upper()}\n"
      f"Слова не должны быть меньше 3х букв и должны быть в загаданном списке слов\n"
      f"Чтобы закончить игру необходимо угадать все слова или написать слово \"СТОП\"\n"
      f"Стартуем!")

while len(player.used_words) != word.counting_words():
    user_answer = input("Введите слово: ")
    if user_answer == "stop" or user_answer == "стоп":
        break
    elif len(user_answer) < 3:
        print("Слишком короткое слово, попробуйте еще раз!")
    elif not user_answer in word.set_of_words:
        print("Данного слова нет в списке слов для угадывания, попробуйте еще раз!")
    elif player.is_already_used(user_answer):
        print("Данное слово уже использовалось, попробуйте еще раз!")
    elif word.word_in_set(user_answer):
        print("Вы угадали, такое слово есть в списке загаданых!")
        player.add_word_to_used(user_answer)
        print()

print(f"Игра завершена! Вы угадали {player.get_words_used()} слов!")
