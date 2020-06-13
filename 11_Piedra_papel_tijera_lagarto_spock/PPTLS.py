# IMPORTAMOS RANDOM PARA QUE LA MAQUINA PUEDA ESCOGER
import random

# ASIGNAMOS LAS POSIBILIDADES A UN NÚMERO DEL 0 AL 4
(PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK) = range(5)

valores = ["PIEDRA", "PAPEL", "TIJERA", "LAGARTO", "SPOCK"]

# La clave representa la posición en el vector de valores. El valor de cada clave es la manera en que un elemento vence a otro y los elentos a los que puede vencer.
# Por ejemplo, la posición 0 representa PIEDRA. PIEDRA aplasta a LAGARTO y PIEDRA aplasta a TIJERA
paradigma = {
    0: [["aplasta a", "revienta "], [LAGARTO, TIJERA]],
    1: [["envuelve a", "desacredita a"], [PIEDRA, SPOCK]],
    2: [["corta a", "mata a"], [PAPEL, LAGARTO]],
    3: [["envenena a", "come a"], [SPOCK, PAPEL]],
    4: [["rompe a", "vaporiza a"], [TIJERA, PIEDRA]]}

(GANAUSUARIO, GANAMAQUINA, EMPATE) = range(3)


# Obtiene una cadena de texto a partir del código de la tirada

# Ej: valorTexto(0) = PIEDRA
def valorTexto(codigo):
    return valores[codigo]

# Devuelve el código de la tirada a partir de la cadena de texto de la tirada
# Ej: textoValor("PIEDRA") = 0


def textoValor(texto):
    for i, valor in enumerate(valores):
        if (texto == valor):
            return i

# Tirada de la máquina


def sacaMaquina():
    tirada = random.randint(0, 5)
    return tirada

# Tirada del usuario


def sacaUsuario():
    tirada = ""
    while not tirada in valores:
        tirada = input(
            'Escoge: piedra, papel, tijera, lagarto o Spock): ').upper()
        return textoValor(tirada)

# Valida la jugada


def juego(usuario, maquina):
    if maquina in paradigma[usuario][1]:
        return GANAUSUARIO
    elif usuario in paradigma[maquina][1]:
        return GANAMAQUINA
    else:
        return EMPATE

# Explica la jugada
# Ej: explica(TIJERA, PAPEL) =


def explica(ganador, perdedor):
    for i, valor in enumerate(paradigma[ganador][1]):
        if (perdedor == valor):
            print(valorTexto(ganador),
                  paradigma[ganador][0][i], valorTexto(perdedor))

########################
### CUERPO PRINCIPAL ###
########################


# Tiradas de los usuarios
usuario = sacaUsuario()
maquina = sacaMaquina()


# Comprueba la jugada y muestra el resultado
resultado = juego(usuario, maquina)
if resultado == GANAUSUARIO:
    explica(usuario, maquina)
    print("¡Has ganado!")
elif resultado == GANAMAQUINA:
    explica(maquina, usuario)
    print("¡Has perdido!")
else:
    print("¡Empate!")
