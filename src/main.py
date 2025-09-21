from src.power import power_function
from src.constants import SAMPLE_CONSTANT, CHARS
from sys import stdin


def main() -> None:
    #Настроим непрерывный ввод строк, которые сразу преобразуем в списки
    for line in stdin:
        line = line.split()
        calc(line)

def calc(line) -> None:
    #проведение рассчетов и вывод результата
    stack = []
    #создание стека, для хранения чисел
    for elem in line:
        #проверка каждого элемента строки(line)
        if is_number(elem):
            stack.append(float(elem))
        elif elem in CHARS:
            print(elem)
        else:
            print(SyntaxError('Unknown character'))
    print(stack)

def is_number(elem):
    """
    Проверяет, является ли строка числом (целым или дробным).
    Такая запись способна обрабатывать унарные символы.
    Вернет True, если строка является числом, False в противном случае.
    """
    try:
        float(elem)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
