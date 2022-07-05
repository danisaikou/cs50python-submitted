def main():
    # Prompt user for input x y z (e.g. 1 + 1)
    # Probably use a split x, y, z = expression.split(" ") will assign x to 1, y to +, 1 to z
    # Output result of x y z as decimal rounded to 1 decimal point

    math = input("Type your arithmetic expression as x y z (e.g. 1 + 1): ")
    x, y, z = math.split(" ")
    if y == "+":
        print(float(round(int(x) + int(z), 1)))
    elif y == "-":
        print(float(round(int(x) - int(z), 1)))
    elif y == "*":
        print(float(round(int(x) * int(z), 1)))
    elif y == "/":
        print(float(round(int(x) / int(z), 1)))
    else:
        print("Please enter a valid equation.")


main()