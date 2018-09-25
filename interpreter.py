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
