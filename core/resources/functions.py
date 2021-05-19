from tkinter import *
from resources.variables import *
from resources.languages import *

def get_filename(file):
    import os
    file = os.path.basename(file)
    file = os.path.splitext(file)
    return file[0]


def translation(*element):
    '''if texts and element[-1] in texts:
        print(element[-1])
        return texts[element]
    else:'''
    with open('languages.json', 'r') as file:
        tmpdict = json.load(file)
    for i in element:
        tmpdict = tmpdict[i]
    return tmpdict


def delete_window_messagebox(master, newroot=False):
    if newroot:
        newroot.destroy()
    master.destroy()

'''import timeit
num_runs = 500
duration = timeit.Timer(lambda: translations('help1')).timeit(number=num_runs)
avg_time = duration / num_runs
print(duration)'''

def show_window_messagebox(title, text, **kwargs):
    '''Show a Tkinter window with a text and one or more buttons

    example: show_window_messagebox('My title', 'A really long text that will be split to another line if its too large, even if it has no spaces at all. But, by the way, here is\nanother line', geometry="*", button="OK")

    kwargs:
    
    "button=button_text", "button2=button_text",
    "buttoncommand=button_command_function (Dont pass this kwarg if you just want the window to be destroyed when the button is pressed)",
    "geometry=window_geometry (Use "*" as keyword value if you want the window size to fit the whole text"'''
    newroot = False
    #if not root:
    win = Tk()
    #newroot.geometry('640x400')
    #win = tk.Toplevel()
    win.title(title)
    win.geometry('500x200')  # Default value
    win.attributes('-topmost', True)
    if not 'buttoncommand' in kwargs:
        kwargs['buttoncommand'] = lambda: delete_window_messagebox(win, newroot)
    for k, v in kwargs.items():
        if k == 'geometry':
            if v == '*':
                '''newtext = text.split('\n')
                longest_line = max(longest_line, key=len)
                for i in newtext:
                    newtext = text.split('\n')
                    longest_line = max(longest_line, key=len)
                    oldlongest = longest_line
                    while True:'''
                newtext = text.split('\n')
                longest_line = max(newtext, key=len)
                while not all(len(newtext[x]) <= 100 for x in range(len(newtext))):  # Split long strings
                    while True:
                        newtext = text.split('\n')
                        longest_line = max(newtext, key=len)
                        oldlongest = longest_line
                        if len(longest_line) >= 100:
                            longest_line = longest_line.split(' ')
                            firsthalf = ' '.join(longest_line[0:int(len(longest_line) / 2)])
                            lasthalf = ' '.join(longest_line[int(len(longest_line) / 2):len(longest_line)])
                            text = text.replace(oldlongest, firsthalf + '\n' + lasthalf)
                            if lasthalf == oldlongest or firsthalf == oldlongest:
                                longest_line = oldlongest
                                firsthalf = longest_line[0:int(len(longest_line) / 2)]
                                lasthalf = longest_line[int(len(longest_line) / 2):len(longest_line)]
                                text = text.replace(oldlongest, firsthalf + '...\n' + lasthalf)
                            if len(firsthalf) <= 100 and len(lasthalf) <= 100: break
                        else:
                            break
                        
                '''for i in newtext:
                    while True:
                        time.sleep(2)
                        newtext2 = text.split('\n')
                        longest_line = max(newtext2, key=len)
                        if len(longest_line) >= 100:
                            longest_line = longest_line.split(' ')
                            newline = ' '.join(longest_line[0:int(len(longest_line) / 2)])
                            newline2 = '\n' + ' '.join(longest_line[int(len(longest_line) / 2):len(longest_line)])
                            longest_line = newline + newline2
                            newtext2 = longest_line
                            if '\n' in longest_line:
                                longest_line = longest_line.split('\n')
                                if all(len(longest_line[x]) <= 100 for x in range(len(longest_line))):
                                    longest_line = '\n'.join(longest_line)
                                    print(longest_line)
                                    break

                        else:
                            break'''
                newtext = text.split('\n')
                longest_line = max(newtext, key=len)
                y = str(int(len(newtext) * 19 + 50))  # 20 or 19.2 or 19
                if int(y) <= 150:
                    y = str(int(150))
                x = str(int(len(longest_line) * 9.2))  # 9.2 looks good
                if int(x) <= 150:
                    x = str(int(150))
                win.geometry(x + 'x' + y)
            else:
                win.geometry(v)
        elif k == 'button':
            button = Button(win, text=v, command=kwargs['buttoncommand'])
            button.grid(padx=5, pady=5, column=1, row=3, sticky=EW)
        elif k == 'button2':
            button2 = Button(wim, text=v, command=kwargs['buttoncommand2'])
            button2.grid(padx=5, pady=5, column=1, row=3, sticky=EW)

    labeltext = Label(win, text=text, font='Courier 11', justify=CENTER)
    labeltext.grid(padx=5, pady=5, column=1, row=2)
    #if newroot:
    win.mainloop()


