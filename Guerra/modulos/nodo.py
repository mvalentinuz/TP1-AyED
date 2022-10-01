# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 13:49:36 2022

@author: alumno
"""

class Nodo:
    
    def __init__(self, datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente
    
    def obtenerAnterior(self):
        return self.anterior

    def asignarDato(self, nuevoDato):
        self.dato = nuevoDato

    def asignarSiguiente(self, nuevoSiguiente):
        self.siguiente = nuevoSiguiente
        
    def asignarAnterior(self, nuevoAnterior):
        self.anterior = nuevoAnterior
        
        
        