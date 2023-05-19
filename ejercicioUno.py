# Random
import random


# Main
def main():
    # Conjunto
    A = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    palabras = []
    palabra = ""
    # palabra que se debe crear de 6 elementos
    comparacionesRepetidas = 0
    contadorGeneral = 0

    while (comparacionesRepetidas <= 20000):
        
        #Generamos una palabra al azar
        for i in range(6):
            palabra += A[random.randint(0, 6)]
        
        # Si la palabra no fue generada antes entonces la añadimos
        if palabra not in palabras:
            palabras.append(palabra)
            print(palabra)
            # Puesto que añadimos una nueva palabra, la contamos
            contadorGeneral += 1
            
            #Reset palabra
            palabra = ""
        else:
            palabra = ""
            comparacionesRepetidas += 1
    print("--- Iteraciones Terminadas -----")
    print(contadorGeneral)


if __name__ == '__main__':
    main()


