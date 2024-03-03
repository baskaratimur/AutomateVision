import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from objek.objectLogin import LoginObject
import json

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.visionplus.id'
        self.wait = WebDriverWait(self.driver, 30)
       
        # init class objek bagian login
        self.login = LoginObject()

    def open(self):
        self.driver.get(self.url)
    
    # ke halaman page login
    def goToLogin(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.login.buttonLoginRegis))).click()
        mainWindow = self.driver.current_window_handle  
        for handle in self.driver.window_handles:  
            if handle != mainWindow:
                self.driver.switch_to.window(handle)
                break

    def inputFormLoginHP(self, username, password):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.login.form_inputPhone).send_keys(username)
        self.driver.find_element(By.XPATH, self.login.form_inputPassword).send_keys(password)
    
    def inputFormEmail(self, username, password):
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.login.formEmail))).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.login.form_inputEmail).send_keys(username)
        self.driver.find_element(By.XPATH, self.login.form_inputPassword).send_keys(password)


    def clickButtonLogin(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login.form_buttonLogin))).click()
    
    # buat sukses case, dari click button login regis, input sampe click login lagi
    def clickLogin(self, username, password):
        self.driver.find_element(By.XPATH, self.login.buttonLoginRegis).click()
        mainWindow = self.driver.current_window_handle  
        for handle in self.driver.window_handles:  
            if handle != mainWindow:
                self.driver.switch_to.window(handle)
                break
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.login.form_inputPhone).send_keys(username)
        self.driver.find_element(By.XPATH, self.login.form_inputPassword).send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.login.form_buttonLogin).click()
        # wait ganti window
        time.sleep(5)
       

    def assertInccorectFormat(self):
        return self.driver.find_element(By.XPATH, self.login.inccorectEmailFormat)
    
    def assertButtonLoginDisabled(self):
        buttonLogin = self.driver.find_element(By.XPATH, self.login.form_buttonLogin)
        if buttonLogin.is_enabled():
            return True
        else:
            return False
    
    def assertLoginUnregistered(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.login.popLoginUnregistered)))

    def assertSuccessLogin(self):
        mainWindow = self.driver.window_handles[0]  
        self.driver.switch_to.window(mainWindow)
        # self.wait.until(EC.presence_of_element_located((By.XPATH, self.login.myProfile))).click()
        # time.sleep(10)
        try:
            self.wait.untill(EC.presence_of_element_located((By.XPATH, self.login.form_inputPassword)))
            return False
        except:
            return True

    def closeBrowser(self):
        if self.driver.session_id:
            self.driver.close()

    def assertWrongPassword(self):
        return self.driver.find_element(By.XPATH, self.login.popWrongPW)
