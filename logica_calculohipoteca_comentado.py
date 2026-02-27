class Error_edad(Exception):
    "se usa cuando la edad es menor a la edad minima para solicitar la hipoteca inversa"
class Eror_porcentaje(Exception):
    "la edad mínima para solicitar hipoteca inversa es de 65 años."

class Error_tasa_negativa(Exception):
    "Error: la tasa de interés debe ser mayor a 0."

def calcular_credito(valor_inmueble, tasa_anual, plazo_anios, porcentaje_financiado, edad):
    """
    Calcula los valores principales de una hipoteca inversa:
    - Cuota mensual
    - Total acumulado pagado
    - Saldo proyectado al final del plazo
    """

    # VALIDACIONES: Se verifican las condiciones mínimas para que el crédito sea válido.
    if edad < 65:
        raise Error_edad ("Error: la edad mínima para solicitar hipoteca inversa es de 65 años.")
    
    # Se valida que el porcentaje financiado esté dentro del rango permitido (0% a 100%).
    if porcentaje_financiado < 0 or porcentaje_financiado > 100:
        raise Eror_porcentaje ("Error: el porcentaje financiado debe ser entre 0 y 100.")
    
    # Se valida que la tasa de interés sea positiva.
    if tasa_anual <= 0:
        raise Error_tasa_negativa ("Error: la tasa de interés debe ser mayor a 0.")


    # CONVERSIÓN A DECIMALES: Se transforman porcentajes a formato decimal para operar matemáticamente.
    tasa_anual = tasa_anual / 100
    porcentaje_financiado = porcentaje_financiado / 100


    # CÁLCULOS PRINCIPALES
    
    # Se calcula el monto real que será financiado según el porcentaje indicado.
    monto_financiado = valor_inmueble * porcentaje_financiado
    
    # Se convierte la tasa anual en tasa mensual.
    tasa_mensual = tasa_anual / 12
    
    # Se calcula el número total de pagos en meses.
    numero_pagos = plazo_anios * 12


    # CUOTA MENSUAL:
    # Se aplica la fórmula financiera de anualidad (equivalente a la función PAGO de Excel).
    cuota_mensual = (
        tasa_mensual * monto_financiado
        / (1 - (1 + tasa_mensual) ** (-numero_pagos))
    )

    
    # TOTAL ACUMULADO:
    # Se calcula el total pagado al final del crédito.
    total_acumulado = cuota_mensual * numero_pagos


    # SALDO PROYECTADO:
    # Se proyecta el valor futuro del monto financiado aplicando interés compuesto anual.
    saldo_proyectado = monto_financiado * (1 + tasa_anual) ** plazo_anios


    # Se retornan los tres resultados principales del cálculo.
    return cuota_mensual, total_acumulado, saldo_proyectado
