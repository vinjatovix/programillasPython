import random

end = '(---------)'
nada = '(         )'
uno = '(    0    )'
dos = '(  0   0  )'


def d1():
    print('\n', end, '\n', nada, '\n', uno, '\n', nada, '\n', end)


def d2():
    print('\n', end, '\n', nada, '\n', dos, '\n', nada, '\n', end)


def d3():
    print('\n', end, '\n', uno, '\n', uno, '\n', uno, '\n', end)


def d4():
    print('\n', end, '\n', dos, '\n', nada, '\n', dos, '\n', end)


def d5():
    print('\n', end, '\n', dos, '\n', uno, '\n', dos, '\n', end)


def d6():
    print('\n', end, '\n', dos, '\n', dos, '\n', dos, '\n', end)


def tirar():
    x = random.randint(1, 6)
    if x == 1:
        d1()
    elif x == 2:
        d2()
    elif x == 3:
        d3()
    elif x == 4:
        d4()
    elif x == 5:
        d5()
    else:
        d6()


def dado6():
    i = 0
    while i == 0:
        tirar()
        repeat = input('¿quieres tirar de nuevo?: s/n ')
        if repeat != 's':
            print('Gracias por jugar')
            i = 1


dado6()
