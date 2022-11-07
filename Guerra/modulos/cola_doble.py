# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:29:34 2022

@author: alumno
"""

from modulos.lista import ListaDobleEnlazada

class ColaDoble:
    
    def __init__(self):
        """
        @brief: El objeto ColaDoble se inicializa conteniendo una lista doblemente enlazada.
        """
        self.lista = ListaDobleEnlazada()
    
    def apilar(self, dato):
        """
        @brief: El método apilar agrega un nodo al inicio.
        @param dato: Es el objeto que va a contener el nodo apilado.
        """
        self.lista.agregar(dato)
    
    def encolar(self, dato):
        """
        @brief: El método encolar anexa un nodo al final.
        @param dato: Es el objeto que va a contener el nodo anexado.
        """
        self.lista.anexar(dato) 
    
    def desencolar(self):
        """
        @brief: El método desencolar extrae el nodo al inicio.
        @return: Es el nodo extraído.
        """
        return self.lista.extraer(0)
    
    def desapilar(self):
        """
        @brief: El método desapilar extrae el nodo al final.
        @return: Es el nodo extraído.
        """
        return self.lista.extraer()

    def tamanio(self):
        """
        @brief: El método tamanio indica la cantidad de nodos en la lista.
        @return: Es el valor que representa la cantidad total de nodos.
        """
        return self.lista.tamanio()
      