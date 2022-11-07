# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 13:52:17 2022

@author: alumno
"""
from modulos.nodo import Nodo

class ListaDobleEnlazada:
    def __init__(self):
        """
        @brief: La lista doblemente enlazada se inicializa con sus referencias de cabeza,
        cola e iterador en None y su contador de tamaño en cero.
        """
        self.cabeza = None
        self.cola = None
        self.iterador = None
        self.contador = 0
            
    def esta_vacia(self):
        """
        @brief: El método esta_vacia confirma si la lista está vacía.
        @return: Devuelve un booleano que indica si su contador de tamaño es nulo.
        """
        return self.contador == 0
 
    def tamanio(self):
        """
        @brief: El método tamanio indica la cantidad de elementos en la lista.
        @return: Devuelve el valor en el contador de tamaño.
        """
        return self.contador

    def agregar(self, dato):
        """
        @brief: El método agregar añade al nuevo nodo en la cabeza de la lista actualizando
        las referencias de la cabeza original y la nueva. Si la lista está vacía 
        simplemente actualiza la referencias inicializadas. En ambos casos aumenta el
        contador de tamaño en uno.
        @param dato: Es el objeto a ingresar a la lista.
        """ 
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
        """
        @brief: El método anexar añade al nuevo nodo en la cola de la lista actualizando
        las referencias de la cola original y la nueva. Si la lista está vacía 
        simplemente actualiza las referencia inicializadas. En ambos casos aumenta el
        contador de tamaño en uno.
        @param dato: Es el objeto a ingresar a la lista.
        """
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
        """
        @brief: El método insertar añade un nuevo nodo en la posición indicada por parámetro.
        Si la posición está por fuera del alcance de índice de la lista, lanza una
        excepción.
        @param posicion: Es la posicion de índice en la lista en donde se inserta.
        @param item: Es el objeto a ingresar a la lista.
        @raise IndexError: Excepción lanzada al ingresar por parámetro una posición no válida.
        """
        nuevoItem = Nodo(item)
        temp = self.cabeza
        indice = 0
            
        if(posicion == 0):
            self.agregar(item)
        elif(self.contador<posicion):
            raise IndexError
        elif(self.contador==posicion):
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
        """
        @brief: El método extraer actualiza las referencias de los nodos asociados a una
        posición determinada por parámetro para quitar un nodo en tal posición y
        devolverlo en la llamada. Si no se especifica parámetro, extrae por defecto
        el último nodo. Si la lista está vacía, no hay nodo que extraer por lo que
        lanza una excepción.
        @param posicion: Es la posicion de índice en la lista en donde se extrae.
        Si no se especifica, se inicializa por defecto para extraer el último nodo.
        @raise Exception: Excepción lanzada al no existir nodo para extraer porque la lista está vacía.
        @raise IndexError: Excepción lanzada al ingresar por parámetro una posición no válida.
        @return temp: Es el nodo extraído.
        """
        if self.esta_vacia():
            raise Exception("La lista está vacía")
        elif(self.contador-1<posicion):
            raise IndexError
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
            elif(posicion==self.tamanio()-1):
                temp = self.cola.obtenerAnterior()
                temp.obtenerAnterior().asignarSiguiente(self.cola)
                self.cola.asignarAnterior(temp.obtenerAnterior())
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
        """
        @brief: El método copiar devuelve una copia del objeto lista para que pueda ser asignado
        a otra instancia.
        @return: Devuelve un objeto ListaDobleEnlazada idéntico al original.
        """
        copia = ListaDobleEnlazada()
        temp = self.cabeza
        while temp is not None:
            copia.anexar(temp.obtenerDato())
            temp = temp.obtenerSiguiente()    
        return copia
    
    def invertir(self):
        """
        @brief: El método invertir espeja el orden de los nodos en la lista.
        """
        temp = self.cabeza
        temp2 = self.cola
        for i in range(self.tamanio()//2):
            aux = temp.obtenerDato()
            temp.asignarDato(temp2.obtenerDato())
            temp2.asignarDato(aux)
            temp, temp2 = temp.obtenerSiguiente(), temp2.obtenerAnterior()
           
    def ordenar(self):
        """
        @brief: El método ordenar organiza los nodos de menor a mayor intercambiando los
        datos de lugar. Se utiliza el método de ordenamiento de inserción.
        """ 
        nodoIndice = self.cabeza
        for indice in range(1,self.tamanio()):
            nodoIndice = nodoIndice.obtenerSiguiente()
            temp = nodoIndice
            valorActual = nodoIndice.obtenerDato()
            posicion = indice

            while posicion>0 and temp.obtenerAnterior().obtenerDato()>valorActual:
                temp.asignarDato(temp.obtenerAnterior().obtenerDato())
                temp = temp.obtenerAnterior()
                posicion = posicion-1 

            temp.asignarDato(valorActual)   
    
    def concatenar(self, Lista):
        """
        @brief: El método concatenar une las referencias de los nodos de una lista con otra para fusionarlas
        en una sola manteniendo el orden de las mismas.
        @param Lista [ListaDobleEnlazada]: Es la lista que va a concatenarse a continuación.
        @return: Es la ListaDobleEnlazada concatenada.
        """
        self.cola.asignarSiguiente(Lista.cabeza)
        self.cola = Lista.cola
        return self
     
    def __add__ (self, Lista):
        """
        @brief: Este método permite sobrecargar el operador + para concatenar.
        @param Lista [ListaDobleEnlazada]: Es la lista que va a concatenarse a continuación.
        @retrun: Es la ListaDobleEnlazada concatenada.
        """
        return self.concatenar(Lista)
       
    def __str__(self):
        """
        @brief: Este método permite mostrar el contenido de la lista como un string.
        @return: Es un string que describe el contenido de la lista.
        """ 
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
        """
        @brief: Este método permite que la lista sea iterable.
        """
        return self
    
    def __next__(self):
        """
        @brief: Este método permite que la lista sea iterable indicando las referencias
        de orden en la lista.
        """
        if self.iterador is not None:
            temp = self.iterador
            self.iterador = self.iterador.obtenerSiguiente()
            return temp
        else:
            raise StopIteration
    