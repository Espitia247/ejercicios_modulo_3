import pytest
from calculadora_IMC import calcular_imc, interpretar_imc



# ----------------------------------------------------------------------
# TESTS PARA calcular_imc()
# ----------------------------------------------------------------------

def test_calcular_imc_valores_normales():
    """Prueba que el cálculo del IMC sea correcto con valores normales."""
    assert calcular_imc(70, 1.75) == pytest.approx(22.86, 0.01)
    assert calcular_imc(60, 1.60) == pytest.approx(23.44, 0.01)


def test_calcular_imc_redondeo():
    """Verifica que el IMC se redondee a dos decimales."""
    imc = calcular_imc(63.5, 1.73)

    assert isinstance(imc, float)
    assert round(imc, 2) == imc  # Debe tener solo dos decimales


def test_calcular_imc_valores_invalidos():
    """Debe lanzar ValueError si peso o altura son cero o negativos."""
    with pytest.raises(ValueError):
        calcular_imc(0, 1.75)
    with pytest.raises(ValueError):
        calcular_imc(70, 0)
    with pytest.raises(ValueError):
        calcular_imc(-70, 1.80)
    with pytest.raises(ValueError):
        calcular_imc(70, -1.80)


# ----------------------------------------------------------------------
# TESTS PARA interpretar_imc()
# ----------------------------------------------------------------------

@pytest.mark.parametrize(
    "imc, esperado",
    [
        (17.0, "Bajo peso"),
        (22.0, "Normal"),
        (27.0, "Sobrepeso"),
        (32.0, "Obesidad clase I (Moderada)"),
        (37.0, "Obesidad clase II (Severa)"),
        (42.0, "Obesidad clase III (Mórbida)"),
    ],
)
def test_interpretar_imc_categorias(imc, esperado):
    """Prueba que la interpretación del IMC coincida con las categorías de la OMS."""
    assert interpretar_imc(imc) == esperado


def test_interpretar_imc_limites_exactos():
    """Verifica las transiciones exactas entre categorías."""
    assert interpretar_imc(18.5) == "Normal"
    assert interpretar_imc(25.0) == "Sobrepeso"
    assert interpretar_imc(30.0) == "Obesidad clase I (Moderada)"
    assert interpretar_imc(35.0) == "Obesidad clase II (Severa)"
    assert interpretar_imc(40.0) == "Obesidad clase III (Mórbida)"
