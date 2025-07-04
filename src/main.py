import sys
import os
import platform 
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import webbrowser

def app():
    def select_file():
        global file 
        file = filedialog.askopenfilename(initialdir = "C:/", title = "Select file...", filetypes = (("Python Source Code","*.py"), ("Python Source Code (no console)","*.pyw")))
        select_file_entry.insert(0, file)
        if file != "":
            select_file_entry.configure(state=DISABLED)

    def select_save():
        global save_path 
        save_path = filedialog.askdirectory(initialdir = "C:/", title = "Select folder...")
        save_path_entry.insert(0, save_path)
        if save_path != "":
            save_path_entry.configure(state=DISABLED)
    
    def select_ico():
        global icon_path
        icon_path = filedialog.askopenfilename(initialdir = "C:/", title = "Select icon...", filetypes = [("Icon","*.ico")])
        icon_path_entry.insert(0, icon_path)
        if icon_path != "":
            icon_path_entry.configure(state=DISABLED)
        
    def convert():
        pip_upgrade = "python -m pip install --upgrade pip"
        install_pyi = "pip install pyinstaller"
        os.system(pip_upgrade)
        os.system(install_pyi)
    
        os.chdir(save_path)
        
        if file.endswith('.pyw'):
            cmd = 'pyinstaller.exe --windowed --onefile ' + '"' + file + '" --icon="' + icon_path + '"' 
            os.system(cmd)
        elif file.endswith('.py'):   
            cmd = 'pyinstaller.exe --onefile ' + '"' + file + '" --icon="' + icon_path + '"'
            os.system(cmd)
        elif file.endswith('.spec'):
            cmd = 'pyinstaller.exe ' + '"' + file + '" --icon="' + icon_path + '"'
            os.system(cmd)

        os.system('pause')

    def show_about():
        os = platform.platform()
        messagebox.showinfo(title="About", message=f".py to .exe                                          \nAuthor: Ashwin Ravuru Kalyan\nVersion: 1.1.0\nOperating System: {os}")

    def show_help():
        webbrowser.open("https://www.google.com/search?q=Convert+python+script+to+windows+executable&sxsrf=ALiCzsbL4aU5J-4_edlEdi8fA3A2LuQbOA%3A1661661028523&ei=ZO8KY_2_H7WZptQP75CAmAU&ved=0ahUKEwj9gd7a2ej5AhW1jIkEHW8IAFMQ4dUDCA4&uact=5&oq=Convert+python+script+to+windows+executable&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBggAEB4QBTIFCAAQhgMyBQgAEIYDOgQIABBHOgcIIxCwAhAnOggIABAeEA0QBUoECEEYAEoECEYYAFD5A1jIB2DzC2gAcAJ4AIABhQGIAYgCkgEDMC4ymAEAoAEByAEIwAEB&sclient=gws-wiz")
    
    window = Tk()
    window.geometry("700x350")
    window.resizable(False, False)
    window.title(".py to .exe")

    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New Window                          ", command=new_window)
    filemenu.add_separator()
    filemenu.add_command(label="Select File...", command=select_file)
    filemenu.add_command(label="Select Folder...", command=select_save)
    filemenu.add_command(label="Select Icon...", command=select_ico)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.destroy)
    menubar.add_cascade(label="File", menu=filemenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Show Help                        ", command=show_help)
    helpmenu.add_separator()
    helpmenu.add_command(label="About", command=show_about)
    menubar.add_cascade(label="Help", menu=helpmenu)

    titleLabel = Label(window, font=("Times New Roman", 25), text=".py to .exe").place(x=280, y=30)
    
    select_file_button = Button(window, text="        Select file...        ", background="#f71661", foreground="#ffffff", activebackground="#cc1452", activeforeground= "#ffffff", command=select_file).place(x=480, y=100)
    save_path_button = Button(window, text="      Select folder...     ", background="#f71661", foreground="#ffffff", activebackground="#cc1452", activeforeground= "#ffffff", command=select_save).place(x=480, y=130)
    select_icon_button = Button(window, text="       Select icon...       ", background="#f71661", foreground="#ffffff", activebackground="#cc1452", activeforeground= "#ffffff", command=select_ico).place(x=480, y=160)
    save_path_button = Button(window, text="           Convert           ", background="#f71661", foreground="#ffffff", activebackground="#cc1452", activeforeground= "#ffffff", command=convert).place(x=297, y=250)

    select_file_entry = Entry(window, width=34)
    select_file_entry.insert(0, "")
    select_file_entry.place(x=250, y=103)

    save_path_entry = Entry(window, width=34)
    save_path_entry.insert(0, "")
    save_path_entry.place(x=250, y=134)

    icon_path_entry = Entry(window, width=34)
    icon_path_entry.insert(0, "")
    icon_path_entry.place(x=250, y=165)

    script_to_convert_label = Label(window, font=("Times New Roman", 11), text="Python script to convert: ").place(x=80, y=100)
    save_exe_label = Label(window, font=("Times New Roman", 11), text="Path to save executable to: ").place(x=80, y=133)
    icon_label = Label(window, font=("Times New Roman", 11), text="Icon file for executable: ").place(x=80, y=165)
    
    window.config(menu=menubar)
    window.mainloop()

def new_window():
    app()

app()
