from tkinter import *
from resources import *
import pickle

def idlist():
    idlistbox = Listbox(tab['idlist'], width=75, height=15, selectmode='multiple', font='Courier 11')
    idlistbox.grid(column=1, row=3, columnspan=5, rowspan=4, sticky=EW)

    scrollbar = Scrollbar(tab['idlist'])
    scrollbar.grid(column=5, row=3, sticky='NSE', rowspan=5)
    idlistbox.config(yscrollcommand = scrollbar.set)  # Linking the listbox with scrollbar
    scrollbar.config(command = idlistbox.yview)

    #idlistlabel = Label(tab['idlist'], text=texts['idlist1'])
    #idlistlabel.grid(column=2, row=0)

    #CreateEntry('idlistpath', 'idlist', 'idlistpath1', 1, 1, 80, 4, W, 0, 0)
    dictlist['idlistpath'] = Entry(tab['idlist'], text=translation('vehicles', 'idlisttab', 'pathtosearchids'), width=80)
    dictlist['idlistpath'].grid(padx=0, pady=5, column=1, row=1, sticky=W, columnspan=4)
    dictlist['idlistpath'].insert(0, translation('vehicles', 'idlisttab', 'pathtosearchids'))
    dictlist['idlistpath'].config(fg='grey')

    idlistitems = {}
    sortbuttons = {}
    sortedorder = True
    sortedby = 'id'

    def sort_listbox_by(args, var=None):
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
                    sortbuttons[k].config(text=translation('vehicles', 'idlisttab', k))
                else:
                    sortbuttons[k].config(text='{:<5}{:^5}{:>5}'.format(' ', translation('vehicles', 'idlisttab', k), (sortedorder and '↓' or '↑')))

        if args == 'id':
            order = lambda x: x[0]
        elif args == 'name':
            order = lambda x: x[1]
        elif args == 'file':
            order = lambda x: x[1][1]

        idlistbox.delete(0, 'end')
        for key, value in sorted(idlistitems.items(), key=order, reverse=sortedorder):
            idlistbox.insert(0, f' {key:<27}{idlistitems[key][0]:^27}{idlistitems[key][1]:>27} ')


    if os.path.isfile(os.getcwd() + '/data/vehicles_ids.pkl'):
        while True:
            try:
                file = open(os.getcwd() + '/data/vehicles_ids.pkl', 'rb')
                idlistitems = pickle.load(file)
            except EOFError:
                break
            file.close()
            for k, v in idlistitems.items():
                idlistitems[k] = [v[0], translation('vehicles', 'idlisttab', 'originsaved')]
            sort_listbox_by('default')
            break
        
        
    def search_ids_in_folder():
        import random #### FOR TESTING
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
        def randintdezena(): return random.randint(-99, 99)
        def randintcentena(): return random.randint(-999, 999)
        def randintmilhar(): return random.randint(-99999, 99999)
        def randfloatdezena(): return round(random.uniform(-99, 99), 2)
        def randfloatcentena(): return round(random.uniform(-999, 999), 2)
        def randfloatmilhar(): return round(random.uniform(-99999, 99999), 2)
        count = 0
        path = '/home/runner/Vehicle-Mod-Editor'
        with os.scandir(path + '/tests') as itr:
            for file in itr:
                if file.name.endswith('.cfg') and file.is_file():
                    os.remove(path + '/tests/' + file.name)
        while count < 10:
            randname = random.choice(veh[1:-1].split(','))
            f = open(path + '/tests/' + randname + '.cfg', 'w')
            line = '{}, {}, {}, {}, {},\t{},\t{}, {}, {}, {},\t{},\t{},\t{},\t{},   {}, {}, {},    {},  {}, {}, {}, {},   {}, {}, {}, {},  {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(randname, randfloatmilhar(), randfloatmilhar(), randfloatdezena(), randfloatdezena(), randfloatdezena(), randfloatdezena(), randintdezena(), randfloatdezena(), randfloatdezena(), randfloatdezena(), randintdezena(), randfloatcentena(), randfloatdezena(), randfloatdezena(), 'R', 'P', randfloatdezena(), randfloatdezena(), '0', randfloatdezena(), randfloatdezena(), randfloatdezena(), randfloatdezena(), randfloatdezena(), randfloatdezena(), randfloatdezena(), randfloatdezena(), randfloatdezena(), randfloatdezena(), randfloatdezena(), randintmilhar(), randintmilhar(), '1', '1', '1') # name, number (14), letter (2), number (19)
            # ((\w+)
            # MALLARD 1700.0 4166.4 2.5 0.0 0.15 0.0 70 0.60 0.85 0.52 4 160.0 24.0 10.0 R P 8.17 0.52 0 35.0 0.7 0.08 3.0 0.30 -0.16 0.5 0.50 0.3 0.52 19000 40000004 4 1 1 1 #nome + 35
            f.write(line)
            f.close
            count += 1
        count = 0

        with os.scandir(path + '/tests') as itr:
            for file in itr:
                if file.name.endswith('.txt') and file.is_file():
                    os.remove(path + '/tests/' + file.name)
        while count < 10:
            randnumb = random.randint(200, 500)
            randname = random.choice(veh[1:-1].split(','))
            f = open('/home/runner/Vehicle-Mod-Editor/tests/' + randname + '.txt', 'w')
            line = '{},\t{}, {},   {}, {},\t{}, {}, {},\t{},\t{}, {},  {},\t{}, {}'.format(randnumb, randname, randname,  'vehicle', randname.upper(), randname.upper(), 'null', 'unused', randfloatcentena(), randfloatmilhar(), randintcentena(), randintdezena(), randfloatdezena(), randfloatdezena(), '0')
            # 549, mallard, mallard, car, MALLARD, MALLARD, null, poorfamily, 10, 0, 0, -1, 0.684, 0.684, 0
            f.write(line)
            f.close()
            count += 1
        path = '/home/runner/Vehicle-Mod-Editor/tests' #### FOR TESTING

        #path = dictlist['idlistpath'].get()
        with os.scandir(path) as itr:
            for file in itr:
                if file.name.endswith('.txt') and file.is_file():
                    with open(path + '/' + file.name, 'r') as read:
                        for line in read:
                            tmp = re.search(r'(\d+),\s+(\w+),\s+\w+,\s+\w+,\s+\w+,\s+\w+,\s+\w+,\s+\w+,\s+-?\d+\.?\d*,\s+-?\d+\.?\d*,\s+-?\d+\.?\d*,\s+-?\d+\.?\d*,\s+-?\d+\.?\d*,\s+-?\d+\.?\d*,\s+-?\d+\.?\d*\s*', line) # integer (id), word (7), number (7)
                            # 549, mallard, mallard, car, MALLARD, MALLARD, null, poorfamily, 10, 0, 0, -1, 0.684, 0.684, 0
                            if tmp:
                                idlistitems[tmp.group(1)] = [tmp.group(2), translation('vehicles', 'idlisttab', 'originnonsaved')]
                                sort_listbox_by('default')


    def save_to_file(*args):
        currentdir = os.getcwd()

        if not os.path.isdir(currentdir + '/data'):
            os.mkdir(currentdir + '/data')

        tmpdict = {}
        for k, v in idlistitems.items():
            if not args:
                idlistitems[k][1] = translation('vehicles', 'idlisttab', 'originsaved')
            if idlistitems[k][1] == translation('vehicles', 'idlisttab', 'originsaved'):
                tmpdict[k] = v

        with open(currentdir + '/data/vehicles_ids.pkl', 'wb+') as file:
            pickle.dump(tmpdict, file)
        '''if not args:
            with open(currentdir + '/data/vehicles_ids.pkl', 'wb+') as file:
                pickle.dump(idlistitems, file)
                for k, v in idlistitems.items():
                    idlistitems[k][1] = translation('vehicles', 'idlisttab', 'originsaved')
        else:
            with open(currentdir + '/data/vehicles_ids.pkl', 'ab+') as file:
                for k, v in args.items():
                    tmpdict = {}
                    tmpdict[k] = [v, translation('vehicles', 'idlisttab', 'originsaved')]
                    print(tmpdict)
                    idlistitems[k] = [v, translation('vehicles', 'idlisttab', 'originsaved')]
                    pickle.dump(tmpdict, file)'''

        sort_listbox_by('default')


    def remove_selection_from_listbox():
        selection = idlistbox.curselection()
        listselection = list(selection)
        for i in reversed(selection):
            value = idlistbox.get(listselection[-1])
            tmp = re.search(r'\s+(\d+)\s+\w+\s+\w+', value)
            if tmp:
                key = tmp.group(1)
                #if idlistitems[key][1] == translation('vehicles', 'idlisttab', 'originsaved'):
                #    idlistitems[key][1] == translation('vehicles', 'idlisttab', 'originnonsaved')
                idlistbox.delete(i)
                del idlistitems[key]
                del listselection[-1]
        save_to_file(True)


    def add_item_into_listbox(newitemid, newitemname, win, label):
        id = newitemid.get()
        name = newitemname.get().lower()
        if not id or not name: label.config(text=translation('vehicles', 'idlisttab', 'additemempty'), fg='red'); return
        if not id.isdecimal(): label.config(text=translation('vehicles', 'idlisttab', 'additemonlynumbers'), fg='red'); return
        if len(id) > 8 or len(name) > 8: label.config(text=translation('vehicles', 'idlisttab', 'additemlength'), fg='red'); return
        for k, v in idlistitems.items():
            if k == id: label.config(text=translation('vehicles', 'idlisttab', 'additemidexists'), fg='red'); return
            if v[0] == name: label.config(text=translation('vehicles', 'idlisttab', 'additemnameexists'), fg='red'); return

        idlistitems[id] = [name, translation('vehicles', 'idlisttab', 'originsaved')]
        save_to_file(True)
        win.destroy()
        

    def cancel_window(win):
        win.destroy()

    def add_item_window():
        win = tk.Toplevel()
        win.title('Add')
        win.geometry('500x200')
        win.attributes('-topmost', True)

        newitemlabel = Label(win, text=translation('vehicles', 'idlisttab', 'newlistitem'))
        newitemlabel.grid(padx=5, pady=5, column=1, row=0, columnspan=2)

        newitemid = Entry(win, width=50, borderwidth=5)
        newitemid.insert(0, 'ID')
        newitemid.grid(padx=5, pady=5, column=1, row=1, columnspan=2)

        newitemname = Entry(win, width=50, borderwidth=5)
        newitemname.insert(0, translation('vehicles', 'idlisttab', 'newlistitemvehicle'))
        newitemname.grid(padx=5, pady=5, column=1, row=2, columnspan=2)

        okbutton = Button(win, text='Ok', command=lambda: add_item_into_listbox(newitemid, newitemname, win, newitemlabel), width=5)
        okbutton.grid(padx=5, pady=5, column=1, row=3, sticky=EW)

        cancelbutton = Button(win, text=translation('others', 'messages', 'cancel'), command=lambda: cancel_window(win), width=5)
        cancelbutton.grid(padx=5, pady=5, column=2, row=3, sticky=EW)

        win.grid_columnconfigure((0, 4), weight=1)
        


    def select_all_items_in_listbox():
        selection = idlistbox.curselection()
        if selection: idlistbox.selection_clear(0, END)
        else: idlistbox.select_set(0, END)


    #savebutton = PhotoImage(data=b64)

    savebutton = PhotoImage(file=os.getcwd() + '/savebutton.png')
    selectall = PhotoImage(file=os.getcwd() + '/selectall.png')
    remove = PhotoImage(file=os.getcwd() + '/remove.png')
    add = PhotoImage(file=os.getcwd() + '/add.png')

    #sortbuttons['vehicleid'] = CreateButton(sortbuttons['vehicleid'], 'idlist', 'ID', lambda: sort_listbox_by('id', 'vehicleid'), 23, 1, 2, W, 1, 0, 0, 0)
    sortbuttons['vehicleid'] = Button(tab['idlist'], text=translation('vehicles', 'idlisttab', 'vehicleid'), command=lambda: sort_listbox_by('id', 'vehicleid'), borderwidth=0, width=23)
    sortbuttons['vehicleid'].grid(column=1, row=2, sticky=W)

    sortbuttons['vehiclename'] = Button(tab['idlist'], text=translation('vehicles', 'idlisttab', 'vehiclename'), command=lambda: sort_listbox_by('name', 'vehiclename'), borderwidth=0, width=23)
    sortbuttons['vehiclename'].grid(column=2, row=2, sticky=EW)
    #sortbuttons['vehiclename'] = CreateButton('vehiclename', 'idlist', 'vehiclename', lambda: sort_listbox_by('name'), 23, 2, 2, EW,  1, 0, 0, 0)

    sortbuttons['vehicleorigin'] = Button(tab['idlist'], text=translation('vehicles', 'idlisttab', 'vehicleorigin'), command=lambda: sort_listbox_by('file', 'vehicleorigin'), borderwidth=0, width=23)
    sortbuttons['vehicleorigin'].grid(column=3, row=2, sticky=EW)
    #sortbuttons['vehicleorigin'] = CreateButton('vehicleorigin', 'idlist', 'vehicleorigin', lambda: sort_listbox_by('file'), 23, 3, 2, EW, 1, 0, 0, 0)
    
    idlistsearch = Button(tab['idlist'], text='>', width=1, command=search_ids_in_folder)
    idlistsearch.grid(padx=0, pady=1, column=5, row=1, sticky=E)

    idlistsave = Button(tab['idlist'], text=' ', width=5, height=1, command=save_to_file, image=savebutton, compound=CENTER)
    idlistsave.grid(padx=0, pady=0, column=0, row=3, sticky='NSW')
    idlistsave.image = savebutton

    idselectall = Button(tab['idlist'], text=' ', width=5, height=1, command=select_all_items_in_listbox, image=selectall, compound=CENTER)
    idselectall.grid(padx=0, pady=0, column=0, row=4, sticky='NSW')
    idselectall.image = selectall

    idlistremove = Button(tab['idlist'], text=' ', width=5, height=1, command=remove_selection_from_listbox, image=remove, compound=CENTER)
    idlistremove.grid(padx=0, pady=0, column=0, row=5, sticky='NSW')
    idlistremove.image = remove

    idlistadd = Button(tab['idlist'], text=' ', width=5, height=1, command=add_item_window, image=add, compound=CENTER)
    idlistadd.grid(padx=0, pady=0, column=0, row=6, sticky='NSW')
    idlistadd.image = add

    #idlistsearch = CreateButton('idlistsearch', 'idlist', '>', search_ids_in_folder, 1,  5, 1, E, 0, 0, 1, )
    #idlistsave = CreateButton('idlistsave', 'idlist', ' ', save_to_file, 5, 0, 3, 'NSW', 1, 0, 0, 2, 1, savebutton, compound=CENTER)
    #idlistselectall = CreateButton('idlistselectall', 'idlist', ' ', select_all_items_in_listbox, 5, 0, 4, 'NSW', 1, 0, 0, 2, 1, selectall, compound=CENTER)
    #idlistremove = CreateButton('idlistremove', 'idlist', ' ', remove_selection_from_listbox, 5, 0, 5, 'NSW', 1, 0, 0, 2, 1, remove, compound=CENTER)
    #idlistadd = CreateButton('idlistadd', 'idlist', ' ', add_item_window, 5, 0, 6, 'NSW', 1, 0, 0, 2, 1, add, compound=CENTER)

    sort_listbox_by('id', 'vehicleid')
    #tab_parent.grid_columnconfigure((0,1, 2, 3, 4), weight=1)
    #root.grid_columnconfigure((0,1, 2, 3, 4), weight=1)
    #tab['idlist'].grid_columnconfigure((0, 7), weight=1)
    #tab['idlist'].grid_rowconfigure((3, 4), weight=1,   uniform='row')
    return