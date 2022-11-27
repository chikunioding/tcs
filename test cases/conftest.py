from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def setup():
    driver=webdriver.Chrome(r"C:\Users\Mayur\PycharmProjects\Windows\Driver\chromedriver.exe")
    return driver
