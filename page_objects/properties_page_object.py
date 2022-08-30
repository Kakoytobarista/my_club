from enums.base_enum import BaseEnum
from page_objects.base_page_object import BasePage
from selenium import webdriver


class PropertiesPageObject(BasePage):
    PROPERTIES_PAGE = f"{BaseEnum.BASE_URL.value}/{BaseEnum.PROPERTIES_PAGE_URL.value}"

    def __init__(self, browser: webdriver,
                 url: str = PROPERTIES_PAGE):
        super().__init__(browser, url)
        self.url = self.PROPERTIES_PAGE
