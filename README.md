# OpenWeather FastAPI

## Visão Geral

Este projeto é uma aplicação FastAPI que integra a API do OpenWeatherMap para obter previsões meteorológicas. Seu objetivo  é fornecer uma maneira automatizada de obter atualizações do tempo para uma cidade específica.

## Começando

### Instalação

Para começar a usar este projeto, siga os passos abaixo:

1. Clone o repositório do projeto:
   ```
    git clone https://github.com/ramonbss/openweather-api
    ```
1. Navegue até o diretório do projeto:
   ```
    cd projeto
    ```
1. Instale as dependências necessárias:
    ```
    pip install -r requirements.txt
    ```

### Executando a Aplicação
Para iniciar o servidor FastAPI, execute o seguinte comando:
   ```
   uvicorn app.main:app
   ```

A porta padrão será a 8000.

## Configurações

### Obter Chaves de API
Acesse [OpenWeatherMap - One Call API](https://openweathermap.org/api/one-call-3)
 e crie uma conta para obter sua chave de API.

### Configuração Local
Antes de iniciar a aplicação, é necessário configurar a credencial para a API do OpenWeatherMap. Essas credenciais devem ser armazenadas de forma segura e podem ser configuradas como variáveis de ambiente, onde serão lidas no módulo **app.services.credenciais**.


### Utilizando a API
#### Postar Atualizações do Tempo
Envie uma requisição HTTP GET para o endpoint **/previsao_de_tempo** incluindo o nome da cidade como parâmetro. Por exemplo:
```
curl http://localhost:8000/previsao_de_tempo?cidade="Sao Paulo"
```
