from fastapi import APIRouter, HTTPException, status
from app.services.openweather import OpenWeather
from app.services.credenciais import CredenciaisOpenWeather

openweather_router = APIRouter()

openweather = OpenWeather(CredenciaisOpenWeather.API_KEY)


@openweather_router.get("/previsao_de_tempo")
def previsao_de_tempo(cidade: str):
    try:
        resposta = openweather.obter_previsao_do_tempo_8_dias(cidade)
        return resposta
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
