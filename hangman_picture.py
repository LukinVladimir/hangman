def hangman_picture(mistake_counter):
    if mistake_counter == 0:
        print(chr(124), chr(124), sep='-----')
        print(chr(124))
        print(chr(124))
        print(chr(124))
        print(chr(124))
        print(chr(124), chr(95), chr(95), chr(95), chr(95))

    elif mistake_counter == 1:
        print(chr(124), chr(124), sep='-----')
        print(chr(124), chr(79), sep='     ')
        print(chr(124))
        print(chr(124))
        print(chr(124))
        print(chr(124), chr(95), chr(95), chr(95), chr(95))

    elif mistake_counter == 2:
        print(chr(124), chr(124), sep='-----')
        print(chr(124), chr(79), sep='     ')
        print(chr(124), chr(124), sep='     ')
        print(chr(124))
        print(chr(124))
        print(chr(124), chr(95), chr(95), chr(95), chr(95))

    elif mistake_counter == 3:
        print(chr(124), chr(124), sep='-----')
        print(chr(124), chr(79), sep='     ')
        print(chr(124), chr(47) + chr(124), sep='    ')
        print(chr(124))
        print(chr(124))
        print(chr(124), chr(95), chr(95), chr(95), chr(95))

    elif mistake_counter == 4:
        print(chr(124), chr(124), sep='-----')
        print(chr(124), chr(79), sep='     ')
        print(chr(124), chr(47) + chr(124) + chr(92), sep='    ')
        print(chr(124))
        print(chr(124))
        print(chr(124), chr(95), chr(95), chr(95), chr(95))

    elif mistake_counter == 5:
        print(chr(124), chr(124), sep='-----')
        print(chr(124), chr(79), sep='     ')
        print(chr(124), chr(47) + chr(124) + chr(92), sep='    ')
        print(chr(124), chr(47), sep='    ')
        print(chr(124))
        print(chr(124), chr(95), chr(95), chr(95), chr(95))

    elif mistake_counter == 6:
        print(chr(124), chr(124), sep='-----')
        print(chr(124), chr(79), sep='     ')
        print(chr(124), chr(47) + chr(124) + chr(92), sep='    ')
        print(chr(124), chr(47) + chr(32) + chr(92), sep='    ')
        print(chr(124))
        print(chr(124), chr(95), chr(95), chr(95), chr(95))
