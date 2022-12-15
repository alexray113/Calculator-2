"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_input = input("Enter an operation and numbers or enter q to quit: ")
    tokens = user_input.split()
    if user_input == "q" or user_input == "quit":
        break
    elif tokens[0] == "add":
        solution = add(int(tokens[1]),int(tokens[2]))
        print(solution)
    elif tokens[0] == "subtract":
        solution = subtract(int(tokens[1]),int(tokens[2]))
        print(solution)
    elif tokens[0] == "multiply":
        solution = multiply(int(tokens[1]),int(tokens[2]))
        print(solution)
    elif tokens[0] == "divide":
        solution = divide(int(tokens[1]),int(tokens[2]))
        print(solution)
    elif tokens[0] == "square":
        solution = square(int(tokens[1]))
        print(solution)
    elif tokens[0] == "cube":
        solution = cube(int(tokens[1]))
        print(solution)
    elif tokens[0] == "power":
        solution = power(int(tokens[1]),int(tokens[2]))
        print(solution)
    elif tokens[0] == "mod":
        solution = mod(int(tokens[1]),int(tokens[2]))
        print(solution)
    else:
        print("Please enter a valid input")
        print()
        continue