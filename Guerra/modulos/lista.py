# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 13:52:17 2022

@author: alumno
"""
from modulos.nodo import Nodo

class ListaDobleEnlazada:

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.iterador = None
        self.contador = 0
        
        
    def esta_vacia(self):
        return self.contador == 0

    def tamanio(self):
        return self.contador

    def agregar(self, dato):
        temp = Nodo(dato)
        if(self.esta_vacia()):
            self.cabeza = temp
            self.cola = self.cabeza
            self.iterador = self.cabeza
            self.contador += 1
        else:
            temp.asignarSiguiente(self.cabeza)
            self.cabeza.asignarAnterior(temp)
            self.cabeza = temp
            self.contador += 1
            
    def anexar(self, dato):
        temp = Nodo(dato)
        if(self.esta_vacia()):
            self.cabeza = temp
            self.cola = self.cabeza
            self.iterador = self.cabeza
            self.contador += 1
        else:
            temp.asignarAnterior(self.cola)
            self.cola.asignarSiguiente(temp)
            self.cola = temp
            self.contador += 1
            
    def insertar(self, posicion, item):
        nuevoItem = Nodo(item)
        temp = self.cabeza
        indice = 0
            
        if(posicion == 0):
            self.agregar(item)
        elif(self.contador-1<posicion):
            raise IndexError
        elif(self.contador-1==posicion):
            self.anexar(item)
        else:
            while indice is not posicion-1:
                temp = temp.obtenerSiguiente()
                indice += 1
            nuevoItem.asignarAnterior(temp)
            nuevoItem.asignarSiguiente(temp.obtenerSiguiente())
            temp.asignarSiguiente(nuevoItem)
            self.contador += 1
    
    def extraer(self, posicion = None):
        if self.esta_vacia():
            raise Exception("La lista está vacía")
        elif(self.contador>1):
            if(posicion == None):
                temp = self.cola.obtenerAnterior()
                temp.asignarSiguiente(None)
                self.contador -= 1
                return self.cola
            elif(posicion==0):
                temp=self.cabeza
                self.cabeza = self.cabeza.obtenerSiguiente()
                self.cabeza.asignarAnterior(None)
                self.contador -= 1
                return temp
            else:
                indice = 0
                temp = self.cabeza
                while indice is not posicion:
                    temp = temp.obtenerSiguiente()
                    indice += 1
                temp.obtenerSiguiente().asignarAnterior(temp.obtenerAnterior())
                temp.obtenerAnterior().asignarSiguiente(temp.obtenerSiguiente())
                self.contador -= 1
                return temp
        elif(self.contador==1):
            temp = self.cabeza
            self.cabeza = None
            self.cola = None
            self.contador -= 1
            return temp
    
    def copiar(self):
        return self
    
    def invertir(self):
        temp = self.cola
        listatemp = ListaDobleEnlazada()
        indice = 0
        while indice is not self.contador:
            listatemp.anexar(temp.obtenerDato())
            temp = temp.obtenerAnterior()
            indice += 1
        self.cabeza = listatemp.cabeza
        self.cola = listatemp.cola
        self = listatemp.copiar()
        
    def ordenar(self):
        estaOrdenada = False
        temp = self.cabeza

        while not estaOrdenada:
            estaOrdenada = True
            for i in range(0, self.tamanio()-1):
                if temp.obtenerSiguiente() is not None:
                    if temp.obtenerDato() > temp.obtenerSiguiente().obtenerDato():
                        aux = temp.obtenerDato()
                        temp.asignarDato(temp.obtenerSiguiente().obtenerDato())
                        temp.obtenerSiguiente().asignarDato(aux)
                        estaOrdenada = False
                if temp.obtenerSiguiente() is not None:
                    temp = temp.obtenerSiguiente()
                else:
                    temp = self.cabeza    
            
    def concatenar(self, Lista):
        temp = self.cola
        temp2 = Lista.cabeza 
        while temp2 is not None:
            self.anexar(temp2.obtenerDato())
            temp , temp2 = temp.obtenerSiguiente() , temp2.obtenerSiguiente()
        return self
        
    def __add__ (self, Lista):
        return self.concatenar(Lista)
        
    def __str__(self):
        temp = self.cabeza
        if not self.esta_vacia():
            string = "["
            while temp is not self.cola:
                string += str(temp.obtenerDato()) + ", "
                temp = temp.obtenerSiguiente()
            string += str(self.cola.obtenerDato())+"]"
        else: 
            string = "[]"
        return string
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iterador is not None:
            temp = self.iterador
            self.iterador = self.iterador.obtenerSiguiente()
            return temp
        else:
            raise StopIteration