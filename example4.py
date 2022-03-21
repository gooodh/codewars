def order_weight(strng):
    list_w = strng.split(' ')

    dict1 = {}
    dict2 = {}
    n = 0

    for i in list_w:
        n += 1
        int_w = int(i)
        dict1[n] = int_w
        tot = 0

        while int_w > 0:  # Программа нахождения суммы всех цифр данного числа
            dig = int_w % 10
            tot += dig
            int_w = int_w // 10

        dict2[n] = tot

    sorted_dict = sorted(dict2.items(), key=lambda x: x[1])  # Sort
    dict2 = dict(sorted_dict)
    mass = ''
    for i in dict2.keys():
        for k in dict1.keys():
            if k == i:
                mass += str(dict1[i]) + " "
                break


    print(mass.strip())


if __name__ == '__main__':
    order_weight('2000 10003 1234000 44444444 9999 11 11 22 123')
