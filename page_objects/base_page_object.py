from selenium import webdriver


class BasePage:
    def __init__(self, browser: webdriver,
                 url: str, timeout: int = 5):
        self.browser: webdriver = browser
        self.url: str = url
        self.browser.get(url)
        self.browser.implicitly_wait(timeout)
