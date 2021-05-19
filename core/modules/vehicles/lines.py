from tkinter import *
from resources import *
import gettext

en = gettext.translation('base', localedir='core/locales', languages=['en'])
en.install()
_ = en.gettext

def lines():
    def rename_vehicle_lines():
        vehpath = dictlist['vehpath'].get()
        modname = dictlist['modname'].get()
        newname = dictlist['newname'].get()
        vehname = dictlist['vehname'].get()
        newid = dictlist['newid'].get()
        saveall = []
        donemsg = False

        if len(modname) == 0 or modname == translation('vehicles', 'linestab', 'modname'):
            messagebox.showwarning('ERROR', '\'' + translation('vehicles', 'linestab', 'modname') + '\'\nCannot be empty\nNão pode estar vazio')
            return
        if len(newname) > 7 or len(newname) == 0:
            messagebox.showwarning(translation('others', 'messages', 'warning'), translation('vehicles', 'linestab', 'modnamelength'))
            return

        file = try_and_open_file(vehpath, modname)
        if not file: return

        while True:
            line = try_and_read_file_line(file, vehpath, modname)
            if not line:
                file.seek(0)
                for x in range(len(saveall)):
                    file.write(saveall[x])
                break
            if len(line) > 0:
                tmp = re.search(r'(\d+),\s+\w+,\s+\w+,\s+\w+,\s+\w+,\s+\w+,\s+\w+,\s+(\w+),\s+-?\d+\.?\d*,\s+-?\d+\.?\d*,\s+-?\d+\.?\d*,\s+-?\d+\.?\d*,\s+-?\d+\.?\d*,\s+-?\d+\.?\d*\s*', line) # integer (id), word (7), number (7)    [vehicles.ide]
                if tmp:
                    if newidbool.get() == True and len(newid) != 0 and newid.isdecimal():
                        line = line.replace(tmp.group(1), newid, 1)
                    if item.get() != translation('others', 'messages', 'default').upper() and item.get() != translation('vehicles', 'linestab', 'vehicleclass'):
                        line = line.replace(tmp.group(2), item.get())
                if modname.lower() in line:
                    line = line.replace(modname.lower(), newname.lower())
                    donemsg = True
                if modname.upper() in line:
                    line = line.replace(modname.upper(), newname.upper())
                    donemsg = True
            saveall.append(line)

        file.close()
        if donemsg == True:
            if os.path.isfile(vehpath + '/' + modname + '.dff'):
                os.rename(vehpath + '/' + modname + '.dff', vehpath + '/' + newname + '.dff')
            if os.path.isfile(vehpath + '/' + modname + '.txd'):
                os.rename(vehpath + '/' + modname + '.txd', vehpath + '/' + newname + '.txd')
            if os.path.isfile(vehpath + '/' + modname + '.txt'):
                os.rename(vehpath + '/' + modname + '.txt', vehpath + '/' + newname + '.txt')
            if not len(vehname) == 0 and not vehname == translation('vehicles', 'linestab', 'vehiclename'):
                if os.path.isfile(vehpath + '/' + modname + '.fxt'):
                    os.rename(vehpath + '/' + modname + '.fxt', vehpath + '/' + newname + '.fxt')
                file = open(vehpath + '/' + newname + '.fxt', 'w')
                file.seek(0)
                file.write(newname.upper() + ' ' + vehname)
                file.close()
            messagebox.showinfo('Info', translation('others', 'messages', 'applied'))
        else:
            messagebox.showerror('ERROR', translation('others', 'errors', 'notapplied'))


    def tip():
        if lang == 'pt_BR' or lang == 'pt_PT':
            messagebox.showinfo('Ajuda', 'Para aplicar as linhas no novo veículo: Coloque o veículo (.txd e .dff) e o arquivo de linhas (.txt) numa pasta (de preferência já dentro do modloader), '
                                            'e renomeie o arquivo de linhas para o mesmo nome do arquivo do veículo. O programa mudará o nome de todos esses arquivos para o novo nome do mod escolhido')
        else:
            messagebox.showinfo('Help', 'To apply the lines to the new vehicle: Place the vehicle (.txd and .dff) and the lines file (.txt) in a folder (preferably already inside the modloader), '
                                                'and rename the line file to the same name as the vehicle file. The program will rename all those files to the name of the new mod name chosen')
                                                

    def configcarpath():
        filename = filedialog.askdirectory()
        dictlist['vehpath'].delete(0, 'end')
        dictlist['vehpath'].insert(0, filename)
        dictlist['vehpath'].config(fg='black')


    def getline(filename, vehpath, modname, saveall, donemsg):
        try:
            file = open(vehpath + '/' + filename, 'r')
        except:
            try:
                file = open(vehpath + '/' + filename, 'r', encoding='utf8', errors='ignore')
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
                        file = open(vehpath + '/' + filename, 'r', encoding='utf8', errors='ignore')
                    except:
                        messagebox.showerror('ERROR', 'Could not read a line in the file, try to remove manually special characters from the file ex. russian, arab characters, etc. or try to change the file encoding')
                    line = file.readline()
                    passed = True
            if not line:
                break
            if modname.lower() in line:
                modname = modname.lower()
            if modname.upper() in line:
                modname = modname.upper()
            #if re.search(modname + ',', line) or re.search(r'\s*' + modname, line) or re.search(modname + r'\s*', line):
            if modname in line:
                if not re.search(r'\w' + modname, line) and not re.search(modname + r'\w', line):
                    '''if filename == 'carmods.dat':
                        line = modname + ', nto_b_l, nto_b_s, nto_b_tw'''
                    saveall.append(line)
                    donemsg = True
        modname = dictlist['modname'].get()
        file.close()
        return donemsg



    def create():
        vehpath = dictlist['vehpath'].get()
        modname = dictlist['modname'].get()
        '''newname = dictlist['newname'].get()
        vehname = dictlist['vehname'].get()
        newid = dictlist['newid'].get()'''
        if not any(ext in modname for ext in vehlist):
            messagebox.showerror('ERROR', 'Could not find  \''+ modname + '\'\nNão foi possível encontrar \'' + modname + '\'')
            return
        saveall = []
        donemsg = False
        if not getline('vehicles.ide', vehpath, modname, saveall, donemsg): return
        if not getline('handling.cfg', vehpath, modname, saveall, donemsg): return
        if not getline('carcols.dat', vehpath, modname, saveall, donemsg): return
        #getline('carmods.dat', vehpath, modname, saveall, donemsg)
        '''line = modname.lower() + ', nto_b_l, nto_b_s, nto_b_tw'
        saveall.append(line)'''
        #donemsg = True
        if donemsg == True:
            if not os.path.isdir(vehpath + '/output/'):
                os.mkdir(vehpath + '/output/')
            file = open(vehpath + '/output/' + modname + '.txt', 'w')
            file.seek(0)
            for x in range(len(saveall)):
                saveall[x] = saveall[x] + '\n'
                file.write(saveall[x])
            file.close()
            messagebox.showinfo('Info', translation('others', 'messages', 'applied'))
        else:
            messagebox.showerror('ERROR',  translation('others', 'errors', 'notapplied'))


    applybutton = Button(tab['lines'], text=translation('others', 'messages', 'apply'), command=rename_vehicle_lines, width=20)
    applybutton.grid(padx=5, pady=5, column=0, row=20)

    configcarpath = Button(tab['lines'], text='...', command=configcarpath, width=4)
    configcarpath.grid(padx=5, pady=5, column=0, row=3, sticky=E)

    tip = Button(tab['lines'], text='?', command=tip, width=3)
    tip.grid(padx=5, pady=5, column=0, row=3, sticky=W)

    create = Button(tab['lines'], text=translation('others', 'messages', 'create'), command=create, width=20)
    create.grid(padx=5, pady=5, column=0, row=22)

    dictlist['vehpath'] = Entry(tab['lines'], width=80, borderwidth=2)
    dictlist['vehpath'].insert(0, _('Caminho para o modelo do veículo'))
    dictlist['vehpath'].config(fg='grey')
    dictlist['vehpath'].grid(padx=50, pady=5, column=0, row=3)
    dictlist['vehpath'].bind('<FocusIn>', onclick)

    dictlist['modname'] = Entry(tab['lines'], width=80, borderwidth=2)
    dictlist['modname'].insert(0, _('Nome do modelo do veículo'))
    dictlist['modname'].config(fg='grey')
    dictlist['modname'].grid(padx=5, pady=5, column=0, row=4)
    dictlist['modname'].bind('<FocusIn>', onclick)

    dictlist['newname'] = Entry(tab['lines'], width=80, borderwidth=2)
    dictlist['newname'].insert(0, _('Novo nome para o modelo do veículo'))
    dictlist['newname'].config(fg='grey')
    dictlist['newname'].grid(padx=5, pady=5, column=0, row=5)
    dictlist['newname'].bind('<FocusIn>', onclick)

    dictlist['vehname'] = Entry(tab['lines'], width=80, borderwidth=2)
    dictlist['vehname'].insert(0, translation('vehicles', 'linestab', 'newvehiclename'))
    dictlist['vehname'].config(fg='grey')
    dictlist['vehname'].grid(padx=5, pady=5, column=0, row=6)
    dictlist['vehname'].bind('<FocusIn>', onclick)

    dictlist['newid'] = Entry(tab['lines'], width=80, borderwidth=2)
    dictlist['newid'].insert(0, translation('vehicles', 'linestab', 'newid'))
    dictlist['newid'].config(fg='grey')
    dictlist['newid'].grid(padx=5, pady=5, column=0, row=7)
    dictlist['newid'].bind('<FocusIn>', onclick)

    newidbool = BooleanVar()
    newidbox = Checkbutton(tab['lines'], variable=newidbool)
    newidbox.grid(column=1, row=7)
    newidbox.select()

    classlist = [translation('others', 'messages', 'default').upper(), 'normal', 'poorfamily', 'richfamily', 'executive', 'worker', 'big', 'taxi', 'moped', 'motorbike', 'leisureboat', 'workerboat', 'bicycle', 'ignore']

    item = StringVar()
    item.set(translation('vehicles', 'linestab', 'vehicleclass'))

    dropmenu = OptionMenu(tab['lines'], item, *classlist)
    dropmenu.config(width=15)
    dropmenu.grid(padx=5, pady=5, column=0, row=10)