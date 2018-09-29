class Interpreter:
    def __init__(self):
        self.stack = []
        self.environment = {}

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

    def STORE_NAME(self, name):
        val = self.stack.pop()
        self.environment[name] = val

    def LOAD_NAME(self, name):
        self.stack.append(self.environment[name])

    def parse_argument(self, instruction, argument, code):
        numbers = {'LOAD_VALUE'}
        names = {'STORE_NAME', 'LOAD_NAME'}

        if instruction in numbers:
            return code['numbers'][argument]
        elif instruction in names:
            return code['names'][argument]

    def run(self, code):
        for step in code['instructions']:
            instruction, raw_arg = step
            arg = self.parse_argument(instruction, raw_arg, code)
            method = getattr(self, instruction)
            if arg is None:
                method()
            else:
                method(arg)

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
