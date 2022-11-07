# -*- coding: utf-8 -*-

from modulos.cola_doble import ColaDoble

class Mazo:
    
    def __init__(self):
        """
        @brief: El objeto mazo se inicializa conteniendo una cola doble que contendrán
        objetos carta.
        """
        self.cartas = ColaDoble()
    
    def ponerArriba(self, carta):
        """
        @brief: El método ponerArriba recibe una carta por parámetro y llama al método
        apilar de ColaDoble.
        @param carta [Carta]: Es el objeto Carta a apilar.
        """
        self.cartas.apilar(carta)
           
    def sacarArriba(self):
        """
        @brief: El método sacarArriba devuelve la carta al frente del mazo llamando
        al método desencolar de ColaDoble.
        @return: Es el objeto Carta que estaba al frente del mazo. 
        """ 
        return self.cartas.desencolar().obtenerDato()
    
    def ponerDebajo(self, carta):
        """
        @brief: El método ponerDebajo recibe una carta por parámetro y llama al método
        encolar de ColaDoble.
        @param carta [Carta]: Es el objeto carta a encolar.
        """
        self.cartas.encolar(carta)
     
    def sacarDebajo(self):
        """
        @brief: El método sacarDebajo devuelve la carta al final del mazo llamando
        al método desapilar de ColaDoble.
        @return: Es el objeto Carta que estaba al final del mazo.
        """  
        return self.cartas.desapilar().obtenerDato()
    
    def tamanio(self):
        """
        @brief: Devuelve la cantidad de cartas llamando al método tamanio de ColaDoble.
        @return: Es el valor que indica la cantidad de cartas en el mazo.
        """
        return self.cartas.tamanio()
                