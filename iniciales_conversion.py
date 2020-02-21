#Conversion de grados
#Elaboró: Juan Jesús Gómez Sánchez
#GDS0152
#20/20/2020

class inicialesConversion:
    def conversion_grados(self):
        c = int(input("Ingresa La Temperatura En Grados Celsius: "))
        f = 9.0/5.0 * c + 32
        print("{}°C Es Equivalente A {}°F".format(c, f))

        f = int(input("Ingresa La Temperatura En Grados Fahrenheit: "))
        c = (f - 32) * 5.0/9.0
        print("{}°F Es Equivalente A {}°C".format(f, c))

fa = inicialesConversion()
fa.conversion_grados()
