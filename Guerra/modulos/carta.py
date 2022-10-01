# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:00:09 2022

@author: alumno
"""

class Carta:
    """El objeto carta se inicializa con un valor y un palo por parámetro""" 
    def __init__(self, valor, palo):  
        self._valor = valor
        self._palo = palo
    """getter de palo"""    
    def obtenerPalo(self):
        return self._palo
    """getter de valor"""
    def obtenerValor(self):
        return self._valor