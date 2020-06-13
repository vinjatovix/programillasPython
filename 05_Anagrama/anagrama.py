def anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    return sorted(palabra1) == sorted(palabra2)

a = input('introdce la primera palabra: \r\n')
b = input('introdce la segunda palabra: \r\n')

print(anagrama(a,b))
