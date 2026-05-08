class ControlAcceso:
    def __init__(self):
        # Atributos iniciales: Diccionario con 3 registros
        self.usuarios_autorizados = {
            "2024001": "Investigador",
            "2024002": "Estudiante",
            "2024003": "Administrador"
        }

    def verificar_permisos(self, matricula):
        """Valida la existencia de la matrícula en el diccionario."""
        if matricula in self.usuarios_autorizados:
            rol = self.usuarios_autorizados[matricula]
            print(f"> [ACCESO CONCEDIDO] Bienvenido, rol detectado: {rol}.")
            return rol
        else:
            print("> [ACCESO DENEGADO] Usuario no registrado en la base de datos de IA.")
            return None

    def registrar_usuario(self):
        """Permite agregar nuevos usuarios si el rol es Administrador."""
        nueva_id = input("Ingrese la nueva matrícula: ")
        nuevo_rol = input("Ingrese el rol (Investigador/Estudiante/Administrador): ")
        self.usuarios_autorizados[nueva_id] = nuevo_rol
        print(f"Usuario {nueva_id} registrado exitosamente.")

# --- Flujo Principal ---
sistema = ControlAcceso()
print("--- Sistema de Seguridad Laboratorio IA - UX ---")

while True:
    try:
        entrada = input("\nIngrese su matrícula (o 'salir' para finalizar): ").strip()
        
        if entrada.lower() == 'salir':
            break
            
        if not entrada:
            raise ValueError("Error: El campo de matrícula no puede estar vacío.")

        # Verificación de permisos
        rol_usuario = sistema.verificar_permisos(entrada)

        # Funcionalidad Extra: Si es administrador, puede agregar usuarios
        if rol_usuario == "Administrador":
            opcion = input("¿Desea registrar un nuevo usuario? (s/n): ").lower()
            if opcion == 's':
                sistema.registrar_usuario()

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        print("--- Intento de acceso registrado en el log del servidor ---")