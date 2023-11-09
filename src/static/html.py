from streamlit.components import v1 as components
import streamlit as st

def logo():
    url_img = 'https://yt3.googleusercontent.com/Zw6DksF6r6iGrKd2_IoqY93NXDtvS6D-8qWfUjw8ImZvA39QrUUQw4f2cFnA7y39-Oy8GFAn=s176-c-k-c0x00ffffff-no-rj'

    logo = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            .container {{
                position: relative;
                text-align: left;
            }}

            .imagem {{
                width: 650px;
                height: 80px;
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

def side_bar():
    st.sidebar.title('Automações')
    with st.sidebar.expander('e-MEC'):
        st.sidebar.radio('Preencher Protocolos',key='fill_protocols')