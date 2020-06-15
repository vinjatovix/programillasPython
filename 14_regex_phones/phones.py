'''
arbir el documento
eliminar los espacios y guiones
buscar cadenas de 9 numeros
guardarlas en un nuevo documento
'''
documento = '14_regex_phones\phones.txt'


def isPhone(string):
    if len(string) != 9:
        return False
    try:
        int(string)
        with open('14_regex_phones\output.txt', 'a') as output:
            output.write(string+'\r\n')
    except:
        return False


def regexPhones(documento):
    with open(documento) as texto:
        texto = texto.read()
        texto = texto.replace(' ', '')
        texto = texto.replace('-', '')
        texto = texto.replace('\n', '')
        texto = texto.replace('.', '')
        texto = texto.replace('+34', '')
        for i in range(len(texto)):
            chunk = texto[i:i+9]
            isPhone(chunk)


regexPhones(documento)
