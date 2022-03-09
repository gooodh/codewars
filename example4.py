def find_it(n):
    list_w = n.split(' ')
    dict1 = {}

    for i in list_w:
        int_w = int(i)
        int_ww = int_w
        tot = 0

        while int_w > 0:
            dig = int_w % 10
            tot += dig
            int_w = int_w // 10

        dict1[int_ww] = tot


        sorted_values = sorted(dict1.values())  # Sort the values
        sorted_dict = {}
        for i in sorted_values:
            for k in dict1.keys():
                if dict1[k] == i:
                    sorted_dict[k] = dict1[k]
                    break


        print(sorted_dict)





if __name__ == '__main__':
    find_it('103 123 4444 99 2000')
