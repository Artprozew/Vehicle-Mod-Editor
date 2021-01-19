import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser
import ctypes
import locale
import re
import os
import time

#  15/01/2021
#  Feito por Artprozew#5202

appname = 'SA Mod Editor'

root = tk.Tk()
root.title(appname)
root.geometry('630x375')
root.resizable(0, 0)

frame = Frame(root, width=200, height=200).grid()

windll = ctypes.windll.kernel32
windll.GetUserDefaultUILanguage()
lang = locale.windows_locale[windll.GetUserDefaultUILanguage()]  #  Língua usada no windows atualmente
#lang = 'en_US'
if lang == 'pt_BR' or lang == 'pt_PT':
    texts = {
    'configini1':'Config .ini',
    'vehlines1':'Linhas',
    'vehsound1':'Sons',
    'npcs1':'Veículos de NPCs',
    'help1':'Ajuda e Info',
    'inipath1':'Caminho para o \'.ini\'',
    'path1':'Caminho para o mod',
    'modname1':'Nome do mod',
    'newname1':'Novo nome do mod',
    'vehname1':'Novo nome do veículo',
    'newid1':'Novo ID do veículo',
    'tip':'Dica: você pode inserir o nome acima ou escolher na lista abaixo',
    'class1':'Classe do veículo',
    'disable1':'NENHUM',
    'vehsound1':'Som do veículo',
    'cfgpath1':'Caminho para o \'vehicleAudioSettings.cfg\'',
    'newveh1':'Nome do mod',
    'vehaudio1':'Nome do veículo para transferir o som',
    'poppath1':'Caminho para o \'cargrp.dat\'',
    'popveh1':'Nome do veículo para inserir',
    'popitem1':'Escolha o grupo',
    'warning1':'Aviso',
    'warn1':'\'Novo nome do mod\' não pode ter mais de 7 caracteres!',
    'apply1':'Aplicar',
    'default1':'PADRÃO',
    'infolabel1':'Se você precisar de ajuda, clique "Mais informações" abaixo para entender\n melhor como funciona. Esse programa irá facilitar e agilizar esse processo.',
    'info':'Mais informações',
    'needed':'Necessidades',
    'vehmodelswarn':'NÃO EDITE ESSA LINHA CASO USE O OPEN LIMIT ADJUSTER\nDESATIVE-A DESMARCANDO NA CAIXA AO LADO\nvá na aba ajuda para saber mais',
    'warnlabel1':'INCOMPATÍVEL COM:\nVersões do Tuning Mod v1.5 ou ANTERIORES\nVersões do Real Traffic Fix v1.2 ou ANTERIORES\nAtualizações OFICIAIS do First Person Mod',
    'handcfg1':'Apply \'handling.cfg\' patch (0|1)',
    'audio1':'Enable vehicle audio loader (0|1)',
    'handlines1':'Number of standard lines',
    'vehmodels1':'Vehicle Models',
    'killable1':'Count of killable model IDs',
    'bike1':'Number of bike lines',
    'plane1':'Number of flying lines',
    'boat1':'Number of boat lines'
    }
else:
    texts = {
    'configini1': 'Config .ini',
    'vehlines1': 'Lines',
    'vehsound1': 'Sounds',
    'npcs1': 'NPCs vehicles',
    'help1': 'Help and Info',
    'inipath1':'Path to \'.ini\' file',
    'path1':'Mod path',
    'modname1':'Mod name',
    'newname1':'New mod name',
    'vehname1':'New vehicle name',
    'newid1':'New vehicle ID',
    'tip':'Tip: you can insert the name above or choose on the list below',
    'class1':'Vehicle class',
    'disable1':'NONE',
    'vehsound1':'Vehicle sound',
    'cfgpath1':'Path to \'vehicleAudioSettings.cfg\'',
    'newveh1':'Mod name',
    'vehaudio1':'Vehicle name to get audio from',
    'poppath1':'Path to \'cargrp.dat\'',
    'popveh1':'Vehicle name to insert',
    'popitem1':'Choose group',
    'warning1':'Warning',
    'warn1':'\'New mod name\' cannot have more than 7 characters!',
    'apply1':'Apply',
    'default1':'DEFAULT',
    'infolabel1': 'If you need help, click "More info" down below to understand\nbetter how it works. This program will make this process easier and faster.',
    'info': 'More info',
    'needed': 'Needs',
    'vehmodelswarn': 'DO NOT EDIT THIS LINE IF YOU ARE USING THE OPEN LIMIT ADJUSTER\nDISABLE IT BY UNMARKING THE CHECKBOX\ngo to the help tab to understand why',
    'warnlabel1': 'INCOMPATIBLE WITH:\nTuning Mod v1.5 or PREVIOUS versions\nReal Traffic Fix v1.2 or PREVIOUS versions\nOFFICIAL updates from First Person Mod',
    'handcfg1': 'Apply \'handling.cfg\' patch (0|1)',
    'audio1': 'Enable vehicle audio loader (0|1)',
    'handlines1': 'Number of standard lines',
    'vehmodels1': 'Vehicle Models',
    'killable1': 'Count of killable model IDs',
    'bike1': 'Number of bike lines',
    'plane1': 'Number of flying lines',
    'boat1': 'Number of boat lines'
    }

