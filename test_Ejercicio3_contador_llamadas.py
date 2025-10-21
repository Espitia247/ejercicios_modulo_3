import pytest
from Ejercicio3_contador_llamadas import crear_contador

# --- PRUEBAS UNITARIAS PARA crear_contador --- #

def test_incremento_basico():
    """
    Verifica que la función incrementar retorne valores consecutivos
    cada vez que se llama.
    """
    contador = crear_contador()
    assert contador() == 1
    assert contador() == 2
    assert contador() == 3


def test_independencia_de_contadores():
    """
    Verifica que dos contadores creados sean independientes
    y mantengan su propio estado interno.
    """
    contador_a = crear_contador()
    contador_b = crear_contador()

    # Contador A
    assert contador_a() == 1
    assert contador_a() == 2

    # Contador B empieza desde 1, no desde 3
    assert contador_b() == 1
    assert contador_b() == 2

    # A continúa su secuencia independiente
    assert contador_a() == 3


def test_tipo_de_retorno():
    """
    Verifica que crear_contador retorna una función.
    """
    contador = crear_contador()
    assert callable(contador), "crear_contador debe retornar una función"


def test_incremento_continuo():
    """
    Verifica que los valores se incrementan de 1 en 1 de forma continua.
    """
    contador = crear_contador()
    resultados = [contador() for _ in range(5)]
    assert resultados == [1, 2, 3, 4, 5]


def test_no_reinicia_el_conteo():
    """
    Verifica que el contador no se reinicia entre llamadas sucesivas.
    """
    contador = crear_contador()
    contador()  # 1
    contador()  # 2
    valor_antes = contador()  # 3
    valor_despues = contador()  # 4
    assert valor_despues == valor_antes + 1
