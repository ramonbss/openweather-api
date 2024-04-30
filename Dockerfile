FROM python:3.12-alpine
WORKDIR /api_openweather

COPY ./requirements.txt /api_openweather/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /api_openweather/app
COPY .env /api_openweather
COPY ./tests /api_openweather/tests

EXPOSE 8001

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]