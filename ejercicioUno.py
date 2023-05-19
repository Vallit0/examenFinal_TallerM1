# Random 
import random
# Main 
def main():

    # Conjunto
    A = ["a","b","c","d","e","f","g","h","i","j"]
    palabras = []
    palabra = ""
    # palabra que se debe crear de 6 elementos
    counter = 0
    contadorGeneral = 0

    while (counter <= 5):
        for i in range(6):
            palabra += A[random.randint(0,6)]
        if palabra not in palabras:
            palabras.append(palabra)
            print(palabra)
            contadorGeneral += 1
            palabra = ""
        else:
            palabra = ""
            counter += 1
    
    print(contadorGeneral)
            
if __name__ == '__main__':
    main()
    

    
