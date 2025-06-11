import random 

def generar_numero_azar(inicio=1, fin=100):
    return random.randint(inicio, fin)

if __name__ == "__main__":
    numero = generar_numero_azar()
    print(f"Número generado al azar: {numero}")
