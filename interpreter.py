class Interpreter:
    def __init__(self):
        self.stack = []

    def LOAD_VALUE(self, number):
        self.stack.append(number)

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def ADD_TWO_VALUES(self):
        n1 = self.stack.pop()
        n2 = self.stack.pop()
        total = n1 + n2
        self.stack.append(total)

    def run(self, code):
        instructions = code['instructions']
        numbers = code['numbers']
        for step in instructions:
            instruction, arg = step
            if instruction == 'LOAD_VALUE':
                n = numbers[arg]
                self.LOAD_VALUE(n)
            elif instruction == 'ADD_TWO_VALUES':
                self.ADD_TWO_VALUES()
            elif instruction == 'PRINT_ANSWER':
                self.PRINT_ANSWER()

if __name__ == '__main__':
    interpreter = Interpreter()
    code = {
            'instructions' : [
                ('LOAD_VALUE', 0),
                ('LOAD_VALUE', 1),
                ('ADD_TWO_VALUES', None),
                ('LOAD_VALUE', 2),
                ('ADD_TWO_VALUES', None),
                ('PRINT_ANSWER', None),
                ],
            'numbers': [7, 5, 8]
            }
    interpreter.run(code)