'''def on_tab_selected(event):
    selected_tab = event.widget.select()
    tab_next = event.widget.tab(selected_tab, "text")'''

def onclick(event):
    if len(inipath.get()) == 0:
        inipath.insert(0, texts['inipath1'])
        inipath.config(fg='grey')
    if len(path.get()) == 0:
        path.insert(0, texts['path1'])
        path.config(fg='grey')
    if len(modname.get()) == 0:
        modname.insert(0, texts['modname1'])
        modname.config(fg='grey')
    if len(newname.get()) == 0:
        newname.insert(0, texts['newname1'])
        newname.config(fg='grey')
    if len(vehname.get()) == 0:
        vehname.insert(0, texts['vehname1'])
        vehname.config(fg='grey')
    if len(newid.get()) == 0:
        newid.insert(0, texts['newid1'])
        newid.config(fg='grey')
    if len(cfgpath.get()) == 0:
        cfgpath.insert(0, texts['cfgpath1'])
        cfgpath.config(fg='grey')
    if len(newveh.get()) == 0:
        newveh.insert(0, texts['newveh1'])
        newveh.config(fg='grey')
    if len(vehaudio.get()) == 0:
        vehaudio.insert(0, texts['vehaudio1'])
        vehaudio.config(fg='grey')
    if len(poppath.get()) == 0:
        poppath.insert(0, texts['poppath1'])
        poppath.config(fg='grey')
    if len(popveh.get()) == 0:
        popveh.insert(0, texts['popveh1'])
        popveh.config(fg='grey')
    if len(handcfg.get()) == 0:
        handcfg.insert(0, texts['handcfg1'])
        handcfg.config(fg='grey')
    if len(audio.get()) == 0:
        audio.insert(0, texts['audio1'])
        audio.config(fg='grey')
    if len(handlines.get()) == 0:
        handlines.insert(0, texts['handlines1'])
        handlines.config(fg='grey')
    if len(vehmodels.get()) == 0:
        vehmodels.insert(0, texts['vehmodels1'])
        vehmodels.config(fg='grey')
    if len(killable.get()) == 0:
        killable.insert(0, texts['killable1'])
        killable.config(fg='grey')
    if len(bike.get()) == 0:
        bike.insert(0, texts['bike1'])
        bike.config(fg='grey')
    if len(plane.get()) == 0:
        plane.insert(0, texts['plane1'])
        plane.config(fg='grey')
    if len(boat.get()) == 0:
        boat.insert(0, texts['boat1'])
        boat.config(fg='grey')
    for x in texts:
        if event.widget.get() in texts[x]:
            event.widget.delete(0, 'end')
            event.widget.config(fg='black')
    return None

tab_parent = ttk.Notebook(root)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)
tab4 = ttk.Frame(tab_parent)
tab5 = ttk.Frame(tab_parent)

#tab_parent.bind("<<NotebookTabChanged>>", on_tab_selected)
tab_parent.add(tab1, text=texts['configini1'])
tab_parent.add(tab2, text=texts['vehlines1'])
tab_parent.add(tab3, text=texts['vehsound1'])
tab_parent.add(tab4, text=texts['npcs1'])
tab_parent.add(tab5, text=texts['help1'])
tab_parent.grid(padx=5, pady=5, column=0, row=0)

