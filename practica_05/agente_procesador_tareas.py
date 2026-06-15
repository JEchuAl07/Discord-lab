import discord
from discord.ext import commands
from tareas_agente import agregar_tarea, listar_tareas, eliminar_tarea

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
tareas = []

@bot.event
async def on_ready():
    print(f"--- Agente Procesador de Tareas Online ---")
    print(f"Conectado como: {bot.user.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!"):
        entrada = message.content.strip()
        cuerpo = entrada[1:].split(" ", 1)
        comando = cuerpo[0].lower()
        argumento = cuerpo[1] if len(cuerpo) > 1 else ""

        if comando == "add":
            respuesta = agregar_tarea(tareas, argumento)
            await message.channel.send(respuesta)
        elif comando == "list":
            respuesta = listar_tareas(tareas)
            await message.channel.send(respuesta)
        elif comando == "remove":
            respuesta = eliminar_tarea(tareas, argumento)
            await message.channel.send(respuesta)

    await bot.process_commands(message)

TOKEN = "TU_TOKEN_DE_DISCORD_AQUI"

if __name__ == "__main__":
    bot.run(TOKEN)