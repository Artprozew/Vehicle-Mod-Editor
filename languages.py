import tkinter as tk
from tkinter import *
import configparser, os
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
    'pedsbutton1': 'Peds',
    'weapbutton1': 'Armas',
    'vehbutton1': 'Veículos',
	'home1': 'Início',
    'configini1':'Config .ini',
    'lines1':'Linhas',
    'sound1':'Sons',
    'npcs1':'Veículos de NPCs',
    'idlist1':'Lista de IDs',
    'help1':'Ajuda e Info',
    'inipath1':'Caminho para o \'fastman92limitAdjuster_GTASA.ini\'',
    'inipath2':'Caminho para o \'fastman92limitAdjuster_GTAVC.ini\'',
    'vehpath1':'Caminho para o veículo',
    'modname1':'Nome do veículo',
    'newname1':'Novo nome do veículo',
    'vehname1':'Nome do veículo no jogo',
    'newid1':'Novo ID do veículo',
    'tip':'Dica: você pode inserir o nome acima ou escolher na lista abaixo',
    'class1':'Classe do veículo',
    'disable1':'NENHUM',
    'vehsound1':'Som do veículo',
    'audiocfgpath1':'Caminho para o \'gtasa_vehicleAudioSettings.cfg\'',
    'audiocfgpath2':'Caminho para o \'gtavc_vehicleAudioSettings.cfg\'',
    'newvehname1':'Nome do veículo',
    'vehaudio1':'Nome do veículo para transferir o som',
    'popcyclepath1':'Caminho para o \'cargrp.dat\'',
    'popcycleveh1':'Nome do veículo para inserir',
    'popitem1':'Escolha o grupo',
    'warning1':'Aviso',
    'warn1':'\'Novo nome do veículo\' não pode ter mais de 7 caracteres!',
    'apply1':'Aplicar',
    'default1':'PADRÃO',
    'infolabel1':'Se você precisar de ajuda, clique \'Mais informações\' abaixo para entender\n melhor como funciona. Esse programa irá facilitar e agilizar esse processo.',
    'info':'Mais informações',
    'needed':'Necessidades',
    'vehmodelswarn':'NÃO EDITE ESSA LINHA CASO USE O OPEN LIMIT ADJUSTER\nDESATIVE-A DESMARCANDO NA CAIXA AO LADO\nvá na aba ajuda para saber mais',
    'warnlabel1':'INCOMPATÍVEL COM:\nVersões do Tuning Mod v1.5 ou ANTERIORES\nVersões do Real Traffic Fix v1.2 ou ANTERIORES\nAtualizações OFICIAIS do First Person Mod',
    'handcfg1':'Apply \'handling.cfg\' patch (0|1)',
    'audio1':'Enable vehicle audio loader (0|1)',
    'handlines1':'Number of standard lines',
    'vehmodels1':'Vehicle Models',
    'killablemodels1':'Count of killable model IDs',
    'bikelines1':'Number of bike lines',
    'planelines1':'Number of flying lines',
    'boatlines1':'Number of boat lines',
    'choose1':'Procurar',
    'remove1':'Remover',
    'create1':'Criar linhas',
    'donemsg1':'Aplicado com sucesso!',
    'errormsg1':'Ocorreu um erro ao tentar concluir o pedido',
    'idlistpath1':'Caminho para onde deseja procurar por IDs',
    'idlistsearch1':'Procurar',
    'idlistadd':'Adicionar',
    'idlistselectall1':'Selecionar todos',
    'idlistsavebutton1':'Salvar todos',
    'idlistvehsaved':'Origem',
    'newitemlabel1':'Adicionar veículo na lista',
    'idlistvehname':'Veículo',
    'cancelbutton1':'Cancelar',
    'additemerrorempty':'As caixas de texto não podem estar vazias',
    'additemerrornumbers':'O ID deve ter apenas números',
    'additemerrorlenght':'O ID e/ou nome não podem ter mais de 8 caracteres',
    'additemerroridexists':'Este ID já está na lista',
    'additemerrornameexists':'Este nome já está na lista',
    'originsaved':'Salvo',
    'originnonsaved':'Não salvo',
    'idlistvehid':'ID'
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