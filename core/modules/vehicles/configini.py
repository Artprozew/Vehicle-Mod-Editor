from tkinter import *
from resources import *
import gettext

_ = gettext.gettext


def configini():
    def configinifile():
        #boollist = ['handcfgvar', 'audiovar', 'handlinesvar', 'vehmodelsvar', 'killablevar', 'bikevar', 'planevar', 'boatvar']
        #itemslist = ['Apply handling.cfg patch =', 'Enable vehicle audio loader =','Number of standard lines =', 'Vehicle Models =', 'Count of killable model IDs =', 'Number of bike lines =', 'Number of flying lines =', 'Number of boat lines =']
        #answer = [dictlist['handcfg'].get(), dictlist['audio'].get(), dictlist['handlines'].get(), dictlist['vehmodels'].get(), dictlist['killablemodels'].get(), dictlist['bikelines'].get(), dictlist['planelines'].get(), dictlist['boatlines'].get()]
        inisave = []
        line = None
        inipath2 = dictlist['inipath'].get()
        file = try_and_open_file(inipath2, 'fastman92limitAdjuster_GTA{}.ini', True)
        if not file: return

        while True:
            line = try_and_read_file_line(file, inipath2)
            if not line:
                file.seek(0)
                for x in range(len(inisave)):
                    file.write(inisave[x])
                break

            if len(line) > 0:
                for k, v in dictlist.items():
                #for x in range(len(itemslist)):
                    #var = itemslist[x]
                    try:
                        var = v[2] + ' ='
                    except TypeError:
                        continue
                        
                    if var in line:
                        num = re.findall(r'\d+', line)
                        tmp = ''.join(num)
                        tmp = var + ' ' + tmp
                        #for k, v in dictlist.items():
                        if not v[0].get().isdecimal() or not v[0].get() or v[1].get() == False:
                        #if not answer[x].isdecimal() or not answer[x] or boollist[x].get()  ==False:
                            var = var + ' ' + ''.join(num)
                            if v[1].get() == False:
                                if not '#' in line and not ';' in line:
                                    var = '#' + var
                        else:
                            var = var + ' ' + v[0].get()
                            donemsg = True
                        #if boollist[x].get() == True and answer[x].isdecimal() and le(answe[x] ) > 0:
                            if '#' in line:
                                tmp = '#' + tmp  # add the '#' so line.replace below will remove it
                            if ';' in line:
                                tmp = ';' + tmp
                        line = line.replace(tmp, var)
            inisave.append(line)
        file.close()
        if donemsg == True:
            messagebox.showinfo(_('Informação'), _('As mudanças foram aplicadas com sucesso'))
        else:
            messagebox.showerror(_('Erro'), _('Ocorreu um erro e as mudanças não puderam ser aplicadas'))


    def onhover(event):
        time.sleep(0.1)
        inihints.configure(text=_('Não mude essa linha'))


    def onleave(event):
        inihints.configure(text='')


    def inipathfile():
        filename = filedialog.askdirectory()
        dictlist['inipath'].delete(0, 'end')
        dictlist['inipath'].insert(0, filename)
        dictlist['inipath'].config(fg='black')


    inihints = Label(tab['configini'], text='', justify='left', anchor=W)
    inihints.grid(padx=0, pady=0, column=1, row=18, sticky=W)

    configini = Button(tab['configini'], text=_('Aplicar'), command=configinifile, width=20)
    configini.grid(padx=5, pady=5, column=1, row=20, sticky=E)

    inipathfile = Button(tab['configini'], text='...', command=inipathfile, width=1)
    inipathfile.grid(padx=5, pady=5, column=3, row=1, columnspan=1, rowspan=1)

    dictlist['inipath'] = Entry(tab['configini'], width=75, borderwidth=2)
    dictlist['inipath'].insert(0, _('Caminho para o "fastman92limitAdjuster_GTASA.ini"'))
    dictlist['inipath'].config(fg='grey')
    dictlist['inipath'].grid(padx=0, pady=5, column=1, row=1, columnspan=2)
    dictlist['inipath'].bind('<FocusIn>', onclick)

    savcbox = Checkbutton(tab['configini'], text='VC', command=functions.savc_checkbox, variable=savcbool)
    savcbox.grid(padx=5, pady=5, column=0, row=1, sticky=W, columnspan=1)
    savcbox.deselect()

    # HANDLING.CFG PATCH
    dictlist['handcfg'] = [Entry(tab['configini'], width=75, borderwidth=2), BooleanVar(), _(&#39;Apply &quot;handling.cfg&quot;&#39;))]
    dictlist['handcfg'][0].insert(0, _('Apply "handling.cfg"'))
    dictlist['handcfg'][0].config(fg='grey')
    dictlist['handcfg'][0].grid(padx=5, pady=5, column=1, row=2, columnspan=2)
    dictlist['handcfg'][0].bind('<FocusIn>', onclick)

    handcfgbox = Checkbutton(tab['configini'], variable=dictlist['handcfg'][1])
    handcfgbox.grid(column=3, row=2)
    handcfgbox.select()

    # AUDIO LOADER
    dictlist['audio'] = [Entry(tab['configini'], width=75, borderwidth=2), BooleanVar(), _('Enable vehicle audio loader')]
    dictlist['audio'][0].insert(0, _('Enable vehicle audio loader'))
    dictlist['audio'][0].config(fg='grey')
    dictlist['audio'][0].grid(padx=5, pady=5, column=1, row=3, columnspan=2)
    dictlist['audio'][0].bind('<FocusIn>', onclick)

    audiobox = Checkbutton(tab['configini'], variable=dictlist['audio'][1])
    audiobox.grid(column=3, row=3)
    audiobox.select()

    # STANDARD LINES
    dictlist['handlines'] = [Entry(tab['configini'], width=75, borderwidth=2), BooleanVar(), translation('vehicles', 'configinitab', 'standardlines')]
    dictlist['handlines'][0].insert(0, translation('vehicles', 'configinitab', 'standardlines'))
    dictlist['handlines'][0].config(fg='grey')
    dictlist['handlines'][0].grid(padx=5, pady=5, column=1, row=4, columnspan=2)
    dictlist['handlines'][0].bind('<FocusIn>', onclick)

    handlinesbox = Checkbutton(tab['configini'], variable=dictlist['handlines'][1])
    handlinesbox.grid(column=3, row=4)
    handlinesbox.select()

    # VEH MODELS
    dictlist['vehmodels'] = [Entry(tab['configini'], width=75, borderwidth=2), BooleanVar(), translation('vehicles', 'configinitab', 'vehiclemodels')]
    dictlist['vehmodels'][0].insert(0, translation('vehicles', 'configinitab', 'vehiclemodels'))
    dictlist['vehmodels'][0].config(fg='grey')
    dictlist['vehmodels'][0].grid(padx=5, pady=5, column=1, row=5, columnspan=2)
    dictlist['vehmodels'][0].bind('<FocusIn>', onclick)
    dictlist['vehmodels'][0].bind('<Enter>', onhover)
    dictlist['vehmodels'][0].bind('<Leave>', onleave)

    vehmodelsbox = Checkbutton(tab['configini'], variable=dictlist['vehmodels'][1])
    vehmodelsbox.grid(column=3, row=5)
    vehmodelsbox.select()

    # KILLABLE MODELS
    dictlist['killablemodels'] = [Entry(tab['configini'], width=75, borderwidth=2), BooleanVar(), translation('vehicles', 'configinitab', 'killablemodels')]
    dictlist['killablemodels'][0].insert(0, translation('vehicles', 'configinitab', 'killablemodels'))
    dictlist['killablemodels'][0].config(fg='grey')
    dictlist['killablemodels'][0].grid(padx=5, pady=5, column=1, row=6, columnspan=2)
    dictlist['killablemodels'][0].bind('<FocusIn>', onclick)

    killablebox = Checkbutton(tab['configini'], variable=dictlist['killablemodels'][1])
    killablebox.grid(column=3, row=6)
    killablebox.select()

    # BIKE
    dictlist['bikelines'] = [Entry(tab['configini'], width=75, borderwidth=2), BooleanVar(), translation('vehicles', 'configinitab', 'bikelines')]
    dictlist['bikelines'][0].insert(0, translation('vehicles', 'configinitab', 'bikelines'))
    dictlist['bikelines'][0].config(fg='grey')
    dictlist['bikelines'][0].grid(padx=5, pady=5, column=1, row=7, columnspan=2)
    dictlist['bikelines'][0].bind('<FocusIn>', onclick)

    bikebox = Checkbutton(tab['configini'], variable=dictlist['bikelines'][1])
    bikebox.grid(column=3, row=7)
    bikebox.select()

    # PLANE
    dictlist['planelines'] = [Entry(tab['configini'], width=75, borderwidth=2), BooleanVar(), translation('vehicles', 'configinitab', 'planelines')]
    dictlist['planelines'][0].insert(0, translation('vehicles', 'configinitab', 'planelines'))
    dictlist['planelines'][0].config(fg='grey')
    dictlist['planelines'][0].grid(padx=5, pady=5, column=1, row=8, columnspan=2)
    dictlist['planelines'][0].bind('<FocusIn>', onclick)

    planebox = Checkbutton(tab['configini'], variable=dictlist['planelines'][1])
    planebox.grid(column=3, row=8)
    planebox.select()

    # BOAT
    dictlist['boatlines'] = [Entry(tab['configini'], width=75, borderwidth=2), BooleanVar(), translation('vehicles', 'configinitab', 'boatlines')]
    dictlist['boatlines'][0].insert(0, translation('vehicles', 'configinitab', 'boatlines'))
    dictlist['boatlines'][0].config(fg='grey')
    dictlist['boatlines'][0].grid(padx=5, pady=5, column=1, row=9, columnspan=2)
    dictlist['boatlines'][0].bind('<FocusIn>', onclick)

    boatbox = Checkbutton(tab['configini'], variable=dictlist['boatlines'][1])
    boatbox.grid(column=3, row=9)
    boatbox.select()
    
    #tab['configini'].columnconfigure((0, 4), weight=1)