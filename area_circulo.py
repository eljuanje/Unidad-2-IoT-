#Calcular el área un círculo
#Elaboró: Juan Jesús Gómez Sánchez
#GDS0152
#20/20/2020

import math

class areaCirculo:
    def area_circulo(self):

        r = int(input("Ingresar radio del círculo: "))
        pi = 3.1416
        print(pi*(r*r))

a = areaCirculo()
a.area_circulo()
