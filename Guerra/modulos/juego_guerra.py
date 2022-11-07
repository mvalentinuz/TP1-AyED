
from modulos.mazo import Mazo
from modulos.carta import Carta
import random

class JuegoGuerra:
    
    def __init__(self, random_seed):
        """
        @brief: Se inicializa el objeto dando valores iniciales, instanciando los mazos 
        y creando el mazo principal mezclando las cartas mediante la utilización de
        una lista de python y el método shuffle que responde a una semilla random
        previamente indicada.
        @param random_seed [int]: Es la semilla que setea el random pseudoaleatorio.
        """
        self.valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.palos = ['♠', '♥', '♦', '♣']
        self.botinGuerra = []
        self.turnos_jugados = 0
        self.ganador = None
        self.empate = False
        self.mazoPrincipal = Mazo()
        self.mazoJugador1 = Mazo()
        self.mazoJugador2 = Mazo()
        
        lista_de_cartas = []
        for valor in self.valores:
            for palo in self.palos:
                lista_de_cartas.append(Carta(valor , palo))
        random.seed(random_seed)
        random.shuffle(lista_de_cartas)
        
        for i in range(len(lista_de_cartas)):
            self.mazoPrincipal.ponerArriba(lista_de_cartas[i])  
    
    def repartir(self):
        """
        @brief: El método repartir distribuye las cartas del mazo principal en los mazos de ambos
        jugadores.
        """
        while self.mazoPrincipal.tamanio() != 0:
            carta = self.mazoPrincipal.sacarArriba()
            self.mazoJugador1.ponerArriba(carta)
            carta = self.mazoPrincipal.sacarArriba()
            self.mazoJugador2.ponerArriba(carta)
           
    def finDelJuego(self):
        """
        @brief: El método finDelJuego chequea si se cumplieron las condiciones de victoria
        o de empate y devuelve true si alguna se satisfizo o false en caso contario.
        @return: Devuelve un booleano que confirma si el juego terminó.
        """
        if(self.mazoJugador1.tamanio() == 0):
            self.ganador = "jugador 2"
            self.proyectarEnConsola(None, None, False, True)
            return True
        elif(self.mazoJugador2.tamanio() == 0):
            self.ganador = "jugador 1"
            self.proyectarEnConsola(None, None, False, True)
            return True
        elif(self.turnos_jugados == 10000):
            self.empate = True
            self.proyectarEnConsola(None, None, False, True)
            return True
        else:
            return False
    
    def jugarTurno(self):
        """
        @brief: El método jugarTurno simula un turno y hace la comparación de las cartas
        jugadas para determinar el ganador de las cartas jugadas en el turno siempre
        que no haya terminado el juego. Cada llamada aumenta los turnos_jugados en 1.
        """
        if (not self.finDelJuego()):
            self.turnos_jugados += 1
            cartaJ1 = self.mazoJugador1.sacarArriba()
            cartaJ2 = self.mazoJugador2.sacarArriba()
            self.proyectarEnConsola(cartaJ1, cartaJ2, False, False)
            if self.valores.index(cartaJ1.obtenerValor()) > self.valores.index(cartaJ2.obtenerValor()):
                self.mazoJugador1.ponerDebajo(cartaJ1)
                self.mazoJugador1.ponerDebajo(cartaJ2)
            elif self.valores.index(cartaJ1.obtenerValor()) < self.valores.index(cartaJ2.obtenerValor()):
                self.mazoJugador2.ponerDebajo(cartaJ1)
                self.mazoJugador2.ponerDebajo(cartaJ2)
            else:
                self.botinGuerra.append(cartaJ1)
                self.botinGuerra.append(cartaJ2)
                self.guerra()
            
    def guerra(self):
        """
        @brief: El método guerra se da en un turno cuando las cartas jugadas tienen el 
        mismo valor. En este evento se pone en juego el botín de guerra y se evaluan
        nuevas cartas jugadas. El evento puede darse consecutivamente si las cartas
        jugadas tienen el mismo valor nuevamente.
        """
        for i in range(0,3):
            if (not self.finDelJuego()):
                carta = self.mazoJugador1.sacarArriba()
                self.botinGuerra.append(carta)
                carta = self.mazoJugador2.sacarArriba()
                self.botinGuerra.append(carta)
        if (not self.finDelJuego()):
            cartaJ1 = self.mazoJugador1.sacarArriba()
            cartaJ2 = self.mazoJugador2.sacarArriba()
            self.proyectarEnConsola(cartaJ1, cartaJ2, True, False)
            if self.valores.index(cartaJ1.obtenerValor()) > self.valores.index(cartaJ2.obtenerValor()):
                for carta in self.botinGuerra:
                    self.mazoJugador1.ponerDebajo(carta)
                self.botinGuerra.clear()
                self.mazoJugador1.ponerDebajo(cartaJ1)
                self.mazoJugador1.ponerDebajo(cartaJ2)
            elif self.valores.index(cartaJ1.obtenerValor()) < self.valores.index(cartaJ2.obtenerValor()):
                for carta in self.botinGuerra:
                    self.mazoJugador2.ponerDebajo(carta)
                self.botinGuerra.clear()
                self.mazoJugador2.ponerDebajo(cartaJ1)
                self.mazoJugador2.ponerDebajo(cartaJ2)
            else:
                self.botinGuerra.append(cartaJ1)
                self.botinGuerra.append(cartaJ2)
                self.guerra()
           
    def iniciar_juego(self):
        """
        @brief: El método iniciar_juego llama a la repartija de cartas y a la ejecución
        de un turno hasta que las condiciones de finalización se hayan dado.
        """ 
        self.repartir()
        while self.ganador == None and self.empate == False:
            self.jugarTurno()
    
    def proyectarEnConsola(self, cartaJugada1, cartaJugada2, hayGuerra, finDelJuego):
        """
        @brief: El método proyectarEnConsola permite la visualiación de la evolución de
        la partida a través de la consola del compilador. Recibe condiciones por 
        parámetro para proyectar correctamente el turno.
        @param cartaJugada1: Es la carta jugada por el Jugador 1 en el turno actual.
        @param cartaJugada2: Es la carta jugada por el Jugador 2 en el turno actual.
        @param hayGuerra: Es un booleano que indica proyectar un escenario de Guerra.
        @param finDelJuego: Es un booleano que indica si el juego sigue en progreso.
        """
        if(not finDelJuego):
            print("--------------------------------------------")
            if (hayGuerra):
                print("            **** Guerra! ****")
            print("Turno: ", self.turnos_jugados)
            print("jugador 1:")
            for carta in range(self.mazoJugador1.tamanio()):
                print("-X", end=" ")
            print(" ")
            print(" ")
            i = 0
            if (hayGuerra):
                print("       ", end=" ")
                for carta in self.botinGuerra:
                    if(i<2):
                        print(carta.obtenerValor()+carta.obtenerPalo(), end=" ")
                        i+=1
                    elif(i>=2 and i<=7):
                        print("-X", end=" ")
                        i+=1
                    else:
                        print(carta.obtenerValor()+carta.obtenerPalo(), end=" ")
                        i=1
                print(cartaJugada1.obtenerValor()+cartaJugada1.obtenerPalo()," ",cartaJugada2.obtenerValor()+cartaJugada2.obtenerPalo())
            else:
                print("                 ", cartaJugada1.obtenerValor()+cartaJugada1.obtenerPalo(),"  ",cartaJugada2.obtenerValor()+cartaJugada2.obtenerPalo())
            print(" ")
            print("jugador 2:")
            for i in range(self.mazoJugador2.tamanio()):
                print("-X", end=" ")
            print(" ")
            print("--------------------------------------------")
        elif(self.ganador is not None):
            print("**** ", self.ganador," gana la partida ****")
        elif(self.empate):
            print("            **** Empate ****")
    