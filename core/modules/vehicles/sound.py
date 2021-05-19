from tkinter import *
from resources import *

def sound():
    savcbox2 = Checkbutton(tab['sound'], text='VC', command=savc_checkbox, variable=savcbool)
    savcbox2.grid(padx=5, pady=5, column=0, row=0, sticky=W)
    savcbox2.deselect()
    
    def configaudio():
        cfgpath2 = dictlist['audiocfgpath'].get()
        vaudio = dictlist['vehaudio'].get()
        vitem = vehitem.get()
        newveh = dictlist['newvehname'].get()
        removecheck = removebool.get()
        linecounter = 0
        cfglines = []
        cfglines2 = []
        addlines = False
        donemsg = False

        if len(vaudio) > 0 and not vaudio == translation('vehicles', 'soundtab', 'vehicletogetsound'):
            if vitem == translation('vehicles', 'soundtab', 'vehiclesound') or vitem == translation('others', 'messages', 'none').upper():
                if not any(ext in vaudio for ext in vehlist) and not removecheck:
                    messagebox.showerror('ERROR', 'Could not find "' + vaudio + '"\nNão foi possível encontrar "'  + vaudio + '"')
                    return
        else:
            if not vitem == translation('vehicles', 'soundtab', 'vehiclesound') and not vitem == translation('others', 'messages', 'none').upper():
                messagebox.showerror('ERROR', 'Cannot be empty')
                return
        cfgfile = try_and_open_file(cfgpath2, 'gta{}_vehicleAudioSettings.cfg', True)

        while True:
            line = try_and_read_file_line(cfgfile, cfgpath2, 'gta{}_vehicleAudioSettings.cfg')
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
                if not vitem == translation('vehicles', 'soundtab', 'vehiclesound') and not vitem == translation('others', 'messages', 'none').upper():
                    if vitem in line:
                        savedline = line
                        savedline = savedline.replace(vitem, newveh)
                        donemsg = True
                if len(vaudio) > 0:
                    if any(ext in vaudio for ext in vehlist):
                        if vaudio in line:
                            savedline = line
                            savedline = savedline.replace(vaudio, newveh)
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
                if not newveh in line:
                    cfglines.append(line)
                else:
                    donemsg = True
        cfgfile.close()
        if donemsg == True:
            messagebox.showinfo('Info', translation('others', 'messages', 'applied'))
        else:
            messagebox.showerror('ERROR', translation('others', 'messages', 'notapplied'))

 
    def configaudiopath():
        filename = filedialog.askdirectory()
        dictlist['cfgpath'].delete(0, 'end')
        dictlist['cfgpath'].insert(0, filename)
        dictlist['cfgpath'].config(fg='black')


    configaudio = Button(tab['sound'], text=translation('others', 'messages', 'apply'), command=configaudio, width=20)
    configaudio.grid(padx=5, pady=5, column=0, row=20)

    configaudiopath = Button(tab['sound'], text='...', command=configaudiopath, width=4)
    configaudiopath.grid(padx=5, pady=5, column=0, row=0, sticky=E)

    removebool = BooleanVar()
    remove = Checkbutton(tab['sound'], text=translation('others', 'messages', 'remove'), variable=removebool)
    remove.grid(padx=5, pady=5, column=0, row=20, sticky=W)

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
    vehlist.insert(0, translation('others', 'messages', 'none').upper())

    labelsoundhint = Label(tab['sound'], text=translation('vehicles', 'soundtab', 'menuhint'))
    labelsoundhint.grid(column=0, row=8)

    def vehicle_sound_hint(*args):
        labelsoundhint.configure(text='')  # When item in class list changes

    vehitem = StringVar()
    vehitem.set(translation('vehicles', 'soundtab', 'vehiclesound'))
    vehitem.trace('w', vehicle_sound_hint)

    vehmenu = OptionMenu(tab['sound'], vehitem, *vehlist)
    vehmenu.config(width=15)
    vehmenu.grid(padx=5, pady=5, column=0, row=9)

    dictlist['audiocfgpath'] = Entry(tab['sound'], width=80, borderwidth=2)
    dictlist['audiocfgpath'].insert(0, translation('vehicles', 'soundtab', 'pathtoaudiocfg'))
    dictlist['audiocfgpath'].config(fg='grey')
    dictlist['audiocfgpath'].grid(padx=50, pady=5, column=0, row=0)
    dictlist['audiocfgpath'].bind('<FocusIn>', onclick)

    dictlist['newvehname'] = Entry(tab['sound'], width=80, borderwidth=2)
    dictlist['newvehname'].insert(0, translation('vehicles', 'soundtab', 'newvehiclename'))
    dictlist['newvehname'].config(fg='grey')
    dictlist['newvehname'].grid(padx=5, pady=5, column=0, row=1)
    dictlist['newvehname'].bind('<FocusIn>', onclick)

    dictlist['vehaudio'] = Entry(tab['sound'], width=80, borderwidth=2)
    dictlist['vehaudio'].insert(0, translation('vehicles', 'soundtab', 'vehicletogetsound'))
    dictlist['vehaudio'].config(fg='grey')
    dictlist['vehaudio'].grid(padx=5, pady=5, column=0, row=2)
    dictlist['vehaudio'].bind('<FocusIn>', onclick)