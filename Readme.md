# API & Webhook Validation

This repository contains simple lightweight test automation with pytest

It supports:

- **API Testing** with schema & status assertion
- **Webhook** async polling and response validation
- **Parallel Execution** & **Allure reporting** for easy and fast test insights
- **Makefile** for easy command execution
- **Test Tagging** to support test priority execution

## 1. Setup Instructions

### Prerequisites

- Python 3
- Access to [reqres.in](https://reqres.in) with API token
- Access to [webhook.site](https://webhook.site)

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
X_API_KEY=XXXXXXXXXXXXXXXXXX
WEBHOOK_TOKEN=XXXXXXXXXXXXXX
```

### Run Tests

Run command

```
pytest -n auto -q --alluredir=allure-results
```

Also, Makefile is added to make executions easier

- To run test normally - `make test`
- To run test **paralelly** - `make test_parallel`
- To run test with verbose - `make test_output`
- Run only **smoke tests** - `make test_smoke`
- Run only **regression tests** - `make test_regression`
- Run test with allure report - `make test_allure`
- Generate allure report - `make allure_generate`
- Serve allure report - `make allure_serve`

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
- The method - poll_for_latest_uuid() will poll every 1 second for total duration of 10 seconds to check for latest UUID
- Fetch the response with latest UUID, get response parse content and validate against payload and also ensuring `x-resuest-time` in header is within 2 minutes

## 4. Trade-offs & Improvements

- reqres.in site limits the requests and sometime getting HTTP status code 429 (Too many requests)
- reqres.in & webhook.site are both free service portal and reliability of services might be doubtful
- Most of the negative scenarios still return success message which compromises testing quality
- In Github actions, uploaded Allure report is not showing up in GitHub pages(unable to fix due to time constraint)

## 5. Test design decision based on risk

- During validation of webhook response only content section with `x-request-time` was validated and not the entire JSON and corresponding schema
