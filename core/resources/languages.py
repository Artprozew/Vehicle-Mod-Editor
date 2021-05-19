import tkinter as tk
from tkinter import *
import configparser
import os
import time

cfg = configparser.ConfigParser()

def write_file():
    cfg.write(open('configs.ini', 'w'))

if not os.path.exists('configs.ini'):
    cfg['CONFIG'] = {'language' : 'None'}
    write_file()

cfg.read('configs.ini')

try:
    cfg.get('CONFIG', 'language')
except:
    cfg['CONFIG'] = {'language' : 'None'}
    write_file()

lang = cfg.get('CONFIG', 'language')

def ptbr():
    cfg['CONFIG']['language'] = 'pt_BR'
    write_file()
    win.destroy()
    os.execl(sys.executable, sys.executable, *sys.argv) # Restart the script
    #sys.stdout.flush()
    #file.flush()
    #os.execv(sys.argv[0], sys.argv)
    #os.execv(sys.executable, ['python'] + sys.argv)

def eng():
    cfg['CONFIG']['language'] = 'en_US'
    write_file()
    win.destroy()
    os.execl(sys.executable, sys.executable, *sys.argv)

if lang != 'pt_BR' and lang != 'en_US':
    win = tk.Toplevel()
    win.title('Language')
    win.geometry('275x225')
    win.attributes('-topmost', True)
    Label(win, text='Choose your language\nEscolha sua linguagem').grid(padx=50, pady=5, column=1, row=0)
    Button(win, text='Português', command=ptbr).grid(padx=5, pady=5, column=1, row=1)
    Button(win, text='English', command=eng).grid(padx=5, pady=5, column=1, row=2)

lang = cfg.get('CONFIG', 'language')

