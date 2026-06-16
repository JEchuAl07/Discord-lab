import discord
import os
import re
from dotenv import load_dotenv
from tareas_agente import agregar_tarea, listar_tareas, eliminar_tarea

ruta_script = os.path.dirname(os.path.abspath(__file__))
ruta_env = os.path.join(ruta_script, '.env')
load_dotenv(dotenv_path=ruta_env)

TOKEN = os.getenv('DISCORD_TOKEN')
tareas = []

def mostrar_bienvenida():
    return (
        "📜 Bot de Gestión de Tareas (Modo Estructurado):\n"
        "📜 Primeros pasos Agente Discord UX:\n"
        "📜 Escriba !Exit para salir del Agente:\n"
        "📜 Escriba !Inicio para mostrar esta bienvenida nuevamente.\n"
        "📜 Comandos disponibles:\n"
        "!add [texto] - Agrega una nueva tarea a la lista\n"
        "!list - Muestra todas las tareas pendientes\n"
        "!del [número] - Elimina una tarea por su índice\n"
    )

def main(entrada):
    PREFIJO = "!"
    if not entrada.startswith(PREFIJO):
        if entrada: 
            print("Recuerda usar '!' para comandos.")
            return "Recuerda usar '!' para comandos."

    cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
    comando = cuerpo[0].lower()
    argumento = cuerpo[1] if len(cuerpo) > 1 else ""

    if comando == "exit":
        print("Saliendo del gestor...")
        return "Saliendo del gestor..."
    elif comando == "inicio":
        print(mostrar_bienvenida())
        return mostrar_bienvenida()
    elif comando == "add":
        resultado = agregar_tarea(tareas, argumento)
        print(f"Resultado: {resultado}")
        return resultado
    elif comando == "list":
        resultado = listar_tareas(tareas)
        print(f"Resultado: {resultado}")
        return resultado
    elif comando == "del":
        resultado = eliminar_tarea(tareas, argumento)
        print(f"Resultado: {resultado}")
        return resultado
    else:
        print(f" Error: Comando '!{comando}' no reconocido.")
        return f" Error: Comando '!{comando}' no reconocido."

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Sincronizado como {client.user} (ID: {client.user.id})')
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f"Mensaje recibido de {message.author}: {message.content}")

    if message.content.startswith('!'):
        resultado = main(message.content)
        print(f"Resultado del procesamiento: {resultado}")
        await message.channel.send(f"**Bot Procesador:**\n{resultado}")

if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)
    else:
        print(f"ERROR: No se encontró el TOKEN. Ruta buscada: {ruta_env}")