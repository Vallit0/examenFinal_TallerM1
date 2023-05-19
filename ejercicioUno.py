# importaciones
import random 

# Conjunto al que le deseamos crear multi-subconjuntos
A = ["a","b","c","d","e","f","g","h","i","j"]
palabras = []
palabra = ""
# palabra que se debe crear de 6 elementos

#contador que nos permitirá abrir o cerrar el ciclo dependiendo de la cantidad de iteraciones 
# sin cambio
counter = 0

while (counter != 5):
    for i in range(6):
        palabra += A[random.randint(1,6)]
    if palabra not in palabras:
        palabras.append(palabra)
        palabra = ""
    else:
        palabra = ""
        counter += 1
