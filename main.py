from math import sqrt

global num


def find_next_square(sq):
    global num
    if sqrt(sq) == int:
        num = sqrt(sq) + 1
        result = num**2
        print(result)
        return result
    elif sqrt(sq) == float:
        return -1


find_next_square(122)
