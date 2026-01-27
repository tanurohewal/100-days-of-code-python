from art import logo

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def divi(n1, n2):
    return n1 / n2

operations = { "+": add, "-": sub, "*": multi, "/": divi }

def calculator():
    print(logo)
    should_accumulate = True
    num1 = float(input("What is the first number: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("pick an operation: ")
        num2 = float(input("What is th second number: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input (f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()
