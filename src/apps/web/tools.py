from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located, \
visibility_of_element_located, alert_is_present
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select

class Action():
    def __init__(self, driver) -> None:
        self.driver = driver
        
            
    def find(self, *locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(presence_of_element_located(*locator))

    def find_reduce(self, *locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(presence_of_element_located(*locator))

    def find_v(self, *locator, timeout=2):
        return WebDriverWait(self.driver, timeout).until(visibility_of_element_located(*locator))
    
    def access_page(self, url : str, load_time : int):
        driver = self.driver
        driver.get(url)
        sleep(load_time)
    
    def close_page(self):
        driver = self.driver
        driver.quit()
    
    def text_clear(self, text_tag):
        self.find(text_tag).clear()
        
    def text_input(self,text_tag, text:str):
        self.find(text_tag).send_keys(text)
        
    def login(self,
                     username_tag : str,
                     password_tag : str,
                     continue_tag : str,
                     login_tag : str,
                     username : str,
                     password : str):
        self.find(username_tag).clear()
        self.find(username_tag).send_keys(username)
        sleep(5)
        self.click(continue_tag, 2)
        sleep(5)
        self.find(password_tag).send_keys(password)
        # self.find(password_tag).send_keys(Keys.ENTER)
        self.click(login_tag, 2)

    def frame_switch_id(self, id):
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_id(id))

    def frame_switch_name(self, name):
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_name(name))
    
    def frame_switch_xpath(self, xpath):
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_xpath(xpath))
    
    def click(self,
                        click_tag : str,
                        qty_attempts: int = 5, 
                        attempts : int = 0):
        try:
            self.find(click_tag).click()
            sleep(2)
        except Exception as x:
            print(x)
            sleep(5)
            attempts =+ 1
            if attempts <= qty_attempts:
                return self.click_element(click_tag, attempts)
            else:
                raise('Não foi possivel clicar no elemento')
            
    def select(self, select_tag, value_tag):
        select = Select(self.find((select_tag)))
        select.select_by_value(value_tag)
    
    def alert_accept(self, timeout=10):
        alert = WebDriverWait(self.driver, timeout).until(alert_is_present(),
                                    'Tempo limite esgotado aguardando o pop-up de alerta aparecer.')
        alert.accept()