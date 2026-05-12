def capturar_sentimientos():
    """Simula la entrada de datos y llena el vector."""
    puntajes = [0, 0, 0]
    print("--- ANALIZADOR DE SENTIMIENTOS IA ---")
    for i in range(5):
        try:
            opcion = int(input(f"Palabra {i+1} - Clasificación (0, 1, 2): "))
            if 0 <= opcion <= 2:
                puntajes[opcion] += 1
            else:
                print("Error: Elige 0, 1 o 2.")
        except ValueError:
            print("Error: Ingresa un número válido.")
    return puntajes

def encontrar_maximo_manual(vector):
    """Encuentra el índice con el valor más alto sin usar max()."""
    max_valor = vector[0]
    indice_max = 0
    
    for i in range(1, len(vector)):
        if vector[i] > max_valor:
            max_valor = vector[i]
            indice_max = i
    return indice_max

def mostrar_resultado(vector, indice):
    """Muestra el estado del vector y la decisión final."""
    categorias = ["Positiva", "Neutral", "Negativa"]
    
    print(f"\nEstado final del vector de características: {vector}")
    print(f"Resultado de IA: La frase es {categorias[indice]} (Predominancia en índice {indice})")

# --- FLUJO PRINCIPAL ---
if __name__ == "__main__":
    # 1. Obtener los datos
    datos = capturar_sentimientos()
    
    # 2. Procesar la información
    ganador = encontrar_maximo_manual(datos)
    
    # 3. Presentar resultados
    mostrar_resultado(datos, ganador)