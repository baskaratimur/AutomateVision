from utils.setup import SetupDriver
from pages.regisPage import registerPage
from utils.generate import Generate
import pytest
import json
import base64

@pytest.fixture(scope='function')
def driver():
    setup_driver = SetupDriver()
    yield setup_driver.driver
    setup_driver.driver.quit()

def test_registerPhonePanjang(driver):
    register = registerPage(driver)
    register.open()
    register.goToRegister()
    register.inputFormRegis("89977758388888", "1234AAaa")
    assert register.assertInvalidData()

def test_registerPhonePendek(driver):
    register = registerPage(driver)
    register.open()
    register.goToRegister()
    register.inputFormRegis("899777", "1234AAaa")
    assert register.assertInvalidData()

def test_registerPasswordPendek(driver):
    register = registerPage(driver)
    register.open()
    register.goToRegister()
    register.inputFormRegis("8997775838", "1234Aa")
    assert register.assertInvalidData()

def test_emptyOTP(driver):
    register = registerPage(driver)
    generate = Generate()
    register.open()
    register.goToRegister()
    username = generate.angkaRandom()
    register.inputFormRegis(username, "1234AAaa")
    register.clickSendOTP()
    register.assertButtonRegisterDisabled()

def test_registerWrongOTP(driver):
    register = registerPage(driver)
    generate = Generate()
    register.open()
    register.goToRegister()
    username = generate.angkaRandom()
    register.inputFormRegis_clickRegis(username, "1234AAaa")
    assert register.assertOTPSalah()

def test_registerSuccess(driver):
    register = registerPage(driver)
    generate = Generate()
    register.open()
    register.goToRegister()
    with open('testdata/config.json') as json_file:
        data = json.load(json_file)
    password = data["password"]
    username = generate.angkaRandom()
    register.inputFormRegis_clickRegis(username, password)
    assert register.assertDiscoverProfile()

def test_registerEmailSuccess(driver):
    register = registerPage(driver)
    generate = Generate()
    register.open()
    register.goToRegister()
    angkarandom = generate.angkaRandom()
    username = "automate"+angkarandom+"@visionplus.id"
    with open('testdata/config.json') as json_file:
        data = json.load(json_file)
    password = data['password']
    register.inputFormRegisEmail(username, password)
    register.clickSendOTP()
    register.clickButtonRegister(username)
    assert register.assertDiscoverProfile(), "Register Fail"


def test_accountRegistered(driver):
    register = registerPage(driver)
    register.open()
    register.goToRegister()
    register.inputFormRegis("8997775838", "1234AAaa")
    register.clickSendOTP()
    assert register.assertAccountRegistered()

def test_accountEmailEmpty(driver):
    register = registerPage(driver)
    register.open()
    register.goToRegister()
    register.inputFormRegisEmail(" ", " ")
    assert register.assertButtonRegisterDisabled()

def test_accountInvalidEmail(driver):
    register = registerPage(driver)
    generate = Generate()
    register.open()
    register.goToRegister()
    angkarandom = generate.angkaRandom()
    username = "baskarati"+angkarandom+"@mncgr1"
    register.inputFormRegisEmail(username, " ")
    assert register.assertInvalidEmail()

def test_clickOTP2times(driver):
    register = registerPage(driver)
    generate = Generate()
    register.open()
    register.goToRegister()
    with open('testdata/config.json') as json_file:
        data = json.load(json_file)
    password = data["password"]
    username = generate.angkaRandom()
    register.inputFormRegis_clickRegis_2menit(username, password)
    assert register.assertOTP2times()
    