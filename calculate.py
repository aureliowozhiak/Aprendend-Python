from myMath import Math

class Calculate:
    def __init__(self):
        self.math = Math()

    def calculate(self, a, b, op):
        if op == "+":
            return self.math.add(a, b)
        elif op == "-":
            return self.math.subtract(a, b)
        elif op == "*":
            return self.math.multiply(a, b)
        elif op == "/":
            return self.math.divide(a, b)
        else:
            return "Invalid operation"
