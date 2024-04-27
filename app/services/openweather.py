import requests


class OpenWeather:
    ENDPOINT_GEOLOCALIZACAO = "http://api.openweathermap.org/geo/1.0/direct?"
    ENDPOINT_PREVISAO_DE_TEMPO = "https://api.openweathermap.org/data/3.0/onecall?"

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def obter_latitude_longitude(self, cidade: str):
        url_api_geolocalizacao = self.construir_url_api_geolocalizacao(cidade)
        resposta = requests.get(url_api_geolocalizacao)
        if resposta.status_code == 200 and resposta.json():
            data = resposta.json()[0]
            return data["lat"], data["lon"]
        else:
            print(
                f"Erro '{resposta.status_code}' ao obter localização da cidade '{cidade}'"
            )
            return None, None

    def obter_previsao_do_tempo_8_dias(self, cidade: str):
        """
        Obtem a previsão de tempo do dia atual e dos próximos 8 dias
         para a cidade escolhida
        """
        latitude, longitude = self.obter_latitude_longitude(cidade)
        if latitude is None or longitude is None:
            return None

        url_api_previsao_do_tempo = self.construir_url_api_previsao_tempo(
            latitude, longitude
        )
        resposta = requests.get(url_api_previsao_do_tempo)
        if resposta.status_code == 200:
            return resposta.json()
        else:
            print(f"Error fetching weather data: {resposta.status_code}")
            return None

    def construir_url_api_geolocalizacao(self, cidade):
        return f"{self.ENDPOINT_GEOLOCALIZACAO}q={cidade}&limit=1&appid={self._api_key}"

    def construir_url_api_previsao_tempo(self, latitude: int, longitude: int):
        return f"{self.ENDPOINT_PREVISAO_DE_TEMPO}lat={latitude}&lon={longitude}&lang=pt_br&exclude=minutely,hourly,alerts&appid={self._api_key}&units=metric"


if __name__ == "__main__":
    from dotenv import load_dotenv
    import os

    load_dotenv()
    api_key = os.getenv("API_KEY")
    openweathter = OpenWeather(api_key)
    openweathter.obter_previsao_do_tempo_8_dias("Salvador")
