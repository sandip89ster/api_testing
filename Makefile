install:
	pip3 install -r requirements.txt

test:
	pytest -v

test_parallel:
	pytest -n auto

test_output:
	pytest -s -v

test_sanity:
	pytest -s -v -m sanity 

test_allure:
	pytest -q --alluredir=allure-results  

allure_generate:
	allure generate allure-results -o allure-report --clean

allure_serve:
	allure serve allure-results  

.PHONY: install test test_parallel test_output test_sanity test_allure allure_generate allure_serve