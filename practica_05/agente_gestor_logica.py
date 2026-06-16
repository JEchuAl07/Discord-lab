import discord
import os
import re
from dotenv import load_dotenv
from agente_logica import analizar_comando, buscar_en_diccionario, validar_variable, historial_comandos, ejecutar_suma, ejecutar_multiplicacion, obtener_fecha_completa

def mostrar_bienvenida():
    return (
        "📜 Bot de Operaciones y Lógica V2 (Modo Estructurado):\n"
        "📜 Primeros pasos Agente Discord UX:\n"
        "📜 Escriba !Exit para salir del Agente:\n"
        "📜 Escriba !Inicio para mostrar esta bienvenida nuevamente.\n"
        "📜 Comandos disponibles:\n"
        "!definir [termino] - Busca conceptos de Python\n"
        "!validar [nombre] - Valida el nombre de una variable\n"
        "!sumar [n1] [n2] - Suma dos números enteros o decimales\n"
        "!multiplicar [n1] [n2] - Multiplica dos números\n"
        "!hora - Muestra la hora del sistema\n"
        "!fecha - Muestra la fecha y hora completa\n"
        "!historial - Muestra los últimos 5 comandos usados\n"
    )

def main(entrada):
    PREFIJO = "!"
    if not entrada.startswith(PREFIJO):
        if entrada: 
            print("Recuerda usar '!' para comandos.")
            return "Recuerda usar '!' para comandos."

    cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
    comando = cuerpo[0].lower()

    if comando == "exit":
        print("Saliendo del gestor...")
        return "Saliendo del gestor..."
    elif comando == "inicio":
        print(mostrar_bienvenida())
        return mostrar_bienvenida()
    elif comando in ["definir", "validar", "hora", "historial", "sumar", "fecha", "multiplicar", "ayuda"]:
        resultado = analizar_comando(entrada)
        print(f"Resultado: {resultado}")
        return resultado
    else:
        resultado = analizar_comando(entrada)
        print(f"Resultado: {resultado}")
        return resultado

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

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
import discord
import os
import re
from dotenv import load_dotenv
from agente_logica import (
    analizar_comando, buscar_en_diccionario, validar_variable, 
    historial_comandos, ejecutar_suma, ejecutar_multiplicacion, obtener_fecha_completa
)

ruta_script = os.path.dirname(os.path.abspath(__file__))
ruta_env = os.path.join(ruta_script, '.env')
load_dotenv(dotenv_path=ruta_env)

TOKEN = os.getenv('DISCORD_TOKEN')

def mostrar_bienvenida():
    return (
        "📜 Bot de Operaciones y Lógica V2 (Modo Estructurado):\n"
        "📜 Primeros pasos Agente Discord UX:\n"
        "📜 Escriba !Exit para salir del Agente:\n"
        "📜 Escriba !Inicio para mostrar esta bienvenida nuevamente.\n"
        "📜 Comandos disponibles:\n"
        "!definir [termino] - Busca conceptos de Python\n"
        "!validar [nombre] - Valida el nombre de una variable\n"
        "!sumar [n1] [n2] - Suma dos números enteros o decimales\n"
        "!multiplicar [n1] [n2] - Multiplica dos números\n"
        "!hora - Muestra la hora del sistema\n"
        "!fecha - Muestra la fecha y hora completa\n"
        "!historial - Muestra los últimos 5 comandos usados\n"
    )

def main(entrada):
    PREFIJO = "!"
    if not entrada.startswith(PREFIJO):
        if entrada: 
            print("Recuerda usar '!' para comandos.")
            return "Recuerda usar '!' para comandos."

    cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
    comando = cuerpo[0].lower()

    if comando == "exit":
        print("Saliendo del gestor...")
        return "Saliendo del gestor..."
    elif comando == "inicio":
        print(mostrar_bienvenida())
        return mostrar_bienvenida()
    elif comando in ["definir", "validar", "hora", "historial", "sumar", "fecha", "multiplicar", "ayuda"]:
        resultado = analizar_comando(entrada)
        print(f"Resultado: {resultado}")
        return resultado
    else:
        resultado = analizar_comando(entrada)
        print(f"Resultado: {resultado}")
        return resultado

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
if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)
    else:
        print("ERROR: No se encontró el TOKEN en el archivo .env")