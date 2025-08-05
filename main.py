import tkinter as tk
import os
import shutil
import easygui

# function for open file
def file_open_box():
    path = easygui.fileopenbox()
    return path

# function for open folder
def directory_open_box():
    path = tk.filedialog.askdirectory()
    return path

# open_file fuction

def open_file():
    path = file_open_box()
    try:
        os.startfile(path)
    except:
        tk.messagebox.showinfo('Error!', 'file not found.')
        
# copy_file function

def copy_file():
    srource = file_open_box()
    destination = directory_open_box()
    try:
        shutil.copy(srource, destination)
        tk.messagebox.showinfo('Error!', 'file copied successfully.')
    except:
        tk.messagebox.showinfo('Error!', 'file not found.')