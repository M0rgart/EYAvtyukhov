from src.power import power_function
from src.constants import SAMPLE_CONSTANT
from sys import stdin


def main() -> None:
    #Настроим непрерывный ввод строк
    for line in stdin:
        #проверка несчатсных скобок [:(]
        check = 0
        for i in line:
            if i == '(':
                check += 1
            elif i == ')':
                check -= 1
            if check < 0:
                #Если в какой-то момент кода будет больше закрытых скобок, чем открытых
                print(SyntaxError)
        if check != 0:
            #Если остались незакрытые скобки
            print(SyntaxError)
        else:
            line = line.replace('(', '').replace(')', '').split()
            #Избаввляемя от скобок, переводим строку в список, запускаем calc - функцию вычисления.
            calc(line)

def calc(line) -> None:
    #проведение рассчетов и вывод результата
    stack = []
    #создание стека, для хранения чисел
    for tok in line:
        #проверка каждого элемента строки(line)
        if is_number(tok):
            # Если tok - число, кладпем его в стек
            stack.append(float(tok))
        else:
            '''
            Если tok - не число, то вытаскиваем два числа из стека.
            Затем через match и case проверяем различные значения tok и производим операции с раннее
            извлеченными числами. Если операции не определена, то выводится SyntaxError.
            '''''
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
                    res = op2 / op1
                case '//':
                    res = op2 // op1
                case '%':
                    res = op2 % op1
                case '**':
                    res = op2 ** op1
                case _:
                    raise SyntaxError('Unknown operations')
            stack.append(res)
    print(*stack if len(stack) == 1 else SyntaxError)

def is_number(tok):
    """
    Проверяет, является ли строка числом (целым или дробным).
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
