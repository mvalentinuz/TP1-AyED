# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 13:49:36 2022

@author: alumno
"""

class Nodo:
    
    """Se inicializa el nodo asignando sus referencias en None y con un dato
    inicial determinado en el momento de instanciar el objeto"""
    def __init__(self, datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None
        
    """Getter de dato"""
    def obtenerDato(self):
        return self.dato
    """Getter de referencia al siguiente"""
    def obtenerSiguiente(self):
        return self.siguiente
    """Getter de referencia al anterior"""
    def obtenerAnterior(self):
        return self.anterior
    """Setter de nuevo dato"""
    def asignarDato(self, nuevoDato):
        self.dato = nuevoDato
    """Setter de referencia al siguiente"""
    def asignarSiguiente(self, nuevoSiguiente):
        self.siguiente = nuevoSiguiente
    """Setter de referencia al siguiente"""    
    def asignarAnterior(self, nuevoAnterior):
        self.anterior = nuevoAnterior
        
        
        