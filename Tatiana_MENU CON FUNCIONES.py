while True:
    try:
        print("********---MENU DE FUNCIONES---********")
        print("****1: GENERAR UN NÚMERO AL AZAR")
        print("****2: ORDENAR NUMEROS DE MENOR A MAYOR")
        print("****3: INGRESAR 5 NÚMEROS Y MOSTRAR EL PROMEDIO")
        print("****4: SALIR ")

        while True :
            try:
                opcion=int(input("INGRESE SU OPCION: "))
                if 0 < opcion <= 4 :
                    print("Opción válida")
                    break
                else:
                    print("Ingrese una opción dentro del rango 1 a 4")
            except ValueError:
                print("Ingrese sólo Numeros enteros entre 1 y 4")

        if opcion==1:
            pass
        elif opcion==2:
            pass
        elif opcion==3:
            pass
        elif opcion==4:
            print("Terminar y salir")
            break
        else:
            print("Debe ingresar sólo numeros enteros dentro del rango")
    except ValueError:
        print("Debe ingresar sólo numeros enteros dentro del rango")  


           