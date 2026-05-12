def monitorear_servidor():
    print("--- TELEMETRÍA DE CLUSTER IA ---")
    
    try:
        # 1. Captura de Telemetría
        temp = float(input("Temperatura actual (°C): "))
        vram = int(input("Uso de Memoria VRAM (%): "))
        enfriamiento = input("¿Enfriamiento activo? (si/no): ").lower().strip()

        # 2. Gestión de Errores (Rango de memoria)
        if vram < 0 or vram > 100:
            print("Error: Lectura de memoria fuera de rango (0-100%).")
            return

        print("\n> Diagnóstico: ", end="")

        # 3. Lógica de Diagnóstico (Estructuras de Control)
        
        # Condición CRÍTICA
        if temp > 90 or vram == 100:
            print("¡ALERTA CRÍTICA! Apagando servidores para evitar daños físicos.")
        
        # Condición de PRECAUCIÓN
        elif 75 <= temp <= 90:
            if enfriamiento == "no":
                print("Peligro: Temperatura alta y enfriamiento desactivado. Pausando entrenamiento.")
            else:
                print("Temperatura elevada. Reduciendo velocidad de procesamiento (Throttling).")
        
        # Estado ÓPTIMO
        elif temp < 75 and vram < 80:
            print("Sistema Estable: Entrenamiento en curso a máxima capacidad.")
            
            # Reto Adicional: Memoria libre
            vram_libre = 100 - vram
            print(f"INFO: Tienes un {vram_libre}% de VRAM disponible para otros procesos.")
        
        # Caso por defecto (Ej: Memoria alta pero temperatura baja)
        else:
            print("Estado preventivo: Carga de memoria alta, pero temperatura estable.")

    except ValueError:
        print("Error: Por favor, ingresa valores numéricos válidos para temperatura y memoria.")

if __name__ == "__main__":
    monitorear_servidor()