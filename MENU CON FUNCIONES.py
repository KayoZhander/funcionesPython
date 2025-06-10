while True:
    try:

        print("********---MENU DE FUNCIONES---********")
        print("****1: GENERAR UN NÚMERO AL AZAR")
        print("****2: ORDENAR NUMEROS DE MENOR A MAYOR")
        print("****3: INGRESAR 5 NÚMEROS Y MOSTRAR EL PROMEDIO")
        print("****4: SALIR ")

        while True :
            try:
                opcion=int(input(" INGRESE SU OPCION :  "))
                if 0 < opcion <= 4 :
                    print(" Opcin válida ")
                    break
                else:
                    print(" Ingrese una opción dentro del rango 1 a 3")
            except ValueError:
                print(" Ingrese sólo Numeros enteros entre 1 y 3")

        if opcion==1 :



        elif opcion==2 :


        elif opcion==3 :


        else opcion==4:
            print("terminar y salir")
            break
    except ValueError:
        print("Debe ingresar sólo numeros enteros dentro del rango")  


           