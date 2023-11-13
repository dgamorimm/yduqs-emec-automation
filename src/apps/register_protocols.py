from time import sleep
from apps.static.html import *
from apps.web.driver import Driver
from apps.web.tools import Action
from apps.web.elements import TagId, TagClass
from apps.utils.file import read_excel, read_excel_all
from loguru import logger

PREFIX = 'fill_protocols'
URL = 'https://emec.mec.gov.br/ies'
LOG = 'data/register_protocol.log'

logger.add(LOG, format="{time} - {level} - {message}")

id_ = TagId()
class_ = TagClass()

def _register_protocol(attempt:int = 0, error:str = None):
    st.session_state['Progress'] = ('Register Protocol',)
    url = st.session_state[f'link_{PREFIX}']
    if attempt <= 3:
        try:
            logger.info(f"Acessando a página para registra protocolos")
            action.access_page(url, 3)
            driver.execute_script("window.focus();")
            for protocol in read_excel_all(excel_file_protocol):
                period, discipline, hours, menu, basic_blb, complement_blb = protocol
                logger.info(f"Cadastrando o protocolo da disciplina: {discipline}")
                action.click(id_.register_protocol, 2)
                action.select(id_.register_protocol_discipline, discipline, 'name')
                action.select(id_.register_protocol_period, period, 'name')
                action.text_clear(id_.register_protocol_hours)
                action.text_input(id_.register_protocol_hours, hours)
                action.text_clear(id_.register_protocol_menu)
                action.text_input(id_.register_protocol_menu, menu)
                action.text_clear(id_.register_protocol_basic_blb)
                action.text_input(id_.register_protocol_basic_blb, basic_blb)
                action.text_clear(id_.register_protocol_complement_blb)
                action.text_input(id_.register_protocol_complement_blb, complement_blb)
                action.click(id_.register_protocol_save, 2)
                action.alert_accept()
                logger.success(f"Protocolo cadastrado")
                sleep(2)
            return True, {}
        except Exception as error:
            attempt =+ 1
            return _register_protocol(attempt, str(error))
    return False, {'Error' : str(error)}
    
def _register_discipline(attempt:int = 0, error:str = None):
    st.session_state['Progress'] = ('Register Discipline',)
    url = 'https://emec.mec.gov.br/modulos/visao_ies/php/ies_componente_curricular.php?'
    if attempt <= 3:
        try:
            logger.info("Acessando a página para cadastrar disciplina")
            action.access_page(url, 3)
            driver.execute_script("window.focus();")
            for discipline in read_excel(excel_file_protocol, 2):
                logger.info(f"Cadastrando a disciplina: {discipline}")
                action.click(id_.register_discipline,2)
                action.text_clear(id_.register_discipline_name)
                action.text_input(id_.register_discipline_name, discipline)
                action.select(id_.register_discipline_status,'S')
                action.click(id_.register_discipline_save,2)
                action.alert_accept()
                logger.success(f"Disciplina cadastrada")
                sleep(1)
            return True, {}
        except Exception as error:
            attempt =+ 1
            return _register_discipline(attempt, str(error))
    return False, {'Error' : str(error)}

def _navigate_IES():
    st.session_state['Progress'] = ('Navigate',)
    try:
        logger.info("Acessando a página inicial")
        action.access_page(URL, 3)
        logger.info("Clicando no pop-up")
        action.click(id_.alert_proto,1)
        logger.info("Clicando no login")
        action.click(class_.sign_in,2)
        logger.info("Pesquisando a IES")
        action.text_input(id_.search_ies, st.session_state[f'link_discipline_{PREFIX}'])
        sleep(8)
        logger.info("Clicando na IES")
        action.click(class_.ies,2)
        return True, {}
    except Exception as error:
        logger.error(str(error))
        return False, {'Error' : str(error)}

def login_emec():
    st.session_state['Progress'] = ('Login',)
    global driver
    global action
    logger.info(" ================ START ================ ")
    logger.info("Acionando o driver")
    driver = Driver().get()
    action = Action(driver)
    logger.info("Acessando a página de login")
    action.access_page(URL, 3)
    driver.execute_script("window.focus();")

def execute_automation():
    st.session_state['Progress'] = ('Processing',)
    navigate, error = _navigate_IES()
    if navigate:
        discipline, error = _register_discipline()
        if discipline:
            protocol, error = _register_protocol()
            if protocol:
                action.close_page()
                st.session_state['Progress'] = ('Success',)
                logger.info(" ================ END ================ ")
                return 'Success'
            else:
                action.close_page()
                st.session_state['Progress'] = ('Error',error)
        else:
            action.close_page()
            st.session_state['Progress'] = ('Error',error)
    else:
        action.close_page()
        st.session_state['Progress'] = ('Error',error) 
    
def register_protocols():
    # st.write(st.session_state)
    if 'Progress' not in st.session_state:
        st.session_state['Progress'] = ('Start',)
    global excel_file_protocol
    
    st.markdown("""## *Inputs*""")    
    excel_file_protocol = st_uploader(f'file_{PREFIX}')
    st_input_text('Insira o link para protocolar', f'link_{PREFIX}')
    st_input_text('Insira o número da IES', f'link_discipline_{PREFIX}')
    
    st.divider()
    st.markdown("""## *Login*""") 
    st_button(login_emec,'Login', 'login_button')
    
    st.divider()    
    st.markdown("""## *Run*""")
    if st.session_state['login_button']:
        st_button(execute_automation, 'Executar', 'login_running')
    else:
        st.warning('⚠ Você tem que realizar o login para executar a automação')
    
    st.divider()    
    st.markdown("""## *Progress*""")
    if st.session_state['Progress'][0] not in ['Success', 'Error']:
        st.info(st.session_state['Progress'][0])
    elif st.session_state['Progress'][0] == 'Success':
        st.markdown("""
                    > *Automação executada com sucesso* ✅
                    """)
    elif st.session_state['Progress'][0] == 'Error':
        st.markdown("""
                    > *Automação com problemas* 🚨
                    """)
        st.error(st.session_state['Progress'][1])