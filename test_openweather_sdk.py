import pytest
import os
import requests_mock
from openweather import OpenWeather


from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def api_key():
    return os.getenv("API_KEY")


@pytest.fixture
def openweather(api_key):
    return OpenWeather(api_key)


@pytest.fixture
def resposta_api_geolocalizacao():
    """Sample JSON response that mimics the OpenWeatherMap Geocoding API response for testing."""
    return [
        {
            "name": "Salvador",
            "lat": -12.9822499,
            "lon": -38.4812772,
            "country": "BR",
            "state": "Bahia",
        }
    ]


def test_api_key(api_key):
    assert api_key is not None


def test_endpoint_geolocalizacao_preenchido(openweather):
    assert openweather.ENDPOINT_GEOLOCALIZACAO is not None
    assert len(openweather.ENDPOINT_GEOLOCALIZACAO) > 0


def test_obter_latitude_longitude(openweather, resposta_api_geolocalizacao):
    with requests_mock.Mocker() as mocker:
        cidade = "Salvador"
        geocode_url = openweather.construir_url_api_geolocalizacao(cidade)
        mocker.get(geocode_url, json=resposta_api_geolocalizacao)
        lat, lon = openweather.obter_latitude_longitude(cidade)
        assert lat == -12.9822499
        assert lon == -38.4812772
