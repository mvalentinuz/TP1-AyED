# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 13:49:36 2022

@author: alumno
"""

class Nodo:
    
    def __init__(self, datoInicial):
        """
        @brief: Se inicializa el nodo asignando sus referencias en None y con un dato
        inicial determinado en el momento de instanciar el objeto.
        @param datoInicial: Es el objeto que va a contener el nodo.
        """
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None
        
    def obtenerDato(self):
        """
        @brief: Getter de dato.
        @return: Es el objeto contenido.
        """
        return self.dato
    
    def obtenerSiguiente(self):
        """
        @brief: Getter de referencia al siguiente.
        @return: Es el nodo enlazado siguiente.
        """
        return self.siguiente

    def obtenerAnterior(self):
        """
        @brief: Getter de referencia al anterior.
        @return: Es el nodo enlazado anterior.
        """
        return self.anterior

    def asignarDato(self, nuevoDato):
        """
        @brief: Setter de dato.
        @param nuevoDato: Es el nuevo objeto asignado a contener por el nodo.
        """
        self.dato = nuevoDato

    def asignarSiguiente(self, nuevoSiguiente):
        """
        @brief: Setter de referencia al siguiente.
        @param nuevoAnterior: Es el nuevo nodo a enlazar como siguiente.
        """
        self.siguiente = nuevoSiguiente
  
    def asignarAnterior(self, nuevoAnterior):
        """
        @brief: Setter de referencia al anterior.
        @param nuevoAnterior: Es el nuevo nodo a enlazar como anterior.
        """
        self.anterior = nuevoAnterior
        
        
        