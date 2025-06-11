import random

# Función para la opción 1
def generar_numero_azar(inicio=1, fin=100):
    return random.randint(inicio, fin)

# Función para la opción 2
def ordenarMayorAMenor(listaNum = []):
    print("Se van a pedir 5 números para ordenarlos de menor a mayor.")

    for i in range(5):
        while True:
            try:
                listaNum += [int(input(f"Ingrese el número {i + 1}: "))]
                break
            except ValueError:
                print("[!] Ingrese un número entero.")

    return sorted(listaNum)

# Función para la opción 3
def promedio():
    suma = 0
    promedio_total = 0

    for i in range(1, 6):
        while True:
            try:
                nota = int(input(f"Ingrese la nota del alumno {i} numeros: \n"))
                break
            except ValueError:
                print("Error: Valor ingresado no es flotante")
        suma = suma + nota

    promedio_total = suma / 5
    print("El promedio de las notas es:", promedio_total)
    
while True:
    try:
        print("********---MENU DE FUNCIONES---********")
        print("****1: GENERAR UN NÚMERO AL AZAR")
        print("****2: ORDENAR NUMEROS DE MENOR A MAYOR")
        print("****3: INGRESAR 5 NÚMEROS Y MOSTRAR EL PROMEDIO")
        print("****4: SALIR ")

        while True:
            try:
                opcion=int(input("INGRESE SU OPCIÓN: "))
                if 0 < opcion <= 4:
                    print("Opción válida")
                    break
                else:
                    print("Error: Ingrese una opción dentro del rango 1 a 4")
            except ValueError:
                print("Error: Ingrese sólo números enteros entre 1 y 4")

        if opcion==1:
            if __name__ == "__main__":
                numero = generar_numero_azar()
                print(f"Número generado al azar: {numero}")
        elif opcion==2:
            print(f"Números de menor a mayor: {ordenarMayorAMenor()}")
        elif opcion==3:
            promedio()
        elif opcion==4:
            print("Terminar y salir")
            break
    except ValueError:
        print("Error: Debe ingresar sólo numeros enteros dentro del rango")  
