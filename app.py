from calculate import Calculate

calc = Calculate()

a =  int(input("Enter first number: "))
b =  int(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

print(calc.calculate(a, b, op))