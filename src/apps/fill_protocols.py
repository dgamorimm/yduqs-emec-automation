from apps.static.html import *

PREFIX = 'fill_protocols'

def execute_automation():
    return 'Executado'

def fill_protocols():
    uploader_file(f'file_{PREFIX}')
    input_link(f'link_{PREFIX}')
    button(execute_automation)