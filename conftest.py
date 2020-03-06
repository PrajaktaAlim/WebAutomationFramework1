from selenium import webdriver
from pytest import fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g.chrome OR firefox")


@fixture(scope="session")
def chrome_browser(pytestconfig):
    browser = pytestconfig.getoption("browser")
    if browser.lower() == "chrome":
        chrome_browser = webdriver.Chrome()
        chrome_browser.implicitly_wait(10)
        chrome_browser.maximize_window()
        yield chrome_browser
        chrome_browser.quit()
