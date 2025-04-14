from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key
#from selenium.webdriver.chrome.options import Options
from base.webDriverFactory import WebDriverFactory


@pytest.fixture()
def setUp(browser):
    # chromeOptions = Options()
    # chromeOptions.add_argument("--incognito")
    wf = WebDriverFactory(browser)
    return wf.getWebDriverInstance()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


############ Pytest Hook for adding envoronmental info in HTML reports###########
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = "Nop Commerce Demo"
    config.stash[metadata_key]['Module Name'] = "Customers"
    config.stash[metadata_key]['Tester Name'] = "Kirti D"


# To edit or modify the default report info
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
