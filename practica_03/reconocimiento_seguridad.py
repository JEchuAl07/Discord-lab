def ejecutar_escaneo():
    # 1. Configuración del Patrón Maestro (Base de Datos)
    patron_maestro = [1, 0, 1, 1, 0]
    lectura_sensor = []
    
    print("--- ESCÁNER BIOMÉTRICO DE IA ---")
    
    # 2. Captura de Datos del Sensor
    for i in range(5):
        while True:
            try:
                bit = int(input(f"Ingrese bit {i+1} (0 o 1): "))
                if bit == 0 or bit == 1:
                    lectura_sensor.append(bit)
                    break
                else:
                    print("Error: Solo se permite 0 o 1.")
            except ValueError:
                print("Error: Ingrese un valor numérico.")

    # 3. Capa de Análisis (Procesamiento de IA)
    coincidencias = 0
    for i in range(5):
        if lectura_sensor[i] == patron_maestro[i]:
            coincidencias += 1
    
    # Cálculo del Nivel de Similitud
    similitud = (coincidencias / 5) * 100
    
    # 4. Toma de Decisiones (Salida)
    print("\n> Comparando lectura con base de datos...")
    print(f"> Coincidencias encontradas: {coincidencias}")
    print(f"> Porcentaje de Similitud: {similitud}%")
    
    if similitud == 100:
        print("ESTADO: ACCESO TOTAL: Identidad Verificada.")
    elif similitud >= 60:
        print("ESTADO: ADVERTENCIA: Similitud parcial. Se requiere verificación manual.")
    else:
        print("ESTADO: ALERTA: Intruso detectado. Sistema bloqueado.")
    
    # Reto Adicional: Visualización de vectores
    print("-" * 30)
    print(f"Patrón Maestro: {patron_maestro}")
    print(f"Lectura Sensor: {lectura_sensor}")

if __name__ == "__main__":
    ejecutar_escaneo()