import discord
import datetime
from discord.ext import commands
from procesador_comandos import procesar_comando_recordar, calcular_uptime, mostrar_ayuda

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
hora_inicio = datetime.datetime.now()

@bot.event
async def on_ready():
    print(f"--- Agente Procesador de Comandos Online ---")
    print(f"Conectado como: {bot.user.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!"):
        entrada = message.content.strip()
        partes = entrada[1:].split(maxsplit=1)
        comando = partes[0].lower()
        argumento = partes[1] if len(partes) > 1 else ""

        if comando == "saludo":
            await message.channel.send(f"Hola, soy {bot.user.name}, ¿en qué puedo ayudarte?")
        elif comando == "ayuda":
            lista_ayuda = "".join(mostrar_ayuda())
            await message.channel.send(lista_ayuda)
        elif comando == "recordar":
            respuesta = procesar_comando_recordar(argumento)
            await message.channel.send(respuesta)
        elif comando == "uptime":
            respuesta = calcular_uptime(hora_inicio)
            await message.channel.send(respuesta)

    await bot.process_commands(message)

TOKEN = "TU_TOKEN_DE_DISCORD_AQUI"

if __name__ == "__main__":
    bot.run(TOKEN)