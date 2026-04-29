import math
from datetime import date

# --- Módulo de Visualización (Procedimiento) ---
def imprimir_encabezado():
    """Imprime el diseño visual del sistema. No retorna valores."""
    hoy = date.today()
    print("=" * 40)
    print(f"{'SISTEMA DE SALUD INTELIGENTE':^40}")
    print(f"{str(hoy):^40}")
    print("=" * 40)

# --- Módulo de Cálculo de IMC (Función) ---
def calcular_imc(peso, estatura):
    """Calcula el IMC y devuelve el valor decimal."""
    return peso / (estatura ** 2)

# --- Módulo de Análisis de Presión (Función) ---
def evaluar_presion(presion_sistolica):
    """Evalúa la presión y devuelve una etiqueta de estado."""
    if presion_sistolica > 140:
        return "Alta"
    else:
        return "Normal"

# --- Lógica Principal ---
if __name__ == "__main__":
    # 1. Mostrar encabezado
    imprimir_encabezado()

    # 2. Captura de datos
    nombre = input("Nombre del Paciente: ")
    try:
        peso = float(input("Peso (kg): "))
        estatura = float(input("Estatura (m): "))
        presion = int(input("Presión Sistólica: "))

        # 3. Llamada a funciones y almacenamiento en variables
        resultado_imc = calcular_imc(peso, estatura)
        estado_presion = evaluar_presion(presion)

        # 4. Salida de resultados
        # Usamos math.ceil para redondear hacia arriba como solicita la práctica
        imc_redondeado = math.ceil(resultado_imc)

        print("\n--- RESULTADOS DEL ANÁLISIS ---")
        print(f"Paciente: {nombre}")
        print(f"IMC Calculado: {imc_redondeado}")
        print(f"Estado de Presión: {estado_presion}")
        print("-" * 31)

    except ValueError:
        print("\n[ERROR] Por favor, ingrese valores numéricos válidos para peso, estatura y presión.")import math
from datetime import date

# --- Módulo de Visualización (Procedimiento) ---
def imprimir_encabezado():
    """Imprime el diseño visual del sistema. No retorna valores."""
    hoy = date.today()
    print("=" * 40)
    print(f"{'SISTEMA DE SALUD INTELIGENTE':^40}")
    print(f"{str(hoy):^40}")
    print("=" * 40)

# --- Módulo de Cálculo de IMC (Función) ---
def calcular_imc(peso, estatura):
    """Calcula el IMC y devuelve el valor decimal."""
    return peso / (estatura ** 2)

# --- Módulo de Análisis de Presión (Función) ---
def evaluar_presion(presion_sistolica):
    """Evalúa la presión y devuelve una etiqueta de estado."""
    if presion_sistolica > 140:
        return "Alta"
    else:
        return "Normal"

# --- Lógica Principal ---
if __name__ == "__main__":
    # 1. Mostrar encabezado
    imprimir_encabezado()

    # 2. Captura de datos
    nombre = input("Nombre del Paciente: ")
    try:
        peso = float(input("Peso (kg): "))
        estatura = float(input("Estatura (m): "))
        presion = int(input("Presión Sistólica: "))

        # 3. Llamada a funciones y almacenamiento en variables
        resultado_imc = calcular_imc(peso, estatura)
        estado_presion = evaluar_presion(presion)

        # 4. Salida de resultados
        # Usamos math.ceil para redondear hacia arriba como solicita la práctica
        imc_redondeado = math.ceil(resultado_imc)

        print("\n--- RESULTADOS DEL ANÁLISIS ---")
        print(f"Paciente: {nombre}")
        print(f"IMC Calculado: {imc_redondeado}")
        print(f"Estado de Presión: {estado_presion}")
        print("-" * 31)

    except ValueError:
        print("\n[ERROR] Por favor, ingrese valores numéricos válidos para peso, estatura y presión.")