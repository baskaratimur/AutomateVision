from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.maximize_window()
    
driver.get("https://www.visionplus.id/webclient/#/")
driver.find_element(By.XPATH, '//span[contains(text(), "Log in/Register")]').click()
time.sleep(1)
mainWindow = driver.current_window_handle
time.sleep(2)
for handle in driver.window_handles:
    if handle != mainWindow:
        driver.switch_to.window(handle)
        break
webSkrg = driver.title
print(webSkrg)
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("08997775838")
driver.find_element(By.XPATH, "//input[@id='fld_Password']").send_keys("4321lupa")

# driver.find_element(By.XPATH, "//input[@id='password']").send_keys("4321lupa")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='btn_Login']").click()
time.sleep(5)
windowutama = driver.window_handles[0]
driver.switch_to.window(windowutama)
driver.find_element(By.XPATH, "//div[contains(text(),'Hello!')]")
driver.find_element(By.XPATH, "//span[contains(text(), 'My profile')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(), 'Live TV')]").click()
time.sleep(1)
wait = WebDriverWait(driver, 10)
time.sleep(10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='player']")))
hoverTV = driver.find_element(By.XPATH, "//video[@id = 'video']")
# atribut_hover = hoverTV.get_attribute('paused')
# title_h = hoverTV.get_attribute('title')
# print(atribut_hover)
# print(title_h)
try:
    # get selector element pause
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#player > div > div.player-paused.layout-align-center-center.layout-column")))
    print("element ada")
except:
    print("element tidak ada brarti belom dipause")
    actions = ActionChains(driver)
    actions.move_to_element(hoverTV).perform()
    time.sleep(2)
    hoverPause = driver.find_element(By.XPATH, "//button[@class= 'md-icon-button pause md-button md-ink-ripple']").click()
    # get selector element pause
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#player > div > div.player-paused.layout-align-center-center.layout-column")))
    print("element  ada, sudah kepause, dari variable hoverPause")


time.sleep(1000)


 # ambil file json
        # with open('testdata/config.json') as json_file:
        #     self.data = json.load(json_file)



#         # regis.py?
#         from selenium import webdriver
# import time
# import random
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import json
# import jsonpath
# import requests
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ["enable-logging"])
# driver = webdriver.Chrome(options=options)
# driver.implicitly_wait(10)
# driver.maximize_window()
    
# driver.get("https://www.visionplus.id/webclient/#/")
# driver.find_element(By.XPATH, '//span[contains(text(), "Log in/Register")]').click()
# time.sleep(1)
# mainWindow = driver.current_window_handle
# time.sleep(2)
# for handle in driver.window_handles:
#     if handle != mainWindow:
#         driver.switch_to.window(handle)
#         break
# webSkrg = driver.title
# print(webSkrg)
# driver.find_element(By.XPATH, "//p[contains(text(), 'Register')]").click()
# #  Generate three random digits
# angka_random = ''.join(random.choices('0123456789', k=5))
# angkahp = "8997777"+angka_random
# print(angka_random)
# # Input angka random ke dalam elemen input
# time.sleep(1)
# driver.find_element(By.XPATH, "//input[@id='phone']").send_keys(angkahp)
# driver.find_element(By.XPATH, "//input[@id='fld_Password']").send_keys("4321Lupa")
# time.sleep(2)
# driver.find_element(By.XPATH, "//button[contains(text(), 'Send OTP')]").click()

# url = 'https://vplus-bss.visionplus.id/cms-service/v1/login'
# data ={
#     "email": "baskara@gmail.com",
#     "password": "4321lupa"
# }
# response = requests.post(url, json=data)
# datajson = response.json()
# dataaccess = jsonpath.jsonpath(datajson, "data.token.access_token")[0]
# # endpoint getotp
# url = 'https://vplus-bss.visionplus.id/otp/v1/admin?'
# params = {"recipient": angkahp}  # Mengubah params menjadi dictionary
# headersAuth = {'Authorization': 'Bearer ' + dataaccess}  # Menggunakan dictionary untuk headers
# response = requests.get(url, headers=headersAuth, params=params)
# dataJSONOTP = json.loads(response.text)
# dataOTP = jsonpath.jsonpath(dataJSONOTP, 'data.data[0].OTP')

# time.sleep(2)
# driver.find_element(By.XPATH, "(//input[@class='otp-input'])[1]").send_keys(dataOTP)
# driver.find_element(By.XPATH, "//p[contains(text(), 'Register')]").click()
# print("berhasil regis")
# time.sleep(50)
# # getotp input
# # (//input[@class='otp-input'])[1]

# # # driver.find_element(By.XPATH, "//input[@id='password']").send_keys("4321lupa")
# # time.sleep(1)
# # driver.find_element(By.XPATH, "//button[@id='btn_Login']").click()
# # time.sleep(5)
# # windowutama = driver.window_handles[0]
# # driver.switch_to.window(windowutama)
# # driver.find_element(By.XPATH, "//div[contains(text(),'Hello!')]")
# # driver.find_element(By.XPATH, "//span[contains(text(), 'My profile')]").click()
# # time.sleep(1)
# # driver.find_element(By.XPATH, "//span[contains(text(), 'Live TV')]").click()
# # time.sleep(1)
# # wait = WebDriverWait(driver, 10)
# # time.sleep(10)
# # element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='player']")))
# # hoverTV = driver.find_element(By.XPATH, "//video[@id = 'video']")
# # # atribut_hover = hoverTV.get_attribute('paused')
# # # title_h = hoverTV.get_attribute('title')
# # # print(atribut_hover)
# # # print(title_h)
# # try:
# #     # get selector element pause
# #     element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#player > div > div.player-paused.layout-align-center-center.layout-column")))
# #     print("element ada")
# # except:
# #     print("element tidak ada brarti belom dipause")
# #     actions = ActionChains(driver)
# #     actions.move_to_element(hoverTV).perform()
# #     time.sleep(2)
# #     hoverPause = driver.find_element(By.XPATH, "//button[@class= 'md-icon-button pause md-button md-ink-ripple']").click()
# #     # get selector element pause
# #     element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#player > div > div.player-paused.layout-align-center-center.layout-column")))
# #     print("element  ada, sudah kepause, dari variable hoverPause")


# # time.sleep(1000)


#  # ambil file json
#         # with open('testdata/config.json') as json_file:
#         #     self.data = json.load(json_file)