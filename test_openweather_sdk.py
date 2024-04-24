import pytest
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def api_key():
    return os.getenv("API_KEY")


def test_api_key(api_key):
    assert api_key is not None
