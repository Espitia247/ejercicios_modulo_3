def crear_contador():
    """
    Función 'fábrica' que crea y retorna una función de conteo.
    Utiliza un closure para mantener el estado de la variable 'conteo'.

    Retorna:
    function: La función interna 'incrementar'.
    """
    # 1. Variable que será capturada por el closure
    conteo = 0

    def incrementar() -> int:
        """
        Función interna (closure) que incrementa y retorna el conteo.

        Utiliza 'nonlocal' para modificar la variable 'conteo' en el
        ámbito de la función externa 'crear_contador'.

        Retorna:
        int: El nuevo valor del conteo.
        """
        # 2. Uso de 'nonlocal' para modificar la variable del scope superior
        nonlocal conteo
        conteo += 1
        return conteo

    # 3. Retorna la función interna
    return incrementar


# ----------------------------------------------------------------------
# 4. Pruebas de Independencia de Contadores
# ----------------------------------------------------------------------

# Crear el primer contador
contador_a = crear_contador()

# Crear el segundo contador
contador_b = crear_contador()

print("--- Contador A (Llamadas) ---")
print(f"Llamada 1: {contador_a()}")  # Esperado: 1
print(f"Llamada 2: {contador_a()}")  # Esperado: 2
print(f"Llamada 3: {contador_a()}")  # Esperado: 3
print("-" * 25)

print("--- Contador B (Llamadas) ---")
# El contador B empieza en 1, demostrando que tiene su propia variable 'conteo'
print(f"Llamada 1: {contador_b()}")  # Esperado: 1
print(f"Llamada 2: {contador_b()}")  # Esperado: 2
print("-" * 25)

print("--- Contador A (Llamada Final) ---")
# El contador A continúa su conteo desde 3
print(f"Llamada 4: {contador_a()}")  # Esperado: 4

# Nota de confirmación:
print("\n Conclusión: Los contadores A y B operan con estados independientes.")