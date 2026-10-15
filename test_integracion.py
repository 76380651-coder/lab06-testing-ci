
from unittest.mock import MagicMock, patch

from facturacion import calcular_total_factura

API_URL = "https://open.er-api.com/v6/latest/USD"


def crear_respuesta_api(tipo_cambio: float = 3.75) -> MagicMock:
    """Crea una respuesta simulada de la API de tipo de cambio."""
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "result": "success",
        "rates": {"PEN": tipo_cambio},
    }
    mock_response.raise_for_status.return_value = None
    return mock_response


def test_integracion_calculo_factura_con_api_simulada():
    """Verifica el cálculo de una factura con una API simulada."""
    mock_response = crear_respuesta_api(3.75)

    with patch(
        "facturacion.requests.get",
        return_value=mock_response,
    ) as mock_get:
        resultado = calcular_total_factura(200.0)

    assert resultado == 750.00
    mock_response.raise_for_status.assert_called_once_with()
    mock_response.json.assert_called_once_with()
    mock_get.assert_called_once_with(API_URL, timeout=10)


def test_integracion_calculo_factura_con_descuento():
    """Verifica el cálculo de una factura con descuento."""
    mock_response = crear_respuesta_api(3.75)

    with patch(
        "facturacion.requests.get",
        return_value=mock_response,
    ) as mock_get:
        resultado = calcular_total_factura(
            200.0,
            aplicar_descuento=True,
        )

    assert resultado == 675.00
    mock_response.raise_for_status.assert_called_once_with()
    mock_response.json.assert_called_once_with()
    mock_get.assert_called_once_with(API_URL, timeout=10)
