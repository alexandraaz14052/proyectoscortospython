from http.client import SWITCHING_PROTOCOLS

import os

def convertir(tipo_pesos, valor_dolar):
    cantidad = float(input("Cuantos pesos "+ tipo_pesos+ " tienes?: "))
    cantidad = cantidad / valor_dolar
    cantidad = round(cantidad,2)
    return cantidad

    


print("\n\n\n\n")
os.system("clear")
print("Bienvenido al conversor de monedas 🤑")

print("1. Pesos Mexicanos")
print("2. Pesos Peruanos")
print("3. Pesos Argentino")
respuesta = input("\nQue tipo de pesos tienes? ")
if respuesta == "1":
    print(convertir("Mexicanos", 20.30))
    print()
    
elif respuesta == "2": 
    print(convertir("Peruanos", 3.72))
    print()
elif respuesta == "3":
    print(convertir("Argentinos", 122.91))
    print()
else:
    print("Ingrese una opcion correcta.")
    print()