import discord
import os
import re
import datetime
from dotenv import load_dotenv
from procesador_comandos import procesar_comando_recordar, calcular_uptime, mostrar_ayuda

ruta_script = os.path.dirname(os.path.abspath(__file__))
ruta_env = os.path.join(ruta_script, '.env')
load_dotenv(dotenv_path=ruta_env)

TOKEN = os.getenv('DISCORD_TOKEN')
hora_inicio = datetime.datetime.now()

def mostrar_bienvenida():
    return (
        "📜 Bot de Procesamiento de Comandos (Modo Estructurado):\n"
        "📜 Primeros pasos Agente Discord UX:\n"
        "📜 Escriba !Exit para salir del Agente:\n"
        "📜 Escriba !Inicio para mostrar esta bienvenida nuevamente.\n"
        "📜 Comandos disponibles:\n"
        "!saludo - Muestra un saludo de bot\n"
        "!recordar [nombre] - Recuerda un nombre proporcionado\n"
        "!uptime - Muestra el tiempo de actividad del bot\n"
        "!ayuda - Muestra esta lista de comandos\n"
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
    elif comando == "saludo":
        return "Hola, soy Discordbot, ¿en qué puedo ayudarte?"
    elif comando == "ayuda":
        return "".join(mostrar_ayuda())
    elif comando == "recordar":
        resultado = procesar_comando_recordar(argumento)
        print(f"Resultado: {resultado}")
        return resultado
    elif comando == "uptime":
        resultado = calcular_uptime(hora_inicio)
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