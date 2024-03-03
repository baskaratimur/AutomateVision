from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from objek.objectRegister import RegisterObject
from utils.generate import Generate
from selenium.webdriver.common.keys import Keys
import time
import random
import json
import jsonpath
import requests
import base64

class registerPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.visionplus.id/webclient/#/"
        self.wait = WebDriverWait(self.driver, 30)
        self.register = RegisterObject()
        self.generate = Generate()

    def open(self):
        self.driver.get(self.url)

    def goToRegister(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.register.buttonLoginRegis))).click()
        mainWindow = self.driver.current_window_handle  
        for handle in self.driver.window_handles:  
            if handle != mainWindow:
                self.driver.switch_to.window(handle)
                break
        self.driver.find_element(By.XPATH, self.register.clickRegister).click()

    def inputFormRegis_clickRegis(self, username, password):   
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.register.inputPhone))).send_keys(username)      
        self.driver.find_element(By.XPATH, self.register.inputPassword).send_keys(password)
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.clickSendOtp))).click()
        if password == '1234AAaa':
            self.driver.find_element(By.XPATH, self.register.inputOTP).send_keys(self.generate.endpointOTP("89977758355"))
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.register.formBtonRegister).click()   
        else:
            # generate otp dlu
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.register.inputOTP).send_keys(self.generate.endpointOTP(username))
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.register.formBtonRegister).click()       
            time.sleep(5)
    

    def inputFormRegis(self, username, password):   
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.register.inputPhone))).send_keys(username)      
        self.driver.find_element(By.XPATH, self.register.inputPassword).send_keys(password)
    
    def inputFormRegis_clickRegis_2menit(self, username, password):   
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.register.inputPhone))).send_keys(username)      
        self.driver.find_element(By.XPATH, self.register.inputPassword).send_keys(password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.register.clickSendOtp).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.register.inputOTP).send_keys(self.generate.endpointOTP(username))
        time.sleep(123)
        
    def inputFormRegisEmail(self, username, password):
        time.sleep(1)
        print(username)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register.halamanEmail))).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.register.inputEmail).send_keys(username)
        self.driver.find_element(By.XPATH, self.register.inputPassword).send_keys(password)
        

    def clickSendOTP(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.register.clickSendOtp))).click()
        time.sleep(2)

    def clickButtonRegister(self, username):
        print(username)
        self.driver.find_element(By.XPATH, self.register.inputOTP).send_keys(self.generate.endpointOTP(username))
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.register.clickRegister).click()  
        time.sleep(5)  
        
    def assertInvalidEmail(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.register.formattEmail)))
        
    #assert sendOTP masih tag P bukan button, karena nomor/data salah jadi sendOTP ga bisadiclick
    def assertInvalidData(self):
        return self.driver.find_element(By.XPATH, self.register.clickSendOtpInactive)
    
    # assert message invalidOTP
    def assertOTPSalah(self):
        return self.driver.find_element(By.XPATH, self.register.messageInvalidOTP)
    
    def assertDiscoverProfile(self):
        mainWindow = self.driver.window_handles[0]  
        self.driver.switch_to.window(mainWindow)
        discoverProfil = self.wait.until(EC.presence_of_element_located((By.XPATH, self.register.discoverProfile)))
        return discoverProfil

    def assertButtonRegisterDisabled(self):
        time.sleep(2)
        buttonRegister = self.driver.find_element(By.XPATH, self.register.clickRegister)
        # cek pake isenabled, kalau buttonregisnya disabled, maka kita return true, tapi kalau enable kita return false
        if buttonRegister.is_enabled():
            return True
        else:
            return False 

    def assertOTP2times(self):
        sendOTP2times = self.driver.find_element(By.XPATH, self.register.clickSendOtp)
        enableOTP2times = sendOTP2times.is_enabled()
        return enableOTP2times

    def assertAccountRegistered(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.register.accountRegistered)))

        # inputPhone = self.wait.until(EC.presence_of_element_located((By.XPATH, self.register.inputPhone)))
        # time.sleep(2)
        # inputPhone.send_keys(username)
        # inputPassword = self.driver.find_element(By.XPATH, self.register.inputPassword)
        # inputPassword.send_keys(password)
        # time.sleep(1)
        # # coba cari element send OTP, apakah jadi button atau masih tag
        # # kalau masih tag maka
        # try:
        #     self.driver.find_element(By.XPATH, self.register.clickSendOtpInactive)
        #     for i in range(14):
        #         inputPhone.send_keys(Keys.BACKSPACE)
        #     for i in range(14):
        #         inputPassword.send_keys(Keys.BACKSPACE)
        #     # stop disini, buat assert button sendOTPinactive
        #     time.sleep(1)
        
        # except:
        # # kalau udah jadi button maka, click buttonnya
            
        #     self.wait.until(EC.presence_of_element_located((By.XPATH, self.register.clickSendOtp))).click()

        #     # buat percabangan lagi, untuk case invalidOTP dan regis berhasil
        #     if username == "8997775835512":
        #         self.driver.find_element(By.XPATH, self.register.inputOTP).send_keys(self.generate.endpointOTP("6289977758355"))
        #         self.driver.find_element(By.XPATH, self.register.formBtonRegister).click()
        #         for i in range(14):
        #          inputPhone.send_keys(Keys.BACKSPACE)
        #         for i in range(14):
        #          inputPassword.send_keys(Keys.BACKSPACE)
        #         time.sleep(5)
        #     else:
        #         print(username)
        #         # buat fungsi regis berhasil
        #         self.driver.find_element(By.XPATH, self.register.inputOTP).send_keys(self.generate.endpointOTP(username))
        #         self.driver.find_element(By.XPATH, self.register.formBtonRegister).click()
        #         time.sleep(50)


        



