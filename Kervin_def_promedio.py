def promedio():
    suma = 0
    promedio_total = 0
    for i in range(1,6):
        nota = int(input(f"ingrese la nota del alumno {i} numeros: ""\n"))
        suma = suma + nota
    promedio_total = suma / 5
    print( "el promedio de las notas es: ", promedio_total)
    
promedio()