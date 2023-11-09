import streamlit as st

def uploader_file(key_name_file:str):
    return st.file_uploader(
    'Suba seu arquivo aqui',
    type=['xlsx'],
    key=key_name_file
    )

def input_link(key_name_link:str):
    return st.text_input('Insera o link aqui',key=key_name_link)

def button(function_name, params:tuple = None):
    if params:
        return st.button(
            'Executar',
            type='primary',
            on_click=function_name,
            args=params
        )
    else:
        return st.button(
            'Executar',
            type='primary',
            on_click=function_name
        )