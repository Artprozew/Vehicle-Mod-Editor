from tkinter import *
from resources import *

def vehnpcs():
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
            messagebox.showinfo('Info', translation('others', 'messages', 'applied'))
        else:
            messagebox.showerror('ERROR', translation('others', 'messages', 'notapplied'))



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
        # tab 4
    def popconfigpath():
        filename = filedialog.askdirectory()
        poppath.delete(0, 'end')
        poppath.insert(0, filename)
        poppath.config(fg='black')


    configcargrp = Button(tab['vehnpcs'], text=translation('others', 'messages', 'apply'), command=configcargrp,width=20)
    configcargrp.grid(padx=5, pady=5, column=0, row=20)

    popcfgpath = Button(tab['vehnpcs'], text='...', command=popconfigpath, width=4)
    popcfgpath.grid(padx=5, pady=5, column=0, row=0, sticky=E)

    pophelp = Button(tab['vehnpcs'], text='?', command=pophelp, width=2)
    pophelp.grid(padx=5, pady=5, column=0, row=2, sticky=E)

    removevar2 = BooleanVar()
    remove2 = Checkbutton(tab['vehnpcs'], text=translation('others', 'messages', 'remove'), variable=removevar2)
    remove2.grid(padx=5, pady=5, column=0, row=20, sticky=W)


    dictlist['popcyclepath'] = Entry(tab['vehnpcs'], width=80, borderwidth=2)
    dictlist['popcyclepath'].insert(0, translation('vehicles', 'vehnpcstab', 'pathtocargrp'))
    dictlist['popcyclepath'].config(fg='grey')
    dictlist['popcyclepath'].grid(padx=50, pady=5, column=0, row=0)
    dictlist['popcyclepath'].bind('<FocusIn>', onclick)

    dictlist['popcycleveh'] = Entry(tab['vehnpcs'], width=80, borderwidth=2)
    dictlist['popcycleveh'].insert(0, translation('vehicles', 'vehnpcstab', 'vehicletoinsert'))
    dictlist['popcycleveh'].config(fg='grey')
    dictlist['popcycleveh'].grid(padx=5, pady=5, column=0, row=1)
    dictlist['popcycleveh'].bind('<FocusIn>', onclick)

    poplist = ['POPCYCLE_GROUP_WORKERS', 'POPCYCLE_GROUP_BUSINESS', 'POPCYCLE_GROUP_CLUBBERS', 'POPCYCLE_GROUP_FARMERS', 'POPCYCLE_GROUP_BEACHFOLK', 'POPCYCLE_GROUP_PARKFOLK',
            'POPCYCLE_GROUP_CASUAL_RICH', 'POPCYCLE_GROUP_CASUAL_AVERAGE', 'POPCYCLE_GROUP_CASUAL_POOR', 'POPCYCLE_GROUP_PROSTITUTES', 'POPCYCLE_GROUP_CRIMINALS',
            'POPCYCLE_GROUP_GOLFERS', 'POPCYCLE_GROUP_SERVANTS', 'POPCYCLE_GROUP_AIRCREW', 'POPCYCLE_GROUP_ENTERTAINERS', 'POPCYCLE_GROUP_OUT_OF_TOWN_FACTORY',
            'POPCYCLE_GROUP_DESERT_FOLK', 'POPCYCLE_GROUP_AIRCREW_RUNWAY', 'Boats']

    popitem = StringVar()
    popitem.set(translation('vehicles', 'vehnpcstab', 'choosevehiclegroup'))

    popmenu = OptionMenu(tab['vehnpcs'], popitem, *poplist)
    popmenu.config(width=40)
    popmenu.grid(padx=5, pady=5, column=0, row=2)
