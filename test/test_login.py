from selenium.webdriver.common.by import By
from pages.loginPage import LoginPage
from utils.setup import SetupDriver
import time
import pytest
import json
import base64

# scope function biar gunakan 1 browser buat setiap function
@pytest.fixture(scope="function")
def driver():
    setup_driver = SetupDriver()
    yield setup_driver.driver
    setup_driver.driver.quit()

def test_loginPhonePanjang(driver):
    login = LoginPage(driver)
    login.open()
    login.goToLogin()
    login.inputFormLoginHP("899777583838383", "1234AAaa")
    assert login.assertButtonLoginDisabled()

def test_phoneEmpty(driver):
    login = LoginPage(driver)
    login.open()
    login.goToLogin()
    login.inputFormLoginHP(" ", " ")
    assert login.assertButtonLoginDisabled()

def test_phoneDikit(driver):
    login = LoginPage(driver)
    login.open()
    login.goToLogin()
    login.inputFormLoginHP("899777", " ")
    assert login.assertButtonLoginDisabled()

def test_loginUnregistered(driver):
    login = LoginPage(driver)
    login.open()
    login.goToLogin()
    login.inputFormLoginHP("899777858585", "1234AAaa")
    login.clickButtonLogin()
    assert login.assertLoginUnregistered()

def test_emailEmpty(driver):
    login = LoginPage(driver)
    login.open()
    login.goToLogin()
    login.inputFormEmail(" ", " ")
    assert login.assertButtonLoginDisabled()

def test_inccorectEmailFormat(driver):
    login = LoginPage(driver)
    login.open()
    login.goToLogin()
    login.inputFormEmail("baskara@gmail", " ")
    assert login.assertInccorectFormat()

def test_unregisteredEmail(driver):
    login = LoginPage(driver)
    login.open()
    login.goToLogin()
    login.inputFormEmail("baskara9023@gmail.com", "1234AAaa")
    login.clickButtonLogin()
    assert login.assertLoginUnregistered()

def test_loginWrongPW(driver):
    login = LoginPage(driver)
    login.open()
    login.clickLogin('8997775838', 'passwordsalah')
    assert login.assertWrongPassword()
    login.closeBrowser()

def test_loginSukses(driver):
    login = LoginPage(driver)
    login.open()
    with open('testdata/config.json') as json_file:
        data = json.load(json_file)
    username = data["username"]
    password = data["password"]
    login.clickLogin(username, password)
    assert login.assertSuccessLogin()
    login.closeBrowser()


