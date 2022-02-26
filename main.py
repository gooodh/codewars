def print_string(namecamel):
    namepy = ''
    n = 0
    for i in namecamel:
        if i == '-' and n != 0:
            namepy += '_' + i

        else:
            namepy += i
    n += 1

    # print(namepy.lower())
    t = ''
    for i in namecamel:
        if i == '-':
            t += i.upper()
            print(t)
        else:
            t += i
            world_c = t.replace('-', '')

        if i == '_':
            t += i.upper()
        else:
            t += i

  #  world_c = t.replace('_', '')
    #return print(world_c)

if __name__ == '__main__':
    print_string('Camel-camel-Camel-Camel-Camel')
