# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 21:55:06 2022

@author: ROMOANMAFR
"""
from modulos.LDE import ListaDobleEnlazada
if __name__ == "__main__":
    
     import time
     import random
     import matplotlib.pyplot as plt
     
     """Caso promedio de ordenamiento por inserción"""
     l = ListaDobleEnlazada()
     n = []
     for i in range(1000):
         n.append(i*10)

     for i in range(1000):
         l.anexar(random.randint(0,100))   
     tiempos = []
    
     for i in range(1000):
         t1 = time.time()
         l.ordenar()
         t2 = time.time()
         total = (t2 - t1)
         tiempos.append(total)
         for i in range(10):
             l.anexar(random.randint(0,100))
    
     plt.plot(n, tiempos)
     plt.show()
     
     """Caso ideal de ordenamiento por inserción, con una lista ya ordenada"""
     l2 = ListaDobleEnlazada()
     n2 = []
     for i in range(1000):
         n2.append(i*10)

     for i in range(1000):
         l2.anexar(i*10)   
     tiempos2 = []
    
     for i2 in range(1000):
         t1 = time.time()
         l2.ordenar()
         t2 = time.time()
         total = (t2 - t1)
         tiempos2.append(total)
         for i in range(10):
             l2.anexar(i*10)
    
     plt.plot(n2, tiempos2)
     plt.show()