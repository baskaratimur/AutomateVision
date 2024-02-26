from utils.setup import SetupDriver
from pages.tvpage import Tvpage
from pages.loginpage import LoginPage
import pytest 

@pytest.fixture(scope="module")
def driver():
    setup_driver = SetupDriver()
    yield setup_driver.driver
    setup_driver.driver.quit()

def test_watchTV(driver):
    tvpage = Tvpage(driver)
    login = LoginPage(driver)
    login.open()
    login.clickLogin("8997775838", "4321lupa")
    tvpage.goTvpage()
    assert tvpage.tvPlay()

def test_watchPause(driver):
    tvpage = Tvpage(driver)
    tvpage.tvPause()
    
    
    

