from random import shuffle


class Carta:
    '''
    Cada carta tiene que tener un valor y pertenecer a un palo.
    En la lógica identificamos cada palo con su indice en la lista (0,1,2,3)
    Lo mismo para cada valor. 
    Para facilitarme la programación he añadido "None" como valores 0 y 1 en la lista valores
    para que el resto correspondan con su índice.

    Ergo, en la lógica tanto el palo como el valor son números enteros. 

    El as de bastos es (12,0), mientras que el 3 de oros es (3,3)
    '''
    palos = ["Bastos", "Copas", "Espadas", "Oros"]
    valores = [None, None, "2", "3", "4", "5",
               "6", "7", "Sota", "Caballo", "Rey", "As"]

    def __init__(self, valor, palo):
        '''Palo y valor son enteros'''
        self.valor = valor
        self.palo = palo

    def __lt__(self, carta2):
        '''Nos servimos de este método mágico para establecer cuando una carta es menor que otra'''
        # comparamos los valores
        if self.valor < carta2.valor:
            return True

        # en caso de empate comparamos los palos
        elif self.valor == carta2.valor:
            if self.palo < carta2.palo:
                return True
            else:
                return False

        else:
            return False

    def __gt__(self, carta2):
        '''Nos servimos de este método mágico para establecer cuando una carta es mayor que otra'''
        # comparamos los valores
        if self.valor > carta2.valor:
            return True

        # en caso de empate comparamos los palos
        elif self.valor == carta2.valor:
            if self.palo > carta2.palo:
                return True
            else:
                return False

        else:
            return False

    def __repr__(self):
        '''Esto es lo que va a permitir nombrar los objetos
        El as de bastos es self.valores[12] + " de " + self.palos[0], 
        El 3 de oros es self.valores[3] + " de " + self.palos[3]
        '''
        nombre = self.valores[self.valor] + " de " + self.palos[self.palo]
        return nombre


class Jugador:
    '''Cada jugador tiene un nombre, una carta en juego y un numero de victorias por partida'''
    def __init__(self, nombre):
        self.victorias = 0
        self.carta = None
        self.nombre = nombre


class Baraja:
    '''
    La baraja tiene 10 valores y 4 palos.
    En el constructor creamos la lista y la barajamos
    '''
    def __init__(self):
        # La lista comienza vacía y le añadimos items iterando 
        self.cartas = []
        # Estas iteraciones se referiran a las listas de la clase Carta
        for valor in range(2, 12):
            for palo in range(4):
                self.cartas.append(Carta(valor, palo))

        # Acto seguido barajamos
        shuffle(self.cartas)

    def coger_carta(self):
        '''
        Cada vez que cogemos una carta la eliminamos de la baraja restante.
        Al acabarse las cartas termina la partida
        '''
        if len(self.cartas) == 0:
            return
        return self.cartas.pop()


class Partida:
    '''
    En el constructor instanciamos una baraja y dos jugadores
    También tiene un vencedor por cada ronda lo averiguaremos con el metodo victorias()
    En cada ronda los jugadores tienen que mostrar_jugada().

    Finalmente definimos la rutina de juego, jugar()
    y como se declara un vencedor, ganador()
    '''
    def __init__(self):
        nombre1 = input("Jugador 1, ¿Cómo te llamas? \r\n")
        nombre2 = input("¿Y cual es tu nombre Jugador 2? \r\n")
        
        self.baraja = Baraja()
        self.p1 = Jugador(nombre1)
        self.p2 = Jugador(nombre2)


    def victorias(self, ganador):
        ronda = "{} gana esta ronda \r\n"
        ronda = ronda.format(ganador)
        print(ronda)


    def mostrar_jugada(self, p1n, p1c, p2n, p2c):
        # n corresponde al nombre del jugador y c a la carta
        jugada = "{} saca {} {} saca {}"
        jugada = jugada.format(p1n, p1c, p2n, p2c)
        print(jugada)




    def jugar(self):
        # Ponemos sobre la mesa las cartas
        cartas = self.baraja.cartas
        print("Empieza la partida")
        # mientras haya por lo menos dos cartas en la baraja para coger podemos dar a escoger si jugar o terminar
        while len(cartas) >= 2:
            mensaje = "Pulsa q para terminar. Cualquier " + "tecla para jugar: \r\n"
            respuesta = input(mensaje).lower()
            if respuesta == 'q':
                break

            # en caso de jugar identificamos a los jugadores y a las cartas que tienen
            p1n = self.p1.nombre
            p2n = self.p2.nombre
            p1c = self.baraja.coger_carta()
            p2c = self.baraja.coger_carta()
            
            self.mostrar_jugada(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.victorias += 1
                self.victorias(self.p1.nombre)
            else:
                self.p2.victorias += 1
                self.victorias(self.p2.nombre)

        win = self.ganador(self.p1, self.p2)
        print("La guerra acaba. GANADOR: {} ".format(win))

    def ganador(self, p1, p2):
        if p1.victorias > p2.victorias:
            return p1.nombre
        if p1.victorias < p2.victorias:
            return p2.nombre
        return "... no hay un ganador ..."


juego = Partida()
juego.jugar()
