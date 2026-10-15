
import requests


def obtener_tipo_cambio() -> float:
    """Consulta el tipo de cambio de USD a PEN."""
    response = requests.get(
        "https://open.er-api.com/v6/latest/USD",
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()

    if data.get("result") != "success":
        raise ValueError("La API no pudo obtener el tipo de cambio")

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

if __name__ == "__main__":
    try:
        tipo_cambio = obtener_tipo_cambio()
        print(f"Tipo de cambio USD a PEN: S/ {tipo_cambio:.4f}")

        total_normal = calcular_total_factura(100)
        total_descuento = calcular_total_factura(100, True)

        print(f"Factura de 100 USD sin descuento: S/ {total_normal:.2f}")
        print(f"Factura de 100 USD con descuento: S/ {total_descuento:.2f}")

    except (requests.RequestException, KeyError, ValueError) as error:
        print(f"No se pudo completar la facturación: {error}")
