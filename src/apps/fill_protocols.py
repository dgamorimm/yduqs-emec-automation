from apps.static.html import *
from selenium import webdriver

PREFIX = 'fill_protocols'
st.session_state['login_emec'] = False

def login_emec():
    global driver
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')
    st.session_state['login_emec'] = True

def execute_automation():
    return 'Executado'

def fill_protocols():
    st.markdown("""## *Inputs*""")    
    uploader_file(f'file_{PREFIX}')
    input_link('Insira o link para protocolar', f'link_{PREFIX}')
    input_link('Insira o número da IES', f'link_discipline{PREFIX}')
    
    st.divider()
    
    st.markdown("""## *Login*""") 

    login()
    button(login_emec,'Login')
    
    st.divider()
    st.markdown("""## *Run*""")
    
    if st.session_state['login_emec']:
        button(execute_automation, 'Executar')
    else:
        st.warning('⚠ Você tem que realizar o login para executar a automação')
    