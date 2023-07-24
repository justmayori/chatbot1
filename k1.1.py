import random 
import pyjokes
from art import *

def game_rspfull(*args: int) -> int:

    def game_rsp(*args):
        variables = ('Ножиці', 'Папір', 'Камінь')
        return random.choice(variables)

    while True:
        user_choice = int(input("1 - Ножиці\n"
                                "2 - Камінь\n"
                                "3 - Папір\n"
                                "0 - Вийти\n"))
        random_var = game_rsp()

        match user_choice:
            case 1:
                user_choice = 'Ножиці'
                if random_var == 'Камінь':
                    print(f"{user_choice} vs {random_var}")
                    print("Ви програли")
                elif random_var == 'Папір':
                    print(f"{user_choice} vs {random_var}")
                    print("Ви виграли")
                elif random_var == 'Ножиці':
                    print(f"{user_choice} vs {random_var}")
                    print("Нічия")
            case 2:
                user_choice = 'Камінь'
                if random_var == 'Камінь':
                    print(f"{user_choice} vs {random_var}")
                    print("Нічия")
                elif random_var == 'Папір':
                    print(f"{user_choice} vs {random_var}")
                    print("Ви програли")
                elif random_var == 'Ножиці':
                    print(f"{user_choice} vs {random_var}")
                    print("Ви виграли")
            case 3:
                user_choice = 'Папір'
                if random_var == 'Папір':
                    print(f"{user_choice} vs {random_var}")
                    print("Нічия")
                elif random_var == 'Ножиці':
                    print(f"{user_choice} vs {random_var}")
                    print("Ви програли")
                elif random_var == 'Камінь':
                    print(f"{user_choice} vs {random_var}")
                    print("Ви виграли")
            case 0:
                print("Допобачення")
                break
            case _:
                print("Некоректний запит")
                continue
# game_rspfull()

def jokesxd():
    joke = pyjokes.get_joke()
    print(joke)

def text2artfunc():
    custom_art = input("Введіть текст англійською: ")
    print(text2art(custom_art)) 

def chat_bot():
    
    while True:
        choice = int(input("Оберіть опцію:\n"
                           "1 - Камінь-ножиці-папір\n"
                           "2 - Жарти англійською\n"
                           "3 - Арт з тексту\n"
                           "0 - Вийти\n"))
        match choice:
            case 1:
                game_rspfull()
            case 2:
                jokesxd()
            case 3:
                text2artfunc()
            case 0:
                break
            case _:
                print("Неправильний вибір. Спробуйте ще раз.")
                continue          


chat_bot()











