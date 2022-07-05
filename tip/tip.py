def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Accept str as input formatted as $##.##
    # Remove the leading $
    d = d.replace("$", "")
    # Return amount as float
    return float(d)

def percent_to_float(p):
    # Accept str as input formatted as ##%
    # Remove trailing %
    p = p.replace("%", "")
    # Return percentage as a float
    return float(p)/100

main()