# сложить значения строк как в столбик  


list_str = ['123456789', '987654321']


def summ_str(list_str):
    dict_digit_nam = {}

    for i in list_str:
        for key, char in enumerate(i[::-1]):
            if key:
            dict_digit_nam[key] = int(char)
    print(dict_digit_nam)


if __name__ == '__main__':
    summ_str(list_str)
