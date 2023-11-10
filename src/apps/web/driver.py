from selenium import webdriver
from fake_useragent import UserAgent
# from fp.fp import FreeProxy

class Settings:
    
    def __init__(self):
        self.opp = webdriver.ChromeOptions()
        self.ua = UserAgent()
        # self.proxy = FreeProxy().get()
    
    def options(self):
          
        self.opp.add_argument("--flag-switches-begin")
        self.opp.add_argument("--flag-switches-end")
        self.opp.add_argument("--origin-trial-disabled-features=WebGPU")
        
        # self.opp.add_argument("--incognito")
        self.opp.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.opp.add_experimental_option('useAutomationExtension', False)
        self.opp.add_argument('--disable-dev-shm-usage')
        self.opp.add_argument('start-maximized')
        self.opp.add_argument('--disable-blink-features=AutomationControlled')
        self.opp.add_argument(f'--user-agent={self.ua.random}')
        self.opp.add_argument('--disable-notifications')
        # self.opp.add_argument(f'--proxy-server={self.proxy}')
        # self.opp.add_argument(f"--profile-directory=Default")
        # self.opp.add_argument(f'--user-data-dir=C:\\Users\\dougl\\development\\src\\apps\\web\\profile')
        self.opp.add_argument('--no-sandbox')
        self.opp.add_argument("--disable-extensions")
        self.opp.add_argument("--disable-gpu")
        self.opp.add_argument("--ignore-certificate-errors")
        self.opp.add_argument('--remote-debugging-port=9922')
        return self.opp

    def service(self):
        return webdriver.ChromeService(executable_path='C:\\Users\\dougl\\development\\src\\apps\\web\\chromedriver\\chromedriver.exe')

class Driver(Settings):
    def __init__(self):
        super().__init__()
    
    
    def get(self):
        service = self.service()
        service.start()
        driver = webdriver.Chrome(service=service.service_url, options=self.options())
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
        return driver