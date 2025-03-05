

class CalculatorModel:

    def __init__(self):
        self.expression = ""    # "23+4*2"

    def add_to_expression(self, char):
        self.expression = self.expression + char

    def remove_last_character(self):
        self.expression = self.expression[:-1]

    def clear_expression(self):
        self.expression = ""

    def calculate(self):
        result = eval(self.expression)
        self.expression = str(result)

    def get_expression(self):
        return self.expression

    def __str__(self):
        return self.expression

if __name__ == '__main__':
    calc = Calculator()
    calc.add_to_expression("123+25*(2+45-544)")

    print(calc.calculate())