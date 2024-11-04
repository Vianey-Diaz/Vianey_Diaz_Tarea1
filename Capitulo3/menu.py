import pila
import cola

def menu():
    while True:
        print("\nSeleccione el archivo a procesar:")
        print("1. Pila")
        print("2. Cola")
        print("0. Salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == '1':
            print("\nProcesando pila:")
            pila_obj = pila.crear_pila()
            pila.procesar_pila(pila_obj)
        elif opcion == '2':
            print("\nProcesando cola:")
            cola_obj = cola.crear_cola()
            cola.procesar_cola(cola_obj)
        elif opcion == '0':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú
menu()
