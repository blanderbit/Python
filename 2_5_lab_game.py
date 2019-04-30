"""
Промоделювати деяку гру. Гра відбувається на
прямокутному полі. Гравець на початку розташовується у правому
верхньому куті. Гравець вміє переміщуватися тільки вліво та вниз.
Кожна клітинка поля має деяку кількість очок. Дані задані у вигляді
файлу. Визначити спосіб переміщення з початкового положення
гравця на вказану користувачем клітинку таким чином, щоб він
призвів до отримання найбільшої кількості очок (розраховується як
сума очок, зібраних протягом всього шляху на кожній клітинці).
"""


import random


FIELD_SIZE = 6
FILE_NAME = 'game_field.txt'
START_POSITION = FIELD_SIZE - 1
START_X = FIELD_SIZE - 1
START_Y = 0


def _write_matrix_to_file(a_matrix, file_to_write):

    def compile_row_string(a_row):
        return str(a_row).strip(']').strip('[').replace(',', '')

    with open(file_to_write, 'w') as f:
        for row in a_matrix:
            f.write(compile_row_string(row)+'\n')

    return True


def _generate_new_field():
    return [[random.randrange(10, 100) for x in range(FIELD_SIZE)] for y in range(FIELD_SIZE)]


def load_game_field():
    with open(FILE_NAME, 'r') as f:
        return [[int(num) for num in line.split(' ')] for line in f]


def print_game_field(matrix):
    print('******* Игровое поле {}x{} *******'.format(FIELD_SIZE, FIELD_SIZE))
    for row in matrix:
        print(' '.join(str(x) for x in row))
    print('**********************************')


def int_input(coordinate):
    while True:
        try:
            value = int(input('Ввведите {}:'.format(coordinate)))
        except ValueError:
            continue
        else:
            if not FIELD_SIZE > value >= 0:
                print('Ввведите число, не больше {}'.format(FIELD_SIZE - 1))
                continue
            else:
                return value


def get_max_path(field, start_x, start_y, end_x, end_y, path):
    if (start_x < end_x or start_x < 0) or (start_y < 0 or start_y > end_y):
        return 0, []

    path.append('({},{})[{}]'.format(FIELD_SIZE - start_y - 1, start_x, field[start_y][start_x]))
    if end_x == START_POSITION and end_y == START_POSITION:
        return field[START_POSITION][START_POSITION], path

    left_path = []
    down_path = []
    left_sum, _ = get_max_path(field, start_x, start_y + 1, end_x, end_y, left_path)
    down_sum, _ = get_max_path(field, start_x - 1, start_y, end_x, end_y, down_path)

    if left_sum > down_sum:
        path += left_path
        return left_sum + field[start_y][start_x], path
    else:
        path += down_path
        return down_sum + field[start_y][start_x], path


def main():
    # генерация нового игрового поля
    _write_matrix_to_file(_generate_new_field(), FILE_NAME)
    game_field = load_game_field()
    print_game_field(game_field)
    print('* Левый нижний угол начало координат (0,0), позиция игрока ({},{}) *'.format(FIELD_SIZE - 1, FIELD_SIZE - 1))
    x = int_input('X')
    y = int_input('Y')
    y = FIELD_SIZE - y - 1
    result_sum, path = get_max_path(game_field, START_POSITION, 0, x, y, [])
    print('Сумма: ' + str(result_sum))
    print('Путь: ')
    print(' -> '.join(str(x) for x in path))


if __name__ == "__main__":
    main()
