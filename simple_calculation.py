print("\nPerform simple calculations\n")
num1, operation, num2 = input("Please enter calculation eg. (3 * 3): ").split()
num1, num2 = int(num1), int(num2)
if (operation == "+"):
    sol = num1 + num2
    print("{} + {} = {}".format(num1, num2, sol))
elif (operation == "-"):
    sol = num1 - num2
    print("{} - {} = {}".format(num1, num2, sol))
elif (operation == "*"):
    sol = num1 * num2
    print("{} * {} = {}".format(num1, num2, sol))
elif (operation == "/"):
    sol = num1 / num2
    print("{} / {} = {}".format(num1, num2, sol))
elif (operation == "%"):
    sol = num1 % num2
    print("{} % {} = {}".format(num1, num2, sol))
else:
    print("Use +, -, /, and %")