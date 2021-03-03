#!/usr/bin/env python
# coding: utf-8

# In[295]:

#Escrito por Alfredo Aguiar 30 de diciembre del 2020.

# importamos las librerías necesarias
import sympy as sp  # librería para cálculo simbólico

from sympy.physics.vector import init_vprinting
init_vprinting(use_latex='mathjax', pretty_print=False)
from sympy.physics.mechanics import dynamicsymbols

#Definir metodos y variables para evitar llamar nuevamente a la liberia tras cargado el modulo.

#Agregar constante pi, a la libraria.
pi = sp.pi

def simbolic(sym):
    #Regresa las variables simbolicas.
    #Recive un string como parametro.
    return dynamicsymbols(sym)


#Definir las variables simbolicas utilizadas por el modulo.
theta1, theta2, l1, l2, theta, alpha, a, d = dynamicsymbols('theta1 theta2 l1 l2 theta alpha a d')

#Definimos las matrices de rotacion y traslacion correspondientes

#Rotacion en Z
rz = sp.Matrix([[sp.cos(theta),-sp.sin(theta),0,0],
               [sp.sin(theta),sp.cos(theta),0,0],
               [0,0,1,0],
               [0,0,0,1]])

#Traslacion en Z
tz = sp.Matrix([[1,0,0,0],
               [0,1,0,0],
               [0,0,1,d],
               [0,0,0,1]])

#Traslacion en X
tx = sp.Matrix([[1,0,0,a],
               [0,1,0,0],
               [0,0,1,0],
               [0,0,0,1]])

#Rotacion en X
rx = sp.Matrix([[1,0,0,0],
               [0,sp.cos(alpha),-sp.sin(alpha),0],
               [0,sp.sin(alpha),sp.cos(alpha),0],
               [0,0,0,1]])


#Ecuacion matricial para obtener DH
DH = rz*tz*tx*rx

def get_origin_dh():
    """
    Regreesa la matriz de parametros de Denavit Hartenberg. (sin ser afectada por ninguna articulacion)
    """
    return DH

class robot:
    #Array al que se le van agregando las articulaciones
    articulation_array = []

    def add_articulation(self, theta_, d_, a_, alpha_):
        """
        Agrega una matriz de DH en 'articulation_array', para la articulacion 'n',
        esta se agrega a un array que guarda las matrices de 'n' articulacion,
        'articulation_array' es un arreglo que contiene las matrices de cada articulacion.
        """
        new_articulation = DH.subs({theta : theta_ , d : d_ , alpha : alpha_ , a : a_ })
        self.articulation_array.append(new_articulation)

    def delete_articulation_matrix(self, index):
        """
        Elimina una de las matrices agregada en 'articulation_array' en base a su posicion seleccionada por index.
        El orden de cada elemento va de 0 a 'n' elementos siendo 'n' el mas reciente, y 0 el mas antiguo.
        """
        if len(self.articulation_array) > 0:
            del self.articulation_array[index]
        else:
            print('Primero agrega elementos al arreglo.')

    def get_articulation_array(self):
        """
        Imprime la matriz 'articulation_array', que es un arreglo con las matrices generadas para 'n' articulacion,
        el orden es de la mas antigua a la mas reciente 
        """
        return self.articulation_array


    def reset_articulation_array(self):
        """
        Resetea y deja vacio el arreglo que contiene las matrices de cada articulacion.
        """ 
        del self.articulation_array[:]


    def solve(self):
        """
        Regresa la matriz resultado de Denavit Hartenberg.
        El retorno de un valor 1, es tomado como error dado que no se ha procesado la informacion.
        """
        T = 1
        for i in range(len(self.articulation_array)):
            T = T * self.articulation_array[i] 
         
        #Regresamos el resultado
        return T

