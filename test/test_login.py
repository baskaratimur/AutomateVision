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

def test_loginPhoneMaxCharacters(driver):
    login = LoginPage(driver)
    login.openWebsite()
    login.clickButtonToLogin()
    login.inputFormLoginHP("899777583838383", "1234AAaa")
    assert login.assertButtonLoginDisabled()

def test_phoneEmpty(driver):
    login = LoginPage(driver)
    login.openWebsite()
    login.clickButtonToLogin()
    login.inputFormLoginHP(" ", " ")
    assert login.assertButtonLoginDisabled()

def test_phoneSmallCharacters(driver):
    login = LoginPage(driver)
    login.openWebsite()
    login.clickButtonToLogin()
    login.inputFormLoginHP("899777", " ")
    assert login.assertButtonLoginDisabled()

def test_loginUnregistered(driver):
    login = LoginPage(driver)
    login.openWebsite()
    login.clickButtonToLogin()
    login.inputFormLoginHP("899777858585", "1234AAaa")
    login.clickLogin()
    assert login.assertLoginUnregistered()

def test_emailEmpty(driver):
    login = LoginPage(driver)
    login.openWebsite()
    login.clickButtonToLogin()
    login.inputFormEmail(" ", " ")
    assert login.assertButtonLoginDisabled()

def test_inccorectEmailFormat(driver):
    login = LoginPage(driver)
    login.openWebsite()
    login.clickButtonToLogin()
    login.inputFormEmail("baskara@gmail", " ")
    assert login.assertInccorectFormat()

def test_unregisteredEmail(driver):
    login = LoginPage(driver)
    login.openWebsite()
    login.clickButtonToLogin()
    login.inputFormEmail("baskara9023@gmail.com", "1234AAaa")
    login.clickLogin()
    assert login.assertLoginUnregistered()

def test_loginWrongPW(driver):
    login = LoginPage(driver)
    login.openWebsite()
    login.loginUser('8997775838', 'passwordsalah')
    assert login.assertWrongPassword()
    

def test_loginSucces(driver):
    login = LoginPage(driver)
    login.openWebsite()
    with open('testdata/dataUser.json') as json_file:
        data = json.load(json_file)
    username = data["username"]
    password = data["password"]
    login.loginUser(username, password)
    assert login.assertSuccessLogin() == True, "Fail to Login"
    


