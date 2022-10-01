# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:29:34 2022

@author: alumno
"""

from modulos.lista import ListaDobleEnlazada

class ColaDoble:
    """El objeto ColaDoble se inicializa conteniendo una lista doblemente enlazada"""
    def __init__(self):
        self.lista = ListaDobleEnlazada()
    
    """apilar agrega un nodo al inicio"""
    def apilar(self, dato):
        self.lista.agregar(dato)
    
    """encolar anexa un nodo al final"""
    def encolar(self, dato):
        self.lista.anexar(dato) 
    
    """desencolar extrae el nodo al inicio"""
    def desencolar(self):
        return self.lista.extraer(0)
    
    """desapilar extrae el nodo al final"""
    def desapilar(self):
        return self.lista.extraer()
    
    """tamanio indica la cantidad de datos en el objeto"""
    def tamanio(self):
        return self.lista.tamanio()
      