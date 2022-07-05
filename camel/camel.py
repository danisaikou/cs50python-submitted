import re

def main():
    camel = input("Enter text in camel case: ")
    snake = convert(camel)
    print(snake)

def convert(text):
    snake_case = re.sub(r"([A-Z])", r"_\1", text).lower()
    return snake_case

main()

# sources: https://lzone.de/examples/Python%20re.sub
# https://pynative.com/python-regex-replace-re-sub/
# https://stackoverflow.com/questions/8934477/making-letters-uppercase-using-re-sub-in-python