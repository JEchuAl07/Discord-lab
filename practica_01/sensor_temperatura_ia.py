"""
    Función que captura, filtra y analiza las lecturas 
    de temperatura de una GPU.
"""
def procesar_datos_gpu():
   
    print("--- SISTEMA DE FILTRADO DE DATOS (SENSOR GPU) ---")
    
    # 1. Captura de Datos
    temperaturas = []
    for i in range(8):
        lectura = float(input(f"Lectura {i + 1}: "))
        temperaturas.append(lectura)

    # 2. Detección de Valores Atípicos (Outliers)
    contador_errores = 0
    for i in range(8):
        # Condición de ruido: menor a 0 o mayor a 100
        if temperaturas[i] < 0 or temperaturas[i] > 100:
            temperaturas[i] = 35.0
            contador_errores += 1

    # 3. Cálculo de la Media Operativa (Manual)
    suma_total = 0
    for temp in temperaturas:
        suma_total += temp
    
    promedio = suma_total / 8

    # 4. Resultados y Regla de IA
    print(f"\nSe detectaron {contador_errores} lecturas erróneas y fueron corregidas a 35.0.")
    print(f"Datos limpios: {temperaturas}")
    print(f"Promedio de operación: {promedio:.2f}°C")

    if promedio > 75:
        print("ALERTA: Activando sistema de enfriamiento líquido")
    else:
        print("Estado: Operación normal")

def main():
    procesar_datos_gpu()

if __name__ == "__main__":
    main() 