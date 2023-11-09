from static.html import *
from apps.fill_protocols import fill_protocols
from selenium import webdriver
import streamlit as st

# Caminho para o seu driver
driver_path = '/caminho/para/o/seu/driver'

# Cria uma nova instância do driver
driver = webdriver.Chrome(driver_path)

# Agora você pode usar o driver para controlar o navegador
driver.get('https://www.google.com')

side_bar()
logo()

fill_protocols()