tab1label = Label(tab1, text='', justify='left', anchor=W)
tab1label.grid(padx=0, pady=0, column=0, row=18, sticky=W)

def onhover(event):
    time.sleep(0.1)
    tab1label.configure(text=texts['vehmodelswarn'])
    root.geometry('630x400')
    return

def onleave(event):
    tab1label.configure(text='')
    root.geometry('630x375')


# ======================== TAB 1 ========================

inipath = Entry(tab1, width=80, borderwidth=2)
inipath.insert(0, texts['inipath1'])
inipath.config(fg='grey')
inipath.grid(padx=50, pady=5, column=0, row=1)
inipath.bind('<Button-1>', onclick)

# HANDLINE.CFG
handcfg = Entry(tab1, width=80, borderwidth=2)
handcfg.insert(0, 'Apply \'handling.cfg\' patch (0|1)')
handcfg.config(fg='grey')
handcfg.grid(padx=5, pady=5, column=0, row=2)
handcfg.bind('<Button-1>', onclick)

handcfgvar = BooleanVar()
handcfgbox = Checkbutton(tab1, variable=handcfgvar)
handcfgbox.grid(column=2, row=2)
handcfgbox.select()

# AUDIO
audio = Entry(tab1, width=80, borderwidth=2)
audio.insert(0, 'Enable vehicle audio loader (0|1)')
audio.config(fg='grey')
audio.grid(padx=5, pady=5, column=0, row=3)
audio.bind('<Button-1>', onclick)

audiovar = BooleanVar()
audiobox = Checkbutton(tab1, variable=audiovar)
audiobox.grid(column=2, row=3)
audiobox.select()

# LINES
handlines = Entry(tab1, width=80, borderwidth=2)
handlines.insert(0, 'Number of standard lines')
handlines.config(fg='grey')
handlines.grid(padx=5, pady=5, column=0, row=4)
handlines.bind('<Button-1>', onclick)

handlinesvar = BooleanVar()
handlinesbox = Checkbutton(tab1, variable=handlinesvar)
handlinesbox.grid(column=2, row=4)
handlinesbox.select()

# VEH MODELS
vehmodels = Entry(tab1, width=80, borderwidth=2)
vehmodels.insert(0, 'Vehicle Models')
vehmodels.config(fg='grey')
vehmodels.grid(padx=5, pady=5, column=0, row=5)
vehmodels.bind('<Button-1>', onclick)
vehmodels.bind('<Enter>', onhover)
vehmodels.bind('<Leave>', onleave)

vehmodelsvar = BooleanVar()
vehmodelsbox = Checkbutton(tab1, variable=vehmodelsvar)
vehmodelsbox.grid(column=2, row=5)
vehmodelsbox.select()

# KILLABLE
killable = Entry(tab1, width=80, borderwidth=2)
killable.insert(0, 'Count of killable model IDs')
killable.config(fg='grey')
killable.grid(padx=5, pady=5, column=0, row=6)
killable.bind('<Button-1>', onclick)

killablevar = BooleanVar()
killablebox = Checkbutton(tab1, variable=killablevar)
killablebox.grid(column=2, row=6)
killablebox.select()

# BIKE
bike = Entry(tab1, width=80, borderwidth=2)
bike.insert(0, 'Number of bike lines')
bike.config(fg='grey')
bike.grid(padx=5, pady=5, column=0, row=7)
bike.bind('<Button-1>', onclick)

bikevar = BooleanVar()
bikebox = Checkbutton(tab1, variable=bikevar)
bikebox.grid(column=2, row=7)
bikebox.select()

# PLANE
plane = Entry(tab1, width=80, borderwidth=2)
plane.insert(0, 'Number of flying lines')
plane.config(fg='grey')
plane.grid(padx=5, pady=5, column=0, row=8)
plane.bind('<Button-1>', onclick)

planevar = BooleanVar()
planebox = Checkbutton(tab1, variable=planevar)
planebox.grid(column=2, row=8)
planebox.select()

# BOAT
boat = Entry(tab1, width=80, borderwidth=2)
boat.insert(0, 'Number of boat lines')
boat.config(fg='grey')
boat.grid(padx=5, pady=5, column=0, row=9)
boat.bind('<Button-1>', onclick)

boatvar = BooleanVar()
boatbox = Checkbutton(tab1, variable=boatvar)
boatbox.grid(column=2, row=9)
boatbox.select()