if lang == 'pt_BR' or lang == 'pt_PT':
    texts = {
    'home': {
        'pedsbutton': 'Peds',
        'weaponsbutton': 'Armas',
        'vehiclesbutton': 'Veículos',
        'home': 'Início'
    },
    'others': {
        'messages': {
            'apply': 'Aplicar',
            'cancel': 'Cancelar',
            'create': 'Criar',
            'default': 'Padrão',
            'remove': 'Remover',
            'none': 'Nenhum',
            'disable': 'Desativar',
            'warning': 'Aviso',
            'applied': 'Aplicado com sucesso!',
            'notapplied': 'Ocorreu um erro ao tentar concluir o pedido',
        },
    },
    'vehicles': {
        'configinitab': {
            'configini': 'Config .ini',
            'inipath': 'Caminho para o "fastman92limitAdjuster_GTASA.ini"',
            'inipathvc': 'Caminho para o "fastman92limitAdjuster_GTAVC.ini"',
            'handlingpatch': 'Apply handling.cfg patch',
            'audioloader': 'Enable vehicle audio loader',
            'standardlines': 'Number of standard lines',
            'vehiclemodels': 'Vehicle Models',
            'killablemodels': 'Count of killable model IDs',
            'bikelines': 'Number of bike lines',
            'planelines': 'Number of flying lines',
            'boatlines': 'Number of boat lines',
            'vehiclemodelswarn': 'NÃO EDITE ESSA LINHA CASO USE O OPEN LIMIT ADJUSTER\nDESATIVE-A DESMARCANDO NA CAIXA AO LADO\nvá na aba ajuda para saber mais',

        },
        'linestab': {
            'lines': 'Linhas',
            'vehiclepath': 'Caminho para o veículo',
            'modname': 'Nome do modelo do veículo',
            'newname': 'Novo nome para o modelo do veículo',
            'newvehiclename': 'Novo nome para o veículo no jogo',
            'newid': 'Novo ID para o veículo',
            'vehicleclass': 'Classe do veículo',
            'modnamelength': '"Novo nome do veículo" não pode ter mais de 7 caracteres'
        },
        'soundtab': {
            'sound': 'Sons',
            'menuhint': 'Dica: você pode inserir o nome do veículo acima ou escolher-o na lista abaixo',
            'vehiclesound': 'Som do veículo',
            'pathtoaudiocfg': 'Caminho para o "gtasa_vehicleAudioSettings.cfg"',
            'pathtoaudiocfgvc': 'Caminho para o "gtavc_vehicleAudioSettings.cfg"',
            'newvehiclename': 'Nome do veículo',
            'vehicletogetsound': 'Nome do veículo para transferir o som',
        },
        'vehnpcstab': {
            'npcsvehicles': 'Veículos de NPCs',
            'pathtocargrp': 'Caminho para o "cargrp.dat"',
            'vehicletoinsert': 'Nome do veículo para inserir',
            'choosevehiclegroup': 'Escolha o grupo'
        },
        'idlisttab': {
            'idlist': 'Lista de IDs',
            'pathtosearchids': 'Caminho para onde deseja procurar por IDs',
            'originsaved': 'Salvo',
            'originnonsaved': 'Não salvo',
            'vehicleid': 'ID',
            'vehiclename': 'Nome',
            'vehicleorigin': 'Origem',
            'newlistitem': 'Adicionar veículo à lista',
            'newlistitemvehicle': 'Veículo',
             'additemempty': 'As caixas de texto não podem estar vazias',
            'additemonlynumbers': 'O ID deve ter apenas números',
            'additemlength': 'O ID e/ou nome não podem ter mais de 8 caracteres',
            'additemidexists': 'Este ID já está na lista',
            'additemnameexists': 'Este nome já está na lista'
        }
    }
}
else:
    texts = {
    'pedsbutton1': 'Peds',
    'weapbutton1': 'Weapons',
    'vehbutton1': 'Vehicles',
	'home1': 'Home',
    'configini1': 'Config .ini',
    'lines1': 'Lines',
    'sound1': 'Sounds',
    'npcs1': 'NPCs vehicles',
    'idlist1':'List of IDs',
    'help1': 'Help and Info',
    'inipath1':'Path to \'fastman92limitAdjuster_GTASA.ini\'',
    'inipath2':'Path to \'fastman92limitAdjuster_GTAVC.ini\'',
    'vehpath1':'Path to the vehicle',
    'modname1':'Vehicle name',
    'newname1':'New vehicle name',
    'vehname1':'Vehicle name in-game',
    'newid1':'New vehicle ID',
    'tip':'Tip: you can insert the name above or choose on the list below',
    'class1':'Vehicle class',
    'disable1':'NONE',
    'vehsound1':'Vehicle sound',
    'audiocfgpath1':'Path to \'gtasa_vehicleAudioSettings.cfg\'',
    'audiocfgpath2':'Path to \'gtavc_vehicleAudioSettings.cfg\'',
    'newvehname1':'Vehicle name',
    'vehaudio1':'Vehicle name to get audio from',
    'popcyclepath1':'Path to \'cargrp.dat\'',
    'popcycleveh1':'Vehicle name to insert',
    'popitem1':'Choose group',
    'warning1':'Warning',
    'warn1':'\'New vehicle name\' cannot have more than 7 characters!',
    'apply1':'Apply',
    'default1':'DEFAULT',
    'infolabel1': 'If you need help, click \'More info\' down below to understand\nbetter how it works. This program will make this process easier and faster.',
    'info': 'More info',
    'needed': 'Needs',
    'vehmodelswarn': 'DO NOT EDIT THIS LINE IF YOU ARE USING THE OPEN LIMIT ADJUSTER\nDISABLE IT BY UNMARKING THE CHECKBOX\ngo to the help tab to understand why',
    'warnlabel1': 'INCOMPATIBLE WITH:\nTuning Mod v1.5 or PREVIOUS versions\nReal Traffic Fix v1.2 or PREVIOUS versions\nOFFICIAL updates from First Person Mod',
    'handcfg1': 'Apply \'handling.cfg\' patch (0|1)',
    'audio1': 'Enable vehicle audio loader (0|1)',
    'handlines1': 'Number of standard lines',
    'vehmodels1': 'Vehicle Models',
    'killablemodels1': 'Count of killable model IDs',
    'bikelines1': 'Number of bike lines',
    'planelines1': 'Number of flying lines',
    'boatlines1': 'Number of boat lines',
    'choose1':'Search',
    'remove1':'Remove',
    'create1':'Create lines',
    'donemsg1':'Applied sucessfully!',
    'errormsg1':'An error occurred while trying to complete the request',
    'idlistpath1':'Path to where you want to search for IDs',
    'idlistsearch1':'Search',
    'idlistadd':'Add',
    'idlistselectall1':'Select all',
    'idlistsavebutton1':'Save all',
    'idlistvehsaved':'Origin',
    'newitemlabel1':'Add vehicle to list',
    'idlistvehname':'Vehicle',
    'cancelbutton1':'Cancel',
    'additemerrorempty':'The text boxes cannot be empty',
    'additemerrornumbers':'The ID must contain numbers-only',
    'additemerrorlenght':'The ID and/or name cannot have more than 8 characters',
    'additemerroridexists':'This ID already is on the list',
    'additemerrornameexists':'This name already is on the list',
    'originsaved':'Saved',
    'originnonsaved':'Non saved',
    'idlistvehid':'ID'
    }

import json
with open('languages.json', 'w') as file:
    json.dump(texts, file, ensure_ascii=False, indent=4, sort_keys=False)