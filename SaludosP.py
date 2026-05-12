CantParticipantes = int(input("Ingrese la cantidad de participantes: "))

nombres = []

for i in range(CantParticipantes):
    nombre = input("Ingrese el nombre del participante: ")
    nombres.append(nombre)

for nombre in nombres:
    print(f"Bienvenido/a, {nombre}")


## 