def has_extension(file):
    """Returns if the given file name ends with a suffix (extension) or not"""
    import os
    __, ext = os.path.splitext(file)
    if ext: return True
    else: return False


def try_and_read_file_line(file, filepath, filename):
    if not filepath.endswith('/') and not filename.startswith('/'):
        filepath = filepath + '/'
    if not has_extension(filename):
        filename += '.txt'

    try:
        line = file.readline()
    except: # i forgot the exception it raises, need to add it here (and in the except below)
        file.close()
        try:
            file = open(filepath + filename, 'r+', encoding='utf8', errors='ignore')
            line = file.readline()
        except:
            messagebox.showerror('ERROR', 'Could not read a line in the file, try to remove manually special characters from the file ex. russian, arab characters etc. Or try to change the file encoding')
            return False
    return line


def try_and_open_file(filepath, filename, savcfile=False):
    if savcfile:
        if filename.startswith('gta'):
            tmp = ['vc', 'sa']
        else:
            tmp = ['VC', 'SA']
        filename = filename.format(savcbool.get() and tmp[0] or tmp[1])
    if not has_extension(filename):
        if savcfile:
            filename += '.ini'
        else:
            filename += '.txt'
    if not filepath.endswith('/') and not filename.startswith('/'):
        filepath += '/'

    try:
        file = open(filepath + filename, 'r+') # i could try with open, but i cant rn
    except  FileNotFoundError:
        messagebox.showerror('ERROR', 'The file "' + filename + '" was not found\nArquivo não encontrado')
        return False
    return file


def onclick(event):
    for k, v in dictlist.items():
        try:
            entry = dictlist[k][0].get()
            dictvar = dictlist[k][0]
        except TypeError:
            entry = dictlist[k].get()
            dictvar = dictlist[k]

        if len(entry) == 0:  # This is for some reason returning True for strings of lenght 1 (and string named bike (wtf?))
            if k == 'inipath' or k == 'audiocfgpath':
                dictvar.insert(0, texts[savcbool.get() and k + '2' or k + '1'])
            else:
                dictvar.insert(0, texts[k + '1'])
            dictvar.config(fg='grey')

    for x in texts:
        if event.widget.get() in texts[x]:
            event.widget.delete(0, 'end')
            event.widget.config(fg='black')
            return


def savc_checkbox():
    if 'inipath' in dictlist:
        dictlist['inipath'].delete(0, 'end')
        dictlist['inipath'].config(fg='grey')
        dictlist['inipath'].insert(0, texts[savcbool.get() and 'inipath2' or 'inipath1'])
        
    if 'audiocfgpath' in dictlist:
        dictlist['audiocfgpath'].delete(0, 'end')
        dictlist['audiocfgpath'].config(fg='grey')
        dictlist['audiocfgpath'].insert(0, texts[savcbool.get() and 'audiocfgpath2' or 'audiocfgpath1'])


def CreateButton(var, tabname, text, command, width, column, row, sticky = None,height = 1, padx=5, pady=5, borderwidth=2, columnspan=1, image=None, compound=None,):
      #exec('%s = Button()' % (var))
      if  text in texts:
          text = texts[text]
      var = Button(tab[tabname], text=text, command=command, width=width,height=height, bd=borderwidth, image=image, compound=compound)
      if image or compound:
          var.image = image
      var.grid(padx=padx, pady=pady, column=column, row=row, sticky=sticky,columnspan=columnspan)
      return var

def CreateEntry(var, tabname, text, column, row, width, columnspan = 1, sticky =None, padx=5, pady=5):
    dictlist[var] = Entry(tab[tabname], width=width, borderwidth=2)
    dictlist[var].insert(0, texts[text])
    dictlist[var].config(fg='grey')
    dictlist[var].grid(padx=padx, pady=pady, column=column, row=row,columnspan=columnspan, sticky=sticky)
    dictlist[var].bind('<FocusIn>', onclick)
    return dictlist[var]