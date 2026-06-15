import pygame
import time

# --- CONFIGURACIÓN DE AUDIO ---
pygame.mixer.init()

def reproducir_efecto(archivo, volumen=1.0, esperar=False):
    """Reproduce un archivo de audio específico en un canal libre."""
    try:
        sonido = pygame.mixer.Sound(archivo)
        sonido.set_volume(volumen)
        canal = sonido.play()
        
        if esperar and canal:
            while canal.get_busy():
                pygame.time.delay(100)
    except pygame.error as e:
        print(f"⚠️ No se pudo reproducir el archivo {archivo}: {e}")

def gestionar_bienestar():
    print("--- 🛡️ SISTEMA INTEGRAL DE BIENESTAR JUVENIL (IA-UX) ---")
    
    try:
        # 1. Inicio: Bienvenida de Claudia
        print("\n🔊 Reproduciendo bienvenida...")
        reproducir_efecto("claudiabienvenida.mp3", volumen=0.9, esperar=True)

        # 2. Captura de Datos
        print("\n📝 Por favor, ingresa tus datos:")
        sueno = float(input("¿Cuántas horas dormiste hoy?: "))
        pasos = int(input("Pasos diarios acumulados: "))
        pantalla = float(input("Horas de uso de pantalla: "))
        comidas = int(input("Comidas sanas realizadas (0-3): "))
        social = float(input("Horas de convivencia con amigos: "))
        familia = int(input("Calidad del ambiente familiar (1-10): "))
        estudio = float(input("Horas de estudio autónomo: "))

        # 3. Procesamiento Lógico y Normalización (0.0 a 1.0)
        s_sueno = min(sueno / 9.0, 1.0)
        s_pasos = min(pasos / 10000, 1.0)
        s_comidas = min(comidas / 3, 1.0)
        s_social = min(social / 1.5, 1.0)
        s_familia = min(familia / 10, 1.0)
        s_estudio = min(estudio / 2.0, 1.0)
        s_pantalla = 1.0 if pantalla <= 2.0 else max(0, 1.0 - ((pantalla - 2.0) / 4))

        # Conversión a porcentajes (0 - 100)
        p_sueno = round(s_sueno * 100)
        p_pasos = round(s_pasos * 100)
        p_comidas = round(s_comidas * 100)
        p_social = round(s_social * 100)
        p_familia = round(s_familia * 100)
        p_estudio = round(s_estudio * 100)
        p_pantalla = round(s_pantalla * 100)

        # Índice Global
        indice = ((s_sueno * 15) + (s_pasos * 15) + (s_comidas * 20) + 
                  (s_social * 15) + (s_familia * 20) + (s_estudio * 10) + (s_pantalla * 5))

        # 4. Mostrar Resultados en Pantalla
        print("\n" + "="*45)
        print(f"⭐ ÍNDICE GLOBAL DE BIENESTAR: {round(indice, 2)}/100")
        print("="*45)
        print(f"🛌 Sueño: {p_sueno}%    | 🍎 Nutrición: {p_comidas}%")
        print(f"🏠 Familia: {p_familia}%  | 📚 Estudio: {p_estudio}%")
        print(f"📱 Pantalla: {p_pantalla}% | 👥 Social: {p_social}%")
        print("-" * 45)

        # =========================================================================
        # 5. EVALUACIÓN INDIVIDUAL: AUDIOS DIFERENTES POR RUBRO BAJO
        # =========================================================================
        print("\n🔍 Analizando indicadores de salud...")
        
        # Cada rubro tiene estrictamente asignado un archivo .mp3 diferente
        rubros = {
            "Sueño": (p_sueno, "Dormir.mp3"),
            "Pasos": (p_pasos, "pasos.mp3"),
            "Nutrición": (p_comidas, "Alimentacion.mp3"),
            "Social": (p_social, "social.mp3"),
            "Familia": (p_familia, "Familia.mp3"),
            "Estudio": (p_estudio, "Estudio.mp3"),
            "Pantalla": (p_pantalla, "pantalla.mp3")
        }

        algun_rubro_bajo = False

        # El ciclo recorre rubro por rubro. Si baja de 60, dispara su audio exclusivo.
        for nombre_rubro, (puntaje, archivo_audio) in rubros.items():
            if puntaje < 60:
                print(f"⚠️ Alerta: {nombre_rubro} deficiente ({puntaje}%).")
                # esperar=True hace que termine un audio antes de empezar el siguiente rubro bajo
                reproducir_efecto(archivo_audio, volumen=0.95, esperar=True)
                algun_rubro_bajo = True

        # --- AUDIO FINAL ---
        if not algun_rubro_bajo:
            # Si TODO fue igual o mayor a 60 (Ninguno falló)
            print("🎉 ¡Excelente! Todos tus indicadores están perfectos.")
            reproducir_efecto("felicitacion.mp3", volumen=0.9, esperar=True)
        else:
            # Cierre común en caso de que haya habido alguna alerta previa
            print("\n🔊 Despedida")
            reproducir_efecto("despedida.mp3", volumen=0.9, esperar=True)

    except ValueError:
        print("\n❌ Error: Por favor ingresa números válidos en las respuestas.")
    except Exception as e:
        print(f"\n❌ Ocurrió un error inesperado: {e}")
    finally:
        pygame.mixer.stop()
        print("\n--- Proceso finalizado en el sistema del Laboratorio IA ---")

if __name__ == "__main__":
    gestionar_bienestar()