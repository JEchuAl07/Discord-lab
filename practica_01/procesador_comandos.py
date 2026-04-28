import datetime

def obtener_saludo(nombre_bot):
    """
    Retorna un saludo formateado
    """
    print("Hola, soy", nombre_bot, ",¿en qué puedo ayudarte?")

def procesar_comando_recordar(comando):
    """
    Valida y procesa la acción de rocordad un dato
    """
    if not comando:
        return "Error: falra el nombre. Uso !recordar [nombre]"
    
    return f"Entendido, recordaré el nombre: {comando}"
def calcular_uptime(hora_inicio):
    """
    Calcula la diferencia de tiempo entre el inicio y el actual (Mostrar actividad del boot)
    """
    ahora = datetime.datetime.now()
    diferencia = ahora - hora_inicio
    segundos = int(diferencia.total_seconds())
    return f"Tiempo de actividad: {segundos} segundos"

    
def mostrar_ayuda():


def iniciar_agente():


def main():
    obtener_saludo("Discordbot")
    procesar_comando_recordar()
    calcular_uptime()
    mostrar_ayuda()
    iniciar_agente()   

if __name__ == "__main__":
    main()