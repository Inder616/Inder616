import art

def add(n1,n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return 0
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    
}

def calculator():
    print(art)
    complete = True 
    number = int(input("What is your first Number?:" ))

    while complete:

        for symbol in operation:
            print(symbol)
        num = int(input("What is your second Number?:"))

        operation_symbol = input("Pick an operation from the line above: ")
        calculation_function = operation[operation_symbol]
        first_answer = calculation_function(number, num)
        print(f"{number} {operation_symbol} {num} = {first_answer}")


        choice = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation: ")
        if choice == "y":
            number = first_answer
        else:
            complete = False
            print("\n" * 20)
            calculator()

calculator()
            


