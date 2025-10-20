""" Autor: Santiago Espitia """

def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula el IMC usando la fórmula IMC = peso / (altura * altura).

    Parámetros:
    peso (float): El peso de la persona en kilogramos (kg).
    altura (float): La altura de la persona en metros (m).

    Retorna:
    float: El IMC redondeado a 2 decimales.
    """
    # Se añade una validación básica para evitar división por cero o valores no físicos.
    if altura <= 0 or peso <= 0:
        raise ValueError("El peso y la altura deben ser valores positivos.")

    imc = peso / (altura ** 2)
    return round(imc, 2)


# ----------------------------------------------------------------------

def interpretar_imc(imc: float) -> str:
    """
    Clasifica el resultado del IMC según las categorías estándar de la OMS.

    Parámetros:
    imc (float): El valor del Índice de Masa Corporal.

    Retorna:
    str: Una cadena de texto con la interpretación del resultado (ej: "Bajo peso").
    """
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25.0:
        return "Normal"
    elif 25.0 <= imc < 30.0:
        return "Sobrepeso"
    elif 30.0 <= imc < 35.0:
        return "Obesidad clase I (Moderada)"
    elif 35.0 <= imc < 40.0:
        return "Obesidad clase II (Severa)"
    else:  # imc >= 40.0
        return "Obesidad clase III (Mórbida)"


# ----------------------------------------------------------------------

def main():

    print("--- Calculadora de IMC ---")

    try:
        # 1. Solicitar datos al usuario y asegurar que sean floats
        peso = float(input(" Digite su peso en kg: "))
        altura = float(input("️ Digite su altura en metros: "))

        # 2. Calcular IMC
        resultado_imc = calcular_imc(peso, altura)

        # 3. Interpretar IMC
        interpretacion = interpretar_imc(resultado_imc)

        # 4. Mostrar el resultado
        print("\n--- Resultado ---")
        print(f"Su IMC es: **{resultado_imc:.2f}**")
        print(f"Clasificación: **{interpretacion}**")

    except ValueError as e:
        # Manejo de errores para entradas no numéricas o valores no válidos (altura/peso <= 0)
        print(f"\n Error de entrada: {e}")
        print("Por favor, ingrese valores numéricos válidos y positivos.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()