import requests
import allure
import logging

logger = logging.getLogger("api_tests")


def post_request(url, payload, headers):
    logger.info(f"Sending POST request to {url}")
    with allure.step("POST /users - create user"):
        response = requests.post(url, json=payload, headers=headers)
    logger.info(f"Response JSON {response.text}")
    return response


def get_request(url, headers):
    logger.info(f"Sending GET request to {url}")
    with allure.step("GET /users - get users"):
        response = requests.get(url, headers=headers)
    logger.info(f"Received json - {response.text}")
    return response


def delete_request(url, headers):
    logger.info(f"Sending DELETE request to {url}")
    with allure.step("DELETE /users - delete user"):
        response = requests.delete(url, headers=headers)
    return response
