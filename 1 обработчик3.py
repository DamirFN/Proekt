from time import sleep

n = '1+146[193-2, 174-2, 186-2, 129-1] на 193.txt'

n1 = '2+129[180-2] на 339.txt'

library = {'45': 'путь к файлу', '129': n1, '193': 'путь к файлу',
           '4': 'путь к файлу', '465': 'путь к файлу', '174': 'путь к файлу',
           '186': 'путь к файлу', '180': 'путь к файлу', '146': n}


def start():
    e = open('120.txt', 'r', -1, 'utf-8')
    for LINE in e:
        print(LINE, end='')
        # sleep(1)
    e.close()
    print('\n')

    s = []
    e0 = open('120.txt', 'r', -1, 'utf-8')
    r = e0.readlines()
    r1 = ', '.join(r).split(' ')
    for r1 in r1:
        if r1 in library:
            s.append(r1)
    e0.close()
    return s

start()

all_a = start()


def f1():
    f_1 = input(f'ВАШ ВЫБОР: Если спрячешься, то жми {all_a[0]}\n')

    if f_1 == all_a[0]:

        e_1_0 = open(library[all_a[0]], 'r', -1, 'utf-8')
        for line in e_1_0:
            print(line, end='')
            sleep(1)
        e_1_0.close()
        print('\n')

        a_1 = []
        e_1_1 = open(library[all_a[0]], 'r', -1, 'utf-8')
        r_1_0 = e_1_1.readlines()
        for r_1_1 in (', '.join(r_1_0)).split(' '):
            if r_1_1 in library:
                a_1.append(r_1_1)
        e_1_1.close()

        if len(a_1) == 1:
            f1()
        if len(a_1) == 2:
            f2()
        if len(a_1) == 3:
            f3()
        if len(a_1) == 4:
            f4()
    else:
        f1()

def f2():
    print(all_a)
    f_2 = input(f'ВАШ ВЫБОР: Если спрячешься, то жми {all_a[0]}, если остаешься, то {all_a[1]}\n')
    if f_2 == all_a[0]:

        e_2_0 = open(library[all_a[0]], 'r', -1, 'utf-8')
        for line in e_2_0:
            print(line, end='')
            sleep(1)
        e_2_0.close()
        print('\n')

        a_2_0 = []
        e_2_0_1 = open(library[all_a[0]], 'r', -1, 'utf-8')
        r_2_0 = e_2_0_1.readlines()
        r_2_1 = ', '.join(r_2_0).split(' ')
        for r_2_2 in r_2_1:
            if r_2_2 in library:
                a_2_0.append(r_2_2)
        e_2_0_1.close()

        if len(a_2_0) == 1:
            f1()
        if len(a_2_0) == 2:
            f2()
        if len(a_2_0) == 3:
            f3()
        if len(a_2_0) == 4:
            f4()

    if f_2 == all_a[1]:

        e_2_0_2 = open(library[all_a[1]], 'r', -1, 'utf-8')
        for line in e_2_0_2:
            print(line, end='')
            sleep(1)
        e_2_0_2.close()
        print('\n')

        a_2_1 = []
        e_2_0_3 = open(library[all_a[1]], 'r', -1, 'utf-8')
        r_2_3 = e_2_0_3.readlines()
        r_2_4 = ', '.join(r_2_3).split(' ')
        for r_2_5 in r_2_4:
            if r_2_5 in library:
                a_2_1.append(r_2_5)
        print(a_2_1)
        e_2_0_3.close()

        if len(a_2_1) == 1:
            f1()
        if len(a_2_1) == 2:
            f2()
        if len(a_2_1) == 3:
            f3()
        if len(a_2_1) == 4:
            f4()
    else:
        f2()

def f3():
    f_3 = input(f'ВАШ ВЫБОР: Если спрячешься, то жми {all_a[0]}, если остаешься, то {all_a[1]}, {all_a[2]}\n')
    if f_3 == all_a[0]:
        e_3_0_0 = open(library[all_a[0]], 'r', -1, 'utf-8')
        for line in e_3_0_0:
            print(line, end='')
            sleep(1)
        e_3_0_0.close()
        print('\n')

        a_3_0_1 = []
        e_3_0_1 = open(library[all_a[0]], 'r', -1, 'utf-8')
        r_3_0_0 = e_3_0_1.readlines()
        r_3_0_1 = ', '.join(r_3_0_0).split(' ')
        for r_3_0_2 in r_3_0_1:
            if r_3_0_2 in library:
                a_3_0_1.append(r_3_0_2)
        e_3_0_1.close()

        if len(a_3_0_1) == 1:
            f1()
        elif len(a_3_0_1) == 2:
            f2()
        elif len(a_3_0_1) == 3:
            f3()
        elif len(a_3_0_1) == 4:
            f4()

    elif f_3 == all_a[1]:
        e_3_1_0 = open(library[all_a[1]], 'r', -1, 'utf-8')
        for line in e_3_1_0:
            print(line, end='')
            sleep(1)
        e_3_1_0.close()
        print('\n')

        a_3_1 = []
        e_3_1_1 = open(library[all_a[1]], 'r', -1, 'utf-8')
        r_3_1_0 = e_3_1_1.readlines()
        r_3_1_1 = ', '.join(r_3_1_0).split(' ')
        for r_3_1_2 in r_3_1_1:
            if r_3_1_2 in library:
                a_3_1.append(r_3_1_2)
        e_3_1_1.close()

        if len(a_3_1) == 1:
            f1()
        elif len(a_3_1) == 2:
            f2()
        elif len(a_3_1) == 3:
            f3()
        elif len(a_3_1) == 4:
            f4()

    elif f_3 == all_a[2]:
        e_3_2_0 = open(library[all_a[2]], 'r', -1, 'utf-8')
        for line in e_3_2_0:
            print(line, end='')
            sleep(1)
        e_3_2_0.close()
        print('\n')

        a_3_2_1 = []
        e_3_2_1 = open(library[all_a[1]], 'r', -1, 'utf-8')
        r_3_2_0 = e_3_2_1.readlines()
        r_3_2_1 = ', '.join(r_3_2_0).split(' ')
        for r_3_2_2 in r_3_2_1:
            if r_3_2_2 in library:
                a_3_2_1.append(r_3_2_2)
        e_3_2_1.close()

        if len(a_3_2_1) == 1:
            f1()
        elif len(a_3_2_1) == 2:
            f2()
        elif len(a_3_2_1) == 3:
            f3()
        elif len(a_3_2_1) == 4:
            f4()
    else:
        f3()

