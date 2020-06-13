def palindromo(palabra):
    palabra = palabra.lower()
    return palabra[::-1] == palabra


print(palindromo(input('introduce un texto: \r\n')))
