# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 13:52:17 2022

@author: alumno
"""
from modulos.Nodo import Nodo

class ListaDobleEnlazada:
    """La lista doblemente enlazada se inicializa con sus referencias de cabeza,
    cola e iterador en None y su contador de tamaño en cero """
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.iterador = None
        self.contador = 0
        
    """El método esta_vacia devuelve un booleano que indica si su contador de 
    tamaño es nulo confirmando o no si la lista está vacía"""    
    def esta_vacia(self):
        return self.contador == 0

    """El método tamanio devuelve el valor en el contador de tamaño que indica
    la cantidad de elementos en la lista""" 
    def tamanio(self):
        return self.contador

    """El método agregar añade al nuevo nodo en la cabeza de la lista actualizando
    las referencias de la cabeza original y la nueva. Si la lista está vacía 
    simplemente actualiza la referencias inicializadas. En ambos casos aumenta el
    contador de tamaño en uno""" 
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
    
    """El método anexar añade al nuevo nodo en la cola de la lista actualizando
    las referencias de la cola original y la nueva. Si la lista está vacía 
    simplemente actualiza las referencia inicializadas. En ambos casos aumenta el
    contador de tamaño en uno"""             
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
    
    """El método insertar añade un nuevo nodo en la posición indicada por parámetro.
    Si la posición está por fuera del alcance de índice de la lista, devuelve la
    excepción IndexError"""
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
    
    """El método extraer actualiza las referencias de los nodos asociados a una
    posición determinada por parámetro para quitar un nodo en tal posición y
    devolverlo en la llamada. Si no se especifica parámetro, extrae por defecto
    el último nodo. Si la lista está vacía, no hay nodo que extraer por lo que
    lanza una excepción"""
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
    
    """El método copiar devuelve el mismo objeto lista para que pueda ser asignado
    a otra instancia"""
    def copiar(self):
        return self
    
    """El método invertir espeja el orden de los nodos en la lista"""
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
        
    """El método ordenar organiza los nodos de menor a mayor intercambiando los
    datos de lugar. Se utiliza el método de ordenamiento de burbuja. En el caso
    más óptimo de que la lista ya esté ordenada, el orden de complejidad será
    O(n) ya que en bucle solo recorrerá la lista una sola vez en n operaciones.
    En el peor caso de que la lista esté invertida, el orden de complejidad será
    O(n^2) ya que el algoritmo recorrerá n veces la lista haciendo n operaciones"""    
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
    
    """El método concatenar une los nodos de una lista en otra para fusionarlas
    en una sola manteniendo el orden de las mismas"""
    def concatenar(self, Lista):
        temp = self.cola
        temp2 = Lista.cabeza 
        while temp2 is not None:
            self.anexar(temp2.obtenerDato())
            temp , temp2 = temp.obtenerSiguiente() , temp2.obtenerSiguiente()
        return self
     
    """Este método permite sobrecargar el operador + para concatenar"""
    def __add__ (self, Lista):
        return self.concatenar(Lista)
    
    """Este método permite mostrar el contenido de la lista como un string"""    
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
    
    """Este método permite que la lista sea iterable"""
    def __iter__(self):
        return self
    
    """Este método permite que la lista sea iterable indicando las referencias
    de orden en la lista"""
    def __next__(self):
        if self.iterador is not None:
            temp = self.iterador
            self.iterador = self.iterador.obtenerSiguiente()
            return temp
        else:
            raise StopIteration
            
            