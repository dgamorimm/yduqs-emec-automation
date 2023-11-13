from streamlit.components import v1 as components
import streamlit as st

def page_config():
    st.set_page_config(
    page_title="YDUQS - Automation",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': "mailto:douglas_amorimm@outlook.com",
        'About': "Versão: 0.0.1"
    }
)

def tabs():
    title_tabs = ['Execução', 'Logs']
    tabs = st.tabs(title_tabs)
    return tabs

def logo():
    url_img = 'https://yt3.googleusercontent.com/Zw6DksF6r6iGrKd2_IoqY93NXDtvS6D-8qWfUjw8ImZvA39QrUUQw4f2cFnA7y39-Oy8GFAn=s176-c-k-c0x00ffffff-no-rj'

    logo = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            .container {{
                position: relative;
                text-align: center;
            }}

            .imagem {{
                width: 120px;
                height: 120px;
                border-radius: 40px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <img class="imagem" src="{url_img}" alt="YDUQS">
        </div>
    </body>
    </html>
    """
    return components.html(html=logo)

def menu():
    st.sidebar.title('Automações')
    with st.sidebar.expander('e-MEC'):
        options = ['Preencher Protocolos', 'Outros']
        return st.radio('Escolha a automação',key='automation', options=options)

def baseboard():
    st.sidebar.markdown("""
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        <br>
                        
                        <style>
                        a {
                            text-decoration: none;
                        }
                        </style>
                        
                        <hr>
                        
                        *Desenvolvido por [Douglas Amorim](https://www.linkedin.com/in/douglas--amorim/)   <img src="https://cdn.icon-icons.com/icons2/1996/PNG/512/linkedin_network_people_professional_profile_services_users_icon_123279.png" height="20">*
                        """,
   unsafe_allow_html=True)