from selenium import webdriver
from fake_useragent import UserAgent

class Driver:
    def __init__(self, browser):
        self.browser = browser
        self.ua = UserAgent()
    
    def _select_driver(self):
        match self.browser:
            case 'Chrome':
                return webdriver.ChromeOptions(), webdriver.Chrome
            case 'Edge':
                return webdriver.EdgeOptions(), webdriver.Edge

    def _options(self):
        options, _ = self._select_driver()
        options.add_argument("--flag-switches-begin")
        options.add_argument("--flag-switches-end")
        options.add_argument("--origin-trial-disabled-features=WebGPU")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('start-maximized')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument(f'--user-agent={self.ua.random}')
        options.add_argument('--disable-notifications')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument('--remote-debugging-port=9922')
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        return options
    
    def get(self):
        _, navigator = self._select_driver()
        driver = navigator(options=self._options())
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
        return driver