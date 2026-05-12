## AGARRANDO LOS DATOS
start = int(input("Ingresa el valor inicial: "))
fin = int(input("Ingresa el valor final: "))
##Creando el contador
contador = 0


## FUNCION PRINCIPAL 
print("Números pares:")
for numero in range(start, fin + 1):
    if numero % 2 == 0:
        print(numero)
        contador += 1
print(f"Se encontraron {contador} números pares en el rango.")