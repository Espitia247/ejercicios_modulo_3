import pytest
from ejercicio4_validador_datos import aplicar_validador, es_email_valido, es_mayor_a_10



# --- PRUEBAS UNITARIAS PARA es_email_valido --- #

def test_es_email_valido_correcto():
    """
    Verifica que los correos con formato válido sean aceptados.
    """
    correos_validos = [
        "usuario@gmail.com",
        "nombre.apellido@dominio.co",
        "test123@mail.com",
        "user-name@empresa.org",
    ]
    for correo in correos_validos:
        assert es_email_valido(correo) is True


def test_es_email_valido_incorrecto():
    """
    Verifica que los correos con formato incorrecto sean rechazados.
    """
    correos_invalidos = [
        "correo_invalido@",
        "sin_arroba.com",
        "@dominio.com",
        "usuario@dominio",
        "",
    ]
    for correo in correos_invalidos:
        assert es_email_valido(correo) is False


# --- PRUEBAS UNITARIAS PARA es_mayor_a_10 --- #

def test_es_mayor_a_10_valores_validos():
    """
    Verifica que los números mayores a 10 sean válidos.
    """
    assert es_mayor_a_10(11)
    assert es_mayor_a_10(25)
    assert es_mayor_a_10(100)


def test_es_mayor_a_10_valores_invalidos():
    """
    Verifica que los números menores o iguales a 10 sean inválidos.
    """
    assert not es_mayor_a_10(10)
    assert not es_mayor_a_10(5)
    assert not es_mayor_a_10(0)
    assert not es_mayor_a_10(-3)


# --- PRUEBAS UNITARIAS PARA aplicar_validador --- #

def test_aplicar_validador_con_emails():
    """
    Prueba que aplicar_validador filtre correctamente una lista de correos.
    """
    correos = ["usuario@gmail.com", "correo_invalido@", "admin@dominio.com"]
    resultado = aplicar_validador(correos, es_email_valido)
    assert resultado == ["usuario@gmail.com", "admin@dominio.com"]


def test_aplicar_validador_con_numeros():
    """
    Prueba que aplicar_validador filtre correctamente una lista de números.
    """
    numeros = [5, 12, 8, 25, 3, 14]
    resultado = aplicar_validador(numeros, es_mayor_a_10)
    assert resultado == [12, 25, 14]


def test_aplicar_validador_lista_vacia():
    """
    Verifica que aplicar_validador maneje correctamente listas vacías.
    """
    assert aplicar_validador([], es_mayor_a_10) == []
    assert aplicar_validador([], es_email_valido) == []


def test_aplicar_validador_sin_coincidencias():
    """
    Verifica que el resultado sea una lista vacía si ningún elemento pasa la validación.
    """
    datos = ["texto", "sin_arroba", "otro"]
    resultado = aplicar_validador(datos, es_email_valido)
    assert resultado == []
