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
    return f"Tarea agregada con éxito"

