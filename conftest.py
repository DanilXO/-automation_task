import pytest
from selenium import webdriver

BANK_SITE_URL = "https://www.mtsbank.ru/"


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="drivers/chromedriver")
    yield driver
    driver.quit()
