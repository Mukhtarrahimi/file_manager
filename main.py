import tkinter as tk
from tkinter import messagebox, filedialog
import os
import shutil
import easygui

# ---------- Functions ----------
def file_open_box():
    path = easygui.fileopenbox()
    return path

def directory_open_box():
    path = filedialog.askdirectory()
    return path

def open_file():
    path = file_open_box()
    try:
        os.startfile(path)
    except:
        messagebox.showinfo('Error!', 'File not found.')

def copy_file():
    source = file_open_box()
    destination = directory_open_box()
    try:
        shutil.copy(source, destination)
        messagebox.showinfo('Success!', 'File copied successfully.')
    except:
        messagebox.showinfo('Error!', 'File not found.')

def delete_file():
    path = file_open_box()
    try:
        os.remove(path)
        messagebox.showinfo('Success!', 'File deleted successfully.')
    except:
        messagebox.showinfo('Error!', 'File could not be deleted.')

def rename_file():
    try:
        file = file_open_box()
        path1 = os.path.dirname(file)
        extension = os.path.splitext(file)[1]
        new_name = easygui.enterbox("Enter new name (without extension):")
        if not new_name:
            return
        path2 = os.path.join(path1, new_name + extension)
        os.rename(file, path2)
        messagebox.showinfo('Success!', 'File renamed successfully.')
    except:
        messagebox.showinfo('Error!', 'Rename failed.')

def move_file():
    source = file_open_box()
    destination = directory_open_box()
    if source == destination:
        messagebox.showinfo('Error!', 'Source and destination are the same.')
    else:
        try:
            shutil.move(source, destination)
            messagebox.showinfo('Success!', 'File moved successfully.')
        except:
            messagebox.showinfo('Error!', 'File move failed.')

def make_directory():
    path = directory_open_box()
    name = easygui.enterbox("Enter folder name:")
    if not name:
        return
    new_path = os.path.join(path, name)
    try:
        os.mkdir(new_path)
        messagebox.showinfo('Success', 'Directory created successfully.')
    except:
        messagebox.showinfo('Error!', 'Directory creation failed.')

def remove_directory():
    path = directory_open_box()
    try:
        os.rmdir(path)
        messagebox.showinfo('Success', 'Directory removed successfully.')
    except:
        messagebox.showinfo('Error!', 'Directory could not be removed.')

def list_files():
    path = directory_open_box()
    file_list = sorted(os.listdir(path))
    list_window = tk.Toplevel(window)
    list_window.title("Files in Folder")
    list_window.geometry("400x300")
    list_window.config(bg="#f1f5f9")
    tk.Label(list_window, text="Files:", font=("Arial", 12, "bold"), bg="#f1f5f9").pack(pady=10)
    listbox = tk.Listbox(list_window, font=("Arial", 10), width=50)
    for i in file_list:
        listbox.insert(tk.END, i)
    listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# ---------- GUI Setup ----------
window = tk.Tk()
window.title("📁 Simple File Manager")
window.geometry("800x600")
window.config(bg="#0f172a")  # dark blue background

# ---------- Style Config ----------
btn_font = ("Segoe UI", 11, "bold")
btn_bg = "#4f46e5"
btn_fg = "#f8fafc"
frame_bg = "#1e293b"

# ---------- Title ----------
tk.Label(window, text="Simple File Manager", font=("Segoe UI", 20, "bold"),
         bg="#0f172a", fg="#facc15").pack(pady=20)

# ---------- Frames ----------
frame_top = tk.Frame(window, bg=frame_bg)
frame_top.pack(pady=10)

frame_middle = tk.Frame(window, bg=frame_bg)
frame_middle.pack(pady=10)

frame_bottom = tk.Frame(window, bg=frame_bg)
frame_bottom.pack(pady=10)

# ---------- Buttons ----------
# Top frame: File operations
tk.Button(frame_top, text="Open File", command=open_file,
          font=btn_font, bg=btn_bg, fg=btn_fg, width=20).grid(row=0, column=0, padx=10, pady=10)

tk.Button(frame_top, text="Copy File", command=copy_file,
          font=btn_font, bg=btn_bg, fg=btn_fg, width=20).grid(row=0, column=1, padx=10, pady=10)

tk.Button(frame_top, text="Move File", command=move_file,
          font=btn_font, bg=btn_bg, fg=btn_fg, width=20).grid(row=0, column=2, padx=10, pady=10)

# Middle frame: File editing
tk.Button(frame_middle, text="Rename File", command=rename_file,
          font=btn_font, bg=btn_bg, fg=btn_fg, width=20).grid(row=0, column=0, padx=10, pady=10)

tk.Button(frame_middle, text="Delete File", command=delete_file,
          font=btn_font, bg=btn_bg, fg=btn_fg, width=20).grid(row=0, column=1, padx=10, pady=10)

tk.Button(frame_middle, text="List Files in Folder", command=list_files,
          font=btn_font, bg=btn_bg, fg=btn_fg, width=20).grid(row=0, column=2, padx=10, pady=10)

# Bottom frame: Directory operations
tk.Button(frame_bottom, text="Make Directory", command=make_directory,
          font=btn_font, bg=btn_bg, fg=btn_fg, width=20).grid(row=0, column=0, padx=10, pady=10)

tk.Button(frame_bottom, text="Remove Directory", command=remove_directory,
          font=btn_font, bg=btn_bg, fg=btn_fg, width=20).grid(row=0, column=1, padx=10, pady=10)

# ---------- Main Loop ----------
window.mainloop()
