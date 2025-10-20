from typing import Callable, List
import re

def aplicar_validador(datos: List, validador: Callable) -> List:
    """
    Aplica una función validadora a cada elemento de la lista y
    devuelve una nueva lista con los elementos que pasaron la validación.

    Parámetros:
        datos (list): Lista de elementos a validar.
        validador (callable): Función que recibe un elemento y retorna True o False.

    Retorna:
        list: Lista de elementos que cumplen la validación.
    """
    return [dato for dato in datos if validador(dato)]


# --- FUNCIONES DE VALIDACIÓN ---

def es_email_valido(email: str) -> bool:
    """
    Verifica si un email tiene un formato válido usando expresiones regulares.
    """
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None


def es_mayor_a_10(numero: int) -> bool:
    """
    Retorna True si el número es mayor a 10.
    """
    return numero > 10


# --- PRUEBAS DE EJEMPLO ---

if __name__ == "__main__":
    correos = ["usuario@gmail.com", "correo_invalido@", "admin@dominio.com", "sin_arroba.com"]
    numeros = [5, 12, 8, 25, 3, 14]

    print("Correos válidos:", aplicar_validador(correos, es_email_valido))
    print("Números mayores a 10:", aplicar_validador(numeros, es_mayor_a_10))
