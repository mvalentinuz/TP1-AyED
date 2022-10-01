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
    
     l = ListaDobleEnlazada()
     n = []
     for i in range(100):
         n.append(i*10)

     for i in range(100):
         l.anexar(random.randint(0,100))   
     tiempos = []
    
     for i in range(100):
         t1 = time.time()
         l.ordenar()
         t2 = time.time()
         total = (t2 - t1)
         tiempos.append(total)
         for i in range(10):
             l.anexar(random.randint(0,100))
    
     plt.plot(n, tiempos)  
     plt.show()
      