import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser
import ctypes
import locale
import re
import os

#  15/01/2021
#  Feito por Artprozew#5202

appname = 'SA Mod Manager'

root = tk.Tk()
root.title(appname)
root.geometry('450x370')
root.resizable(0, 0)

frame = Frame(root, width=200, height=200).grid()

windll = ctypes.windll.kernel32  # getting windows language
windll.GetUserDefaultUILanguage()
lang = locale.windows_locale[windll.GetUserDefaultUILanguage()]

def on_tab_selected(event):
    selected_tab = event.widget.select()
    tab_next = event.widget.tab(selected_tab, "text")

tab_parent = ttk.Notebook(root)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)
tab4 = ttk.Frame(tab_parent)
tab5 = ttk.Frame(tab_parent)

tab_parent.bind("<<NotebookTabChanged>>", on_tab_selected)
tab_parent.add(tab1, text='Config')
tab_parent.add(tab2, text='Vehicle Lines')
tab_parent.add(tab3, text='Vehicle Sound')
tab_parent.add(tab4, text='Vehicle of NPCs')
tab_parent.add(tab5, text='Help')
tab_parent.grid(padx=5, pady=5, column=0, row=0)

tab1label = Label(tab1, text=' ', justify='left', anchor='w')
tab1label.grid(padx=15, pady=15, column=0, row=20, sticky='w')

# ======================== TAB 1 ========================

inipath = Entry(tab1, width=50, borderwidth=2)
inipath.insert(0, 'Path to \'.ini\' file')
inipath.config(fg='grey')
inipath.grid(padx=50, pady=5, column=0, row=1)

# HANDLINE.CFG
handcfg = Entry(tab1, width=50, borderwidth=2)
handcfg.insert(0, 'Apply \'handling.cfg\' patch (0|1)')
handcfg.config(fg='grey')
handcfg.grid(padx=5, pady=5, column=0, row=2)

handcfgvar = BooleanVar()
handcfgbox = Checkbutton(tab1, variable=handcfgvar)
handcfgbox.grid(column=2, row=2)
handcfgbox.select()

# AUDIO
audio = Entry(tab1, width=50, borderwidth=2)
audio.insert(0, 'Enable vehicle audio loader (0|1)')
audio.config(fg='grey')
audio.grid(padx=5, pady=5, column=0, row=3)

audiovar = BooleanVar()
audiobox = Checkbutton(tab1, variable=audiovar)
audiobox.grid(column=2, row=3)
audiobox.select()

# LINES
handlines = Entry(tab1, width=50, borderwidth=2)
handlines.insert(0, 'Number of standard lines')
handlines.config(fg='grey')
handlines.grid(padx=5, pady=5, column=0, row=4)

handlinesvar = BooleanVar()
handlinesbox = Checkbutton(tab1, variable=handlinesvar)
handlinesbox.grid(column=2, row=4)
handlinesbox.select()

# VEH MODELS
vehmodels = Entry(tab1, width=50, borderwidth=2)
vehmodels.insert(0, 'Vehicle Models')
vehmodels.config(fg='grey')
vehmodels.grid(padx=5, pady=5, column=0, row=5)

vehmodelsvar = BooleanVar()
vehmodelsbox = Checkbutton(tab1, variable=vehmodelsvar)
vehmodelsbox.grid(column=2, row=5)
vehmodelsbox.select()

# KILLABLE
killable = Entry(tab1, width=50, borderwidth=2)
killable.insert(0, 'Count of killable model IDs')
killable.config(fg='grey')
killable.grid(padx=5, pady=5, column=0, row=6)

killablevar = BooleanVar()
killablebox = Checkbutton(tab1, variable=killablevar)
killablebox.grid(column=2, row=6)
killablebox.select()

# BIKE
bike = Entry(tab1, width=50, borderwidth=2)
bike.insert(0, 'Number of bike lines')
bike.config(fg='grey')
bike.grid(padx=5, pady=5, column=0, row=7)

bikevar = BooleanVar()
bikebox = Checkbutton(tab1, variable=bikevar)
bikebox.grid(column=2, row=7)
bikebox.select()

# PLANE
plane = Entry(tab1, width=50, borderwidth=2)
plane.insert(0, 'Number of flying lines')
plane.config(fg='grey')
plane.grid(padx=5, pady=5, column=0, row=8)

planevar = BooleanVar()
planebox = Checkbutton(tab1, variable=planevar)
planebox.grid(column=2, row=8)
planebox.select()

# BOAT
boat = Entry(tab1, width=50, borderwidth=2)
boat.insert(0, 'Number of boat lines')
boat.config(fg='grey')
boat.grid(padx=5, pady=5, column=0, row=9)

boatvar = BooleanVar()
boatbox = Checkbutton(tab1, variable=boatvar)
boatbox.grid(column=2, row=9)
boatbox.select()

# ======================== TAB 2 ========================

path = Entry(tab2, width=50, borderwidth=2)
path.insert(0, 'Mod path')
path.config(fg='grey')
path.grid(padx=50, pady=5, column=0, row=3)

modname = Entry(tab2, width=50, borderwidth=2)
modname.insert(0, 'Mod name')
modname.config(fg='grey')
modname.grid(padx=5, pady=5, column=0, row=4)

newname = Entry(tab2, width=50, borderwidth=2)
newname.insert(0, 'New name')
newname.config(fg='grey')
newname.grid(padx=5, pady=5, column=0, row=5)

carname = Entry(tab2, width=50, borderwidth=2)
carname.insert(0, 'New vehicle name')
carname.config(fg='grey')
carname.grid(padx=5, pady=5, column=0, row=6)

