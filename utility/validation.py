import pytest, json
from jsonschema import validate, ValidationError
import allure
from dotenv import load_dotenv
import logging
from datetime import datetime, timezone
from dateutil import parser

logger = logging.getLogger("api_tests")


def assert_schema(instance, schema):
    logger.info("Response received - asserting schema")
    with allure.step("Validate JSON schema"):
        try:
            validate(instance=instance, schema=schema)
        except ValidationError as e:
            raise AssertionError("schema validation failed")


def assert_status(response, expected):
    logger.info(f"Received status {response.status_code}")
    with allure.step(f"assert status {expected} - got {response.status_code}"):
        assert response.status_code == expected


def assert_text(response, expected):
    logger.info(f"Received test {response.text}")
    with allure.step(f"assert status {expected} - got {response.text}"):
        assert expected in response.text


def assert_user(body, payload):
    logger.info("Asserting name  - %s", body["name"])
    assert body["name"] == payload["name"]
    logger.info("Asserting job  - %s", body["job"])
    assert body["job"] == payload["job"]
    logger.info("Asserting id  - %s", body["id"])
    assert "id" in body
    assert body["id"].isdigit()
    logger.info("Asserting createdAt - %s", body["createdAt"])
    assert "createdAt" in body
    try:
        datetime.fromisoformat(body["createdAt"])
    except ValueError:
        pytest.fail(f"createdAt is not a valid datetime format : {body['createdAt']}")


def assert_length(text, value):
    logger.info("Asserting text length - %s", text)
    assert len(text) > value


def assert_payload(payload, value):
    logger.info("Asserting payload - %s", value)
    assert payload == json.loads(value)


def assert_time_less_than_2_min(value):
    logger.info("Asserting time less than 2 min - %s", value)
    current_time = datetime.now(timezone.utc)
    parsed_time = parser.isoparse(value)
    age = (current_time - parsed_time).total_seconds()
    assert age < 120
