import logging

logging.basicConfig(filename="D:/Users/HP/Desktop/Крестики-нолики/who_won.log", level=logging.DEBUG,
                    format='%(asctime)s - %(message)s')

board = list(range(1, 10))
victory = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
           (1, 4, 7), (2, 5, 8), (3, 6, 9),
           (1, 5, 9), (3, 5, 7)]


# Menu function is created
def menu():
    print("*" * 35)
    print("Добро пожаловать в Крестики-Нолики!")
    print("*" * 35)

    start = int(input("Начнем игру? \n"
                      "1 = Да, 2 = Перейти к истории игр \n"
                      "Введите значения из вариантов выше чтобы продолжить: "))
    # Checking input values for start
    if not (start in range(1, 3)):
        print("------------------------------")
        print("ВЫ ВВЕЛИ НЕПОДХОДЯЩЕЕ ЧИСЛО! \n"
              "Введите значения 1 либо 2!")
        print("------------------------------")
        menu()
    print("------------------------------")

    while start == 1:
        global Player1
        global Player2
        Player1 = input("Игрок 1, введите Ваше имя: ")
        Player2 = input("Игрок 2, введите Ваше имя: ")
        main()
        if win_combination():
            break
    else:
        hist = int(input("Хотите посмотреть историю игр? \n"
                         "1 = Да, 2 = Перейти к очистке истории игр \n"
                         "Введите значения из вариантов выше чтобы продолжить: "))
        print("------------------------------")
        # Checking input values for hist
        if not (hist in range(1, 3)):
            print("------------------------------")
            print("ВЫ ВВЕЛИ НЕПОДХОДЯЩЕЕ ЧИСЛО! \n"
                  "Введите значения 1 либо 2!")
            print("------------------------------")
            menu()
        print("------------------------------")

        if hist == 1:
            history = open("who_won.log", 'r')
            reading = history.read()
            history.close()
            print(reading)
            exit = int(input("Введите 1, чтобы выйти в меню: "))
            if exit == 1:
                menu()
        else:
            clear_hist = int(input("Хотите очистить историю игр? \n"
                                   "1 = Да, 2 = Перейти к началу игры \n"
                                   "Введите значения из вариантов выше чтобы продолжить: "))
            print("------------------------------")
            # Checking input values for clear_hist
            if not (clear_hist in range(1, 3)):
                print("------------------------------")
                print("ВЫ ВВЕЛИ НЕПОДХОДЯЩЕЕ ЧИСЛО! \n"
                      "Введите значения 1 либо 2!")
                print("------------------------------")
                menu()
            print("------------------------------")

            if clear_hist == 1:
                file = open("who_won.log", "r+")
                file.truncate()
                file.close()
                print("История игр успешно очищена!")
                to_menu = int(input("Введите 1, чтобы вернуться в меню: "))
                if to_menu == 1:
                    menu()
            else:
                return menu()


# Formatting the board
def my_board():
    print("-------------")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
    print("-------------")


# Taking input of first player
def player_input(player_sign):
    while True:
        sign = input(Player1 + ", в какую клетку пишем " + player_sign + "?" + ": ")
        if not (sign in "1 2 3 4 5 6 7 8 9"):
            print("Повторите процесс, такого поля не существует \n"
                  "Введите числа от 1 до 9"
                  )
            continue
        sign = int(sign)
        if str(board[sign - 1]) in "X O":    # Checking if the cell is not empty
            print("Клетку кто-то занял")
            continue
        board[sign - 1] = player_sign
        break


# Taking input of second player
def player_input1(player_sign1):
    while True:
        sign = input(Player2 + ", в какую клетку пишем " + player_sign1 + "?" + ": ")
        if not (sign in "1 2 3 4 5 6 7 8 9"):
            print("Повторите процесс, такого поля не существует \n"
                  "Введите числа от 1 до 9"
                  )
            continue
        sign = int(sign)
        if str(board[sign - 1]) in "X O":
            print("Клетку кто-то занял")
            continue
        board[sign - 1] = player_sign1
        break


def win_combination():
    for each in victory:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False


# Defining main playable function
def main():
    counter = 0
    while True:
        my_board()
        if counter % 2 == 0:
            player_input("X")
        else:
            player_input1("O")
        if counter > 3:
            winner = win_combination()
            if winner == "X":
                my_board()
                print("Победная комбинация" + ", игрок " + Player1 + " выиграл!")
                logging.debug("Победная комбинация" + ", игрок " + Player1 + " выиграл!")
                global board
                board = list(range(1, 10))
                break
            if winner == "O":
                my_board()
                print("Победная комбинация" + ", игрок " + Player2 + " выиграл!")
                logging.debug("Победная комбинация" + ", игрок " + Player2 + " выиграл!")
                board = list(range(1, 10))
                break
        counter += 1
        if counter > 8:
            my_board()
            print("Победитель не выявлен! \n"
                  "Сыграйте еще раз")
            break
    print("------------------------------")
    play_more = int(input("Хотите еще партию? \n"
                          "1 = Да, 2 = Перейти в меню \n"
                          "Введите значения из вариантов выше, чтобы продолжить: "))

    if not (play_more in range(1, 3)):
        print("------------------------------")
        print("ВЫ ВВЕЛИ НЕПОДХОДЯЩЕЕ ЧИСЛО! \n"
              "Введите значения 1 либо 2!")
        print("------------------------------")

    if play_more == 1:
        main()
    else:
        menu()


menu()
