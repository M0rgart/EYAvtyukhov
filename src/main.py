from sys import stdin


def main() -> None:
    for line in stdin:
        run(line)


def run(line) -> None:
    # Настроим непрерывный ввод строк
    '''
    Решаем проблесу скобок: создаем переменные lastOpen и firtsClose.
    В первой находится id последней открывающей скобки, во второй id первой после нее закрывающей скобки.
    Из-за особенности записи они 100 процентов будут связанны друг с другом.
    При удалении данных скобок переменные обновятся и найдут еще одну пару. Это будет повторяться до тех пор, пока
    в строке не закончатся открывающие скобки. Остается проверить отсутствие закрывающих и работа со скобками окончена
    Данный способ не является самым оптимальным, но позволяет решить проблему отдельно от остального кода.
    '''
    while True:
        lastOpen = line.rfind('(')
        firtsClose = line[lastOpen:].find(')') + lastOpen
        if lastOpen == -1 or firtsClose == -1:
            break
        else:
            BracketLine = line[lastOpen + 1:firtsClose]
            check = -1
            for char in BracketLine.split():
                if is_number(char):
                    check += 1
                elif char in '+-**//%':
                    check -= 1
                else:
                    exit('UnknownOperand')
            if check == 0:
                line = line[:lastOpen] + line[lastOpen + 1:firtsClose] + line[firtsClose + 1:]
            else:
                exit('InvalidSyntax')

    line = line.split()
    print(calc(line))


def calc(line) -> None:
    # проведение рассчетов и вывод результата
    stack = []
    # создание стека, для хранения чисел
    for tok in line:
        # проверка каждого элемента строки(line)
        if is_number(tok):
            # Если tok - число, кладпем его в стек
            stack.append(float(tok))
        else:
            '''
            Если tok - не число, то вытаскиваем два числа из стека.
            Затем через match и case проверяем различные значения tok и производим операции с раннее
            извлеченными числами. Если операции не определена, то выводится UnknownOperand.
            '''''
            if len(stack) < 2:
                exit('SyntaxError')
            else:
                op1 = stack.pop()
                op2 = stack.pop()
            match tok:
                case '+':
                    res = op2 + op1
                case '-':
                    res = op2 - op1
                case '*':
                    res = op2 * op1
                case '/':
                    if op1 == 0:
                        exit('ZeroDivisionError')
                    res = op2 / op1
                case '//':
                    if op1 == 0:
                        exit('ZeroDivisionError')
                    if int(op2) != float(op2):
                        exit('RealNumberDivisionError')
                    res = op2 // op1
                case '%':
                    if op1 == 0:
                        exit('ZeroDivisionError')
                    if int(op2) != float(op2):
                        exit('RealNumberDivisionError')
                    res = op2 % op1
                case '**':
                    res = op2 ** op1
                case _:
                    exit('UnknownOperand')
            stack.append(res)
    if len(stack) == 1:
        return stack[0]
    else:
        exit('SyntaxError')


def is_number(tok):
    """
    Проверяет, является ли строка числом (целым или дробны  м).
    Такая запись способна обрабатывать унарные + и -.
    Вернет True, если строка является числом, False в противном случае.

    Почему именно такая запись унарных символов (-3 +4 +)?
    1) проще (привычнее) для понимания как пользователю, так и программисту.
    2) благодаря такой записи можно проверять число через try float, что ускоряет процесс.
    3) не на всех устройствах есть возможность вводить $ и ~
    """
    try:
        float(tok)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