# ======================== TAB 2 ========================

path = Entry(tab2, width=80, borderwidth=2)
path.insert(0, texts['path1'])
path.config(fg='grey')
path.grid(padx=50, pady=5, column=0, row=3)
path.bind('<Button-1>', onclick)

modname = Entry(tab2, width=80, borderwidth=2)
modname.insert(0, texts['modname1'])
modname.config(fg='grey')
modname.grid(padx=5, pady=5, column=0, row=4)
modname.bind('<Button-1>', onclick)

newname = Entry(tab2, width=80, borderwidth=2)
newname.insert(0, texts['newname1'])
newname.config(fg='grey')
newname.grid(padx=5, pady=5, column=0, row=5)
newname.bind('<Button-1>', onclick)

vehname = Entry(tab2, width=80, borderwidth=2)
vehname.insert(0, texts['vehname1'])
vehname.config(fg='grey')
vehname.grid(padx=5, pady=5, column=0, row=6)
vehname.bind('<Button-1>', onclick)

newid = Entry(tab2, width=80, borderwidth=2)
newid.insert(0, texts['newid1'])
newid.config(fg='grey')
newid.grid(padx=5, pady=5, column=0, row=7)
newid.bind('<Button-1>', onclick)

newidvar = BooleanVar()
newidbox = Checkbutton(tab2, variable=newidvar)
newidbox.grid(column=1, row=7)
newidbox.select()

label = Label(tab3, text=texts['tip'])
label.grid(column=0, row=8)

list = [texts['default1'], 'normal', 'poorfamily', 'richfamily', 'executive', 'worker', 'big', 'taxi', 'moped', 'motorbike', 'leisureboat', 'workerboat', 'bicycle', 'ignore']

item = StringVar()
item.set(texts['class1'])

dropmenu = OptionMenu(tab2, item, *list)
dropmenu.config(width=15)
dropmenu.grid(padx=5, pady=5, column=0, row=10)

# ======================== TAB 3 ========================


veh = '[landstal,bravura,buffalo,linerun,peren,sentinel,dumper,firetruk,trash,stretch,manana,infernus,voodoo,pony,mule,cheetah,ambulan,leviathn,moonbeam,esperant,taxi,washing,bobcat,mrwhoop,bfinject,' \
          'hunter,premier,enforcer,securica,banshee,predator,bus,rhino,barracks,hotknife,artict1,previon,coach,cabbie,stallion,rumpo,rcbandit,romero,packer,monster,' \
          'admiral,squalo,seaspar,pizzaboy,tram,artict2,turismo,speeder,reefer,tropic,flatbed,yankee,caddy,solair,topfun,skimmer,pcj600,faggio,freeway,rcbaron,rcraider,' \
          'glendale,oceanic,sanchez,sparrow,patriot,quad,coastg,dinghy,hermes,sabre,rustler,zr350,walton,regina,comet,bmx,burrito,camper,marquis,baggage,dozer,maverick,' \
          'vcnmav,rancher,fbiranch,virgo,greenwoo,jetmax,hotring,sandking,blistac,polmav,boxville,benson,mesa,rcgoblin,hotrina,hotrinb,bloodra,rnchlure,supergt,elegant,' \
          'journey,bike,mtbike,beagle,cropdust,stunt,petro,rdtrain,nebula,majestic,buccanee,shamal,hydra,fcr900,nrg500,copbike,cement,towtruck,fortune,cadrona,fbitruck,' \
          'willard,forklift,tractor,combine,feltzer,remingtn,slamvan,blade,freight,streak,vortex,vincent,bullet,clover,sadler,firela,hustler,intruder,primo,cargobob,' \
          'tampa,sunrise,merit,utility,nevada,yosemite,windsor,monstera,monsterb,uranus,jester,sultan,stratum,elegy,raindanc,rctiger,flash,tahoma,savanna,bandito,freiflat,' \
          'streakc,kart,mower,duneride,sweeper,broadway,tornado,at400,dft30,huntley,stafford,bf400,newsvan,tug,petrotr,emperor,wayfarer,euros,hotdog,club,freibox,artict3,' \
          'androm,dodo,rccam,launch,copcarla,copcarsf,copcarvg,copcarru,picador,swatvan,alpha,phoenix,glenshit,sadlshit,bagboxa,bagboxb,tugstair,boxburg,farmtr1,utiltr1]'

