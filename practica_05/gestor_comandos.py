import datetime

def analizar_comando(entrada):
    
    mensaje = entrada.lower().strip()

    if mensaje.startswith("!"):
        partes = mensaje.split(" ", 1)
        comando = partes[0]
        argumento = partes[1] if len(partes) > 1 else None

        if comando == "!definir":
            return buscar_en_diccionario(argumento)
        elif comando == "!validar":
            return validar_variable(argumento)
        elif comando == "!hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f"La hora actual es: {ahora}"
        elif comando == "!ayuda":
            return ("Comandos disponibles:\n"
                    "!definir [termino] - Busca conceptos de Python\n"
                    "!validar [nombre] - Valida el valor de una variable\n"
                    "!hora - Muestra la hora del sistema\n"
                    "!ayuda - Muestra esta lista de comandos")
        else:
            return "Comando no reconocido. Escribe !ayuda para ver los comandos disponibles."
    
    return "Recuerda que los comandos deben comenzar con '!'. Escribe !ayuda para ver los comandos disponibles."

def buscar_en_diccionario(termino):
    if not termino:
        return "Debes escribir qué término quieres definir. Ej: '!definir list' "
    
    conocimiento= {
        "variable": "Un espacio en memoria para almacenar datos que pueden cambiar durante la ejecución del programa.",
        "lista": "Una colección ordenada y mutable de elementos, que puede contener diferentes tipos de datos.",
        "tupla": "Una colección ordenada e inmutable de elementos, que puede contener diferentes tipos de datos.",
    }
    return conocimiento.get(termino, f"No se encontró una definición para '{termino}'.")

def validar_variable(nombre):
    if not nombre:
        return "Debes escribir el nombre de la variable que quieres validar. Ej: '!validar edad' "
    
    if nombre[0].isdigit():
        return f"'{nombre}' no es un nombre de variable válido. No puede comenzar con un número."
    if " " in nombre:
        return f"'{nombre}' no es un nombre de variable válido. No puede contener espacios."
    if not nombre.isidentifier():
        return f"'{nombre}' no es un nombre de variable válido. Debe ser un identificador válido en Python."
    return f"'{nombre}' es un nombre de variable válido."

if __name__ == "__main__":
    print("--- Agente de Lógica: Fase de Comandos ---")
    print("Prueba comandos como: !validar 123hola o !definir lista\n")
 
    while True:
        user_input = input("Alumno >> ")
        if user_input.lower() in ["salir", "exit"]: break
 
        respuesta = analizar_comando(user_input)
        print(f"Bot >> {respuesta}\n")
