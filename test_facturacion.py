
from unittest.mock import patch

import pytest

from facturacion import calcular_total_factura


def test_calcular_total_factura_exitoso_con_mock():
    with patch(
        "facturacion.obtener_tipo_cambio",
        return_value=3.80,
    ):
        resultado = calcular_total_factura(100.0)

    assert resultado == 380.00


def test_calcular_total_factura_con_descuento_mock():
    with patch(
        "facturacion.obtener_tipo_cambio",
        return_value=3.80,
    ):
        resultado = calcular_total_factura(
            100.0,
            aplicar_descuento=True,
        )

    assert resultado == 342.00


def test_calcular_total_factura_monto_invalido_lanza_excepcion():
    with pytest.raises(ValueError) as exc_info:
        calcular_total_factura(-50.0)

    assert str(exc_info.value) == (
        "El monto de la factura debe ser mayor a cero"
    )
