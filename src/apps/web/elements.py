from selenium.webdriver.common.by import By

class TagId:
    def __init__(self) -> None:
        self.username = (By.ID, 'accountId')
        self.password = (By.ID, 'password')
        self.alert_proto = (By.ID, 'inputPrototypeButton1')
        self.login = (By.ID, 'submit-button')
        self.search_ies = (By.ID, 'pesq_nome')
        self.register_discipline = (By.ID, 'cadastrar_componente')
        self.register_discipline_name = (By.ID, 'txtDsDisciplina')
        self.register_discipline_status = (By.ID, 'selStatus')
        self.register_discipline_save = (By.ID, 'btnSubmit')
        self.register_protocol = (By.ID, 'componentes_curriculares')
        self.register_protocol_discipline = (By.ID, 'selCoDisciplina')
        self.register_protocol_period = (By.ID, 'selNuPeriodo')
        self.register_protocol_hours = (By.ID, 'txtNuCargaHoraria')
        self.register_protocol_menu = (By.ID, 'txaDsConteudo')
        self.register_protocol_basic_blb = (By.ID, 'txaDsBibliografiaBasica')
        self.register_protocol_complement_blb = (By.ID, 'txaDsBibliografiaComplementar')
        self.register_protocol_save = (By.ID, 'btnSalvarDisciplina')
        

class TagClass:
    def __init__(self) -> None:
        self.sign_in = (By.CLASS_NAME, 'sign-in-govBr')
        self.continue_login = (By.CLASS_NAME, 'button-continuar')
        self.ies = (By.CLASS_NAME, 'corDetalhe_1')

class TagXPath:
    def __init__(self) -> None:
        self.regulation = (By.XPATH, '//img[@src="/emec/img/novo-layout/regulacao_avaliacao_inativo_.gif"]')
        # self.profile_ies = (By.XPATH, "//div[@class='listaPerfis']")
        # self.profile_ies_table = (By.XPATH, './/table')
        # self.profile_ies_table_record = (By.XPATH, './/td')

class TagCSS:
    def __init__(self) -> None:
        self.regulation = (By.CLASS_NAME, '#tabs1 > ul > li:nth-child(4) > a > img')