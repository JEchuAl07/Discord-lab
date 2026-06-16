import discord
import datetime
from procesador_comandos import mostrar_ayuda, procesar_comando_recordar, calcular_uptime, mostrar_ayuda

def bienvenida():
    return "¡Bienvenido al agente procesador de comandos! Usa !saludo, !ayuda, !recordar [nombre] o !uptime para interactuar."

def main():
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

            if comando == "saludo":
                respuesta = f"¡Hola, {message.author.name}! Soy tu bot de Discord."
            elif comando == "ayuda":
                respuesta = mostrar_ayuda()
            elif comando == "recordar":
                respuesta = procesar_comando_recordar(argumento)
            elif comando == "uptime":
                respuesta = calcular_uptime(bot.start_time)
            else:
                respuesta = "Comando no reconocido. Escribe !ayuda para ver los comandos disponibles."

            await message.channel.send(respuesta)

TOKEN = ""

if __name__ == "__main__":
    main()