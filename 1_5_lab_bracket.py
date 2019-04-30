"""
Відомо, що у заданому тексті можуть зустрічатися дужки. З
заданого рядка вилучити текст, що розташований в дужках (разом з
дужками та відповідною кількістю пробілів). Передбачити можливість
ситуації, коли дужки закриті невірно. У випадку такої ситуації
вилучення тексту, розташованого після відкритої дужки або перед
закритою дужкою, не виконувати. Повідомити, якщо хоча б одна
дужка не закрита або не відкрита вчасно.
"""

LEFT_BRACKET = '('
RIGHT_BRACKET = ')'


def _new_expected_bracket(expected_bracket):
    return RIGHT_BRACKET if expected_bracket == LEFT_BRACKET else LEFT_BRACKET


def _print_error(bracket):
    print(bracket + ' открыта невовремя, ожидалась ' + _new_expected_bracket(bracket))


def main():
    string = input('Enter text: ') or 'aaa( bb   cc ) d )f((e (g))()(())'
    main_result = ''
    local_result = ''
    is_inside = False
    expected_bracket = LEFT_BRACKET

    for c in string:
        is_closed = False
        if not is_inside or c == RIGHT_BRACKET:
            if c == LEFT_BRACKET or c == RIGHT_BRACKET:
                if c == expected_bracket:
                    local_result += c
                    if expected_bracket == LEFT_BRACKET:
                        expected_bracket = _new_expected_bracket(expected_bracket)
                        is_inside = True
                    elif expected_bracket == RIGHT_BRACKET:
                        expected_bracket = _new_expected_bracket(expected_bracket)
                        is_inside = False
                        is_closed = True  # встретили закрывающую скобку без ошибок
                else:
                    # встретили неправильную скобку, сбрасываем результат
                    _print_error(c)
                    expected_bracket = LEFT_BRACKET
                    local_result = ''
                    is_inside = False
        elif is_inside and c == _new_expected_bracket(expected_bracket):
            # встретили неправильную скобку внутри, сбрасываем результат
            _print_error(c)
            expected_bracket = LEFT_BRACKET
            local_result = ''
            is_inside = False
        else:
            # внутри скобок, записываем символы
            local_result += c
        if is_closed:
            # сохраняем текст между скобками, т.к. не было проблем и скобка закрылась вовремя
            main_result += local_result
            local_result = ''
    print(main_result)


if __name__ == "__main__":
    main()
