from dotenv import load_dotenv
from dataclasses import dataclass
import os

load_dotenv()


class CredenciaisOpenWeather:
    API_KEY = os.getenv("API_KEY")
