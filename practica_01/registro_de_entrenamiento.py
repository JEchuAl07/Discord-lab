class MonitorEntrenamiento:
    def __init__(self, umbral_convergencia=0.01):
        self.historial_errores = []
        self.umbral_convergencia = umbral_convergencia

    def registrar_epoca(self, valor_error):
        # Lógica de validación para números negativos
        if valor_error < 0:
            raise ValueError("El error no puede ser un valor negativo.")
        
        self.historial_errores.append(valor_error)
        print("> Registro exitoso.")
        
        # Verificación de convergencia
        if valor_error < self.umbral_convergencia:
            print(f"[SISTEMA] Entrenamiento completado: Se alcanzó el objetivo de precisión (Error: {valor_error}).")
            return True # Opcional: para detener el ciclo externamente
        return False

# --- Flujo Principal ---
monitor = MonitorEntrenamiento(umbral_convergencia=0.01)

print("--- Iniciando Monitor de Red Neuronal ---")

epocas_a_registrar = 5
contador = 1

while contador <= epocas_a_registrar:
    try:
        entrada = input(f"Ingrese el error de la Época {contador}: ")
        valor = float(entrada)
        
        # Registrar y verificar si hubo éxito
        monitor.registrar_epoca(valor)
        contador += 1
        
    except ValueError as e:
        # Captura tanto letras (de float()) como el error negativo (lanzado manualmente)
        if "negativo" in str(e):
            print(f"> [ERROR] {e}")
        else:
            print("> [ERROR] Entrada inválida. Por favor, ingrese un número decimal.")

# --- Análisis de Datos Final ---
print("\n--- Resumen de Entrenamiento ---")
if monitor.historial_errores:
    historial = monitor.historial_errores
    promedio = sum(historial) / len(historial)
    mejor_error = min(historial)

    print(f"Historial: {historial}")
    print(f"Promedio de Error: {promedio:.4f}")
    print(f"Mejor resultado obtenido: {mejor_error}")
else:
    print("No se registraron datos válidos.")