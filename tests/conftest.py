from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from Testdata.testdata import Testdata


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption("--username", action="store", help="input username")
    parser.addoption("--password", action="store", help="input password")
    parser.addoption("--product", action="store", help="product")


@pytest.fixture(scope="class", autouse=True)
def setup(request):
    """
        Set the driver to take from user,Url and return it to use
    """
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service(Testdata.chrome_executable_path)
        driver = webdriver.Chrome(service=service_obj)
        driver.get(Testdata.base_url)
        driver.maximize_window()
        request.cls.driver = driver
        yield
        driver.quit()


@pytest.fixture
def params(request):
    """
        Set the username,password,product to take from user
    """
    params = {'username': request.config.getoption('--username'), 'password': request.config.getoption('--password'),
              'product': request.config.getoption('--product')}
    if params['username'] is None and params['password'] is None:
        pytest.skip()
    return params
