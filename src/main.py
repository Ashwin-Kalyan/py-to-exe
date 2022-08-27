import sys
import os
from tkinter import *
from tkinter import filedialog

window = Tk()

file = filedialog.askopenfilename(initialdir = "./", title = "Select file...", filetypes = ((".py files","*.py"), (".pyw files","*.pyw"), (".spec","*.spec")))

pip_upgrade = ("python -m pip install --upgrade pip")
install_pyi = ("pip install pyinstaller")
os.system(pip_upgrade)
os.system(install_pyi)

if file == "." or file == None:
    sys.exit()

if file.endswith('.pyw'):
    cmd = ('pyinstaller.exe --windowed --onefile ' + '"' + file + '"')
    os.system(cmd)

elif file.endswith('.py'):   
    cmd = ('pyinstaller.exe --onefile ' + '"' + file + '"')
    os.system(cmd)

elif file.endswith('.spec'):
    cmd = ('pyinstaller.exe ' + '"' + file + '"')
    os.system(cmd)

os.system('pause')
window.mainloop()