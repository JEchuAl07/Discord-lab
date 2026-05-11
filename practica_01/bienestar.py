import pygame
import time

# --- CONFIGURACIÓN DE AUDIO ---
pygame.mixer.init()

def reproducir_efecto(archivo, volumen=1.0, esperar=False):
    """Reproduce un archivo de audio específico."""
    sonido = pygame.mixer.Sound(archivo)
    sonido.set_volume(volumen)
    canal = sonido.play()
    if esperar:
        while canal.get_busy():
            pygame.time.delay(100)

def gestionar_bienestar():
    print("--- 🛡️ SISTEMA INTEGRAL DE BIENESTAR JUVENIL (IA-UX) ---")
    
    try:
        # 1. Inicio: Música de fondo y Bienvenida de Claudia
        # Cargamos el fondo en el canal de música (bucle)
        print("\nReproduciendo bienvenida...")
        reproducir_efecto("claudiabienvenida.mp3", volumen=0.9, esperar=True)

        # 2. Captura de Datos (El programa espera a que el usuario escriba)
        print("\nPor favor, ingresa tus datos:")
        sueno = float(input("¿Cuántos horas dormiste hoy?6: "))
        pasos = int(input("Pasos diarios: "))
        pantalla = float(input("Horas de pantalla: "))
        comidas = int(input("Comidas sanas: "))
        social = float(input("Horas con amigos: "))
        familia = int(input("Ambiente familiar (1-10): "))
        estudio = float(input("Horas de estudio: "))

        # 3. Procesamiento Lógico (Cálculo interno)
        s_sueno = min(sueno / 9.0, 1.0)
        s_pasos = min(pasos / 10000, 1.0)
        s_comidas = min(comidas / 3, 1.0)
        s_social = min(social / 1.5, 1.0)
        s_familia = min(familia / 10, 1.0)
        s_estudio = min(estudio / 2.0, 1.0)
        s_pantalla = 1.0 if pantalla <= 2.0 else max(0, 1.0 - ((pantalla - 2.0) / 4))

        indice = ((s_sueno * 15) + (s_pasos * 15) + (s_comidas * 20) + 
                  (s_social * 15) + (s_familia * 20) + (s_estudio * 10) + (s_pantalla * 5))

        # 4. Mostrar Resultados en Pantalla
        print("\n" + "="*45)
        print(f"⭐ ÍNDICE GLOBAL DE BIENESTAR: {round(indice, 2)}/100")
        print("="*45)
        print(f"🛌 Sueño: {round(s_sueno*100)}% | 🍎 Nutrición: {round(s_comidas*100)}%")
        print(f"🏠 Familia: {round(s_familia*100)}% | 📚 Estudio: {round(s_estudio*100)}%")
        print("-" * 45)

        # 5. Cierre: Narración de resultados pre-grabada
        print("\nReproduciendo mensaje de cierre...")
        reproducir_efecto("resultados.mp3", volumen=0.9, esperar=True)

    except Exception as e:
        print(f"Error: Asegúrate de que los archivos .mp3 existan. {e}")
    finally:
        pygame.mixer.music.stop()
        print("\n--- Proceso finalizado en el sistema del Laboratorio IA ---")

if __name__ == "__main__":
    gestionar_bienestar()