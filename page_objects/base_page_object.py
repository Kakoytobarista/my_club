class BasePage:
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.get(url)
        self.browser.implicitly_wait(timeout)
