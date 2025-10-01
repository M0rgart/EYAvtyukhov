import unittest
from unittest.mock import patch
from io import StringIO
import sys
from src.main import calc, run


class TestCalculator(unittest.TestCase):
    def test_calc_addition(self):
        self.assertEqual(calc(["2", "3", "+"]), 5.0)

    def test_calc_subtraction(self):
        self.assertEqual(calc(["5", "2", "-"]), 3.0)

    def test_calc_multiplication(self):
        self.assertEqual(calc(["4", "3", "*"]), 12.0)

    def test_calc_division(self):
        self.assertEqual(calc(["10", "2", "/"]), 5.0)

    def test_calc_floor_division(self):
        self.assertEqual(calc(["10", "3", "//"]), 3.0)

    def test_calc_modulo(self):
        self.assertEqual(calc(["10", "3", "%"]), 1.0)

    def test_calc_power(self):
        self.assertEqual(calc(["2", "3", "**"]), 8.0)

    def test_calc_complex_expression(self):
        self.assertEqual(calc(["2", "3", "+", "5", "*"]), 25.0)

    def test_calc_division_by_zero(self):
        with self.assertRaises(SystemExit) as context:
            calc(["5", "0", "/"])
        self.assertEqual(str(context.exception), 'ZeroDivisionError')

    def test_calc_floor_division_by_zero(self):
        with self.assertRaises(SystemExit) as context:
            calc(["5", "0", "//"])
        self.assertEqual(str(context.exception), 'ZeroDivisionError')

    def test_calc_modulo_by_zero(self):
        with self.assertRaises(SystemExit) as context:
            calc(["5", "0", "%"])
        self.assertEqual(str(context.exception), 'ZeroDivisionError')

    def test_calc_real_number_floor_division(self):
        with self.assertRaises(SystemExit) as context:
            calc(["5.5", "2", "//"])
        self.assertEqual(str(context.exception), 'RealNumberDivisionError')

    def test_calc_real_number_modulo(self):
        with self.assertRaises(SystemExit) as context:
            calc(["5.5", "2", "%"])
        self.assertEqual(str(context.exception), 'RealNumberDivisionError')

    def test_calc_invalid_syntax(self):
        with self.assertRaises(SystemExit) as context:
            calc(["2", "+"])
        self.assertEqual(str(context.exception), 'SyntaxError')

    def test_calc_unknown_operand(self):
        with self.assertRaises(SystemExit) as context:
            calc(["2", "3", "&"])
        self.assertEqual(str(context.exception), 'UnknownOperand')

    def test_run_simple_expression(self):
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            run("2 3 +")
            self.assertEqual(stdout.getvalue().strip(), "5.0")

    def test_run_nested_parentheses(self):
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            run("( 2 3 + ) 5 *")
            self.assertEqual(stdout.getvalue().strip(), "25.0")

    def test_run_parentheses_and_operators(self):
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            run("( 10 2 / ) 3 +")
            self.assertEqual(stdout.getvalue().strip(), "8.0")

    def test_run_empty_parentheses(self):
        with self.assertRaises(SystemExit) as context:
            run("()")
        self.assertEqual(str(context.exception), 'InvalidSyntax')

    def test_run_invalid_syntax_parentheses(self):
        with self.assertRaises(SystemExit) as context:
            run("(2 + )")

        self.assertEqual(str(context.exception), 'InvalidSyntax')

    def test_run_unknown_operand_parentheses(self):
        with self.assertRaises(SystemExit) as context:
            run("(2 & 3)")
        self.assertEqual(str(context.exception), 'UnknownOperand')

    def test_run_no_parentheses(self):
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            run("1 2 + 3 *")
            self.assertEqual(stdout.getvalue().strip(), '9.0')

    def test_run_complex_expression_with_parentheses(self):
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            run("2 ( 3 4 + ) *")
            self.assertEqual(stdout.getvalue().strip(), '14.0')

    if __name__ == '__main__':
        unittest.main()
