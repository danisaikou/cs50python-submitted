def main():
    with_vowels = input("Text: ")
    remove_vowels(with_vowels)

def remove_vowels(words):
    no_a = words.replace("a", "")
    no_A = no_a.replace("a", "")

    no_e = no_A.replace("e", "")
    no_E = no_e.replace("E", "")

    no_i = no_E.replace("i", "")
    no_I = no_i.replace("I", "")

    no_o = no_I.replace("o", "")
    no_O = no_o.replace("O", "")

    no_u = no_O.replace("u", "")
    no_U = no_u.replace("U", "")

    print(no_U)

    # o = "o"
    # list = words.split(o)
    # removed_o = "".join(list)
    # a = "a"
    # list_minus_o = removed_o.split(a)
    # removed_a = "".join(list_minus_o)
    # e = "e"
    # list_minus_oa = removed_a.split(e)
    # removed_e = "".join(list_minus_oa)
    # i = "i"
    # list_minus_oae = removed_e.split(i)
    # removed_i = "".join(list_minus_oae)
    # u = "u"
    # list_minus_oaei = removed_i.split(u)
    # removed_u = "".join(list_minus_oaei)
    # print(removed_u)


main()