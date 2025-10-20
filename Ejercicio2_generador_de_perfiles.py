def crear_perfil(nombre: str, edad: int, *hobbies: str, **redes_sociales: str) -> str:
    """
    Genera un perfil de usuario, aceptando argumentos obligatorios,
    posicionales variables (hobbies) y de palabra clave variable (redes_sociales).

    Parámetros:
    nombre (str): Nombre del usuario (obligatorio).
    edad (int): Edad del usuario (obligatorio).
    *hobbies (Tuple[str]): Argumentos posicionales variables para hobbies.
    **redes_sociales (Dict[str, str]): Argumentos de palabra clave variable
                                        para redes sociales (Clave=Red, Valor=Usuario).

    Retorna:
    str: Un perfil de usuario formateado con toda la información.
    """

    # 1. Información básica
    perfil = f"=== PERFIL DE USUARIO ===\n"
    perfil += f" Nombre: {nombre}\n"
    perfil += f" Edad: {edad} años\n"

    # 2. Hobbies (*args)
    perfil += "\nPasatiempos (Hobbies):\n"
    if hobbies:
        # Une los hobbies con comas para una presentación limpia
        perfil += f"  - {', '.join(hobbies)}\n"
    else:
        perfil += "  - No especificados.\n"

    # 3. Redes Sociales (**kwargs)
    perfil += "\nRedes Sociales:\n"
    if redes_sociales:
        # Itera sobre la clave (red) y el valor (usuario) del diccionario
        for red, usuario in redes_sociales.items():
            perfil += f"  - {red.capitalize()}: {usuario}\n"
    else:
        perfil += "  - Ninguna especificada.\n"

    perfil += "========================="

    return perfil


# --- EJEMPLO DE USO ---

# Escenario 1: Perfil completo
perfil_completo = crear_perfil(
    "Ana Torres",
    28,
    "fotografía",
    "senderismo",
    "cocinar",
    instagram="@anatorresfotos",
    twitter="@anatorres_dev",
    linkedin="ana-torres-12345"
)
print("--- Escenario 1: Perfil Completo ---")
print(perfil_completo)
print("\n" + "=" * 40 + "\n")

# Escenario 2: Sin hobbies, con algunas redes
perfil_minimo_redes = crear_perfil(
    "Carlos Mena",
    45,
    facebook="CarlosMenaOficial",
    email="carlos.mena@empresa.com"
)
print("--- Escenario 2: Sin Hobbies, con Redes ---")
print(perfil_minimo_redes)
print("\n" + "=" * 40 + "\n")

# Escenario 3: Solo datos obligatorios
perfil_basico = crear_perfil("Lucía Gómez", 22)
print("--- Escenario 3: Solo Datos Obligatorios ---")
print(perfil_basico)