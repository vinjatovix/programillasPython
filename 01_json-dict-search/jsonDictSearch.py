# importamos json y una librería que nos permite encontrar resultados similares
import json
from difflib import get_close_matches

# Escogemos la ruta del diccionario
data = json.load(open(input('introduce la ruta completa del archivo json: ')))

# En la función buscar


def buscar(palabra):
    # Buscaremos por minúsculas
    palabra = palabra.lower()
    if palabra in data:
        return data[palabra]
    # Buscaremos la primera mayúscula
    elif palabra.title() in data:
        return data[palabra.title()]
    # Buscaremos todo mayúsculas
    elif palabra.upper() in data:
        return data[palabra.upper()]

    # Si no se encuentra buscaremos el resultado parecido más cercano
    elif len(get_close_matches(palabra, data.keys())) > 0:
        print("tal vez quisiste decir %s en su lugar" %
              get_close_matches(palabra, data.keys())[0])

        y = 0
        while y == 0:
            # Se le da la opción al usuario de ver la alternativa y se valida su respuesta
            decide = input("pulsa 's' si es así, y 'n' en caso contrario: ")
            if decide == "s":
                return data[get_close_matches(palabra, data.keys())[0]]
                y = 1
            elif decide == "n":
                return("en serio?")
                break
            else:
                print("lo siento, no te he entendido, pulsa 's' o 'n': ")
    else:
        print("pues no se que decir...")


# Con esto le pedimos la palabra al usuario
palabra = input("¿Qué palabra quieres buscar?: ")

# Con esto ofrecemos la respuesta
output = buscar(palabra)

# Puede ser que haya mas de una respuesta para una palabra, o sea una lista...
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
