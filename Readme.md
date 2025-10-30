# API & Webhook Validation

This repository contains simple lightweight test automation with pytest

It supports:

- **API Testing** with schema & status assertion
- **Webhook** async polling and response validation
- **Parallel Execution** & **Allure reporting** for easy and fast test insights
- **Makefile** for easy command execution

## 1. Setup Instructions

### Prerequisites

- Python 3
- Access to [reqres.in](https://reqres.in) with API token
- Access to [webhook.site] (https://webhook.site)

### Installation

```
git clone <repo-url>
cd api_testing
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Environment Variables

Create .env file in root of project
set the following properties with actual keys

```
REQ_RES_URL=https://reqres.in/api
X_API_KEY=XXXXXXXXXXXXXXXXXX
WEBHOOK_URL=https://webhook.site
WEBHOOK_TOKEN=XXXXXXXXXXXXXX
```

### Run Tests

Run command

```
pytest -n auto -q --alluredir=allure-results
```

### Launch Allure Reports

Run command

To generate report,

```
allure generate allure-results -o allure-report --clean
```

To serve report,

```
allure serve allure-results
```

## 2. Framework & Library choices

| Library / Framework |         Usage         |                 Reason                  |
| :-----------------: | :-------------------: | :-------------------------------------: |
|       Pytest        |    Test Framework     | Preferred framework for this assignment |
|      Requests       |      HTTP client      |       Easy & cleaner API handling       |
|     Jsonschema      |   Schema Validation   |  Good response valiadation of schemas   |
|    allure-pytest    |       Reporting       |     Good reporting of test results      |
|    python-dotenv    | Environment variables |     Managing environment variables      |
|    pytest-xdist     |  Test runs parallel   |         Resuce execution times          |

## 3. Webhook validation logic

- Trigger a POST request with webhook.site with custom header `x-request-time`
- The method - poll_for_latest_uuid() will poll every 1 secnd for total duration of 10 seconds to check for latest UUID
- Fetch the response with latest UUID, get response parse content and validate against payload and also ensuring `x-resuest-time` in header is within 2 minutes

## 4. Trade-offs & Improvements

- reqres.in site limits the requests and sometime getting HTTP status code 429 (Too many requests)
- reqres.in & webhook.site are both free service portal and reliability of services might be doubtful

## 5. Test design decision based on risk

- During validation of webhook response only content section with `x-request-time` was validated and not the entire JSON and corresponding schema
