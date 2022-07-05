# Prompt user for time
# Output breakfast (7am - 8am), lunch (12 - 13), dinner (18 - 19), or nothing

def main():
    # Call convert
    prompt = input("What time is it? ")
    result = convert(prompt)
    if result >=7.0 and result <=8.0:
        print("breakfast time")
    elif result >=12.0 and result <=13.0:
        print("lunch time")
    elif result >=18.0 and result <=19.0:
        print("dinner time")


def convert(time):
    # Convert time (str in 24-hr format) to float
    # e.g. 7:30 should return 7.5
    hours, minutes = time.split(":")
    converted = float(hours) + (float(minutes)/60)
    return converted

if __name__ == "__main__":
    main()