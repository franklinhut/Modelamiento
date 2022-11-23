#método de la secante
#integrantes :Campuzano Espianal José Luis, Villegas Lopez Franklin,Menendez Mendoza Luis
import math as m 
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return eval(funcion) 

def secante(x0,x1,iteraciones):
    for i in range(iteraciones):
        x2 = x1 - (f(x1)*(x1-x0))/(f(x1)-f(x0))
        x0 = x1
        x1 = x2
        print("x",i,"=",x2)
    return x2

funcion = input("Ingrese la funcion: ")
x0 = float(input("Ingrese el valor de x0: "))
x1 = float(input("Ingrese el valor de x1: "))   
iteraciones = int(input("Ingrese el numero de iteraciones: "))
print("La raiz es: ",secante(x0,x1,iteraciones))

    


