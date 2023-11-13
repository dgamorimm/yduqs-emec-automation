from time import sleep
from apps.static.html import *
from apps.web.driver import Driver
from apps.web.tools import Action
from apps.web.elements import TagId, TagClass, TagXPath, TagCSS
from apps.utils.file import read_excel

PREFIX = 'fill_protocols'
URL = 'https://emec.mec.gov.br/ies'

id_ = TagId()
class_ = TagClass()
xpath_ = TagXPath()
css_ = TagCSS()

def _register_protocol():
    try:
        ...
    except Exception as error:
        return False, {'Error' : str(error)}
    
def _register_discipline():
    url = 'https://emec.mec.gov.br/modulos/visao_ies/php/ies_componente_curricular.php?'
    try:
        action.access_page(url, 3)
        driver.execute_script("window.focus();")
        for discipline in read_excel(excel_file_protocol, 2):
            action.click(id_.register_discipline,2)
            action.text_clear(id_.register_discipline_name)
            action.text_input(id_.register_discipline_name, discipline)
            action.select(id_.register_discipline_status,'S')
            action.click(id_.register_discipline_save,2)
            action.alert_accept()
            sleep(2)
        return True, {}
    except Exception as error:
        return False, {'Error' : str(error)}

def _navigate_IES():
    try:
        action.access_page(URL, 3)
        action.click(id_.alert_proto,1)
        action.click(class_.sign_in,2)
        action.text_input(id_.search_ies, st.session_state[f'link_discipline_{PREFIX}'])
        action.click(class_.ies,2)
        return True, {}
    except Exception as error:
        return False, {'Error' : str(error)}

def login_emec():
    global driver
    global action
    driver = Driver().get()
    action = Action(driver)
    action.access_page(URL, 3)
    driver.execute_script("window.focus();")

def execute_automation():
    navigate, error = _navigate_IES()
    if navigate:
        discipline, error = _register_discipline()
        return discipline
    #     if discipline:
    #         protocol, error = _register_protocol()
    #         if protocol:
    #             return 'Executado com Sucesso !!!'
    #         else:
    #             return error
    #     else:
    #             return error
    else:
        return error

def fill_protocols():
    global excel_file_protocol
    st.write(st.session_state)
    st.markdown("""## *Inputs*""")    
    excel_file_protocol = st_uploader(f'file_{PREFIX}')
    st_input_text('Insira o link para protocolar', f'link_{PREFIX}')
    st_input_text('Insira o número da IES', f'link_discipline_{PREFIX}')
    
    st.divider()
    
    # st.markdown("""## *Login*""") 

    # st_login()
    st_button(login_emec,'Login', 'login_button')
    
    st.divider()    
    st.markdown("""## *Run*""")
    
    if st.session_state['login_button']:
        st_button(execute_automation, 'Executar', 'login_running')
    else:
        st.warning('⚠ Você tem que realizar o login para executar a automação')