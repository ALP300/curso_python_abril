def ejercicio_numeros_primos():
    inicio = int(input("Ingresa el número inicial: "))
    final = int(input("Ingresa el número final: "))
    print(f"Números primos entre {inicio} y {final}:")

    for n in range(inicio, final + 1):
        if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
            print(n, end=" ")
    print("\n")

ejercicio_numeros_primos()