
import requests


def obtener_tipo_cambio() -> float:
    """Consulta el tipo de cambio de USD a PEN."""
    response = requests.get(
        "https://api.exchangerate.host/latest",
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()
    return float(data["rates"]["PEN"])


def calcular_total_factura(
    monto_usd: float,
    aplicar_descuento: bool = False,
) -> float:
    """Calcula el total de una factura en soles."""
    if monto_usd <= 0:
        raise ValueError(
            "El monto de la factura debe ser mayor a cero"
        )

    tipo_cambio = obtener_tipo_cambio()
    total_pen = monto_usd * tipo_cambio

    if aplicar_descuento:
        total_pen *= 0.90

    return round(total_pen, 2)
