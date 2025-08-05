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