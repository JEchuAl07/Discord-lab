# --- MÓDULO DE SENSORES (VECTORES 1D) ---
print("--- MÓDULO DE SENSORES (VECTORES) ---")
sensores_distancia = []
total_distancia = 0

for i in range(5):
    while True:
        try:
            dist = float(input(f"Ingrese distancia sensor {i+1}: "))
            sensores_distancia.append(dist)
            total_distancia += dist
            break
        except ValueError:
            print("[ERROR] Ingrese un número válido.")

promedio_prox = total_distancia / len(sensores_distancia)
estado = "Seguro" if promedio_prox >= 2.0 else "Crítico"

print(f"\nPromedio de proximidad: {promedio_prox:.2f}m. Estado: {estado}.")
if promedio_prox < 2.0:
    print("Aviso: Reduciendo velocidad global.")


# --- MÓDULO DE VISIÓN (MATRICES 2D) ---
print("\n--- MÓDULO DE VISIÓN (MATRICES) ---")
print("Llenando matriz de cámara 3x3:")

# Declaramos la matriz 3x3
camara_ia = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
puntos_brillantes = 0

# Lectura de Arreglo (Ciclos anidados)
for fila in range(3):
    for col in range(3):
        while True:
            try:
                brillo = int(input(f"Fila {fila}, Col {col} (Brillo 0-255): "))
                
                # Operación de saturación (Validación)
                if brillo > 255:
                    brillo = 255
                elif brillo < 0:
                    brillo = 0
                
                camara_ia[fila][col] = brillo
                
                # Conteo de píxeles de alta intensidad (> 200)
                if brillo > 200:
                    puntos_brillantes += 1
                break
            except ValueError:
                print("[ERROR] Ingrese un número entero.")

# Escritura de Arreglo (Visualización en tabla)
print("\nVisualización de la imagen capturada:")
for fila in camara_ia:
    # Formateamos con corchetes y espacios para que parezca una matriz real
    print(f"[ {'  '.join(f'{pixel:3}' for pixel in fila)} ]")

# Resultado Final
print("\n--- Resultado de Análisis IA ---")
print(f"Se detectaron {puntos_brillantes} píxeles de alta intensidad.")