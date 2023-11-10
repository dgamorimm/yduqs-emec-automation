from time import sleep
from apps.static.html import *
from apps.web.driver import Driver
from apps.web.tools import Action
from apps.web.elements import TagId, TagClass, TagXPath, TagCSS
from selenium.webdriver.common.keys import Keys
import pyautogui

# URL='https://emec.mec.gov.br/ies'
URL='https://emec.mec.gov.br/emec/nova'
PREFIX = 'fill_protocols'
id_ = TagId()
class_ = TagClass()
xpath_ = TagXPath()
css_ = TagCSS()

def login_emec():
    global driver
    global action
    driver = Driver().get()
    action = Action(driver)
    action.access_page(URL, 3)
    driver.switch_to.window(driver.window_handles[0])
    # sleep(2)
    # driver.execute_script("window.focus();")
    action.click(xpath_.regulation,3)
    action.click(id_.alert_proto,1)
    pyautogui.hotkey('ctrl','n')
    driver.switch_to.window(driver.window_handles[1])
    action.access_page(URL, 3)
    action.click(xpath_.regulation,3)
    action.click(id_.alert_proto,1)
    action.click(class_.sign_in,2)
    action.login(id_.username,
                 id_.password,
                 class_.continue_login,
                 id_.login,
                 st.session_state['cpf'],
                 st.session_state['password'])
    pyautogui.press('enter')

def execute_automation():
    return 'Executado'

def fill_protocols():
    st.write(st.session_state)
    st.markdown("""## *Inputs*""")    
    st_uploader(f'file_{PREFIX}')
    st_input_text('Insira o link para protocolar', f'link_{PREFIX}')
    st_input_text('Insira o número da IES', f'link_discipline{PREFIX}')
    
    st.divider()
    
    st.markdown("""## *Login*""") 

    st_login()
    st_button(login_emec,'Login', 'login_button')
    
    st.divider()    
    st.markdown("""## *Run*""")
    
    if st.session_state['login_button']:
        st_button(execute_automation, 'Executar', 'login_running')
    else:
        st.warning('⚠ Você tem que realizar o login para executar a automação')
    