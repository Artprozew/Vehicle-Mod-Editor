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
        pass #http://download.gta-expert.it/index.php?act=download&amp;id=5743
    # https://tuningmod.mixmods.com.br/p/ids.html

def vehpage():
    # add maior#b64 = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAG5JREFUWEdjZBhgwDjA9jOMOmA0BCgNgZPQRGxObmKm1AH/oRaTbQ7ZGqEWjzpgNARGQ4CmIQAqZMzILWDQ9J0C8rEWVvjKgQF3ADGep2kUjDpgNARGQ2BIhMCAN8mICSW8aihtko06YDQEKA4BAH+uFiGo0ir0AAAAAElFTkSuQmCC'
    # selectall maior#b64 = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAARNJREFUWEdjZBhgwDjA9jOMOgBbCIgAo2UmEH8G4gRoFK0B0sFQNkxPCJC/GioWCqRBakDgP5ReC6RBakBgARDzAnE6EL9BjnZsDgBpDAJiZAModQBM/zokj4Ddgc0BINfyAPFxIO6FurYYSFtC2TBfWQD5JVCxHiB9AsqGhQQ2/V+AahIIhQCyPM3ZgzIX4AtCUkKEUBTiTAPYUjFyIiTWEYQS8eB1ADYfYsuGuEICWwjiDDViEyFdHQDL50/Q8jZ6SUhKCIDKDBm0coLsNEAo1AglYhT92AwjyQAswUCSfmwOGPAoGM0FhOJw+JeEA14ZERvEVFFHqFChiiX4DBmUTbIBb5QOeLOc5vE+2ioeVCEAAOJpeCEczAJ5AAAAAElFTkSuQmCC'
    #with open('add.png', 'wb') as f:
    #    f.write(base64.decodebytes(b64))

    


    


    





    



 


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


  
  

  





    # help page
    '''needed = Button(tab5, text=texts['needed'], command=needed)
    needed.grid(padx=5, pady=5, column=0, row=5)

    moreinfo = Button(tab5, text=texts['info'], command=moreinfo)
    moreinfo.grid(padx=5, pady=5, column=0, row=20)'''