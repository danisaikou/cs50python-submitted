# Prompt teller for greeting
def main():
    greeting = input("How's it going?! ").strip().lower()
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


main()

