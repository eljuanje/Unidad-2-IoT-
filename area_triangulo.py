#Calcular área del tríangulo
#Elaboró: Juan Jesús Gómez Sánchez
#GDS0152
#20/20/2020

import math

class areaTriangulo:
    def area_triangulo(self):
        b = int(input("Ingresa la Base del Tríangulo: "))
        a = int(input("Ingresa la Altura del Tríangulo: "))
        print(b*a/2)        

t = areaTriangulo()
t.area_triangulo()
