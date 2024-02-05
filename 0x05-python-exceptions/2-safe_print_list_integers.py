#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            i += 1
        except IndexError:
            print()
            return i
        except (ValueError, TypeError):
            continue

    print()
    return i
