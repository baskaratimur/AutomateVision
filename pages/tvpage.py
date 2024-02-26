import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Tvpage:
    def __init__(self, driver):
        self.driver = driver

    def goTvpage(self):
        mainWindow = self.driver.window_handles[0]
        self.driver.switch_to.window(mainWindow)
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.untill(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'My profile')]")))
        except:
            pass
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'My profile')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Live TV')]").click()
        
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='player']")))
       

    def tvPlay(self):
        hoverTV = self.driver.find_element(By.XPATH, "//video[@id = 'video']")
        atribut_hover = hoverTV.get_attribute('title')
        return (atribut_hover)

    def tvPause(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class= 'md-icon-button pause md-button md-ink-ripple']")))
        self.driver.find_element(By.XPATH, "//button[@class= 'md-icon-button pause md-button md-ink-ripple']").click()
        return self.driver.find_element(By.CSS_SELECTOR, "#player > div > div.player-paused.layout-align-center-center.layout-column")





# Live TV')]").click()
# time.sleep(1)
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='player']")))
# hoverTV = driver.find_element(By.XPATH, "//div[@id= 'player']")
# actions = ActionChains(driver)
# actions.move_to_element(hoverTV).perform()
# time.sleep(2)
# hoverTV = driver.find_element(By.XPATH, "//button[@class= 'md-icon-button pause md-button md-ink-ripple']").click()

# time.sleep(10)