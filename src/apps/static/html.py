import streamlit as st

def st_uploader(key_name_file:str):
    return st.file_uploader(
    'Suba seu arquivo aqui',
    type=['xlsx'],
    key=key_name_file
    )

def st_login():
    st.text_input('CPF', max_chars=11, key='cpf')
    st.text_input('Senha', type='password', key='password')

def st_input_text(label:str, key_name_link:str):
    return st.text_input(label,key=key_name_link)

def st_button(function_name, name:str, key_name_button:str, params:tuple = None):
    if params:
        return st.button(
            name,
            type='primary',
            on_click=function_name,
            args=params,
            key=key_name_button,
            use_container_width = True
        )
    else:
        return st.button(
            name,
            type='primary',
            on_click=function_name,
            key=key_name_button,
            use_container_width = True
        )