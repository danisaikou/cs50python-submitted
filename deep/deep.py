# Prompt user for answer to The Question

def main():
    x = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
    if is_answer(x):
        print("Yes")
    else:
        print("No")
# Output Yes if 42 / forty-two or forty two else output No

def is_answer(n):
    return n.lower().strip() == "forty two" or n.lower().strip() == "forty-two" or n.strip() == "42"

main()

