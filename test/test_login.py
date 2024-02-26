from selenium.webdriver.common.by import By
from pages.loginpage import LoginPage
from utils.setup import SetupDriver
import time
import pytest

# buat fixture siapa tidak function membuka browser baru dengan session baru
@pytest.fixture(scope="function")
def driver():
    setup_driver = SetupDriver()
    yield setup_driver.driver
    setup_driver.driver.quit()


def test_loginSukses(driver):
    login = LoginPage(driver)
    login.open()
    login.clickLogin("08997775838", "4321lupa")
    assert login.successLogin()
    login.closeBrowser()


def test_loginUnregistered(driver):
    login = LoginPage(driver)
    login.open()
    login.clickLogin("1234213", "4321lupa")
    assert login.unregisteredAkun()
    login.closeBrowser()


def test_loginWrongPW(driver):
    login = LoginPage(driver)
    login.open()
    login.clickLogin('8997775838', '4123lupaaaa')
    assert login.wrongPassword()
    login.closeBrowser()




# def test_loginWrongPW():
#     login = LoginPage(drivers)
#     login.open()
#     login.clickLogin(login.username, "123213")
#     assert login.wrongPassword()
    
# def test_loginUnregistered():
#     login = LoginPage(drivers)
#     login.open()
#     login.clickLogin("123123asdas", "4321lupa")
#     assert login.unregisteredAkun()