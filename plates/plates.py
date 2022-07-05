import string
import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if (
        character_limit(s)
        and two_letters(s)
        and not_zero_first(s)
        and punctuation_check(s)
        and middle_numbers(s)
        ):
        return True

def character_limit(chars):
    # max 6 min 2 characters
    if (len(chars) <= 6) and (len(chars) >= 2):
        return True

def two_letters(two):
    # must start with two letters
    if two[0].isalpha():
        if two[1].isalpha():
            return True

def not_zero_first(plate):
    # The first number used cannot be a ‘0’
    if plate.isalpha():
        return True
    elif plate.isalnum():
        i = [x.isnumeric() for x in plate].index(True)
        #return True
        #if i == range(0,9):
        if int(plate[i]) != 0:
            return True
    else:
        return False

def punctuation_check(plate_chars):
    # “No periods, spaces, or punctuation marks are allowed.”
    if plate_chars.isalnum():
        return True

def middle_numbers(end):
    # Numbers cannot be used in the middle of a plate; they must come at the end.
    # Validate if string has numbers
    if end.isalpha():
        return True

            #  If string has numbers, confirm there are no letters after numbers
            # numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    elif end.isalnum():
        list = [char for char in end]
        any_numbers = False
        for i in list:
            if i.isdigit():
                if i=='0' and not any_numbers:
                    return False
                any_numbers = True
            elif i.isalpha():
                if any_numbers:
                    return False
            else:
                return False
        return True

    # if a number has a letter after it = bad
    #if x.index[i].isdigit() and x.index[i+1].isalpha():
    #    return False



main()