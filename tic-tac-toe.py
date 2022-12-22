def yello():
    print("-------------------")
    print("  Приветствуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - строка  ")
    print(" y - столбец ")


field = [[' '] * 3 for i in range(3)]
count_of_steps = 0


def show():
    print(f"  0 1 2")
    for i in range(3):
        row_info = " ".join(field[i])
        print(f"{i} {row_info}")


def check_win():
    win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
           ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
           ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coordinates in win:
        sym = []
        for p in coordinates:
            sym.append(field[p[0]][p[1]])
        if sym == ['X', 'X', 'X']:
            print('Выиграл Х')
            return True
        if sym == ['0', '0', '0']:
            print('Выиграл 0')
            return True
    return False


def question():
    while True:
        coordinates = input(' ').split()
        if len(coordinates) != 2:
            print('Введите две координаты')
            continue
        x, y = coordinates
        if not (x.isdigit()) and not (y.isdigit()):
            print('Введите цифры, не текст')
            continue
        x, y = int(x), int(y)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Введите координаты в диапазоне от 0 до 2')
            continue
        if field[x][y] != ' ':
            print('Данная клетка занята, введите другие координаты')
            continue

        return x, y


yello()

show()

question()


while True:
    count_of_steps += 1
    show()
    if count_of_steps % 2 != 1:
        print('Сейчас ход O')
    else:
        print('Сейчас ход X')

    x, y = question()

    if count_of_steps % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = 'O'

    if check_win():
        break
    if count_of_steps == 9:
        print('Ничья')
        break
