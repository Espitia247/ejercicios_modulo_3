import pytest
from Ejercicio2_generador_de_perfiles import crear_perfil


# --- PRUEBAS UNITARIAS PARA crear_perfil --- #

def test_perfil_completo():
    """
    Verifica que el perfil se genere correctamente con todos los parámetros:
    nombre, edad, varios hobbies y redes sociales.
    """
    resultado = crear_perfil(
        "Ana Torres",
        28,
        "fotografía",
        "senderismo",
        "cocinar",
        instagram="@anatorresfotos",
        twitter="@anatorres_dev",
        linkedin="ana-torres-12345"
    )

    assert "Ana Torres" in resultado
    assert "28 años" in resultado
    assert "fotografía, senderismo, cocinar" in resultado
    assert "Instagram: @anatorresfotos" in resultado
    assert "Linkedin: ana-torres-12345" in resultado
    assert resultado.startswith("=== PERFIL DE USUARIO ===")
    assert resultado.endswith("=========================")


def test_perfil_sin_hobbies_con_redes():
    """
    Verifica que el perfil muestre el mensaje correcto cuando no se pasan hobbies,
    pero sí redes sociales.
    """
    resultado = crear_perfil(
        "Carlos Mena",
        45,
        facebook="CarlosMenaOficial",
        email="carlos.mena@empresa.com"
    )

    assert "Carlos Mena" in resultado
    assert "45 años" in resultado
    assert "No especificados" in resultado
    assert "Facebook: CarlosMenaOficial" in resultado
    assert "Email: carlos.mena@empresa.com" in resultado


def test_perfil_solo_datos_obligatorios():
    """
    Verifica el comportamiento del perfil cuando solo se pasan los datos obligatorios.
    """
    resultado = crear_perfil("Lucía Gómez", 22)

    assert "Lucía Gómez" in resultado
    assert "22 años" in resultado
    assert "No especificados" in resultado
    assert "Ninguna especificada" in resultado


def test_perfil_sin_redes_pero_con_hobbies():
    """
    Verifica que el perfil se genere correctamente si hay hobbies pero no redes.
    """
    resultado = crear_perfil("Santiago Espitia", 30, "programar", "viajar")

    assert "Santiago Espitia" in resultado
    assert "30 años" in resultado
    assert "programar, viajar" in resultado
    assert "Ninguna especificada" in resultado


def test_formato_general():
    """
    Asegura que el formato general del perfil contenga los encabezados esperados.
    """
    resultado = crear_perfil("Laura", 19)
    assert "=== PERFIL DE USUARIO ===" in resultado
    assert "Pasatiempos (Hobbies):" in resultado
    assert "Redes Sociales:" in resultado
    assert "=========================" in resultado
