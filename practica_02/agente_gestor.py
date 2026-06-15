import discord
from discord.ext import commands
from gestor_comandos import analizar_comando

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"--- Agente Gestor Online ---")
    print(f"Conectado como: {bot.user.name} (ID: {bot.user.id})")
    print("Esperando comandos en los canales de Discord...\n")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!"):
        respuesta = analizar_comando(message.content)
        await message.channel.send(respuesta)

    await bot.process_commands(message)

TOKEN = "TU_TOKEN_DE_DISCORD_AQUI"

if __name__ == "__main__":
    bot.run(TOKEN)