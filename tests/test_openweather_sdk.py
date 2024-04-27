import pytest
import os
import requests_mock
from app.services.openweather import OpenWeather


from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def api_key():
    return "api_falsa"


@pytest.fixture
def cidade():
    return "Salvador"


@pytest.fixture
def openweather(api_key):
    return OpenWeather(api_key)


@pytest.fixture
def resposta_api_geolocalizacao(cidade):
    return [
        {
            "name": cidade,
            "lat": -12.9822499,
            "lon": -38.4812772,
            "country": "BR",
            "state": "Bahia",
        }
    ]


@pytest.fixture
def resposta_api_previsao_tempo():
    return {
        "current": {"temp": 28, "weather": [{"description": "nuvens dispersas"}]},
        "daily": [
            {"dt": 1713987437, "temp": {"day": 28}},
            {"dt": 1714073837, "temp": {"day": 29}},
            {"dt": 1714160237, "temp": {"day": 24}},
            {"dt": 1714246637, "temp": {"day": 26}},
            {"dt": 1714333037, "temp": {"day": 25}},
            {"dt": 1714419437, "temp": {"day": 25}},
        ],
    }


def test_leitura_api_key():
    assert os.getenv("API_KEY") is not None


def test_endpoint_geolocalizacao_preenchido(openweather):
    assert openweather.ENDPOINT_GEOLOCALIZACAO is not None
    assert len(openweather.ENDPOINT_GEOLOCALIZACAO) > 0


def test_endpoint_previsao_temperatura_preenchido(openweather):
    assert openweather.ENDPOINT_PREVISAO_DE_TEMPO is not None
    assert len(openweather.ENDPOINT_PREVISAO_DE_TEMPO) > 0


def test_obter_latitude_longitude(openweather, resposta_api_geolocalizacao, cidade):
    with requests_mock.Mocker() as mocker:
        geocode_url = openweather.construir_url_api_geolocalizacao(cidade)
        mocker.get(geocode_url, json=resposta_api_geolocalizacao)
        lat, lon = openweather.obter_latitude_longitude(cidade)
        assert lat == -12.9822499
        assert lon == -38.4812772


def test_obter_previsao_tempo(
    openweather, cidade, resposta_api_geolocalizacao, resposta_api_previsao_tempo
):
    with requests_mock.Mocker() as mocker:
        url_geolocalizacao = openweather.construir_url_api_geolocalizacao(cidade)
        latitude = resposta_api_geolocalizacao[0]["lat"]
        longitude = resposta_api_geolocalizacao[0]["lon"]
        url_previsao_de_tempo = openweather.construir_url_api_previsao_tempo(
            latitude, longitude
        )
        mocker.get(url_geolocalizacao, json=resposta_api_geolocalizacao)
        mocker.get(url_previsao_de_tempo, json=resposta_api_previsao_tempo)
        dados_previsoes = openweather.obter_previsao_do_tempo_8_dias(cidade)
        assert dados_previsoes is not None
        assert dados_previsoes["current"]["temp"] == 28
