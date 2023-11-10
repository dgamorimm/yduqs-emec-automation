from selenium.webdriver.common.by import By

class TagId:
    def __init__(self) -> None:
        self.username = (By.ID, 'accountId')
        self.password = (By.ID, 'password')
        self.alert_proto = (By.ID, 'inputPrototypeButton1')
        self.login = (By.ID, 'submit-button')

class TagClass:
    def __init__(self) -> None:
        self.sign_in = (By.CLASS_NAME, 'sign-in-govBr')
        self.continue_login = (By.CLASS_NAME, 'button-continuar')

class TagXPath:
    def __init__(self) -> None:
        self.regulation = (By.XPATH, '//img[@src="/emec/img/novo-layout/regulacao_avaliacao_inativo_.gif"]')

class TagCSS:
    def __init__(self) -> None:
        self.regulation = (By.CLASS_NAME, '#tabs1 > ul > li:nth-child(4) > a > img')