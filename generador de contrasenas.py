from random import randint


def generatepass():
    numeros = ["1","2","3","4","5","6","7","8","9"] 
    mayusculas = ["A","B","C","D","E","F","G","H"]
    minusculas = ["a","b","c","d","e","f","g","h"]   
    simbolos = ["/","*","%","@","#","$"]
    conjunto = numeros + mayusculas + minusculas + simbolos
    generatepass = []

    for i in range(10):
        indice = randint(0,len(conjunto))
        indice = conjunto[indice]
        generatepass.append(indice)
        
    generatepass = ''.join(generatepass)
    return generatepass

def run():
    passw = generatepass()
    print("Tu contraseña es " + passw)




    


if __name__ == "__main__":
    run()