vehlist = sorted(veh[1:-1].split(','))
vehlist.insert(0, texts['disable1'])

vehitem = StringVar()
vehitem.set(texts['vehsound1'])

vehmenu = OptionMenu(tab3, vehitem, *vehlist)
vehmenu.config(width=15)
vehmenu.grid(padx=5, pady=5, column=0, row=9)

cfgpath = Entry(tab3, width=80, borderwidth=2)
cfgpath.insert(0, texts['cfgpath1'])
cfgpath.config(fg='grey')
cfgpath.grid(padx=50, pady=5, column=0, row=0)
cfgpath.bind('<Button-1>', onclick)

newveh = Entry(tab3, width=80, borderwidth=2)
newveh.insert(0, texts['newveh1'])
newveh.config(fg='grey')
newveh.grid(padx=5, pady=5, column=0, row=1)
newveh.bind('<Button-1>', onclick)

vehaudio = Entry(tab3, width=80, borderwidth=2)
vehaudio.insert(0, texts['vehaudio1'])
vehaudio.config(fg='grey')
vehaudio.grid(padx=5, pady=5, column=0, row=2)
vehaudio.bind('<Button-1>', onclick)

# ======================== TAB 4 ========================

poppath = Entry(tab4, width=80, borderwidth=2)
poppath.insert(0, texts['poppath1'])
poppath.config(fg='grey')
poppath.grid(padx=50, pady=5, column=0, row=0)
poppath.bind('<Button-1>', onclick)

popveh = Entry(tab4, width=80, borderwidth=2)
popveh.insert(0, texts['popveh1'])
popveh.config(fg='grey')
popveh.grid(padx=5, pady=5, column=0, row=1)
popveh.bind('<Button-1>', onclick)

poplist = ['POPCYCLE_GROUP_WORKERS', 'POPCYCLE_GROUP_BUSINESS', 'POPCYCLE_GROUP_CLUBBERS', 'POPCYCLE_GROUP_FARMERS', 'POPCYCLE_GROUP_BEACHFOLK', 'POPCYCLE_GROUP_PARKFOLK',
           'POPCYCLE_GROUP_CASUAL_RICH', 'POPCYCLE_GROUP_CASUAL_AVERAGE', 'POPCYCLE_GROUP_CASUAL_POOR', 'POPCYCLE_GROUP_PROSTITUTES', 'POPCYCLE_GROUP_CRIMINALS',
           'POPCYCLE_GROUP_GOLFERS', 'POPCYCLE_GROUP_SERVANTS', 'POPCYCLE_GROUP_AIRCREW', 'POPCYCLE_GROUP_ENTERTAINERS', 'POPCYCLE_GROUP_OUT_OF_TOWN_FACTORY',
           'POPCYCLE_GROUP_DESERT_FOLK', 'POPCYCLE_GROUP_AIRCREW_RUNWAY', 'Boats']

popitem = StringVar()
popitem.set(texts['popitem1'])

popmenu = OptionMenu(tab4, popitem, *poplist)
popmenu.config(width=40)
popmenu.grid(padx=5, pady=5, column=0, row=2)

# ======================== TAB 5 ========================

infolabel = Label(tab5, text=texts['infolabel1'])
infolabel.grid(padx=80, pady=5, column=0, row=0)

warnlabel = Label(tab5, text=texts['warnlabel1'])
warnlabel.grid(padx=5, pady=5, column=0, row=1)

contact = Label(tab5, text='Discord: Artprozew#5202')
contact.grid(padx=5, pady=0, column=0, row=22, sticky=W+S)

def configcargrp():
    poppathvar = poppath.get()
    popvehvar = popveh.get()
    popitemvar = popitem.get()
    popsave = []
    lineveh = []
    popfile = open(poppathvar + "\\" + "cargrp.dat", 'r+')
    while True:
        line = popfile.readline()
        if not line:
            popfile.seek(0)
            for x in range(len(popsave)):
                popfile.write(popsave[x])
            break
        if popitemvar in line:
            str = line.split('#')
            str = ' '.join(str[0].split())  # Remover tabs, espaços
            str = str.split(', ')
            lineveh = [', '.join(str[n:]) for n in range(len(str))]  # Juntando na lista cada item do popcycle
            index = len(lineveh) - 1
            line = line.replace(lineveh[index], lineveh[index] + ", " + popvehvar)
        popsave.append(line)
    popfile.close()


