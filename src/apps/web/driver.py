from selenium import webdriver
from fake_useragent import UserAgent

class Settings:
    
    def __init__(self):
        self.opp = webdriver.ChromeOptions()
        self.ua = UserAgent()
    
    def options(self):
          
        self.opp.add_argument("--flag-switches-begin")
        self.opp.add_argument("--flag-switches-end")
        self.opp.add_argument("--origin-trial-disabled-features=WebGPU")
        self.opp.add_argument('--disable-dev-shm-usage')
        self.opp.add_argument('start-maximized')
        self.opp.add_argument('--disable-blink-features=AutomationControlled')
        self.opp.add_argument(f'--user-agent={self.ua.random}')
        self.opp.add_argument('--disable-notifications')
        self.opp.add_argument('--no-sandbox')
        self.opp.add_argument("--disable-extensions")
        self.opp.add_argument("--disable-gpu")
        self.opp.add_argument("--ignore-certificate-errors")
        self.opp.add_argument('--remote-debugging-port=9922')
        self.opp.add_experimental_option('useAutomationExtension', False)
        self.opp.add_experimental_option("excludeSwitches", ["enable-automation"])
        return self.opp

class Driver(Settings):
    
    def __init__(self):
        super().__init__()
    
    def get(self):
        driver = webdriver.Chrome(options=self.options())
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
        return driver