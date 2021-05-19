# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import webbrowser
import ctypes
import locale
import re
import os
import logging
import sys
import time
import datetime # we wouldnt need this neither pytz
import pytz
import modules
from resources import *
import gettext # pygettext -d base -o core/locales/base.pot core/main.py
#                           # cd /home/runner/Vehicle-Mod-Editor/core/locales
#                           # msgfmt -o base.mo base

#import ipdb # debugging # python -m ipdb core/main.py

#en = gettext.translation(get_filename(__file__), localedir='core/locales', languages=['en'])
#en.install()
#_ = en.gettext
#_ = gettext.gettext
gettext.install('base')

#  15/01/2021
#  Made by Artprozew

#raise RuntimeError('test main')
logger.info(__file__ + ' initialized')
#raise RuntimeError('teste')

def Alarme(): return True

def ShowTime(): # remove this before releasing idiot
    tz = pytz.timezone('Brazil/East')
    timeanddate = datetime.datetime.now(tz)
    daynumber = timeanddate.weekday()
    dayname = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    searchall = re.search('(\d+)-(\d+)-(\d+)\s+(\d+):(\d+):\d+\.\d+', str(timeanddate))
    if searchall:
        year = searchall.group(1)
        month = searchall.group(2)
        day = searchall.group(3)
        hour = searchall.group(4)
        minute = searchall.group(5)
        dayofweek = dayname[daynumber]
        if not daynumber == 5 and not daynumber == 6:
            dayofweek = '{}-Feira'.format(dayofweek)
        stringtime = 'Data: {}/{}/{}, {}\nHora: {}:{}'.format(day, month, year, dayofweek, hour, minute)
        if int(hour) > 5 and int(hour) < 8 and Alarme:
            print('VAI DORMIR\nVAI DORMIR\nVAI DORMIR\t\tVAI DORMIR\nVAI DORMIR\t\tVAI DORMIR\nVAI DORMIR\t\tVAI DORMIR')
        return stringtime
print(ShowTime())


root.title('Vehicle Mod Editor v0.4.3')
root.geometry('830x430')
root.resizable(0, 0)
#frame = Frame(root, width=200, height=200).grid()

if os.path.isfile('vme.ico'):
    root.iconbitmap('vme.ico')

'''def on_tab_selected(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, 'text')'''

tab0 = ttk.Frame(tab_parent)
#tabhelp = ttk.Frame(tab_parent)
tab_parent.add(tab0, text=_('Início'))
#tab_parent.add(tabhelp, text=texts['help1'])
tab_parent.grid(padx=5, pady=5, column=0, row=0)

def VehiclesTabs():
    for k in tab:
        if tab[k].winfo_exists():
            tab[k].destroy()

    tab['configini'] = ttk.Frame(tab_parent)
    tab['lines'] = ttk.Frame(tab_parent)
    tab['sound'] = ttk.Frame(tab_parent)
    tab['vehnpcs'] = ttk.Frame(tab_parent)
    tab['idlist'] = ttk.Frame(tab_parent)
    tab_parent.bind('<<NotebookTabChanged>>', on_tab_selected)
    tab_parent.add(tab['configini'], text=_('Config .ini'))
    tab_parent.add(tab['lines'], text=_('Linhas'))
    tab_parent.add(tab['sound'], text=_('Sons'))
    tab_parent.add(tab['vehnpcs'], text=_("Veículos de NPCs"))
    tab_parent.add(tab['idlist'], text=_("Lista de IDs"))
    tab_parent.grid(padx=5, pady=5, column=0, row=0, sticky=(N,S,E,W))
    '''for i in tab:
        tab[i].columnconfigure((0,5), weight=1)
    tab_parent.columnconfigure((0,5), weight=1)
    tab_parent.grid_columnconfigure((0,5), weight=1)
    tab_parent.rowconfigure((0,5), weight=1)
    tab_parent.grid_rowconfigure((0,5), weight=1)
    style = Style(tab_parent)
    style.theme_use('clam')'''
    '''style = Style()
    style.configure('TButton', font =('calibri', 20, 'bold'), borderwidth = '4')
    style.map('TButton', foreground = [('active', 'disabled', 'green')], background = [('active', 'black')])'''


def on_tab_selected(event):
    selected = tab_parent.tab(tab_parent.select(), 'text')
    for k, v in tab.items():
        #print(k, v)
        tabtext = tab_parent.tab(tab[k])['text']
        if tabtext == selected:
            call_func = getattr(sys.modules['modules.vehicles.{0}'.format(k)], k)
            call_func()
            #locals()tab[k]()

            
def pedpage():
    print('a')

vehiclebutton = Button(tab0, text=_('Vehicles'), command=VehiclesTabs, width=80, borderwidth=2)
vehiclebutton.grid(padx=5, pady=5, column=0, row=1)

weaponsbutton = Button(tab0, text=_('Weapons'), command=VehiclesTabs, width=80, borderwidth=2)
weaponsbutton.grid(padx=5, pady=5, column=0, row=2)

pedsbutton = Button(tab0, text=_('Peds'), command=pedpage, width=80, borderwidth=2)
pedsbutton.grid(padx=5, pady=5, column=0, row=3)

# ======================== TAB 5 ========================

'''infolabel = Label(tab5, text=texts['infolabel1'])
infolabel.grid(padx=80, pady=5, column=0, row=0)

warnlabel = Label(tab5, text=texts['warnlabel1'])
warnlabel.grid(padx=5, pady=5, column=0, row=1)

contact = Label(tab5, text='Discord: Artprozew#5202')
contact.grid(padx=5, pady=0, column=0, row=22, sticky=W+S)'''


root.mainloop()