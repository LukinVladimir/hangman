def print_hangman_picture_0(num):
    print(chr(124), chr(124), sep='-----')
    print(chr(124))
    print(chr(124))
    print(chr(124))
    print(chr(124))
    print(chr(124), chr(95), chr(95), chr(95), chr(95))


def print_hangman_picture_1(num):
    print(chr(124), chr(124), sep='-----')
    print(chr(124), chr(79), sep='     ')
    print(chr(124))
    print(chr(124))
    print(chr(124))
    print(chr(124), chr(95), chr(95), chr(95), chr(95))


def print_hangman_picture_2(num):
    print(chr(124), chr(124), sep='-----')
    print(chr(124), chr(79), sep='     ')
    print(chr(124), chr(124), sep='     ')
    print(chr(124))
    print(chr(124))
    print(chr(124), chr(95), chr(95), chr(95), chr(95))


def print_hangman_picture_3(num):
    print(chr(124), chr(124), sep='-----')
    print(chr(124), chr(79), sep='     ')
    print(chr(124), chr(47) + chr(124), sep='    ')
    print(chr(124))
    print(chr(124))
    print(chr(124), chr(95), chr(95), chr(95), chr(95))


def print_hangman_picture_4(num):
    print(chr(124), chr(124), sep='-----')
    print(chr(124), chr(79), sep='     ')
    print(chr(124), chr(47) + chr(124) + chr(92), sep='    ')
    print(chr(124))
    print(chr(124))
    print(chr(124), chr(95), chr(95), chr(95), chr(95))


def print_hangman_picture_5(num):
    print(chr(124), chr(124), sep='-----')
    print(chr(124), chr(79), sep='     ')
    print(chr(124), chr(47) + chr(124) + chr(92), sep='    ')
    print(chr(124), chr(47), sep='    ')
    print(chr(124))
    print(chr(124), chr(95), chr(95), chr(95), chr(95))


def print_hangman_picture_6(num):
    print(chr(124), chr(124), sep='-----')
    print(chr(124), chr(79), sep='     ')
    print(chr(124), chr(47) + chr(124) + chr(92), sep='    ')
    print(chr(124), chr(47) + chr(32) + chr(92), sep='    ')
    print(chr(124))
    print(chr(124), chr(95), chr(95), chr(95), chr(95))


# mistake_counter_dict = {
#     0: print_hangman_picture_0,
#     1: print_hangman_picture_1,
#     2: print_hangman_picture_2,
#     3: print_hangman_picture_3,
#     4: print_hangman_picture_4,
#     5: print_hangman_picture_5,
#     6: print_hangman_picture_6
# }