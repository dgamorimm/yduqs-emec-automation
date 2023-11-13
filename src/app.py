from static.html import *
from apps.register_protocols import register_protocols

page_config()
logo()
automation = menu()
baseboard()
if automation == 'Preencher Protocolos':
    tab = tabs()
    with tab[0]:
        register_protocols()
    with tab[1]:
        ...