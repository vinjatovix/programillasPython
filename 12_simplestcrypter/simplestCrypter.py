def crpt(string):
    d = {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': 'º', 'K': 'ª', 'L': '!', 'M': '|',
         'N': '@', 'Ñ': '"', 'O': '#', 'P': '·', 'Q': '~', 'R': '$', 'S': '%', 'T': '€', 'U': '&', 'V': '¬', 'W': '/', 'X': '(', 'Y': ')', 'Z': '='}
    enc = ''
    for l in string:
        if l.upper() in d:
            enc = enc + d[l.upper()]
        # print(d[l.upper()])
    print(enc)


crpt(input('dime algo: \r\n'))
