#iniciales_sumatoria.py
#Elaboró: Juan Jesús Gómez Sánchez
#GDS0152
#20/20/2020

class inicialesSumatorias:
    def iniciales_sumatorias():
        print("Sumatoria de Valores")
        numero = int(input("¿Cuántos Valores Introducirás? "))

        if numero < 10:
            print("¡¡¡Bueno, Tu Estas P3nd3jo o Que!!!, ¡Deben Ser 10 o Más Valores! Bai :)")
        else:
            suma = 0
            for i in range(1, numero + 1):
                valor = float(input(f"Escriba el Valor {i}: "))
                suma = suma + valor
            print(f"La Suma Total de Todos Los Valores es: {suma}")


    if __name__ == "__main__":
        iniciales_sumatorias()

i = inicialesSumatorias()
i.iniciales_sumatorias