def configaudio():
    cfgpath2 = cfgpath.get()
    vaudio = vehaudio.get()
    vitem = vehitem.get()
    newvehvar = newveh.get()
    savedline = ''
    line = ''
    cfglines = []
    cfglines2 = []
    addlines = False
    cfgfile = open(cfgpath2 + "\\" + "gtasa_vehicleAudioSettings.cfg", 'r+')
    while True:
        line = cfgfile.readline()
        if not line:
            cfgfile.seek(0)
            for x in range(len(cfglines)):
                cfgfile.write(cfglines[x])
            if len(savedline) > 0:
                cfgfile.write(savedline)
            for x in range(len(cfglines2)):
                cfgfile.write(cfglines2[x])
            break
        if not vitem == texts['vehsound1'] and not vitem == texts['disable1']:
            if vitem in line:
                savedline = line
                savedline = savedline.replace(vitem, newvehvar)
        if len(vaudio) > 0:
            if any(ext in vaudio for ext in vehlist):
                if vaudio in line:
                    savedline = line
                    savedline = savedline.replace(vaudio, newvehvar)
        if addlines == True:
            cfglines2.append(line)
        else:
            cfglines.append(line)
        if ';start' in line:
            addlines = True
    cfgfile.close()


def configini():
    boollist = [handcfgvar, audiovar, handlinesvar, vehmodelsvar, killablevar, bikevar, planevar, boatvar]
    itemslist = ['Apply handling.cfg patch =', 'Enable vehicle audio loader =', 'Number of standard lines =',
                 'Vehicle Models =', 'Count of killable model IDs =', 'Number of bike lines =',
                 'Number of flying lines =', 'Number of boat lines =']
    answer = [handcfg.get(), audio.get(), handlines.get(), vehmodels.get(), killable.get(),
              bike.get(), plane.get(), boat.get()]
    inisave = []
    inipath2 = inipath.get()
    inifile = open(inipath2 + "\\" + "fastman92limitAdjuster_GTASA.ini", 'r+')
    while True:
        line = inifile.readline()
        if not line:
            inifile.seek(0)
            for x in range(len(inisave)):
                inifile.write(inisave[x])
            break
        if len(line) > 0:
            for x in range(len(itemslist)):
                var = itemslist[x]
                if var in line:
                    num = re.findall(r'\d+', line)
                    str = ''.join(num)
                    str = var + " " + str
                    if not answer[x].isdecimal() or not answer[x] or boollist[x].get() == False:
                        var = var + " " + ''.join(num)
                        if boollist[x].get() == False:
                            if not "#" in line and not ";" in line:
                                var = "#" + var
                    else:
                        var = var + " " + answer[x]
                    if boollist[x].get() == True:
                        if "#" in line:
                            str = "#" + str  # Adicionar para o .replace remover
                        if ";" in line:
                            str = ";" + str
                    line = line.replace(str, var)
        inisave.append(line)
    inifile.close()


def rename():
    pathvar = path.get()
    modnamevar = modname.get()
    newnamevar = newname.get()
    vehnamevar = vehname.get()
    newidinput = newid.get()
    saveall = []
    if len(newnamevar) > 7:
        messagebox.showwarning(texts['warning1'], texts['warn1'])
        return
    file = open(pathvar + "\\" + modnamevar + ".txt", 'r+')
    while True:
        line = file.readline()
        if not line:
            file.seek(0)
            for x in range(len(saveall)):
                file.write(saveall[x])
            break
        if len(line) > 0:
            if modnamevar.lower() in line:
                line = line.replace(modnamevar.lower(), newnamevar.lower())
            if modnamevar.upper() in line:
                line = line.replace(modnamevar.upper(), newnamevar.upper())
            if item.get() != texts['default1'] or item.get() != texts['class1']:
                x = 1
                for x in range(len(list)):
                    if list[x] in line:
                        line = line.replace(list[x], item.get())
                        break
            if newidvar.get() == True:
                str = re.search(r'\d*,', line)
                if str:
                    line = line.replace(str.group(), newidinput + ",")
        saveall.append(line)
    file.close()
    if os.path.isfile(pathvar + "\\" + modnamevar + '.dff'):
        os.rename(pathvar + "\\" + modnamevar + ".dff", pathvar + "\\" + newnamevar + ".dff")
    if os.path.isfile(pathvar + "\\" + modnamevar + ".txd"):
        os.rename(pathvar + "\\" + modnamevar + ".txd", pathvar + "\\" + newnamevar + ".txd")
    if os.path.isfile(pathvar + "\\" + modnamevar + ".txt"):
        os.rename(pathvar + "\\" + modnamevar + ".txt", pathvar + "\\" + newnamevar + ".txt")
    file = open(pathvar + "\\" + newnamevar + ".fxt", "w")
    file.write(newnamevar.upper() + " " + vehnamevar)
    file.close()


