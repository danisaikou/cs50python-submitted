# Define the main function
def main():
    emoticon = input("Type your smiley face: ")
    print(convert(emoticon))

# Define function to convert from :) to 🙂 and :( to 🙁
def convert(emoji):
    return emoji.replace(":)", "🙂").replace(":(", "🙁")

# Call main
main()