import time
from utility.api_client import post_request, get_request
from utility.validation import assert_status


def get_latest_uuid(base, token):
    response = get_request(f"{base}/token/{token}/requests?sorting=newest", None)
    assert_status(response, 200)
    body = response.json()
    try:
        return body["data"][0]["uuid"]
    except IndexError:
        return 0


def poll_for_latest_uuid(old_value, base, token):
    start_time = time.monotonic()
    new_value = get_latest_uuid(base, token)
    while old_value == new_value and time.monotonic() - start_time < 10:
        print(old_value, new_value)
        new_value = get_latest_uuid(base, token)
        time.sleep(1)
    return new_value
