from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class BaseElementObject:
    ELEMENT_XPATH = None

    def __init__(self, browser):
        self.driver: webdriver = browser
        self.element: WebElement = browser.find_element(by=By.XPATH,
                                                        value=self.ELEMENT_XPATH)

    def _click(self, xpath: str):
        """Method for clicking with WebDriverWait"""
        try:
            element = WebDriverWait(self.element, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            element.click()
        except NoSuchElementException as exception:
            raise exception

    def _get_text(self, xpath: str) -> str:
        """Method for getting text with WebDriverWait"""
        try:
            element = WebDriverWait(self.element, 20).until(
                EC.visibility_of_element_located((By.XPATH, xpath)))
            return element.text
        except NoSuchElementException as exception:
            raise exception
