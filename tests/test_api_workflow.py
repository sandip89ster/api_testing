import pytest
import allure
from datetime import datetime
import logging
from tests.data.users import USERS, INVALID_USER_DATA
from utility.api_client import post_request, get_request, delete_request
from utility.validation import *

logger = logging.getLogger("api_tests")


@allure.epic("ReqRes API Test")
@allure.feature("User endpoint")
class TestUsers:
    @pytest.mark.parametrize(
        "payload", USERS, ids=lambda p: f"{p['name']} - {p['job']}"
    )
    def test_create_user(self, payload, headers, base_url, load_schema):
        response = post_request(f"{base_url}/users", payload, headers)
        allure.attach(response.text, "response.json", allure.attachment_type.JSON)
        assert_status(response, 201)
        body = response.json()
        assert_user(body, payload)
        schema = load_schema("create_user.json")
        assert_schema(body, schema)

    def test_get_users(self, base_url, headers, load_schema):
        response = get_request(f"{base_url}/users", headers)
        allure.attach(response.text, "response.json", allure.attachment_type.JSON)
        assert_status(response, 200)
        body = response.json()
        logger.info(f"Response received - check user data exists")
        assert len(body["data"]) > 0
        schema = load_schema("get_users.json")
        assert_schema(body, schema)

    def test_delete_user(self, headers, base_url):
        response = delete_request(f"{base_url}/users/2", headers)
        assert_status(response, 204)

    #  negative scenario - Create user - anonymous
    @pytest.mark.parametrize(
        "payload", USERS, ids=lambda p: f"{p['name']} - {p['job']}"
    )
    def test_create_user_anonymous(self, base_url, payload):
        response = post_request(f"{base_url}/users", payload, None)
        allure.attach(response.text, "response.json", allure.attachment_type.JSON)
        body = response.json()
        logger.info(f"Received response - {response.text}")
        logger.info("Asserting error - %s", body["error"])
        assert body["error"] == "Missing API key"

    # negative case - delete user - anonymous
    def test_delete_user_anonymous(self, base_url):
        response = delete_request(f"{base_url}/users", None)
        allure.attach(response.text, "response.json", allure.attachment_type.JSON)
        assert_status(response, 401)
        body = response.json()
        logger.info(f"Received response - {response.text}")
        logger.info("Asserting error - %s", body["error"])
        assert body["error"] == "Missing API key"

    # negative case - get user - anonymous (without header still able to access the results)
    def test_get_users_anonymous(self, base_url):
        response = get_request(f"{base_url}/users", None)
        assert_status(response, 200)
        body = response.json()
        print(response.status_code)

    # negative scenario - Invalid data for post (no matter the input able to get successful result)
    # Scenario 1 : Empty name & job, Scenario 2 : No name, Scenario 3 : no job, Scenario 4 : Numeric name & job,
    # Scenario 5 : Special characters in name & job, Scenario 6 : Invalid JSON objects, Scenario 7 : Invalid duplicating JSON objects
    @pytest.mark.parametrize("payload", INVALID_USER_DATA)
    def test_create_user_invalid(self, payload, headers, base_url):
        response = post_request(f"{base_url}/users", payload, headers)
        print(response.status_code)

    # negative case - delete without resource id (without resource id still getting successful result)
    def test_delete_user_invalid(self, headers, base_url):
        response = delete_request(f"{base_url}/users", headers)
        print(response.status_code)
