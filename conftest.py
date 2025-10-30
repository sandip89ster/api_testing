import os
import json
import pytest
import pathlib
from dotenv import load_dotenv
import logging
from datetime import datetime, timezone


LOG_DIR = pathlib.Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "api_test.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()],
)
logger = logging.getLogger("api_tests")
logging.debug("Logger initiated")

load_dotenv()

BASE = os.getenv("REQ_RES_URL")
WEBHOOK_BASE = os.getenv("WEBHOOK_URL")

WEBHOOK_TOKEN = os.getenv("WEBHOOK_TOKEN")
WEBHOOK_URL = f"{WEBHOOK_BASE}/{WEBHOOK_TOKEN}"

SCHEMA_DIR = pathlib.Path(__file__).parent / "tests" / "schema"


@pytest.fixture(scope="session")
def base_url():
    return BASE


@pytest.fixture(scope="session")
def webhook_base_url():
    return WEBHOOK_BASE


@pytest.fixture(scope="session")
def webhook_token():
    return WEBHOOK_TOKEN


@pytest.fixture(scope="session")
def webhook_url():
    return WEBHOOK_URL


@pytest.fixture(scope="session")
def headers():
    return {"Content-Type": "application/json", "x-api-key": os.getenv("X_API_KEY")}


@pytest.fixture(scope="session")
def webhook_headers():
    return {
        "Content-Type": "application/json",
        "x-request-time": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


@pytest.fixture(scope="session")
def load_schema():
    def _load(name):
        with open(SCHEMA_DIR / name, "r") as f:
            return json.load(f)

    return _load
