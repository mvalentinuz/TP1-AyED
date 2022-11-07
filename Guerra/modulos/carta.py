# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:00:09 2022

@author: alumno
"""

class Carta:
    
    def __init__(self, valor, palo):  
        """
        @brief: El objeto carta se inicializa con un valor y un palo por parámetro.
        @param valor [int]: Es el número que indica el valor de la carta.
        @param palo [char]: Es el carácter que indica el palo de la carta.
        """ 
        self._valor = valor
        self._palo = palo
       
    def obtenerPalo(self):
        """
        @brief: Getter del palo de la carta.
        @return: es el carácter representativo del palo de la carta.
        """ 
        return self._palo
    
    def obtenerValor(self):
        """
        @brief: Getter del valor de la carta.
        @return: es el número representativo del valor de la carta.
        """ 
        return self._valor