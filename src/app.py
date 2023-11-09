from static.html import *
from apps.fill_protocols import fill_protocols

page_config()
side_bar()
logo()
tab = tabs()
with tab[0]:
    fill_protocols()
with tab[1]:
    ...