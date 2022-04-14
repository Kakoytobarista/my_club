from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BaseElementObject:
    ELEMENT_XPATH = None

    def __init__(self, driver):
        self.driver = driver
        self.element = driver.find_element_by_xpath(self.ELEMENT_XPATH)

    def click_(self, xpath):
        # element = WebDriverWait(self.element, 20).until(
        #     EC.presence_of_element_located((By.XPATH, xpath)))
        # element.click()
        self.element.find_element_by_xpath(xpath=xpath).click()