def pophelp():
    if lang == 'pt_BR' or lang == 'pt_PT':
        messagebox.showinfo('Ajuda', 'Uma explicação dos grupos de veículos usados por NPCs, postado na MixMods (pelo "Tripa Seca"?)\n'
                                     '\nWORKERS = Áreas industriais de cada cidade (SOMENTE cidades).'
                                     '\nBUSINESS = Centro das cidades, nas áreas com comércio e prédio altos.'
                                     '\nCLUBBERS = Geralmente aparecem junto na mesma área que os grupos Business e Average, mas somente de madrugada (23:00 - 06:00 em ponto).'
                                     '\nFARMERS = Área rural de Red County, Flint County, Whetstone e Bone County (Não conta Tierra Robada, que é de outro grupo).'
                                     '\nBEACHFOLK = Área de praia ao sul e leste de Los Santos (Santa Maria, Verona, Verdant Bluffs e Playa del Seville SOMENTE).'
                                     '\nPARKFOLK = Demais áreas de praia do estado em San Fierro (Ocean Flats e Missionary Hill) e Las Venturas (Blackfield) + Mulholland em Los Santos.'
                                     '\nCASUAL RICH = Áreas ricas de cada cidade (Rodeo, Richman, Paradiso, Prickle Pine, The Strip por exemplo).'
                                     '\nCASUAL AVERAGE = Esse é o grupo mais amplo, spawna em todas as áreas da cidade, menos a industrial, e também nas rodovias pelo interior. Recomendado adicionar aqui.'
                                     '\nCASUAL POOR = Áreas pobres, como East Los Santos.'
                                     '\nPROSTITUTES = Só aparece de noite, principalmente em áreas pobres, mas outras também.'
                                     '\nCRIMINALS = Grupo dos criminosos, os que você bate o carro e saem com um taco pra te bater, aparecem em qualquer parte.'
                                     '\nGOLFERS = Os motoristas do Caddy nos circuitos dos campos de golfe.'
                                     '\nSERVANTS = Alguns funcionários/trabalhadores?'
                                     '\nAIRCREW = Dirigem nas ruas AO REDOR dos aeroportos de cada cidade, menos o abandonado.'
                                     '\nENTERTAINERS = São aqueles Elvis que aparecem em The Strip, os carros daqui SÓ spawnam nela.'
                                     '\nOUT OF THE TOWN FACTORY = Áreas industriais FORA das cidades (Fallen Tree, Octane Springs, Hunter Quarry).'
                                     '\nDESERT FOLK = Grupo de fazendeiro que aparecem em Tierra Robada e também em Montgomery Intersection.'
                                     '\nAIRCREW RUNWAY = Aqueles Baggages e Tugs que ficam rodando ao redor dos hangares DENTRO dos aeroportos de Los Santos e Las Venturas.'
                                     '\nBoats = Barcos', detail='')
    else:
        messagebox.showinfo('Help',
                            'An explanation of the vehicle groups used by NPCs, posted on MixMods (by "Tripa Seca"?)\n'
                            '\nWORKERS = Industrial areas of each city (cities ONLY).'
                            '\nBUSINESS = Center of the cities, in the areas with commerce and high buildings.'
                            '\nCLUBBERS = They usually appear together in the same area as the Business and Average groups, but only at dawn (23:00 - 06:00 or 11:00 PM - 06:00 AM).'
                            '\nFARMERS = Rural area of Red County, Flint County, Whetstone and Bone County (Does not count Tierra Robada, which is from another group).'
                            '\nBEACHFOLK = Beach area on south and east of Los Santos (Santa Maria, Verona, Verdant Bluffs and Playa del Seville ONLY).'
                            '\nPARKFOLK = Other beach areas in San Fierro (Ocean Flats and Missionary Hill) and Las Venturas (Blackfield) + Mulholland in Los Santos.'
                            '\nCASUAL RICH = Rich areas of each city (Rodeo, Richman, Paradiso, Prickle Pine, The Strip for example).'
                            '\nCASUAL AVERAGE = This is the broadest group, they spawn in all areas of the city, except the industrial one, and also on some highways. Recommended to add here.'
                            '\nCASUAL POOR = Poor areas, like East Los Santos.'
                            '\nPROSTITUTES = It only appears at night, mainly in poor areas, but also others.'
                            '\nCRIMINALS = Group of criminals, the ones that you hit the car and come out with a bat to hit you, appear anywhere.'
                            '\nGOLFERS = Caddy drivers on golf course circuits.'
                            '\nSERVANTS = Some employees/workers?'
                            '\nAIRCREW = They drive on the streets AROUND the airports of each city, except the abandoned one.'
                            '\nENTERTAINERS = It\'s those Elvis who appear on The Strip, the cars here ONLY spawn on it.'
                            '\nOUT OF THE TOWN FACTORY = Industrial areas OUTSIDE the cities (Fallen Tree, Octane Springs, Hunter Quarry).'
                            '\nDESERT FOLK = Farmer\'s group appearing in Tierra Robada and also in Montgomery Intersection.'
                            '\nAIRCREW RUNWAY = Those Baggages and Tugs that are around the hangars INSIDE Los Santos and Las Venturas airports.', detail='')


