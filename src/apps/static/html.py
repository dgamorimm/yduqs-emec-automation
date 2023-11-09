import streamlit as st

def uploader_file(key_name_file:str):
    return st.file_uploader(
    'Suba seu arquivo aqui',
    type=['xlsx'],
    key=key_name_file
    )

def login():
    st.text_input('CPF', max_chars=11, key='cpf')
    st.text_input('Senha', type='password', key='password')

def input_link(key_name_link:str):
    return st.text_input('Insera o link aqui',key=key_name_link)

def button(function_name,name:str, params:tuple = None):
    if params:
        return st.button(
            name,
            type='primary',
            on_click=function_name,
            args=params,
            use_container_width = True
        )
    else:
        return st.button(
            name,
            type='primary',
            on_click=function_name,
            use_container_width = True
        )