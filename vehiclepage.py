from tkinter import *
from tkinter .ttk import *
from variables import *
from languages import *
from images import *
import os
import pickle
import base64

class Constants:
    @property
    def none():
        pass #http://download.gta-expert.it/index.php?act=download&id=5743
    # https://tuningmod.mixmods.com.br/p/ids.html

def vehpage():
    # add maior#b64 = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAG5JREFUWEdjZBhgwDjA9jOMOmA0BCgNgZPQRGxObmKm1AH/oRaTbQ7ZGqEWjzpgNARGQ4CmIQAqZMzILWDQ9J0C8rEWVvjKgQF3ADGep2kUjDpgNARGQ2BIhMCAN8mICSW8aihtko06YDQEKA4BAH+uFiGo0ir0AAAAAElFTkSuQmCC'
    # selectall maior#b64 = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAARNJREFUWEdjZBhgwDjA9jOMOgBbCIgAo2UmEH8G4gRoFK0B0sFQNkxPCJC/GioWCqRBakDgP5ReC6RBakBgARDzAnE6EL9BjnZsDgBpDAJiZAModQBM/zokj4Ddgc0BINfyAPFxIO6FurYYSFtC2TBfWQD5JVCxHiB9AsqGhQQ2/V+AahIIhQCyPM3ZgzIX4AtCUkKEUBTiTAPYUjFyIiTWEYQS8eB1ADYfYsuGuEICWwjiDDViEyFdHQDL50/Q8jZ6SUhKCIDKDBm0coLsNEAo1AglYhT92AwjyQAswUCSfmwOGPAoGM0FhOJw+JeEA14ZERvEVFFHqFChiiX4DBmUTbIBb5QOeLOc5vE+2ioeVCEAAOJpeCEczAJ5AAAAAElFTkSuQmCC'
    #with open('add.png', 'wb') as f:
    #    f.write(base64.decodebytes(b64))
    dictlist = {}
    for k in tab:
        if tab[k].winfo_exists():
            tab[k].destroy()

    '''def on_tab_selected(event):
        if tab_parent.tab(tab_parent.select(), 'text') == texts['idlist1']:
            get_vehicle_ids()'''


    tab['configini'] = ttk.Frame(tab_parent)
    tab['lines'] = ttk.Frame(tab_parent)
    tab['sound'] = ttk.Frame(tab_parent)
    tab['vehnpcs'] = ttk.Frame(tab_parent)
    tab['idlist'] = ttk.Frame(tab_parent)
    #tab_parent.bind('<<NotebookTabChanged>>', on_tab_selected)
    tab_parent.add(tab['configini'], text=texts['configini1'])
    tab_parent.add(tab['lines'], text=texts['lines1'])
    tab_parent.add(tab['sound'], text=texts['sound1'])
    tab_parent.add(tab['vehnpcs'], text=texts['npcs1'])
    tab_parent.add(tab['idlist'], text=texts['idlist1'])
    tab_parent.grid(padx=5, pady=5, column=0, row=0, sticky=(N,S,E,W))
    #for i in tab:
    #    tab[i].columnconfigure((0,5), weight=1)
    #tab_parent.columnconfigure((0,5), weight=1)
    #tab_parent.grid_columnconfigure((0,5), weight=1)
    #tab_parent.rowconfigure((0,5), weight=1)
    #tab_parent.grid_rowconfigure((0,5), weight=1)
    #style = Style(tab_parent)
    #style.theme_use('clam')

    inihints = Label(tab['configini'], text='', justify='left', anchor=W)
    inihints.grid(padx=0, pady=0, column=0, row=18, sticky=W)

    def savc():
        dictlist['inipath'].delete(0, 'end')
        dictlist['inipath'].config(fg='grey')
        dictlist['audiocfgpath'].delete(0, 'end')
        dictlist['audiocfgpath'].config(fg='grey')
        if savcbool.get() == True:
            dictlist['inipath'].insert(0, texts['inipath2'])
            dictlist['audiocfgpath'].insert(0, texts['audiocfgpath2'])
        else:
            dictlist['inipath'].insert(0, texts['inipath1'])
            dictlist['audiocfgpath'].insert(0, texts['audiocfgpath1'])
        return


    savcbool = BooleanVar()
    savcbox = Checkbutton(tab['configini'], text='VC', command=savc, variable=savcbool)
    savcbox.grid(padx=5, pady=5, column=0, row=1, sticky=W)
    savcbox.deselect()

    savcbox2 = Checkbutton(tab['sound'], text='VC', command=savc, variable=savcbool)
    savcbox2.grid(padx=5, pady=5, column=0, row=0, sticky=W)
    savcbox2.deselect()

    def onclick(event):
        for k, v in dictlist.items():
            if len(dictlist[k].get()) == 0:
                if k == 'inipath' and savcbool.get() == True or k == 'audiocfgpath' and savcbool.get() == True:
                    dictlist[k].insert(0, texts[k + '2'])
                else:
                    dictlist[k].insert(0, texts[k + '1'])
                dictlist[k].config(fg='grey')
        for x in texts:
            if event.widget.get() in texts[x]:
                event.widget.delete(0, 'end')
                event.widget.config(fg='black')
        return


    def CreateEntry(var, tabname, text, column, row, width, columnspan = 1, sticky = None, padx=5, pady=5):
        dictlist[var] = Entry(tab[tabname], width=width, borderwidth=2)
        dictlist[var].insert(0, texts[text])
        dictlist[var].config(fg='grey')
        dictlist[var].grid(padx=padx, pady=pady, column=column, row=row, columnspan=columnspan, sticky=sticky)
        dictlist[var].bind('<FocusIn>', onclick)
        return dictlist[var]


    def onhover(event):
        time.sleep(0.1)
        inihints.configure(text=texts['vehmodelswarn'])
        root.geometry('630x400')


    def onleave(event):
        inihints.configure(text='')
        root.geometry('630x375')

    
    def configcargrp():
        poppathvar = popcyclepath.get()
        popvehvar = popcycleveh.get()
        popitemvar = popitem.get()
        removecheck = removevar2.get()
        popsave = []
        lineveh = []
        line = ''
        donemsg = False
        try:
            popfile = open(poppathvar + '/' + 'cargrp.dat', 'r+')
        except:
            messagebox.showerror('ERROR', 'The file \'cargrp.dat\' was not found\nArquivo não encontrado')
            return
        passed = False
        while True:
            try:
                line = popfile.readline()
            except:
                if passed == False:
                    popfile.close()
                    try:
                        popfile = open(poppathvar + '/' + 'cargrp.dat', 'r+', encoding='utf8', errors='ignore')
                    except:
                        messagebox.showerror('ERROR', 'Could not read a line in the file, try to remove manually special characters from the file ex. russian, arab characters, etc. or try to change the file encoding')
                    line = popfile.readline()
                    passed = True
            if not line:
                popfile.seek(0)
                for x in range(len(popsave)):
                    popfile.write(popsave[x])
                break
            if popitemvar in line:
                if removecheck == False:
                    str = line.split('#')
                    str = ' '.join(str[0].split())  # Remover tabs, espaços
                    str = str.split(', ')
                    lineveh = [', '.join(str[n:]) for n in range(len(str))]  # Juntando na lista cada item do popcycle
                    index = len(lineveh) - 1
                    line = line.replace(lineveh[index], lineveh[index] + ', ' + popvehvar)
                    donemsg = True
                else:
                    line = line.replace(', ' + popvehvar, '')
                    line = line.replace(popvehvar, '')
                    donemsg = True
            popsave.append(line)
        popfile.close()
        if donemsg == True:
            messagebox.showinfo('Info', texts['donemsg1'])
        else:
            messagebox.showerror('ERROR', texts['errormsg1'])


    def configaudio():
        cfgpath2 = dictlist['audiocfgpath'].get()
        vaudio = dictlist['vehaudio'].get()
        vitem = vehitem.get()
        newvehvar = dictlist['newvehname'].get()
        removecheck = removevar.get()
        savedline = ''
        line = ''
        linecounter = 0
        cfglines = []
        cfglines2 = []
        addlines = False
        passed = False
        donemsg = False
        if savcvar.get() == False:
            try:
                cfgfile = open(cfgpath2 + '/' + 'gtasa_vehicleAudioSettings.cfg', 'r+')
            except:
                messagebox.showerror('ERROR', 'The file \'gtasa_vehicleAudioSettings.cfg\' was not found\nArquivo não encontrado')
                return
        else:
            try:
                cfgfile = open(cfgpath2 + '/' + 'gtavc_vehicleAudioSettings.cfg', 'r+')
            except:
                messagebox.showerror('ERROR', 'The file \'gtavc_vehicleAudioSettings.cfg\' was not found\nArquivo não encontrado')
                return
        if len(vaudio) > 0 and not vaudio == texts['vehsound1']:
            if vitem == texts['vehsound1'] or vitem == texts['disable1']:
                if not any(ext in vaudio for ext in vehlist) and removecheck == False:
                    messagebox.showerror('ERROR', 'Could not find \'' + vaudio + '\'\nNão foi possível encontrar \''  + vaudio + '\'')
                    return
        while True:
            try:
                line = cfgfile.readline()
            except:
                if passed == False:
                    cfgfile.close()
                    try:
                        if savcvar.get() == False:
                            cfgfile = open(cfgpath2 + '/' + 'gtasa_vehicleAudioSettings.cfg', 'r+', encoding='utf8', errors='ignore')
                        else:
                            cfgfile = open(cfgpath2 + '/' + 'gtavc_vehicleAudioSettings.cfg', 'r+', encoding='utf8', errors='ignore')
                    except:
                        messagebox.showerror('ERROR', 'Could not read a line in the file, try to remove manually special characters from the file ex. russian, arab characters, etc. or try to change the file encoding')
                    line = cfgfile.readline()
                    passed = True
            if not line:
                cfgfile.seek(0)
                for x in range(len(cfglines)):
                    cfgfile.write(cfglines[x])
                if removecheck == False:
                    if len(savedline) > 0:
                        cfgfile.write(savedline)
                    for x in range(len(cfglines2)):
                        cfgfile.write(cfglines2[x])
                break
            if removecheck == False:
                if not vitem == texts['vehsound1'] and not vitem == texts['disable1']:
                    if vitem in line:
                        savedline = line
                        savedline = savedline.replace(vitem, newvehvar)
                        donemsg = True
                if len(vaudio) > 0:
                    if any(ext in vaudio for ext in vehlist):
                        if vaudio in line:
                            savedline = line
                            savedline = savedline.replace(vaudio, newvehvar)
                            donemsg = True
                if addlines == True:
                    cfglines2.append(line)
                else:
                    cfglines.append(line)
                if '; A                                         B             C      D      E         F            G            H         I            J           K          L          M           N                 O' in line:
                    linecounter += 1
                    if linecounter == 7:
                        addlines = True
            else:
                if not newvehvar in line:
                    cfglines.append(line)
                else:
                    donemsg = True
        cfgfile.close()
        if donemsg == True:
            messagebox.showinfo('Info', texts['donemsg1'])
        else:
            messagebox.showerror('ERROR', texts['errormsg1'])


    def configini():
        boollist = [handcfgvar, audiovar, handlinesvar, vehmodelsvar, killablevar, bikevar, planevar, boatvar]
        itemslist = ['Apply handling.cfg patch =', 'Enable vehicle audio loader =', 'Number of standard lines =',
                    'Vehicle Models =', 'Count of killable model IDs =', 'Number of bike lines =',
                    'Number of flying lines =', 'Number of boat lines =']
        answer = [dictlist['handcfg'].get(), dictlist['audio'].get(), dictlist['handlines'].get(), dictlist['vehmodels'].get(), dictlist['killablemodels'].get(),
                dictlist['bikelines'].get(), dictlist['planelines'].get(), dictlist['boatlines'].get()]
        inisave = []
        inipath2 = inipath.get()
        line = ''
        if savcvar.get() == False:
            try:
                inifile = open(inipath2 + '/' + 'fastman92limitAdjuster_GTASA.ini', 'r+')
            except:
                messagebox.showerror('ERROR', 'The file \'' + fastman92limitAdjuster_GTASA.ini + '\' was not found\nArquivo não encontrado')
                return
        else:
            try:
                inifile = open(inipath2 + '/' + 'fastman92limitAdjuster_GTAVC.ini', 'r+')
            except:
                messagebox.showerror('ERROR', 'The file \'' + fastman92limitAdjuster_GTAVC.ini + '\' was not found\nArquivo não encontrado')
                return
        passed = False
        while True:
            try:
                line = inifile.readline()
            except:
                if passed == False:
                    inifile.close()
                    try:
                        if savcvar.get() == False:
                            inifile = open(inipath2 + '/' + 'fastman92limitAdjuster_GTASA.ini', 'r+', encoding='utf8', errors='ignore')
                        else:
                            inifile = open(inipath2 + '/' + 'fastman92limitAdjuster_GTAVC.ini', 'r+', encoding='utf8', errors='ignore')
                    except:
                        messagebox.showerror('ERROR', 'Could not read a line in the file, try to remove manually special characters from the file ex. russian, arab characters, etc. or try to change the file encoding')
                    line = inifile.readline()
                    passed = True
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
                        tmp = ''.join(num)
                        tmp = var + ' ' + tmp
                        if not answer[x].isdecimal() or not answer[x] or boollist[x].get() == False:
                            var = var + ' ' + ''.join(num)
                            if boollist[x].get() == False:
                                if not '#' in line and not ';' in line:
                                    var = '#' + var
                        else:
                            var = var + ' ' + answer[x]
                            donemsg = True
                        #if boollist[x].get() == True and answer[x].isdecimal() and len(answer[x]) > 0:
                            if '#' in line:
                                tmp = '#' + tmp  # Adicionar para o .replace remover
                            if ';' in line:
                                tmp = ';' + tmp
                        line = line.replace(tmp, var)
            inisave.append(line)
        inifile.close()
        if donemsg == True:
            messagebox.showinfo('Info', texts['donemsg1'])
        else:
            messagebox.showerror('ERROR', texts['errormsg1'])


    def rename():
        pathvar = dictlist['vehpath'].get()
        modnamevar = dictlist['modname'].get()
        newnamevar = dictlist['newname'].get()
        vehnamevar = dictlist['vehname'].get()
        newidinput = dictlist['newid'].get()
        saveall = []
        line = ''
        passed = False
        if len(modnamevar) == 0 or modnamevar == texts['modname1']:
            messagebox.showwarning('ERROR', '\'' + texts['modname1'] + '\'\nCannot be empty\nNão pode estar vazio')
            return
        if len(newnamevar) > 7 or len(newnamevar) == 0:
            messagebox.showwarning(texts['warning1'], texts['warn1'])
            return
        try:
            file = open(pathvar + '/' + modnamevar + '.txt', 'r+')
        except:
            messagebox.showerror('ERROR', 'The file \'' + modnamevar + '.txt\' was not found\nArquivo não encontrado')
            return
        while True:
            try:
                line = file.readline()
            except:
                if passed == False:
                    file.close()
                    try:
                        file = open(pathvar + '/' + modnamevar + '.txt', 'r+', encoding='utf8', errors='ignore')
                    except:
                        messagebox.showerror('ERROR', 'Could not read a line in the file, try to remove manually special characters from the file ex. russian, arab characters, etc. or try to change the file encoding')
                    line = file.readline()
                    passed = True
            if not line:
                file.seek(0)
                for x in range(len(saveall)):
                    file.write(saveall[x])
                break
            if len(line) > 0:
                if newidvar.get() == True:
                    if len(newidinput) != 0 and newidinput.isdecimal():
                        tmp = re.search(r'\d*,\s*' + modnamevar, line)
                        if tmp:
                            line = line.replace(tmp.group(), newidinput + ',\t' + modnamevar)
                tmp = re.search(modnamevar.upper() + r',\s*\w*,', line)
                if tmp:
                    line = line.replace(tmp.group(), modnamevar.upper() + ',\t' + modnamevar.upper() + ',')
                if modnamevar.lower() in line:
                    line = line.replace(modnamevar.lower(), newnamevar.lower())
                    donemsg = True
                if modnamevar.upper() in line:
                    line = line.replace(modnamevar.upper(), newnamevar.upper())
                    donemsg = True
                if item.get() != texts['default1'] and item.get() != texts['class1']:
                    x = 1
                    for x in range(len(classlist)):
                        if classlist[x] in line:
                            line = line.replace(classlist[x], item.get())
                            break
            saveall.append(line)
        file.close()
        if donemsg == True:
            if os.path.isfile(pathvar + '/' + modnamevar + '.dff'):
                os.rename(pathvar + '/' + modnamevar + '.dff', pathvar + '/' + newnamevar + '.dff')
            if os.path.isfile(pathvar + '/' + modnamevar + '.txd'):
                os.rename(pathvar + '/' + modnamevar + '.txd', pathvar + '/' + newnamevar + '.txd')
            if os.path.isfile(pathvar + '/' + modnamevar + '.txt'):
                os.rename(pathvar + '/' + modnamevar + '.txt', pathvar + '/' + newnamevar + '.txt')
            if not len(vehnamevar) == 0 and not vehnamevar == texts['vehname1']:
                if os.path.isfile(pathvar + '/' + modnamevar + '.fxt'):
                    os.rename(pathvar + '/' + modnamevar + '.fxt', pathvar + '/' + newnamevar + '.fxt')
                file = open(pathvar + '/' + newnamevar + '.fxt', 'w')
                file.seek(0)
                file.write(newnamevar.upper() + ' ' + vehnamevar)
                file.close()
            messagebox.showinfo('Info', texts['donemsg1'])
        else:
            messagebox.showerror('ERROR', texts['errormsg1'])


    def pophelp():
        if lang == 'pt_BR' or lang == 'pt_PT':
            messagebox.showinfo('Ajuda', 'Uma explicação dos grupos de veículos usados por NPCs, postado na MixMods (pelo \'Tripa Seca\'?)\n'
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
                                'An explanation of the vehicle groups used by NPCs, posted on MixMods (by \'Tripa Seca\'?)\n'
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
            if messagebox.askyesno('Prosseguir?', 'Você irá precisar do \'Silent\'s ASI Loader\' e \'fastman92 limit adjuster\'\nGostaria de visitar o website para baixá-los?'):
                webbrowser.open('https://www.mixmods.com.br/2013/02/silent-asi-loader.html')
                webbrowser.open('http://mixmods.com.br/2015/09/fastman92-limit-adjuster.html')
        else:
            if messagebox.askyesno('Proceed?', 'You will need \'Silent\'s ASI Loader\' and \'fastman92 limit adjuster\'\nWould you like to visit the website to download them?'):
                webbrowser.open('https://gtaforums.com/topic/523982-relopensrc-silents-asi-loader/')
                webbrowser.open('gtaforums.com/topic/733982-fastman92-limit-adjuster/')


    def tip():
        if lang == 'pt_BR' or lang == 'pt_PT':
            messagebox.showinfo('Ajuda', 'Para aplicar as linhas no novo veículo: Coloque o veículo (.txd e .dff) e o arquivo de linhas (.txt) numa pasta (de preferência já dentro do modloader), '
                                            'e renomeie o arquivo de linhas para o mesmo nome do arquivo do veículo. O programa mudará o nome de todos esses arquivos para o novo nome do mod escolhido')
        else:
            messagebox.showinfo('Help', 'To apply the lines to the new vehicle: Place the vehicle (.txd and .dff) and the lines file (.txt) in a folder (preferably already inside the modloader), '
                                                'and rename the line file to the same name as the vehicle file. The program will rename all those files to the name of the new mod name chosen')


    def inipathfile():
        filename = filedialog.askdirectory()
        inipath.delete(0, 'end')
        inipath.insert(0, filename)
        inipath.config(fg='black')


    def configcarpath():
        filename = filedialog.askdirectory()
        path.delete(0, 'end')
        path.insert(0, filename)
        path.config(fg='black')


    def configaudiopath():
        filename = filedialog.askdirectory()
        cfgpath.delete(0, 'end')
        cfgpath.insert(0, filename)
        cfgpath.config(fg='black')


    def popconfigpath():
        filename = filedialog.askdirectory()
        poppath.delete(0, 'end')
        poppath.insert(0, filename)
        poppath.config(fg='black')


    def getline(filename, pathvar, modnamevar, saveall, donemsg):
        try:
            file = open(pathvar + '/' + filename, 'r')
        except:
            try:
                file = open(pathvar + '/' + filename, 'r', encoding='utf8', errors='ignore')
            except:
                messagebox.showerror('ERROR', 'The file \'' + filename + '\' was not found\nArquivo não encontrado')
                return False
        passed = False
        donemsg = False
        while True:
            try:
                line = file.readline()
            except:
                if passed == False:
                    file.close()
                    try:
                        file = open(pathvar + '/' + filename, 'r', encoding='utf8', errors='ignore')
                    except:
                        messagebox.showerror('ERROR', 'Could not read a line in the file, try to remove manually special characters from the file ex. russian, arab characters, etc. or try to change the file encoding')
                    line = file.readline()
                    passed = True
            if not line:
                break
            if modnamevar.lower() in line:
                modnamevar = modnamevar.lower()
            if modnamevar.upper() in line:
                modnamevar = modnamevar.upper()
            #if re.search(modnamevar + ',', line) or re.search(r'\s*' + modnamevar, line) or re.search(modnamevar + r'\s*', line):
            if modnamevar in line:
                if not re.search(r'\w' + modnamevar, line) and not re.search(modnamevar + r'\w', line):
                    '''if filename == 'carmods.dat':
                        line = modnamevar + ', nto_b_l, nto_b_s, nto_b_tw'''
                    saveall.append(line)
                    donemsg = True
        modnamevar = dictlist['modname'].get()
        file.close()
        return donemsg


    def create():
        pathvar = dictlist['vehpath'].get()
        modnamevar = dictlist['modname'].get()
        '''newnamevar = dictlist['newname'].get()
        vehnamevar = dictlist['vehname'].get()
        newidinput = dictlist['newid'].get()'''
        if not any(ext in modnamevar for ext in vehlist):
            messagebox.showerror('ERROR', 'Could not find  \''+ modnamevar + '\'\nNão foi possível encontrar \'' + modnamevar + '\'')
            return
        saveall = []
        donemsg = False
        if not getline('vehicles.ide', pathvar, modnamevar, saveall, donemsg): return
        if not getline('handling.cfg', pathvar, modnamevar, saveall, donemsg): return
        if not getline('carcols.dat', pathvar, modnamevar, saveall, donemsg): return
        #getline('carmods.dat', pathvar, modnamevar, saveall, donemsg)
        '''line = modnamevar.lower() + ', nto_b_l, nto_b_s, nto_b_tw'
        saveall.append(line)'''
        #donemsg = True
        if donemsg == True:
            if not os.path.isdir(pathvar + '/output/'):
                os.mkdir(pathvar + '/output/')
            file = open(pathvar + '/output/' + modnamevar + '.txt', 'w')
            file.seek(0)
            for x in range(len(saveall)):
                saveall[x] = saveall[x] + '\n'
                file.write(saveall[x])
            file.close()
            messagebox.showinfo('Info', texts['donemsg1'])
        else:
            messagebox.showerror('ERROR', texts['errormsg1'])


    def CreateButton(var, tabname, text, command, width, column, row, sticky = None, height = 1, padx=5, pady=5, borderwidth=2, columnspan=1, image=None, compound=None,):
        #exec('%s = Button()' % (var))
        if  text in texts:
            text = texts[text]
        var = Button(tab[tabname], text=text, command=command, width=width, height=height, bd=borderwidth, image=image, compound=compound)
        if image or compound:
            var.image = image
        var.grid(padx=padx, pady=pady, column=column, row=row, sticky=sticky, columnspan=columnspan)
        return var


    # BUTTONS
    # tab 1
    configini = Button(tab['configini'], text=texts['apply1'], command=configini,width=20)
    configini.grid(padx=5, pady=5, column=0, row=20)

    inipathfile = Button(tab['configini'], text='...', command=inipathfile,width=4)
    inipathfile.grid(padx=5, pady=5, column=0, row=1, sticky=E)

    # tab 2
    configcar = Button(tab['lines'], text=texts['apply1'], command=rename, width=20)
    configcar.grid(padx=5, pady=5, column=0, row=20)

    configcarpath = Button(tab['lines'], text='...', command=configcarpath, width=4)
    configcarpath.grid(padx=5, pady=5, column=0, row=3, sticky=E)

    tip = Button(tab['lines'], text='?', command=tip, width=3)
    tip.grid(padx=5, pady=5, column=0, row=3, sticky=W)

    create = Button(tab['lines'], text=texts['create1'], command=create, width=20)
    create.grid(padx=5, pady=5, column=0, row=22)

    # tab 3
    configaudio = Button(tab['sound'], text=texts['apply1'], command=configaudio, width=20)
    configaudio.grid(padx=5, pady=5, column=0, row=20)

    configaudiopath = Button(tab['sound'], text='...', command=configaudiopath, width=4)
    configaudiopath.grid(padx=5, pady=5, column=0, row=0, sticky=E)

    removevar = BooleanVar()
    remove = Checkbutton(tab['sound'], text=texts['remove1'], variable=removevar)
    remove.grid(padx=5, pady=5, column=0, row=20, sticky=W)

    # tab 4
    configcargrp = Button(tab['vehnpcs'], text=texts['apply1'], command=configcargrp,width=20)
    configcargrp.grid(padx=5, pady=5, column=0, row=20)

    popcfgpath = Button(tab['vehnpcs'], text='...', command=popconfigpath, width=4)
    popcfgpath.grid(padx=5, pady=5, column=0, row=0, sticky=E)

    pophelp = Button(tab['vehnpcs'], text='?', command=pophelp, width=2)
    pophelp.grid(padx=5, pady=5, column=0, row=2, sticky=E)

    removevar2 = BooleanVar()
    remove2 = Checkbutton(tab['vehnpcs'], text=texts['remove1'], variable=removevar2)
    remove2.grid(padx=5, pady=5, column=0, row=20, sticky=W)

    # tab 5
    '''needed = Button(tab5, text=texts['needed'], command=needed)
    needed.grid(padx=5, pady=5, column=0, row=5)

    moreinfo = Button(tab5, text=texts['info'], command=moreinfo)
    moreinfo.grid(padx=5, pady=5, column=0, row=20)'''

    # ENTRIES
    # ======================== TAB 1 ========================

    dictlist['inipath'] = Entry(tab['configini'], width=80, borderwidth=2)
    dictlist['inipath'].insert(0, texts['inipath1'])
    dictlist['inipath'].config(fg='grey')
    dictlist['inipath'].grid(padx=50, pady=5, column=0, row=1)
    dictlist['inipath'].bind('<FocusIn>', onclick)

    # HANDLINE.CFG
    dictlist['handcfg'] = Entry(tab['configini'], width=80, borderwidth=2)
    dictlist['handcfg'].insert(0, 'Apply \'handling.cfg\' patch (0|1)')
    dictlist['handcfg'].config(fg='grey')
    dictlist['handcfg'].grid(padx=5, pady=5, column=0, row=2)
    dictlist['handcfg'].bind('<FocusIn>', onclick)

    handcfgbool = BooleanVar()
    handcfgbox = Checkbutton(tab['configini'], variable=handcfgbool)
    handcfgbox.grid(column=2, row=2)
    handcfgbox.select()

    # AUDIO
    dictlist['audio'] = Entry(tab['configini'], width=80, borderwidth=2)
    dictlist['audio'].insert(0, 'Enable vehicle audio loader (0|1)')
    dictlist['audio'].config(fg='grey')
    dictlist['audio'].grid(padx=5, pady=5, column=0, row=3)
    dictlist['audio'].bind('<FocusIn>', onclick)

    audiobool = BooleanVar()
    audiobox = Checkbutton(tab['configini'], variable=audiobool)
    audiobox.grid(column=2, row=3)
    audiobox.select()

    # LINES
    dictlist['handlines'] = Entry(tab['configini'], width=80, borderwidth=2)
    dictlist['handlines'].insert(0, 'Number of standard lines')
    dictlist['handlines'].config(fg='grey')
    dictlist['handlines'].grid(padx=5, pady=5, column=0, row=4)
    dictlist['handlines'].bind('<FocusIn>', onclick)

    handlinesbool = BooleanVar()
    handlinesbox = Checkbutton(tab['configini'], variable=handlinesbool)
    handlinesbox.grid(column=2, row=4)
    handlinesbox.select()

    # VEH MODELS
    dictlist['vehmodels'] = Entry(tab['configini'], width=80, borderwidth=2)
    dictlist['vehmodels'].insert(0, 'Vehicle Models')
    dictlist['vehmodels'].config(fg='grey')
    dictlist['vehmodels'].grid(padx=5, pady=5, column=0, row=5)
    dictlist['vehmodels'].bind('<FocusIn>', onclick)
    dictlist['vehmodels'].bind('<Enter>', onhover)
    dictlist['vehmodels'].bind('<Leave>', onleave)

    vehmodelsbool = BooleanVar()
    vehmodelsbox = Checkbutton(tab['configini'], variable=vehmodelsbool)
    vehmodelsbox.grid(column=2, row=5)
    vehmodelsbox.select()

    # KILLABLE MODELS
    dictlist['killablemodels'] = Entry(tab['configini'], width=80, borderwidth=2)
    dictlist['killablemodels'].insert(0, 'Count of killable model IDs')
    dictlist['killablemodels'].config(fg='grey')
    dictlist['killablemodels'].grid(padx=5, pady=5, column=0, row=6)
    dictlist['killablemodels'].bind('<FocusIn>', onclick)

    killablemodelsbool = BooleanVar()
    killablebox = Checkbutton(tab['configini'], variable=killablemodelsbool)
    killablebox.grid(column=2, row=6)
    killablebox.select()

    # BIKE
    dictlist['bikelines'] = Entry(tab['configini'], width=80, borderwidth=2)
    dictlist['bikelines'].insert(0, 'Number of bike lines')
    dictlist['bikelines'].config(fg='grey')
    dictlist['bikelines'].grid(padx=5, pady=5, column=0, row=7)
    dictlist['bikelines'].bind('<FocusIn>', onclick)

    bikelinesbool = BooleanVar()
    bikebox = Checkbutton(tab['configini'], variable=bikelinesbool)
    bikebox.grid(column=2, row=7)
    bikebox.select()

    # PLANE
    dictlist['planelines'] = Entry(tab['configini'], width=80, borderwidth=2)
    dictlist['planelines'].insert(0, 'Number of flying lines')
    dictlist['planelines'].config(fg='grey')
    dictlist['planelines'].grid(padx=5, pady=5, column=0, row=8)
    dictlist['planelines'].bind('<FocusIn>', onclick)

    planelinesbool = BooleanVar()
    planebox = Checkbutton(tab['configini'], variable=planelinesbool)
    planebox.grid(column=2, row=8)
    planebox.select()

    # BOAT
    dictlist['boatlines'] = Entry(tab['configini'], width=80, borderwidth=2)
    dictlist['boatlines'].insert(0, 'Number of boat lines')
    dictlist['boatlines'].config(fg='grey')
    dictlist['boatlines'].grid(padx=5, pady=5, column=0, row=9)
    dictlist['boatlines'].bind('<FocusIn>', onclick)

    boatlinesbool = BooleanVar()
    boatbox = Checkbutton(tab['configini'], variable=boatlinesbool)
    boatbox.grid(column=2, row=9)
    boatbox.select()

    # ======================== TAB 2 ========================

    dictlist['vehpath'] = Entry(tab['lines'], width=80, borderwidth=2)
    dictlist['vehpath'].insert(0, texts['vehpath1'])
    dictlist['vehpath'].config(fg='grey')
    dictlist['vehpath'].grid(padx=50, pady=5, column=0, row=3)
    dictlist['vehpath'].bind('<FocusIn>', onclick)

    dictlist['modname'] = Entry(tab['lines'], width=80, borderwidth=2)
    dictlist['modname'].insert(0, texts['modname1'])
    dictlist['modname'].config(fg='grey')
    dictlist['modname'].grid(padx=5, pady=5, column=0, row=4)
    dictlist['modname'].bind('<FocusIn>', onclick)

    dictlist['newname'] = Entry(tab['lines'], width=80, borderwidth=2)
    dictlist['newname'].insert(0, texts['newname1'])
    dictlist['newname'].config(fg='grey')
    dictlist['newname'].grid(padx=5, pady=5, column=0, row=5)
    dictlist['newname'].bind('<FocusIn>', onclick)

    dictlist['vehname'] = Entry(tab['lines'], width=80, borderwidth=2)
    dictlist['vehname'].insert(0, texts['vehname1'])
    dictlist['vehname'].config(fg='grey')
    dictlist['vehname'].grid(padx=5, pady=5, column=0, row=6)
    dictlist['vehname'].bind('<FocusIn>', onclick)

    dictlist['newid'] = Entry(tab['lines'], width=80, borderwidth=2)
    dictlist['newid'].insert(0, texts['newid1'])
    dictlist['newid'].config(fg='grey')
    dictlist['newid'].grid(padx=5, pady=5, column=0, row=7)
    dictlist['newid'].bind('<FocusIn>', onclick)

    newidvar = BooleanVar()
    newidbox = Checkbutton(tab['lines'], variable=newidvar)
    newidbox.grid(column=1, row=7)
    newidbox.select()

    labelsoundhint = Label(tab['sound'], text=texts['tip'])
    labelsoundhint.grid(column=0, row=8)

    def LabelSoundHintMsg(*args):
        labelsoundhint.configure(text='') # when item in classlist changes


    classlist = [texts['default1'], 'normal', 'poorfamily', 'richfamily', 'executive', 'worker', 'big', 'taxi', 'moped', 'motorbike', 'leisureboat', 'workerboat', 'bicycle', 'ignore']

    item = StringVar()
    item.set(texts['class1'])

    dropmenu = OptionMenu(tab['lines'], item, *classlist)
    dropmenu.config(width=15)
    dropmenu.grid(padx=5, pady=5, column=0, row=10)

    #fixname = '[]'

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
    vehitem.set(texts['sound1'])
    vehitem.trace('w', LabelSoundHintMsg)

    vehmenu = OptionMenu(tab['sound'], vehitem, *vehlist)
    vehmenu.config(width=15)
    vehmenu.grid(padx=5, pady=5, column=0, row=9)

    dictlist['audiocfgpath'] = Entry(tab['sound'], width=80, borderwidth=2)
    dictlist['audiocfgpath'].insert(0, texts['audiocfgpath1'])
    dictlist['audiocfgpath'].config(fg='grey')
    dictlist['audiocfgpath'].grid(padx=50, pady=5, column=0, row=0)
    dictlist['audiocfgpath'].bind('<FocusIn>', onclick)

    dictlist['newvehname'] = Entry(tab['sound'], width=80, borderwidth=2)
    dictlist['newvehname'].insert(0, texts['newvehname1'])
    dictlist['newvehname'].config(fg='grey')
    dictlist['newvehname'].grid(padx=5, pady=5, column=0, row=1)
    dictlist['newvehname'].bind('<FocusIn>', onclick)

    dictlist['vehaudio'] = Entry(tab['sound'], width=80, borderwidth=2)
    dictlist['vehaudio'].insert(0, texts['vehaudio1'])
    dictlist['vehaudio'].config(fg='grey')
    dictlist['vehaudio'].grid(padx=5, pady=5, column=0, row=2)
    dictlist['vehaudio'].bind('<FocusIn>', onclick)

    # ======================== TAB 4 ========================

    dictlist['popcyclepath'] = Entry(tab['vehnpcs'], width=80, borderwidth=2)
    dictlist['popcyclepath'].insert(0, texts['popcyclepath1'])
    dictlist['popcyclepath'].config(fg='grey')
    dictlist['popcyclepath'].grid(padx=50, pady=5, column=0, row=0)
    dictlist['popcyclepath'].bind('<FocusIn>', onclick)

    dictlist['popcycleveh'] = Entry(tab['vehnpcs'], width=80, borderwidth=2)
    dictlist['popcycleveh'].insert(0, texts['popcycleveh1'])
    dictlist['popcycleveh'].config(fg='grey')
    dictlist['popcycleveh'].grid(padx=5, pady=5, column=0, row=1)
    dictlist['popcycleveh'].bind('<FocusIn>', onclick)

    poplist = ['POPCYCLE_GROUP_WORKERS', 'POPCYCLE_GROUP_BUSINESS', 'POPCYCLE_GROUP_CLUBBERS', 'POPCYCLE_GROUP_FARMERS', 'POPCYCLE_GROUP_BEACHFOLK', 'POPCYCLE_GROUP_PARKFOLK',
            'POPCYCLE_GROUP_CASUAL_RICH', 'POPCYCLE_GROUP_CASUAL_AVERAGE', 'POPCYCLE_GROUP_CASUAL_POOR', 'POPCYCLE_GROUP_PROSTITUTES', 'POPCYCLE_GROUP_CRIMINALS',
            'POPCYCLE_GROUP_GOLFERS', 'POPCYCLE_GROUP_SERVANTS', 'POPCYCLE_GROUP_AIRCREW', 'POPCYCLE_GROUP_ENTERTAINERS', 'POPCYCLE_GROUP_OUT_OF_TOWN_FACTORY',
            'POPCYCLE_GROUP_DESERT_FOLK', 'POPCYCLE_GROUP_AIRCREW_RUNWAY', 'Boats']

    popitem = StringVar()
    popitem.set(texts['popitem1'])

    popmenu = OptionMenu(tab['vehnpcs'], popitem, *poplist)
    popmenu.config(width=40)
    popmenu.grid(padx=5, pady=5, column=0, row=2)

    # TAB 5

    idlistbox = Listbox(tab['idlist'], width=75, height=15, selectmode='multiple', font='Courier 11')
    idlistbox.grid(column=1, row=3, columnspan=5, rowspan=4, sticky=EW)

    scrollbar = Scrollbar(tab['idlist'])
    scrollbar.grid(column=5, row=3, sticky='NSE', rowspan=5)
    idlistbox.config(yscrollcommand = scrollbar.set) # linking listbox with scrollbar
    scrollbar.config(command = idlistbox.yview)

    #idlistlabel = Label(tab['idlist'], text=texts['idlist1'])
    #idlistlabel.grid(column=2, row=0)

    CreateEntry('idlistpath', 'idlist', 'idlistpath1', 1, 1, 80, 4, W, 0, 0)

    idlistitems = {}
    sortbuttons = {}
    sortedorder = True
    sortedby = 'id'

    def SortBy(args, var=None):
        nonlocal sortedorder
        nonlocal sortedby

        if not args == 'default':
            if sortedorder: sortedorder = False
            else: sortedorder = True
            sortedby = args
        else:
            args = sortedby

        if var:
            for k, v in sortbuttons.items():
                if not k == var:
                    sortbuttons[k].config(text=texts[k])
                else:
                    sortbuttons[k].config(text='{:<5}{:^5}{:>5}'.format(' ', texts[k], (sortedorder and '↓' or '↑')))

        if args == 'id':
            order = lambda x: x[0]
        elif args == 'name':
            order = lambda x: x[1]
        elif args == 'file':
            order = lambda x: x[1][1]

        idlistbox.delete(0, 'end')
        for key, value in sorted(idlistitems.items(), key=order, reverse=sortedorder):
            idlistbox.insert(0, f' {key:<27}{idlistitems[key][0]:^27}{idlistitems[key][1]:>27} ')


    if os.path.isfile(os.getcwd() + '/data/idsdata.pkl'):
        while True:
            try:
                file = open(os.getcwd() + '/data/idsdata.pkl', 'rb')
                idlistitems = pickle.load(file)
            except EOFError:
                break
            file.close()
            for k, v in idlistitems.items():
                idlistitems[k] = [v[0], texts['originsaved']]
            SortBy('default')
            break
        
        
    def search():
        import random
        count = 0
        path = '/home/runner/Vehicle-Mod-Editor'
        with os.scandir(path + '/tests') as itr:
            for file in itr:
                if file.name.endswith('.txt') and file.is_file():
                    os.remove(path + '/tests/' + file.name)
        while count < 10:
            randnumb = random.randint(200, 500)
            randname = random.choice(veh[1:-1].split(','))
            f = open('/home/runner/Vehicle-Mod-Editor/tests/' + randname + '.txt', 'w')
            line = '{},\t{},\t{},\t{},\t{},\tnull, null, null, {},\t{},\t-{}, {}, {},\t1, 50.0, 0'.format(randnumb, randname, randname,  randname.upper(), randname.upper(), random.uniform(30, 300), random.uniform(50, 900),random.randint(0, 500), random.randint(0, 100), random.randint(100, 2000))
            f.write(line)
            f.close()
            count += 1
        #time.sleep(1)
        #path = dictlist['idlistpath'].get() # /home/runner/Vehicle-Mod-Editor
        path = '/home/runner/Vehicle-Mod-Editor/tests'
        with os.scandir(path) as itr:
            for file in itr:
                if file.name.endswith('.txt') and file.is_file():
                    with open(path + '/' + file.name, 'r') as read:
                        for line in read:
                            tmp = re.search(r'(\d+),\s+(\w+),\s+\w+,\s+\w+,\s+\w+,\s+\w+,\s+\w+,\s+\w+,\s+-?\d+\.?\d*,\s+-?\d+\.?\d*,\s+-?\d+\.?\d*,\s+-?\d+\.?\d*,\s+-?\d+\.?\d*,\s+-?\d+\.?\d*,\s+-?\d+\.?\d*,\s+-?\d+\.?\d*\s*', line) # integer, word (7), number (8)
                            if tmp:
                                idlistitems[tmp.group(1)] = [tmp.group(2), texts['originnonsaved']]
        #idlistitems.sort(key=int)
        idlistbox.delete(0, 'end')
        SortBy('default')




    '''style = Style()
        style.configure('TButton', font =('calibri', 20, 'bold'), borderwidth = '4')
            style.map('TButton', foreground = [('active', 'disabled', 'green')], background = [('active', 'black')])'''

    def SaveToFile(*kwargs):
        currentdir = os.getcwd()

        if not os.path.isdir(currentdir + '/data'):
            os.mkdir(currentdir + '/data')

        tmpdict = {}
        for k, v in idlistitems.items():
            if not kwargs:
                idlistitems[k][1] = texts['originsaved']
            if idlistitems[k][1] == texts['originsaved']:
                tmpdict[k] = v

        with open(currentdir + '/data/idsdata.pkl', 'wb+') as file:
            pickle.dump(tmpdict, file)
        '''if not kwargs:
            with open(currentdir + '/data/idsdata.pkl', 'wb+') as file:
                pickle.dump(idlistitems, file)
                for k, v in idlistitems.items():
                    idlistitems[k][1] = texts['originsaved']
        else:
            with open(currentdir + '/data/idsdata.pkl', 'ab+') as file:
                for k, v in kwargs.items():
                    tmpdict = {}
                    tmpdict[k] = [v, texts['originsaved']]
                    print(tmpdict)
                    idlistitems[k] = [v, texts['originsaved']]
                    pickle.dump(tmpdict, file)'''

        SortBy('default')


    def RemoveFromList():
        selection = idlistbox.curselection()
        listselection = list(selection)
        for i in reversed(selection):
            value = idlistbox.get(listselection[-1])
            tmp = re.search(r'\s+(\d+)\s+\w+\s+\w+', value)
            if tmp:
                key = tmp.group(1)
                #if idlistitems[key][1] == texts['originsaved']:
                #    idlistitems[key][1] == texts['originnonsaved']
                idlistbox.delete(i)
                del idlistitems[key]
                del listselection[-1]
                    
        SaveToFile(None)


    def AddToList(newitemid, newitemname, win, label):
        id = newitemid.get()
        name = newitemname.get().lower()
        if not id or not name: label.config(text=texts['additemerrorempty'], fg='red'); return
        if not id.isdecimal(): label.config(text=texts['additemerrornumbers'], fg='red'); return
        if len(id) > 8 or len(name) > 8: label.config(text=texts['additemerrorlenght'], fg='red'); return
        for k, v in idlistitems.items():
            if k == id: label.config(text=texts['additemerroridexists'], fg='red'); return
            if v[0] == name: label.config(text=texts['additemerrornameexists'], fg='red'); return

        idlistitems[id] = [name, texts['originsaved']]
        SaveToFile(None)
        win.destroy()
        

    def CancelAdding(win):
        win.destroy()

    def AddWindow():
        win = tk.Toplevel()
        win.title('Add')
        win.geometry('500x200')
        win.attributes('-topmost', True)

        newitemlabel = Label(win, text=texts['newitemlabel1'])
        newitemlabel.grid(padx=5, pady=5, column=1, row=0, columnspan=2)

        newitemid = Entry(win, width=50, borderwidth=5)
        newitemid.insert(0, 'ID')
        newitemid.grid(padx=5, pady=5, column=1, row=1, columnspan=2)

        newitemname = Entry(win, width=50, borderwidth=5)
        newitemname.insert(0, texts['idlistvehname'])
        newitemname.grid(padx=5, pady=5, column=1, row=2, columnspan=2)

        okbutton = Button(win, text='Ok', command=lambda: AddToList(newitemid, newitemname, win, newitemlabel), width=5)
        cancelbutton = Button(win, text=texts['cancelbutton1'], command=lambda: CancelAdding(win), width=5)
        okbutton.grid(padx=5, pady=5, column=1, row=3, sticky=EW)
        cancelbutton.grid(padx=5, pady=5, column=2, row=3, sticky=EW)

        win.grid_columnconfigure((0, 4), weight=1)
        


    def SelectAll():
        selection = idlistbox.curselection()
        if selection: idlistbox.selection_clear(0, END)
        else: idlistbox.select_set(0, END)


    #savebutton = PhotoImage(data=b64)

    savebutton = PhotoImage(file=os.getcwd() + '/savebutton.png')
    selectall = PhotoImage(file=os.getcwd() + '/selectall.png')
    remove = PhotoImage(file=os.getcwd() + '/remove.png')
    add = PhotoImage(file=os.getcwd() + '/add.png')

    #sortbuttons['idlistvehid'] = CreateButton(sortbuttons['idlistvehid'], 'idlist', 'ID', lambda: SortBy('id', 'idlistvehid'), 23, 1, 2, W, 1, 0, 0, 0)
    sortbuttons['idlistvehid'] = Button(tab['idlist'], text=texts['idlistvehid'], command=lambda: SortBy('id', 'idlistvehid'), borderwidth=0, width=23)
    sortbuttons['idlistvehid'].grid(column=1, row=2, sticky=W)

    sortbuttons['idlistvehname'] = Button(tab['idlist'], text=texts['idlistvehname'], command=lambda: SortBy('name', 'idlistvehname'), borderwidth=0, width=23)
    sortbuttons['idlistvehname'].grid(column=2, row=2, sticky=EW)
    #sortbuttons['idlistvehname'] = CreateButton('idlistvehname', 'idlist', 'idlistvehname', lambda: SortBy('name'), 23, 2, 2, EW,  1, 0, 0, 0)

    sortbuttons['idlistvehsaved'] = Button(tab['idlist'], text=texts['idlistvehsaved'], command=lambda: SortBy('file', 'idlistvehsaved'), borderwidth=0, width=23)
    sortbuttons['idlistvehsaved'].grid(column=3, row=2, sticky=EW)
    #sortbuttons['idlistvehsaved'] = CreateButton('idlistvehsaved', 'idlist', 'idlistvehsaved', lambda: SortBy('file'), 23, 3, 2, EW, 1, 0, 0, 0)
    
    idlistsearch = CreateButton('idlistsearch', 'idlist', '>', search, 1,  5, 1, E, 0, 0, 1)

    idlistsave = CreateButton('idlistsave', 'idlist', ' ', SaveToFile, 5, 0, 3, 'NSW', 1, 0, 0, 2, 1, savebutton, compound=CENTER)
    idlistselectall = CreateButton('idlistselectall', 'idlist', ' ', SelectAll, 5, 0, 4, 'NSW', 1, 0, 0, 2, 1, selectall, compound=CENTER)
    idlistremove = CreateButton('idlistremove', 'idlist', ' ', RemoveFromList, 5, 0, 5, 'NSW', 1, 0, 0, 2, 1, remove, compound=CENTER)
    idlistadd = CreateButton('idlistadd', 'idlist', ' ', AddWindow, 5, 0, 6, 'NSW', 1, 0, 0, 2, 1, add, compound=CENTER)

    SortBy('id', 'idlistvehid')
    #tab_parent.grid_columnconfigure((0,1, 2, 3, 4), weight=1)
    #root.grid_columnconfigure((0,1, 2, 3, 4), weight=1)
    #tab['idlist'].grid_columnconfigure((0, 7), weight=1)
    #tab['idlist'].grid_rowconfigure((3, 4), weight=1,   uniform='row')
    return