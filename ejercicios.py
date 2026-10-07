import random
# ==========================================
# EJERCICIO 1
# ==========================================
def buscar_multiplo_rec(actual, fin, paso, mejor=None):
    """
    Recorre recursivamente desde 'actual' hasta 'fin' con el paso indicado.
    paso = 1 si va hacia adelante (busca el máximo múltiplo de 3).
    paso = -1 si va hacia atrás (busca el mínimo múltiplo de 3).
    """
    if actual % 3 == 0:
        if mejor is None:
            mejor = actual
        else:
            if paso == 1:
                mejor = max(mejor, actual)  # Máximo si va hacia adelante
            else:
                mejor = min(mejor, actual)  # Mínimo si va hacia atrás

    if actual == fin:
        return mejor

    return buscar_multiplo_rec(actual + paso, fin, paso, mejor)

def ejercicio_1():
    print("--- EJERCICIO 1 ---")
    inicio = int(input("Ingrese el número de inicio: "))
    fin = int(input("Ingrese el número de fin: "))

    paso = 1 if inicio <= fin else -1
    
    resultado = buscar_multiplo_rec(inicio, fin, paso)
    
    if resultado is None:
        print(f"No hay múltiplos de 3 en el rango [{inicio}, {fin}].")
    else:
        tipo = "máximo" if paso == 1 else "mínimo"
        print(f"El {tipo} múltiplo de 3 encontrado es: {resultado}")


# ==========================================
# EJERCICIO 2
# ==========================================
def generar_lista_rec(n):
    """Genera recursivamente una lista de n números aleatorios entre 10 y 99."""
    if n <= 0:
        return []
    numero_aleatorio = random.randint(10, 99)
    return [numero_aleatorio] + generar_lista_rec(n - 1)

def sumar_multiplos_rec(lista):
    """Calcula recursivamente la suma de los múltiplos de 3 de una lista."""
    if not lista:
        return 0
    cabeza = lista[0]
    resto = lista[1:]
    
    valor = cabeza if cabeza % 3 == 0 else 0
    return valor + sumar_multiplos_rec(resto)

def ejercicio_2():
    print("\n--- EJERCICIO 2 ---")
    n = int(input("Ingrese la cantidad de elementos a generar: "))
    
    lista = generar_lista_rec(n)
    print(f"Lista generada: {lista}")
    
    suma = sumar_multiplos_rec(lista)
    print(f"La suma de los múltiplos de 3 es: {suma}")


# ==========================================
# EJECUCIÓN PRINCIPAL
# ==========================================
if __name__ == "__main__":
    ejercicio_1()
    ejercicio_2()