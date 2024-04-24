import requests


class OpenWeather:
    ENDPOINT_GEOLOCALIZACAO = "http://api.openweathermap.org/geo/1.0/direct?"

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

    def construir_url_api_geolocalizacao(self, cidade):
        return f"{self.ENDPOINT_GEOLOCALIZACAO}q={cidade}&limit=1&appid={self._api_key}"


if __name__ == "__main__":
    from dotenv import load_dotenv
    import os

    load_dotenv()
    api_key = os.getenv("API_KEY")
    openweathter = OpenWeather(api_key)
    openweathter.obter_latitude_longitude("Fortaleza")
