# Получение статистики сервера (как общая так и для одного пользователя)

import requests

key = True


# метод для выбора статистики
def stat():
    print("""
        1 - Полная статистика
        2 - Статистика пользователя
        3 - Выход""")

    what_stat = str(input("Введите номер получаемой статистики: "))
    return what_stat


# метод для выхода из программы
def exit_loop():
    input_for_exit = input("Хотите выйти? (y/n) ")
    if input_for_exit == "y":
        return False
    elif input_for_exit == "n":
        return True


while key:
    key_stat = stat()
    if key_stat == "1":
        statistics = requests.get("http://127.0.0.1:5000/statistic")
        data = statistics.json()
        print("All users on server: ", data["Users"])
        print("All messages on server: ", data["All messages"])
        key = exit_loop()
    elif key_stat == "2":
        user_name = input("Введите имя пользователя: ")
        user_statistic = requests.post(
            "http://127.0.0.1:5000/userstat",
            json={"username": user_name}
        )
        data_statist = user_statistic.json()
        print("Сообщений пользователя ", user_name, ": ", data_statist)
        key = exit_loop()
    elif key_stat == "3":
        break
