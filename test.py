from tkinter import ttk
from tkinter import *
from variables import *
from languages import *


def savc():
    if savcvar.get() == True:
        inipath.delete(0, &#39;end&#39;)
        inipath.insert(0, texts[&#39;inipath2&#39;])
        inipath.config(fg=&#39;grey&#39;)
        cfgpath.delete(0, &#39;end&#39;)
        cfgpath.insert(0, texts[&#39;cfgpath2&#39;])
        cfgpath.config(fg=&#39;grey&#39;)
    else:
        inipath.delete(0, &#39;end&#39;)
        inipath.insert(0, texts[&#39;inipath1&#39;])
        inipath.config(fg=&#39;grey&#39;)
        cfgpath.delete(0, &#39;end&#39;)
        cfgpath.insert(0, texts[&#39;cfgpath1&#39;])
        cfgpath.config(fg=&#39;grey&#39;)


def onclick(event):
    if len(inipath.get()) == 0:
        if savcvar.get() == True:
            inipath.insert(0, texts[&#39;inipath2&#39;])
        else:
            inipath.insert(0, texts[&#39;inipath1&#39;])
        inipath.config(fg=&#39;grey&#39;)
    if len(path.get()) == 0:
        path.insert(0, texts[&#39;path1&#39;])
        path.config(fg=&#39;grey&#39;)
    if len(modname.get()) == 0:
        modname.insert(0, texts[&#39;modname1&#39;])
        modname.config(fg=&#39;grey&#39;)
    if len(newname.get()) == 0:
        newname.insert(0, texts[&#39;newname1&#39;])
        newname.config(fg=&#39;grey&#39;)
    if len(vehname.get()) == 0:
        vehname.insert(0, texts[&#39;vehname1&#39;])
        vehname.config(fg=&#39;grey&#39;)
    if len(newid.get()) == 0:
        newid.insert(0, texts[&#39;newid1&#39;])
        newid.config(fg=&#39;grey&#39;)
    if len(cfgpath.get()) == 0:
        if savcvar.get() == True:
            cfgpath.insert(0, texts[&#39;cfgpath2&#39;])
        else:
            cfgpath.insert(0, texts[&#39;cfgpath1&#39;])
        cfgpath.config(fg=&#39;grey&#39;)
    if len(newveh.get()) == 0:
        newveh.insert(0, texts[&#39;newveh1&#39;])
        newveh.config(fg=&#39;grey&#39;)
    if len(vehaudio.get()) == 0:
        vehaudio.insert(0, texts[&#39;vehaudio1&#39;])
        vehaudio.config(fg=&#39;grey&#39;)
    if len(poppath.get()) == 0:
        poppath.insert(0, texts[&#39;poppath1&#39;])
        poppath.config(fg=&#39;grey&#39;)
    if len(popveh.get()) == 0:
        popveh.insert(0, texts[&#39;popveh1&#39;])
        popveh.config(fg=&#39;grey&#39;)
    if len(handcfg.get()) == 0:
        handcfg.insert(0, texts[&#39;handcfg1&#39;])
        handcfg.config(fg=&#39;grey&#39;)
    if len(audio.get()) == 0:
        audio.insert(0, texts[&#39;audio1&#39;])
        audio.config(fg=&#39;grey&#39;)
    if len(handlines.get()) == 0:
        handlines.insert(0, texts[&#39;handlines1&#39;])
        handlines.config(fg=&#39;grey&#39;)
    if len(vehmodels.get()) == 0:
        vehmodels.insert(0, texts[&#39;vehmodels1&#39;])
        vehmodels.config(fg=&#39;grey&#39;)
    if len(killable.get()) == 0:
        killable.insert(0, texts[&#39;killable1&#39;])
        killable.config(fg=&#39;grey&#39;)
    if len(bike.get()) == 0:
        bike.insert(0, texts[&#39;bike1&#39;])
        bike.config(fg=&#39;grey&#39;)
    if len(plane.get()) == 0:
        plane.insert(0, texts[&#39;plane1&#39;])
        plane.config(fg=&#39;grey&#39;)
    if len(boat.get()) == 0:
        boat.insert(0, texts[&#39;boat1&#39;])
        boat.config(fg=&#39;grey&#39;)
    for x in texts:
        if event.widget.get() in texts[x]:
            event.widget.delete(0, &#39;end&#39;)
            event.widget.config(fg=&#39;black&#39;)
    return


def onhover(event):
    time.sleep(0.1)
    tab1label.configure(text=texts[&#39;vehmodelswarn&#39;])
    root.geometry(&#39;630x400&#39;)


def onleave(event):
    tab1label.configure(text=&#39;&#39;)
    root.geometry(&#39;630x375&#39;)


def vehpage():
    tab_parent = ttk.Notebook(root)
    tab1 = ttk.Frame(tab_parent)
    tab2 = ttk.Frame(tab_parent)
    tab3 = ttk.Frame(tab_parent)
    tab4 = ttk.Frame(tab_parent)
    tab5 = ttk.Frame(tab_parent)
    #tab_parent.bind(&#39;&lt;&lt;NotebookTabChanged&gt;&gt;&#39;, on_tab_selected)
    tab_parent.add(tab1, text=texts[&#39;configini1&#39;])
    tab_parent.add(tab2, text=texts[&#39;vehlines1&#39;])
    tab_parent.add(tab3, text=texts[&#39;vehsound2&#39;])
    tab_parent.add(tab4, text=texts[&#39;npcs1&#39;])
    tab_parent.add(tab5, text=texts[&#39;help1&#39;])
    tab_parent.grid(padx=5, pady=5, column=0, row=0)

    print(&#39;created&#39;)
    savcvar = BooleanVar()
    savcbox = Checkbutton(tab1, text=&#39;VC&#39;, command=savc, variable=savcvar)
    savcbox.grid(padx=5, pady=5, column=0, row=1, sticky=W)
    savcbox.deselect()

    savcbox2 = Checkbutton(tab3, text=&#39;VC&#39;, command=savc, variable=savcvar)
    savcbox2.grid(padx=5, pady=5, column=0, row=0, sticky=W)
    savcbox2.deselect()

    tab1label = Label(tab1, text=&#39;&#39;, justify=&#39;left&#39;, anchor=W)
    tab1label.grid(padx=0, pady=0, column=0, row=18, sticky=W)

    # ======================== TAB 1 ========================

    inipath = Entry(tab1, width=80, borderwidth=2)
    inipath.insert(0, texts[&#39;inipath1&#39;])
    inipath.config(fg=&#39;grey&#39;)
    inipath.grid(padx=50, pady=5, column=0, row=1)
    inipath.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)

    # HANDLINE.CFG
    handcfg = Entry(tab1, width=80, borderwidth=2)
    handcfg.insert(0, &#39;Apply \&#39;handling.cfg\&#39; patch (0|1)&#39;)
    handcfg.config(fg=&#39;grey&#39;)
    handcfg.grid(padx=5, pady=5, column=0, row=2)
    handcfg.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)

    handcfgvar = BooleanVar()
    handcfgbox = Checkbutton(tab1, variable=handcfgvar)
    handcfgbox.grid(column=2, row=2)
    handcfgbox.select()

    # AUDIO
    audio = Entry(tab1, width=80, borderwidth=2)
    audio.insert(0, &#39;Enable vehicle audio loader (0|1)&#39;)
    audio.config(fg=&#39;grey&#39;)
    audio.grid(padx=5, pady=5, column=0, row=3)
    audio.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)

    audiovar = BooleanVar()
    audiobox = Checkbutton(tab1, variable=audiovar)
    audiobox.grid(column=2, row=3)
    audiobox.select()

    # LINES
    handlines = Entry(tab1, width=80, borderwidth=2)
    handlines.insert(0, &#39;Number of standard lines&#39;)
    handlines.config(fg=&#39;grey&#39;)
    handlines.grid(padx=5, pady=5, column=0, row=4)
    handlines.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)

    handlinesvar = BooleanVar()
    handlinesbox = Checkbutton(tab1, variable=handlinesvar)
    handlinesbox.grid(column=2, row=4)
    handlinesbox.select()

    # VEH MODELS
    vehmodels = Entry(tab1, width=80, borderwidth=2)
    vehmodels.insert(0, &#39;Vehicle Models&#39;)
    vehmodels.config(fg=&#39;grey&#39;)
    vehmodels.grid(padx=5, pady=5, column=0, row=5)
    vehmodels.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)
    vehmodels.bind(&#39;&lt;Enter&gt;&#39;, onhover)
    vehmodels.bind(&#39;&lt;Leave&gt;&#39;, onleave)

    vehmodelsvar = BooleanVar()
    vehmodelsbox = Checkbutton(tab1, variable=vehmodelsvar)
    vehmodelsbox.grid(column=2, row=5)
    vehmodelsbox.select()

    # KILLABLE
    killable = Entry(tab1, width=80, borderwidth=2)
    killable.insert(0, &#39;Count of killable model IDs&#39;)
    killable.config(fg=&#39;grey&#39;)
    killable.grid(padx=5, pady=5, column=0, row=6)
    killable.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)

    killablevar = BooleanVar()
    killablebox = Checkbutton(tab1, variable=killablevar)
    killablebox.grid(column=2, row=6)
    killablebox.select()

    # BIKE
    bike = Entry(tab1, width=80, borderwidth=2)
    bike.insert(0, &#39;Number of bike lines&#39;)
    bike.config(fg=&#39;grey&#39;)
    bike.grid(padx=5, pady=5, column=0, row=7)
    bike.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)

    bikevar = BooleanVar()
    bikebox = Checkbutton(tab1, variable=bikevar)
    bikebox.grid(column=2, row=7)
    bikebox.select()

    # PLANE
    plane = Entry(tab1, width=80, borderwidth=2)
    plane.insert(0, &#39;Number of flying lines&#39;)
    plane.config(fg=&#39;grey&#39;)
    plane.grid(padx=5, pady=5, column=0, row=8)
    plane.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)

    planevar = BooleanVar()
    planebox = Checkbutton(tab1, variable=planevar)
    planebox.grid(column=2, row=8)
    planebox.select()

    # BOAT
    boat = Entry(tab1, width=80, borderwidth=2)
    boat.insert(0, &#39;Number of boat lines&#39;)
    boat.config(fg=&#39;grey&#39;)
    boat.grid(padx=5, pady=5, column=0, row=9)
    boat.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)

    boatvar = BooleanVar()
    boatbox = Checkbutton(tab1, variable=boatvar)
    boatbox.grid(column=2, row=9)
    boatbox.select()

    # ======================== TAB 2 ========================

    path = Entry(tab2, width=80, borderwidth=2)
    path.insert(0, texts[&#39;path1&#39;])
    path.config(fg=&#39;grey&#39;)
    path.grid(padx=50, pady=5, column=0, row=3)
    path.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)

    modname = Entry(tab2, width=80, borderwidth=2)
    modname.insert(0, texts[&#39;modname1&#39;])
    modname.config(fg=&#39;grey&#39;)
    modname.grid(padx=5, pady=5, column=0, row=4)
    modname.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)

    newname = Entry(tab2, width=80, borderwidth=2)
    newname.insert(0, texts[&#39;newname1&#39;])
    newname.config(fg=&#39;grey&#39;)
    newname.grid(padx=5, pady=5, column=0, row=5)
    newname.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)

    vehname = Entry(tab2, width=80, borderwidth=2)
    vehname.insert(0, texts[&#39;vehname1&#39;])
    vehname.config(fg=&#39;grey&#39;)
    vehname.grid(padx=5, pady=5, column=0, row=6)
    vehname.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)

    newid = Entry(tab2, width=80, borderwidth=2)
    newid.insert(0, texts[&#39;newid1&#39;])
    newid.config(fg=&#39;grey&#39;)
    newid.grid(padx=5, pady=5, column=0, row=7)
    newid.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)

    newidvar = BooleanVar()
    newidbox = Checkbutton(tab2, variable=newidvar)
    newidbox.grid(column=1, row=7)
    newidbox.select()

    label = Label(tab3, text=texts[&#39;tip&#39;])
    label.grid(column=0, row=8)

    list = [texts[&#39;default1&#39;], &#39;normal&#39;, &#39;poorfamily&#39;, &#39;richfamily&#39;, &#39;executive&#39;, &#39;worker&#39;, &#39;big&#39;, &#39;taxi&#39;, &#39;moped&#39;, &#39;motorbike&#39;, &#39;leisureboat&#39;, &#39;workerboat&#39;, &#39;bicycle&#39;, &#39;ignore&#39;]

    item = StringVar()
    item.set(texts[&#39;class1&#39;])

    dropmenu = OptionMenu(tab2, item, *list)
    dropmenu.config(width=15)
    dropmenu.grid(padx=5, pady=5, column=0, row=10)

    #fixname = &#39;[]&#39;

    # ======================== TAB 3 ========================


    veh = &#39;[landstal,bravura,buffalo,linerun,peren,sentinel,dumper,firetruk,trash,stretch,manana,infernus,voodoo,pony,mule,cheetah,ambulan,leviathn,moonbeam,esperant,taxi,washing,bobcat,mrwhoop,bfinject,&#39; \
            &#39;hunter,premier,enforcer,securica,banshee,predator,bus,rhino,barracks,hotknife,artict1,previon,coach,cabbie,stallion,rumpo,rcbandit,romero,packer,monster,&#39; \
            &#39;admiral,squalo,seaspar,pizzaboy,tram,artict2,turismo,speeder,reefer,tropic,flatbed,yankee,caddy,solair,topfun,skimmer,pcj600,faggio,freeway,rcbaron,rcraider,&#39; \
            &#39;glendale,oceanic,sanchez,sparrow,patriot,quad,coastg,dinghy,hermes,sabre,rustler,zr350,walton,regina,comet,bmx,burrito,camper,marquis,baggage,dozer,maverick,&#39; \
            &#39;vcnmav,rancher,fbiranch,virgo,greenwoo,jetmax,hotring,sandking,blistac,polmav,boxville,benson,mesa,rcgoblin,hotrina,hotrinb,bloodra,rnchlure,supergt,elegant,&#39; \
            &#39;journey,bike,mtbike,beagle,cropdust,stunt,petro,rdtrain,nebula,majestic,buccanee,shamal,hydra,fcr900,nrg500,copbike,cement,towtruck,fortune,cadrona,fbitruck,&#39; \
            &#39;willard,forklift,tractor,combine,feltzer,remingtn,slamvan,blade,freight,streak,vortex,vincent,bullet,clover,sadler,firela,hustler,intruder,primo,cargobob,&#39; \
            &#39;tampa,sunrise,merit,utility,nevada,yosemite,windsor,monstera,monsterb,uranus,jester,sultan,stratum,elegy,raindanc,rctiger,flash,tahoma,savanna,bandito,freiflat,&#39; \
            &#39;streakc,kart,mower,duneride,sweeper,broadway,tornado,at400,dft30,huntley,stafford,bf400,newsvan,tug,petrotr,emperor,wayfarer,euros,hotdog,club,freibox,artict3,&#39; \
            &#39;androm,dodo,rccam,launch,copcarla,copcarsf,copcarvg,copcarru,picador,swatvan,alpha,phoenix,glenshit,sadlshit,bagboxa,bagboxb,tugstair,boxburg,farmtr1,utiltr1]&#39;

    vehlist = sorted(veh[1:-1].split(&#39;,&#39;))
    vehlist.insert(0, texts[&#39;disable1&#39;])

    vehitem = StringVar()
    vehitem.set(texts[&#39;vehsound1&#39;])

    vehmenu = OptionMenu(tab3, vehitem, *vehlist)
    vehmenu.config(width=15)
    vehmenu.grid(padx=5, pady=5, column=0, row=9)

    cfgpath = Entry(tab3, width=80, borderwidth=2)
    cfgpath.insert(0, texts[&#39;cfgpath1&#39;])
    cfgpath.config(fg=&#39;grey&#39;)
    cfgpath.grid(padx=50, pady=5, column=0, row=0)
    cfgpath.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)

    newveh = Entry(tab3, width=80, borderwidth=2)
    newveh.insert(0, texts[&#39;newveh1&#39;])
    newveh.config(fg=&#39;grey&#39;)
    newveh.grid(padx=5, pady=5, column=0, row=1)
    newveh.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)

    vehaudio = Entry(tab3, width=80, borderwidth=2)
    vehaudio.insert(0, texts[&#39;vehaudio1&#39;])
    vehaudio.config(fg=&#39;grey&#39;)
    vehaudio.grid(padx=5, pady=5, column=0, row=2)
    vehaudio.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)

    # ======================== TAB 4 ========================

    poppath = Entry(tab4, width=80, borderwidth=2)
    poppath.insert(0, texts[&#39;poppath1&#39;])
    poppath.config(fg=&#39;grey&#39;)
    poppath.grid(padx=50, pady=5, column=0, row=0)
    poppath.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)

    popveh = Entry(tab4, width=80, borderwidth=2)
    popveh.insert(0, texts[&#39;popveh1&#39;])
    popveh.config(fg=&#39;grey&#39;)
    popveh.grid(padx=5, pady=5, column=0, row=1)
    popveh.bind(&#39;&lt;FocusIn&gt;&#39;, onclick)

    poplist = [&#39;POPCYCLE_GROUP_WORKERS&#39;, &#39;POPCYCLE_GROUP_BUSINESS&#39;, &#39;POPCYCLE_GROUP_CLUBBERS&#39;, &#39;POPCYCLE_GROUP_FARMERS&#39;, &#39;POPCYCLE_GROUP_BEACHFOLK&#39;, &#39;POPCYCLE_GROUP_PARKFOLK&#39;,
            &#39;POPCYCLE_GROUP_CASUAL_RICH&#39;, &#39;POPCYCLE_GROUP_CASUAL_AVERAGE&#39;, &#39;POPCYCLE_GROUP_CASUAL_POOR&#39;, &#39;POPCYCLE_GROUP_PROSTITUTES&#39;, &#39;POPCYCLE_GROUP_CRIMINALS&#39;,
            &#39;POPCYCLE_GROUP_GOLFERS&#39;, &#39;POPCYCLE_GROUP_SERVANTS&#39;, &#39;POPCYCLE_GROUP_AIRCREW&#39;, &#39;POPCYCLE_GROUP_ENTERTAINERS&#39;, &#39;POPCYCLE_GROUP_OUT_OF_TOWN_FACTORY&#39;,
            &#39;POPCYCLE_GROUP_DESERT_FOLK&#39;, &#39;POPCYCLE_GROUP_AIRCREW_RUNWAY&#39;, &#39;Boats&#39;]

    popitem = StringVar()
    popitem.set(texts[&#39;popitem1&#39;])

    popmenu = OptionMenu(tab4, popitem, *poplist)
    popmenu.config(width=40)
    popmenu.grid(padx=5, pady=5, column=0, row=2)