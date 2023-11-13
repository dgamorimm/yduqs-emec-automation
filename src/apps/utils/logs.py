from st_aggrid import AgGrid, AgGridTheme, ColumnsAutoSizeMode
import streamlit as st
import pandas as pd
import os

def title(title_text:str):
    st.markdown(f"## *{title_text}*")  

def visualize(file_path:str):
    logs = pd.read_csv(file_path, sep='|', names=['datetime', 'app', 'level', 'name', 'function', 'line', 'message'])
    AgGrid(logs, theme=AgGridTheme.ALPINE, columns_auto_size_mode= ColumnsAutoSizeMode.FIT_CONTENTS)

def log_monitor(file_path:str):
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        if file_size < 1024 * 1024 * 1024:
            print(f'O arquivo {file_path} existe e é menor que 1GB.')
        else:
            os.remove(file_path)