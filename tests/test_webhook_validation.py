import pytest, time
import logging
from utility.api_client import post_request, get_request
from utility.validation import *
from utility.webhook_helper import get_latest_uuid, poll_for_latest_uuid

logger = logging.getLogger("api_tests")


class TestWebhook:
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_webhook(
        self, webhook_base_url, webhook_token, webhook_url, webhook_headers
    ):
        uuid = get_latest_uuid(webhook_base_url, webhook_token)
        payload = {"event": "user_created", "data": {"id": 123, "name": "john"}}
        response = post_request(webhook_url, payload, webhook_headers)
        assert_status(response, 200)
        assert_text(response, "This URL has no default content configured.")
        latest_uuid = poll_for_latest_uuid(uuid, webhook_base_url, webhook_token)
        response = get_request(
            f"{webhook_base_url}/token/{webhook_token}/request/{latest_uuid}", None
        )
        assert_status(response, 200)
        allure.attach(response.text, "response.json", allure.attachment_type.JSON)
        body = response.json()
        assert_payload(payload, body["content"])
        assert_time_less_than_2_min(body["headers"]["x-request-time"][0])
