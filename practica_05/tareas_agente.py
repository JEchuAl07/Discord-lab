import datetime
def agregar_tarea(lista_tareas, descripcion):
    """
    Agregar una tarea si cumple con los requisitos
    """

    if len(descripcion) < 3:
        return "La descripción es demasiado corta. Debe tener al menos 3 caracteres."
    
    if len(lista_tareas) >= 5:
        return "No puedes agregar más de 5 tareas. Elimina una tarea antes de agregar otra."
    
    #Crear formato para tarea
    fecha = datetime.datetime.now().strftime("%H:%M")
    nueva_tarea = f"{descripcion} - {fecha}"
    lista_tareas.append(nueva_tarea)
    return "Tarea agregada con éxito"

def listar_tareas(lista_tareas):
    """
    Formatea la vista de tareas para su visualización
    """
    if not lista_tareas:
        return "No hay tareas en la lista."
    
    #Agregar una variable llamada resultado

    resultado = "Listado de tareas:\n"
    #Iterar la lista de tareas y formatear la salida
    for i, tarea in enumerate(lista_tareas, start=1):
        resultado += f"{i}. {tarea}\n"
    return resultado

def eliminar_tarea(lista_tareas, indice):
    """
    Elimina una tarea de la lista según su índice
    """
    if not indice.isdigit():
        return "Índice inválido. Por favor, ingresa un número válido."
    
    indice = int(indice)-1

    #Agregamos la logica para preguntar si el elemento está en la lista

    if indice < 1 or indice > len(lista_tareas):
        return "Índice inválido. Por favor, ingresa un número válido."
    elif 0 <= indice < len(lista_tareas):
        tarea_eliminada = lista_tareas.pop(indice)
        return f"Tarea '{tarea_eliminada}' eliminada con éxito."
    
def main():
    tareas = []
    print("Bienvenido al gestor de taeras")
    activa = True
    while activa:
        entrada = input(">>> ").strip()
        if not entrada.startswith("!"):
            print("Recuerda que los comandos deben comenzar con '!'.")
            continue
        cuerpo= entrada[1:].split(" ", 1)
        comando = cuerpo[0].lower
        argumento = cuerpo[1] if len(cuerpo) > 1 else ""

        if commando == "add":
            resultado = agregar_tarea(tareas, argumento)
            print(resultado)