def moreinfo():
    if lang == 'pt_BR' or lang == 'pt_PT':
        if messagebox.askyesno('Prosseguir?', 'Você será redirecionado para um website, deseja prosseguir?'):
            webbrowser.open('https://www.mixmods.com.br/2015/12/tutorial-adicionar-carros-sem-substituir.html')
    else:
        if messagebox.askyesno('Proceed?', 'You will be redirected to a website, do you like to proceed?'):
            webbrowser.open('https://gtaforums.com/topic/832297-satut-how-to-add-new-cars-without-replacing/')


def needed():
    if lang == 'pt_BR' or lang == 'pt_PT':
        if messagebox.askyesno('Prosseguir?', 'Você irá precisar do "Silent\'s ASI Loader" e "fastman92 limit adjuster"\nGostaria de visitar o website para baixá-los?'):
            webbrowser.open('https://www.mixmods.com.br/2013/02/silent-asi-loader.html')
            webbrowser.open('http://mixmods.com.br/2015/09/fastman92-limit-adjuster.html')
    else:
        if messagebox.askyesno('Proceed?', 'You will need "Silent\'s ASI Loader" and "fastman92 limit adjuster"\nWould you like to visit the website to download them?'):
            webbrowser.open('https://gtaforums.com/topic/523982-relopensrc-silents-asi-loader/')
            webbrowser.open('gtaforums.com/topic/733982-fastman92-limit-adjuster/')


# tab 1
configini = Button(tab1, text=texts['apply1'], command=configini, width=20)
configini.grid(padx=5, pady=5, column=0, row=20)

# tab 2
configcar = Button(tab2, text=texts['apply1'], command=rename, width=20)
configcar.grid(padx=5, pady=5, column=0, row=20)

# tab 3
configaudio = Button(tab3, text=texts['apply1'], command=configaudio, width=20)
configaudio.grid(padx=5, pady=5, column=0, row=20)

# tab 4
configcargrp = Button(tab4, text=texts['apply1'], command=configcargrp, width=20)
configcargrp.grid(padx=5, pady=5, column=0, row=20)

pophelp = Button(tab4, text='?', command=pophelp, width=2)
pophelp.grid(padx=5, pady=5, column=0, row=2, stick=E)

# tab 5
needed = Button(tab5, text=texts['needed'], command=needed)
needed.grid(padx=5, pady=5, column=0, row=5)

moreinfo = Button(tab5, text=texts['info'], command=moreinfo)
moreinfo.grid(padx=5, pady=5, column=0, row=20)

def callback(*args):
    label.configure(text=' ')
    # when item in list changes
vehitem.trace("w", callback)

root.mainloop()
