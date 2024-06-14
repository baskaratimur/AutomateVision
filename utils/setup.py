from selenium import webdriver

class SetupDriver:
    def __init__(self, headless=True):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ["enable-logging"])
        if headless:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')  # Optional, but recommended
            options.add_argument('--no-sandbox')   # Recommended if running as root user
            options.add_argument('--disable-dev-shm-usage')  # Recommended to avoid resource issues
            options.add_argument('--window-size=2560x1600')  # Optional, specify window size if needed
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

     

