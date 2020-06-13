listaInicial = []
trios = []
# minimo = 0
decryptedMsg = ''


def stringToArray():
    global listaInicial
    with open('08.-simple_decrypter/testdata.txt') as f:
        f = f.read()
        listaInicial = f.split(' ')
        listaInicial = ''.join(listaInicial)
        listaInicial = f.split('.')
        listaInicial = listaInicial[1:]


def sumar3():
    conteo = 0
    cartera = 0
    global trios
    global minimo
    for n in listaInicial:
        if conteo <= 2:
            cartera += int(n)
            conteo += 1

        if conteo == 3:
            trios.append(cartera)
            cartera = 0
            conteo = 0

    # minimo = min(trios)


def convAscii(offset):
    global decryptedMsg
    decryptedMsg = ''
    for n in trios:
        menosPass = int(n) - offset
        char = chr(menosPass)
        decryptedMsg += char

    print(decryptedMsg)


def posibles(offset):
    nImp = 0
    for n in trios:
        menosPass = int(n) - offset
        if menosPass < 32 or menosPass > 126:
            nImp += 1

    return nImp


def fuerza():
    for i in range(min(trios)+1):
        imps = posibles(i)
        if imps < 15:
            print(
                f'-------------------------- vuelta {i} --------------------------')
            convAscii(i)


def start():
    stringToArray()
    sumar3()
    fuerza()


start()
