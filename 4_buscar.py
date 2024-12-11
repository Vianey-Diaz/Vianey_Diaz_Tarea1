def buscar_elemento(arreglo, numero):
    if numero in arreglo:
        print(f"El {numero} se encuentraa en el arreglo")
    else:
        print(f"El {numero} NO se encuentra en el arreglo")

arreglo = [1, 2, 3, 4, 5, 6]
numero = int(input("Ingresa el número que deseas buscar: "))
buscar_elemento(arreglo, numero)
