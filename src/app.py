from static.html import *
from apps.register_protocols import register_protocols
from apps.utils import logs
import os

LOGS_REG_PROTOCOL =  'src/apps/data/register_protocol.log'

page_config()
logo()
automation = menu()
baseboard()
if automation == 'Preencher Protocolos':
    tab = tabs()
    with tab[0]:
        register_protocols()
    with tab[1]:
        
        if os.path.isfile(LOGS_REG_PROTOCOL):
            logs.visualize(LOGS_REG_PROTOCOL)