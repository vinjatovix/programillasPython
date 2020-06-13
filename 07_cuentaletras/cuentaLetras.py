import collections

def cuentaletras(string):
    cntDir = {}
    for l in string:
        if l in cntDir:
            cntDir[l] += 1
        else:
            cntDir[l] = 1
    od = collections.OrderedDict(sorted(cntDir.items()))
    print(od)


cuentaletras(input('introduce un texto'))