newid = Entry(tab2, width=50, borderwidth=2)
newid.insert(0, 'New vehicle ID')
newid.config(fg='grey')
newid.grid(padx=5, pady=5, column=0, row=7)

newidvar = BooleanVar()
newidbox = Checkbutton(tab2, variable=newidvar)
newidbox.grid(column=1, row=7)
newidbox.select()

label = Label(tab2, text='Choose the vehicle class')
label.grid(column=0, row=9)

list = ['default', 'normal', 'poorfamily', 'richfamily', 'executive', 'worker', 'big', 'taxi', 'moped', 'motorbike', 'leisureboat', 'workerboat', 'bicycle', 'ignore']

item = StringVar()
item.set('Vehicle class')

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
vehlist.insert(0, 'DISABLE')

vehitem = StringVar()
vehitem.set('Vehicle sound')

vehmenu = OptionMenu(tab3, vehitem, *vehlist)
vehmenu.config(width=15)
vehmenu.grid(padx=5, pady=5, column=0, row=8)

cfgpath = Entry(tab3, width=50, borderwidth=2)
cfgpath.insert(0, '\'vehicleAudioSettings.cfg\' file path')
cfgpath.config(fg='grey')
cfgpath.grid(padx=50, pady=5, column=0, row=0)

newveh = Entry(tab3, width=50, borderwidth=2)
newveh.insert(0, 'New vehicle model name')
newveh.config(fg='grey')
newveh.grid(padx=5, pady=5, column=0, row=1)

vehaudio = Entry(tab3, width=50, borderwidth=2)
vehaudio.insert(0, 'Model name to get audio from (or use the list below)')
vehaudio.config(fg='grey')
vehaudio.grid(padx=5, pady=5, column=0, row=2)

# ======================== TAB 4 ========================

poppath = Entry(tab4, width=50, borderwidth=2)
poppath.insert(0, '\'cargrp.dat\' file path')
poppath.config(fg='grey')
poppath.grid(padx=50, pady=5, column=0, row=0)

popveh = Entry(tab4, width=50, borderwidth=2)
popveh.insert(0, 'Vehicle name to insert')
popveh.config(fg='grey')
popveh.grid(padx=5, pady=5, column=0, row=1)

poplist = ['POPCYCLE_GROUP_WORKERS', 'POPCYCLE_GROUP_BUSINESS', 'POPCYCLE_GROUP_CLUBBERS', 'POPCYCLE_GROUP_FARMERS', 'POPCYCLE_GROUP_BEACHFOLK', 'POPCYCLE_GROUP_PARKFOLK',
           'POPCYCLE_GROUP_CASUAL_RICH', 'POPCYCLE_GROUP_CASUAL_AVERAGE', 'POPCYCLE_GROUP_CASUAL_POOR', 'POPCYCLE_GROUP_PROSTITUTES', 'POPCYCLE_GROUP_CRIMINALS',
           'POPCYCLE_GROUP_GOLFERS', 'POPCYCLE_GROUP_SERVANTS', 'POPCYCLE_GROUP_AIRCREW', 'POPCYCLE_GROUP_ENTERTAINERS', 'POPCYCLE_GROUP_OUT_OF_TOWN_FACTORY',
           'POPCYCLE_GROUP_DESERT_FOLK', 'POPCYCLE_GROUP_AIRCREW_RUNWAY', 'Boats']

popitem = StringVar()
popitem.set('Choose group')

popmenu = OptionMenu(tab4, popitem, *poplist)
popmenu.config(width=40)
popmenu.grid(padx=5, pady=5, column=0, row=10)



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
        if not vitem == 'Vehicle sound' and not vitem == 'DISABLE':
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
    carnamevar = carname.get()
    newidinput = newid.get()
    saveall = []
    if len(newnamevar) > 7:
        messagebox.showwarning('Warning', '\'New name\' cannot have more than 7 characters!')
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
            if item.get() != 'default' or item.get() != 'Vehicle class':
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
    file.write(newnamevar.upper() + " " + carnamevar)
    file.close()


def dependencies():
    if lang == 'pt_BR':
        messagebox.showwarning('Aviso', 'Para mais informações, visite www.mixmods.com.br/2015/12/tutorial-adicionar-carros-sem-substituir.html')
    else:
        messagebox.showwarning(('Warning', 'For more information, visit www.mixmods.com.br/2015/12/tutorial-adicionar-carros-sem-substituir.html'))
    webbrowser.open('https://www.mixmods.com.br/2013/02/silent-asi-loader.html')
    webbrowser.open('http://mixmods.com.br/2015/09/fastman92-limit-adjuster.html')


# tab 1
configini = Button(tab1, text='Apply', command=configini, width=20)
configini.grid(padx=5, pady=5, column=0, row=20)

# tab 2
configcar = Button(tab2, text='Configure', command=rename)
configcar.grid(padx=5, pady=5, column=0, row=2, sticky=E)

dependencies = Button(tab2, text='Dependencies', command=dependencies)
dependencies.grid(padx=5, pady=5, column=0, row=20)

# tab 3
configaudio = Button(tab3, text='Apply', command=configaudio, width=20)
configaudio.grid(padx=5, pady=5, column=0, row=20)

# tab 4
configcargrp = Button(tab4, text='Apply', command=configcargrp, width=20)
configcargrp.grid(padx=5, pady=5, column=0, row=20)

'''def callback(*args):
    label.configure(text='Selecinado: {}'.format(vehitem.get()))
    # when item in list changes
vehitem.trace("w", callback)'''

root.mainloop()
