def to_camel_case(text):
    if text is not None:
        camel_case = ''
        n = 0
        k = 0
        for i in text:
            if i == '-' or i == '_':
                ic = i.replace('-', '').replace('_', '')
                camel_case += ic
                n += 1

            if n != k and i != '_' and i != '-':
                ic = i.upper()
                camel_case += ic
                k = n

            else:
                ic = i.replace('-', '').replace('_', '')
                camel_case += ic


        print(camel_case)


if __name__ == '__main__':
    to_camel_case('a-pippi_Is-cute')
