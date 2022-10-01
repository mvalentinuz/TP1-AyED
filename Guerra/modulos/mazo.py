# -*- coding: utf-8 -*-

from modulos.cola_doble import ColaDoble

class Mazo:
    """El objeto mazo se inicializa conteniendo una cola doble que contendrán
    objetos carta"""
    def __init__(self):
        self.cartas = ColaDoble()
    
    """El método ponerArriba recibe una carta por parámetro y llama al método
    apilar de ColaDoble"""
    def ponerArriba(self, carta):
        self.cartas.apilar(carta)
        
    """El método sacarArriba devuelve la carta al frente del mazo llamando
    al método desencolar de ColaDoble"""    
    def sacarArriba(self):
        return self.cartas.desencolar().obtenerDato()
    
    """El método ponerDebajo recibe una carta por parámetro y llama al método
    encolar de ColaDoble"""
    def ponerDebajo(self, carta):
        self.cartas.encolar(carta)
    
    """El método sacarDebajo devuelve la carta al final del mazo llamando
    al método desapilar de ColaDoble"""   
    def sacarDebajo(self):
        return self.cartas.desapilar().obtenerDato()
    
    """Devuelve la cantidad de cartas llamando al método tamanio de ColaDoble"""
    def tamanio(self):
        return self.cartas.tamanio()
                