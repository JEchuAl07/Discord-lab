import discord
from tareas_agente import agregar_tarea, listar_tareas, eliminar_tarea

def bienvenida():
    return "¡Bienvenido al gestor de tareas! Usa !agregar, !listar o !eliminar para gestionar tus tareas."

def main():
    bienvenida()
    intents = discord.Intents.default()
    intents.message_content = True
    bot = discord.Client(intents=intents)

    @bot.event
    async def on_ready():
        print(f'Bot conectado como {bot.user}')

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        if message.content.startswith('!'):
            comando = message.content[1:].split()[0].lower()
            argumento = ' '.join(message.content.split()[1:])

            if comando == "agregar":
                respuesta = agregar_tarea(tareas, argumento)
            elif comando == "listar":
                respuesta = listar_tareas(tareas)
            elif comando == "eliminar":
                respuesta = eliminar_tarea(tareas, argumento)
            else:
                respuesta = "Comando no reconocido. Usa !agregar, !listar o !eliminar."

            await message.channel.send(respuesta)

TOKEN = "MTUxNjQzODk4NjEyODg4MzcyMg.GCCyfU.wVDjxpYrn37D3-Pm5QvH-I6huiu9hNt6WnsUjA"

if __name__ == "__main__":
    tareas = []
    main()