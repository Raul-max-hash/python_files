#Algoritmo burbuja

lista = [2, 4, 6, 8, 10, 12, 23, 45, 67]

print("Si - S o No - N
option = input("Deseas agregar un numero?: ")

while option.lower() == "s":
    n = int(input("Escribe un numero: "))
    if n > 0:
        lista.append(n)
    else:
        print("Error escribe un numero mayor que 0")

    option = input("Desea agregar un numero?: ")
    if option.lower() == "n":
        print("Ok...")
        break

#Estructura del algoritmo burbuja
for i in range(1, len(lista)):
    print(f"Pasada: {i}")
    for j in range(0, len(lista) - i):
        print(f"Comparacion de lista {j} y lista {j+1}")
        if lista[j] > lista[j+1]:
            elemento = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = elemento
            print("Se intercambian")
        print(f"Estado actual de la lista: {lista}")

print(lista)
