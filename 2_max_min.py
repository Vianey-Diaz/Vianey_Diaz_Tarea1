numeros=[2, 6, 7, 9, 21, 3, 1]

maximo= numeros[0]
minimo= numeros[0]

for num in numeros:
    if num > maximo:
        maximo=num

    if num < minimo:
        minimo = num

print(f"El valor maximo es: {maximo}")
print(f"El valor minimo es: {minimo}")

