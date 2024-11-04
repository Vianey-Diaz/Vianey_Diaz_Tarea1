# ArrayClient.py

# Importar la clase Array
from Array import Array, OrderedRecordArray # type: ignore

# Crear instancias de la clase Array con diferentes tipos de datos
arr1 = Array(10)
arr2 = Array(10)
arr3 = Array(10)

# Insertar elementos en los arreglos
arr1.insert(1)
arr1.insert(2)
arr1.insert(3)
arr1.insert(10)
arr1.insert(20)
arr1.insert(5)
arr1.insert(3)


arr2.insert("a")
arr2.insert(0)
arr2.insert(5.5)
arr2.insert("b")
arr2.insert("c")
arr2.insert("d")
arr2.insert(0)
arr2.insert(7)

arr3.insert("a")
arr3.insert("b")
arr3.insert("c")
arr3.insert("d")
arr3.insert("e")
arr3.insert("f")
arr3.insert("g")
# Ejercicio 1 getmaxnun
print("Ejercicio 1 getmaxnun")
# Probar el método getMaxNum en diferentes arreglos
print("Máximo número en arr1:", arr1.getMaxNum())  # Debería devolver 3
print("Máximo número en arr2:", arr2.getMaxNum())  # Debería devolver 5.5
print("Máximo número en arr3:", arr3.getMaxNum())  # Debería devolver None

# Insertar ceros y probar de nuevo
arr1.insert(0)
print("Máximo número en arr1 después de insertar 0:", arr1.getMaxNum())  # Debería seguir devolviendo 3

# Insertar números negativos y probar de nuevo
arr2.insert(-2)
print("Máximo número en arr2 después de insertar -2:", arr2.getMaxNum())  # Debería seguir devolviendo 5.5

# Ejercicio 2 deletmaxnum
print("Ejercicio 2 deletmaxnum")
# Probar el metodo deleteMaxNum
print("Array 1:")
print("Max number:", arr1.deleteMaxNum())  # Debería imprimir 20 y eliminarlo del arreglo
arr1.traverse()  # Debería imprimir 1, 2, 3, 10, 5

print("\nArray 2:")
print("Max number:", arr2.deleteMaxNum())  # Debería imprimir 0 y eliminarlo del arreglo
arr2.traverse()  # Debería imprimir "a", 0, 5.5, "b", "c", "d", 0, -2

print("\nArray 3:")
print("Max number:", arr3.deleteMaxNum())  # Debería imprimir None ya que no hay números
arr3.traverse()  # Debería imprimir "a", "b", "c", "d", "e", "f", "g"

# Ejercicio 3 ordenar el arreglo 
print("Ejercicio 3 ordenar el arreglo ")
def sortArrayDescending(arr):
    sorted_arr = Array(arr.get_nItems())  # Utiliza el método público para obtener el tamaño
    while len(arr) > 0:
        max_num = arr.deleteMaxNum()
        if max_num is not None:
            sorted_arr.insert(max_num)
    return sorted_arr

if __name__ == "__main__":


    print("Contenido original del arreglo:")
    arr1.traverse()

    sorted_arr = sortArrayDescending(arr1)

    print("Contenido del arreglo ordenado:")
    sorted_arr.traverse()

# Ejercicio 4 eliminar datos duplicados 
print("Ejercicio 4 eliminar datos duplicados")
if __name__ == "__main__":
    arr5 = Array(10)
    arr5.insert(5)
    arr5.insert(3.5)
    arr5.insert(5)
    arr5.insert(10)
    arr5.insert(0)
    arr5.insert(3.5)
    arr5.insert(7)

    print("Contenido original del arreglo:")
    arr5.traverse()

    arr5.removeDupes()

    print("Contenido del arreglo despues de eliminar los duplicados:")
    arr5.traverse()

# Ejercicio 5 fusionar dos arreglos 
print("Ejercicio 5 fusionar dos arreglos ")

if __name__ == "__main__":
    arr1 = OrderedRecordArray(10)
    arr1.insert(1)
    arr1.insert(3)
    arr1.insert(5)
    arr1.insert(7)

    arr2 = OrderedRecordArray(10)
    arr2.insert(2)
    arr2.insert(4)
    arr2.insert(6)
    arr2.insert(8)

    print("Array 1 contenido:")
    arr1.traverse()

    print("Array 2 contenido:")
    arr2.traverse()

    arr1.merge(arr2)

    print("Contenido del arreglo 1 despues de la fusion con el arreglo 2:")
    arr1.traverse()

    # Ejercicio 6 eliminar elemento dada una llave 
print("Ejercicio 6 eliminar elemento dada una llave ")
if __name__ == "__main__":
    arr6 = OrderedRecordArray(10)
    arr6.insert(1)
    arr6.insert(3)
    arr6.insert(3)
    arr6.insert(5)
    arr6.insert(7)
    arr6.insert(3)

    print("Contenido original del arreglo:")
    arr6.traverse()

    arr6.delete(3)

    print("Contenido del arreglo despues de eliminar la llave 3:")
    arr6.traverse()

# Ejercicio 7
# Prueba de la clase con ambas estrategias de expansión
print("Ejercicio 7 usando estrategias para el incremento de datos en un arreglo lleno")

def test_ordered_record_array():
    print("Prueba con incremento fijo:")
    array_fixed = OrderedRecordArray(5, resize_strategy='fixed', increment=5)
    for i in range(20):
        array_fixed.insert(i)
        print(f"Array después de insertar {i}: {array_fixed._a}")

    print("\nPrueba con multiplicación:")
    array_multiple = OrderedRecordArray(5, resize_strategy='multiple', multiple=2)
    for i in range(20):
        array_multiple.insert(i)
        print(f"Array después de insertar {i}: {array_multiple._a}")

test_ordered_record_array()

# Ejercicio extra
print ("Ejercicio extra, sacar el promedio de los datos de un arreglo") 

if __name__ == "__main__": 
    arr7 = Array(10)
    arr7.insert(1)
    arr7.insert(4)
    arr7.insert(7)
    arr7.insert(5)
    arr7.insert(6)
    arr7.insert(78)
    arr7.insert(34)
    arr7.insert(0)
    arr7.insert(23)
    arr7.insert(12)

    print("El arreglo original es:")
    arr7.traverse()

    promedio = arr7.calcular_promedio()
    print(f"El promedio de los números en el arreglo es: {promedio}")

if __name__ == "__main__":
    arr8 = Array(10)
    arr8.insert(1)
    arr8.insert(4)
    arr8.insert(7)
    arr8.insert(5)
    arr8.insert(6)
    arr8.insert(73)
    arr8.insert(34)
    arr8.insert(7)
    arr8.insert(23)
    arr8.insert(12)

    # Contar números pares
    numerosPares = arr8.cuenta(0)
    print(f"La cantidad de números pares es: {numerosPares}")

    # Contar números impares
    numerosImpares = arr8.cuenta(1)
    print(f"La cantidad de números impares es: {numerosImpares}")


