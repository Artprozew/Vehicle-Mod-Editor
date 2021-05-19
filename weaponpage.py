from tkinter import *
from variables import *
from languages import *

def weappage():
    for k in tab:
        if tab[k].winfo_exists():
            tab[k].destroy()

    tab['weapini'] = ttk.Frame(tab_parent)
    tab['weaplines'] = ttk.Frame(tab_parent)
    tab['weapsound'] = ttk.Frame(tab_parent)
    tab_parent.add(tab['weapini'], text=texts['configini1'])
    tab_parent.add(tab['weaplines'], text=texts['vehlines1'])
    tab_parent.add(tab['weapsound'], text=texts['vehsound2'])

    