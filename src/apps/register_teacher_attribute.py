
from time import sleep
from apps.static.html import *
from apps.web.driver import Driver
from apps.web.tools import Action
from apps.web.elements import TagId, TagClass, TagCSS
from apps.utils.file import read_excel, read_excel_all
from apps.utils import logs
from loguru import logger

PREFIX = 'fill_teacher_attribute'
URL = 'https://emec.mec.gov.br/ies'
LOG = 'src/apps/data/register_teacher_attribute.log'

logger.remove()
logger.add(LOG, format="{time}|register_attribute_teacher|{level}|{name}|{function}|{line}|{message}")

id_ = TagId()
class_ = TagClass()
css_ = TagCSS()

def login_emec(browser):
    logs.log_monitor(LOG)
    st.session_state['Progress'] = ('Login',)
    global driver
    global action
    logger.info(" ================ START ================ ")
    logger.info("Acionando o driver")
    driver = Driver(browser).get()
    action = Action(driver)
    logger.info("Acessando a página de login")
    action.access_page(URL, 3)
    driver.execute_script("window.focus();")

def _register_teacher_attributes(attempt:int = 0, error:str = None):
    st.session_state['Progress'] = ('Register Teacher Attributes',)
    url = st.session_state[f'link_{PREFIX}']
    
    logger.info(f"Acessando a página para modificar os atributos dos docentes")
    action.access_page(url, 3)
    driver.execute_script("window.focus();")
    documents = action.find(css_.teachers_cpfs)
    logger.info(f"Documento :: {documents}")
    for document in documents:
        logger.info(f"Documento :: {document.text}")

def _navigate_IES():
    st.session_state['Progress'] = ('Navigate',)
    try:
        logger.info("Acessando a página inicial")
        action.access_page(URL, 3)
        logger.info("Clicando no pop-up")
        if action.element_exists(tag=id_.alert_proto, timeout=5):
            action.click(id_.alert_proto,1)
        logger.info("Clicando no login")
        action.click(id_.sign_in,2)
        logger.info("Pesquisando a IES")
        action.text_input(id_.search_ies, st.session_state[f'link_discipline_{PREFIX}'],'slow')
        sleep(8)
        logger.info("Clicando na IES")
        action.click(class_.ies,2)
        return True, {}
    except Exception as error:
        logger.error(str(error))
        return False, {'Error' : str(error)}

def execute_automation():
        st.session_state['Progress'] = ('Processing',)
        navigate, error = _navigate_IES()
        if navigate:
            _register_teacher_attributes()
            logger.info(" ================ END ================ ")
            return 'Success'
        else:
            action.close_page()
            st.session_state['Progress'] = ('Error',error)

def register_teacher_attribute():
    # st.write(st.session_state)
    if 'Progress' not in st.session_state:
        st.session_state['Progress'] = ('Start',)
    global excel_file_teacher_attribute
    
    st.markdown("""## *Browser*""")
    browser = st_radio_button('Escolha o navegador:', ['Chrome', 'Edge'], True)
    
    st.divider()
    st.markdown("""## *Inputs*""")    
    excel_file_teacher_attribute = st_uploader(f'file_{PREFIX}')
    st_input_text('Insira o link direto para preencher os atributos', f'link_{PREFIX}')
    st_input_text('Insira o número da IES', f'link_discipline_{PREFIX}')
    
    st.divider()
    st.markdown("""## *Login*""") 
    st_button(login_emec,'Login', 'login_button', (browser, ))
    
    st.divider()
    st.markdown("""## *Run*""")
    if st.session_state['login_button']:
        st_button(execute_automation, 'Executar', 'login_running')
    else:
        st.warning('⚠ Você tem que realizar o login para executar a automação')
        
    
    