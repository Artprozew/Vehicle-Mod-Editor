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
import time
import datetime # we wouldnt need these neither pytz
import pytz
import vehiclepage
import weaponpage
from variables import *
from languages import *

#  15/01/2021
#  Feito por Artprozew

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
    tab_text = event.widget.tab(selected_tab, "text")'''

tab0 = ttk.Frame(tab_parent)
#tabhelp = ttk.Frame(tab_parent)
tab_parent.add(tab0, text=texts['home1'])
#tab_parent.add(tabhelp, text=texts['help1'])


tab_parent.grid(padx=5, pady=5, column=0, row=0)

def pedpage():
    print('a')

vehiclebutton = Button(tab0, text=texts['vehbutton1'], command=vehiclepage.vehpage, width=80, borderwidth=2)
vehiclebutton.grid(padx=5, pady=5, column=0, row=1)

weaponsbutton = Button(tab0, text=texts['weapbutton1'], command=weaponpage.weappage, width=80, borderwidth=2)
weaponsbutton.grid(padx=5, pady=5, column=0, row=2)

pedsbutton = Button(tab0, text=texts['pedsbutton1'], command=pedpage, width=80, borderwidth=2)
pedsbutton.grid(padx=5, pady=5, column=0, row=3)

# ======================== TAB 5 ========================

'''infolabel = Label(tab5, text=texts['infolabel1'])
infolabel.grid(padx=80, pady=5, column=0, row=0)

warnlabel = Label(tab5, text=texts['warnlabel1'])
warnlabel.grid(padx=5, pady=5, column=0, row=1)

contact = Label(tab5, text='Discord: Artprozew#5202')
contact.grid(padx=5, pady=0, column=0, row=22, sticky=W+S)'''




root.mainloop()
