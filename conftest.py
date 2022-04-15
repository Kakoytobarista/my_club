import os.path
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    options = Options()
    options.headless = True

    if browser_name == "chrome":
        print("\nStart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nStart firefox browser for test..")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nQuit browser..")
    browser.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    timestamp = datetime.now().strftime('%H-%M-%S')
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        feature_request = item.funcargs['request']
        driver = feature_request.getfixturevalue('browser')
        path = os.path.abspath(__name__)
        driver.save_screenshot(f'{path}/reports/' + timestamp + '.png')

        extra.append(pytest_html.extras.image(f'{path}/reports/'
                                              + timestamp + '.png'))

        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            # extra.append(pytest_html.extras.image('/home/aslan/gitProjects/Testing-infotecs/reports/'))
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra
