def check_winner(area):
    if area[0][0] == area[0][1] == area[0][2]:
        return area[0][0]
    if area[1][0] == area[1][1] == area[1][2]:
        return area[1][0]
    if area[2][0] == area[2][1] == area[2][2]:
        return area[2][0]
    if area[0][0] == area[1][0] == area[2][0]:
        return area[0][0]
    if area[0][1] == area[1][1] == area[2][1]:
        return area[0][1]
    if area[0][2] == area[1][2] == area[2][2]:
        return area[0][2]
    if area[0][0] == area[1][1] == area[2][2]:
        return area[0][0]
    if area[0][2] == area[1][1] == area[2][0]:
        return area[0][2]

def check_coor(str):
    dict = {"row": "строки", "column": "столбца"}
    temp = 0

    while temp == 0:
        temp = input(f"Введите номер {dict[str]} (1,2,3): ")
        if temp.lower() == "сдаюсь":
            return -1
        if temp not in ["1", "2", "3"]:
            print("Недопустимый номер! Попробуйте ещё раз.")
            temp = 0
    return (int(temp)) - 1

def draw_area():
    for i in area:
        print(*i)
    print()

game_continue = True

while game_continue == True:
    area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
    turn = 0
    print("Добро пожаловать в крестики-нолики!\nЕсли захотите заранее закончить игру, то введите слово - Сдаюсь\n")

    while turn < 10:
        turn += 1
        print(f"Ход: {turn}")
        if turn % 2 == 0:
            print("Ходят нолики")
            turn_char = "0"
        else:
            print("Ходят крестики")
            turn_char = "X"

        while True:

            row = check_coor("row")
            if row == -1:
                turn = 10
                break
            column = check_coor("column")
            if column == -1:
                turn = 10
                break

            if area[row][column] == '*':
                area[row][column] = turn_char
                break
            else:
                print("Ячейка уже занята, попробуйте ещё раз!")
                continue

        if row == -1 or column == -1:
            break

        draw_area()

        if turn >= 5:
            if check_winner(area) == "X":
                print("Крестики победили!\n")
                break
            elif check_winner(area) == "0":
                print("Нолики победили!\n")
                break
            elif turn == 9:
                print("Похоже это ничья!!!\n")

    if input("Если хотите сыграть ещё раз, то введите слово - Да: ").lower() != 'да':
        game_continue = False
    else:
        print()
