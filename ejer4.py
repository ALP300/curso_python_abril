'''
Suma condicional de múltiplos: 
Pide un número N y suma solo los múltiplos de 
3 o 5 hasta N. Muestra la suma y los 
múltiplos encontrados.
'''
N = int(input("Ingresa un número: "))
# Validar opción
opcion = input("¿Quieres múltiplos de 3 o de 5? (3/5): ")
while opcion != "3" and opcion != "5":
    print("Error: debes escribir 3 o 5")
    opcion = input("Intenta de nuevo (3/5): ")
suma = 0
multiplos = []
for i in range(1, N + 1):
    if opcion == "3" and i % 3 == 0:
        suma += i
        multiplos.append(i)
    elif opcion == "5" and i % 5 == 0:
        suma += i
        multiplos.append(i)
print("Múltiplos encontrados:", multiplos)
print("Suma total:", suma)