def f4():
    print(all_a)
    f_4 = input(f'ВАШ ВЫБОР: {all_a[0]}, {all_a[1]}, {all_a[2]}, {all_a[3]}\n')
    if f_4 == all_a[0]:
        e_4_0_0 = open(library[all_a[0]], 'r', -1, 'utf-8')
        for line in e_4_0_0:
            print(line, end='')
            sleep(1)
        e_4_0_0.close()
        print('\n')

        a_4_0 = []
        e_4_0_1 = open(library[all_a[0]], 'r', -1, 'utf-8')
        r_4_0_0 = e_4_0_1.readlines()
        r_4_0_1 = ', '.join(r_4_0_0).split()
        for r_4_0_2 in r_4_0_1:
            if r_4_0_2 in library:
                a_4_0.append(r_4_0_2)
        e_4_0_1.close()

        if len(a_4_0) == 1:
            f1()
        if len(a_4_0) == 2:
            f2()
        if len(a_4_0) == 3:
            f3()
        if len(a_4_0) == 4:
            f4()

    elif f_4 == all_a[1]:
        e_4_1_0 = open(library[all_a[1]], 'r', -1, 'utf-8')
        for line in e_4_1_0:
            print(line, end='')
            sleep(1)
        e_4_1_0.close()
        print('\n')

        a_4_1 = []
        e_4_1_1 = open(library[all_a[1]], 'r', -1, 'utf-8')
        r_4_1_0 = e_4_1_1.readlines()
        r_4_1_1 = ', '.join(r_4_1_0).split()
        for r_4_1_2 in r_4_1_1:
            if r_4_1_2 in library:
                a_4_1.append(r_4_1_2)
        e_4_1_1.close()

        if len(a_4_1) == 1:
            f1()
        if len(a_4_1) == 2:
            f2()
        if len(a_4_1) == 3:
            f3()
        if len(a_4_1) == 4:
            f4()

    elif f_4 == all_a[2]:
        e_4_2_0 = open(library[all_a[2]], 'r', -1, 'utf-8')
        for line in e_4_2_0:
            print(line, end='')
            sleep(1)
        e_4_2_0.close()
        print('\n')

        a_4_2 = []
        e_4_2_1 = open(library[all_a[2]], 'r', -1, 'utf-8')
        r_4_2_0 = e_4_2_1.readlines()
        r_4_2_1 = ', '.join(r_4_2_0).split()
        for r_4_2_2 in r_4_2_1:
            if r_4_2_2 in library:
                a_4_2.append(r_4_2_2)
        e_4_2_1.close()

        if len(a_4_2) == 1:
            f1()
        if len(a_4_2) == 2:
            f2()
        if len(a_4_2) == 3:
            f3()
        if len(a_4_2) == 4:
            f4()

    elif f_4 == all_a[3]:
        e_4_3_0 = open(library[all_a[3]], 'r', -1, 'utf-8')
        for line in e_4_3_0:
            print(line, end='')
            sleep(1)
        e_4_3_0.close()
        print('\n')

        a_4_3 = []
        e_4_3_1 = open(library[all_a[3]], 'r', -1, 'utf-8')
        r_4_3_0 = e_4_3_1.readlines()
        r_4_3_1 = ', '.join(r_4_3_0).split()
        for r_4_3_2 in r_4_3_1:
            if r_4_3_2 in library:
                a_4_3.append(r_4_3_2)
        e_4_3_1.close()

        if len(a_4_3) == 1:
            f1()
        if len(a_4_3) == 2:
            f2()
        if len(a_4_3) == 3:
            f3()
        if len(a_4_3) == 4:
            f4()

if len(all_a) == 1:
    f1()
if len(all_a) == 2:
    f2()
