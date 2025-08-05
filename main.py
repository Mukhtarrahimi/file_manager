import tkinter as tk
from tkinter import messagebox, filedialog
import os
import shutil
import easygui

# ---------- Functions ----------
def file_open_box():
    return easygui.fileopenbox()

def directory_open_box():
    return filedialog.askdirectory()

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
    list_window.geometry("300x200")
    list_window.config(bg="#f1f5f9")
    tk.Label(list_window, text="Files:", font=("Arial", 11, "bold"), bg="#f1f5f9").pack(pady=8)
    listbox = tk.Listbox(list_window, font=("Arial", 10), width=40, height=8)
    for i in file_list:
        listbox.insert(tk.END, i)
    listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# ---------- GUI Setup ----------
window = tk.Tk()
window.title("📁 Simple File Manager")
window.geometry("500x350")
window.config(bg="#0f172a")

# ---------- Styles ----------
btn_font = ("Segoe UI", 9, "bold")
btn_bg = "#4f46e5"
btn_fg = "#f8fafc"
frame_bg = "#1e293b"

# ---------- Title ----------
tk.Label(window, text="Simple File Manager", font=("Segoe UI", 14, "bold"),
         bg="#0f172a", fg="#facc15").pack(pady=10)

# ---------- Buttons Frame ----------
buttons_frame = tk.Frame(window, bg=frame_bg)
buttons_frame.pack(pady=5)

# Button Layout (2 columns)
buttons = [
    ("📂 Open File", open_file),
    ("📋 Copy File", copy_file),
    ("📤 Move File", move_file),
    ("✏️ Rename File", rename_file),
    ("🗑️ Delete File", delete_file),
    ("📄 List Files", list_files),
    ("📁 Make Folder", make_directory),
    ("🚫 Remove Folder", remove_directory),
]

for index, (text, cmd) in enumerate(buttons):
    row = index // 2
    col = index % 2
    tk.Button(buttons_frame, text=text, command=cmd, font=btn_font,
              bg=btn_bg, fg=btn_fg, width=24, height=2,
              relief='flat', activebackground='#6366f1', activeforeground='white')\
        .grid(row=row, column=col, padx=10, pady=7)

# ---------- Mainloop ----------
window.mainloop()
