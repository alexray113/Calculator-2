"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
for line in open("inputs.txt"):
    tokens = line.split()
    if tokens[0] == "q" or tokens[0] == "quit":
        break

    elif tokens[0] == "add":
        try:
            solution = add(float(tokens[1]),float(tokens[2]))
            print(solution)
        except:
            print("Please enter two numbers")

    elif tokens[0] == "subtract":
        try:
            solution = subtract(float(tokens[1]),float(tokens[2]))
            print(solution)
        except:
            print("Please enter two numbers.")

    elif tokens[0] == "multiply":
        try:
            solution = multiply(float(tokens[1]),float(tokens[2]))
            print(solution)
        except:
            print("Please enter two numbers.")

    elif tokens[0] == "divide":
        try:
            solution = divide(float(tokens[1]),float(tokens[2]))
            print(solution)
        except:
            print("Please enter two numbers")

    elif tokens[0] == "square":
        solution = square(float(tokens[1]))
        print(solution)

    elif tokens[0] == "cube":
        solution = cube(float(tokens[1]))
        print(solution)

    elif tokens[0] == "power":
        try:
            solution = power(float(tokens[1]),float(tokens[2]))
            print(solution)
        except:
            print("Please enter two numbers")

    elif tokens[0] == "mod":
        try:
            solution = mod(float(tokens[1]),float(tokens[2]))
            print(solution)
        except:
            print("Please enter two numbers")

    else:
        print("Please enter a valid input")
        print()

"inputs.txt".close()