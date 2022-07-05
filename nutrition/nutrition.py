def main():
    # Input a fruit case-insensitively
    fruit = input("Input a fruit: ").lower()
    # Output number of calories for one portion of the fruit
    count = calorie_count(fruit)
    if calorie_count(fruit):
        print("Calories:", count)


def calorie_count(i):
    the_table = {
        "apple": "130",
        "avocado": "50",
        "banana": "110",
        "cantaloupe": "50",
        "grapefruit": "60",
        "grapes": "90",
        "honeydew": "50",
        "kiwifruit": "90",
        "lemon": "15",
        "lime": "20",
        "nectarine": "60",
        "orange": "80",
        "peach": "60",
        "pear": "100",
        "pineapple": "50",
        "plums": "70",
        "strawberries": "50",
        "sweet cherries": "100",
        "tangerine": "50",
        "watermelon": "80",
    }
    for fruit, cals in the_table.items():
        if fruit == i:
            return cals
        

main()