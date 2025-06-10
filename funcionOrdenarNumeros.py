listaNumeros = []

def ordenarMayorAMenor(listaNum):
    listaNum = sorted(listaNum)
    return listaNum[::-1]

for i in range(5):
    while True:
        try:
            numero = int(input("Ingrese un número: "))
        except ValueError:
            print("[! Ingrese un número entero.")
            continue

        listaNumeros += [numero] # append
        break

print(f"Números de mayor a menor: {ordenarMayorAMenor(listaNumeros)}")