def main():
    coins = 0
    total = 0
    while total < 50:
        coins = int(input("Insert a coin: "))
        if coins in [5, 10, 25]:
            total += coins
            if total < 50:
                print("Amount due:", 50 - total)
            elif total > 50:
                print("Change owed:", total - 50)
                break
            elif total == 50:
                print("Change owed: 0")
                break
        elif coins not in [5, 10, 25]:
            print("Amount due:", 50 - total)
        else:
            break

main()