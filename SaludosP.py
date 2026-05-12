CantParticipantes = int(input("Ingrese la cantidad de participantes: "))
nombres = []

## Guardar Nombres ##
for i in range(CantParticipantes):
    nombre = input("Ingrese el nombre del participante: ")
    nombres.append(nombre)

## Saludar participantes ##
contador = 1
for nombre in nombres:
    print(f"Bienvenido/a numero {contador}, {nombre}")
    contador += 1

## Mensaje final
print(f"Capacitacion inicializada. Total de participantes saludados: {CantParticipantes}")



## 
