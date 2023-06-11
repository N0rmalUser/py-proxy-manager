import os
import shutil
import winreg
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time

# Параметры
button_name = "Настройка прокси"        # Название кнопки
file_name = "proxy.exe"                 # Название файла (если как-то переименовал)
index = False
PRIMARY_COLOR = "#24292e"
SECONDARY_COLOR = "#f6f8fa"
#----------
def copy_file(source_file, destination_folder):
    try:
        expanded_source_file = os.path.expanduser(source_file)
        shutil.copy(expanded_source_file, destination_folder)
        print("Файл успешно скопирован")
    except Exception as e:
        print("Ошибка при копировании файла:", e)

def create_registry_key(key_path):
    try:
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)
        print("Раздел успешно создан:", key_path)
        winreg.CloseKey(key)
    except Exception as e:
        print("Ошибка при создании раздела:", e)

def set_default_registry_value(key_path, file_name):
    try:
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, key_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "", 0, winreg.REG_SZ, file_name)
        winreg.CloseKey(key)
        print("Значение по умолчанию успешно изменено")
    except Exception as e:
        print("Ошибка при изменении значения по умолчанию:", e)
        
def continue_button_clicked():
    global button_name
    choose()
    button_name = text_entry.get()
    window.destroy()

def show_installation_complete():
    messagebox.showinfo("Установка завершена", "Установка завершена")

def handle_enter(event):
    continue_button_clicked()

def clear_placeholder(event):
    if text_entry.get() == "Название кнопки":
        text_entry.delete(0, "end")
        text_entry.configure(fg="black")

def restore_placeholder(event):
    if text_entry.get() == "":
        text_entry.insert(0, "Название кнопки")
        text_entry.configure(fg="gray")

def setup():
    current_dir = os.path.dirname(__file__)
    source_file = f"{current_dir}\{file_name}"
    destination_folder = "C:\Windows\System32"
    copy_file(source_file, destination_folder)
    key_path = f"Directory\Background\shell\{button_name}\command"
    create_registry_key(key_path)
    set_default_registry_value(key_path, file_name)
    time.sleep(2)
    messagebox.showinfo("Установка завершена", "Установка завершена успешно!")

def cancel():
    time.sleep(2)
    messagebox.showinfo("Установка отменена", "Установка отменена((")

def choose():
    global index
    index = True
window = tk.Tk()
window.title("Окошко с вводом текста")      # Заголовок окна
window_width = 600
window_height = 250
screen_width = window.winfo_screenwidth()   # Устанавливаем размеры окна
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")  # Устанавливаем позицию окна
window.overrideredirect(True)               # Удаляем верхнюю часть окна (заголовок и границы)
window.config(bg=PRIMARY_COLOR)             # Устанавливаем цвет фона
title_label = tk.Label(window, text="Установка приложения", font=("Arial", 18, "bold"), fg=SECONDARY_COLOR, bg=PRIMARY_COLOR)
title_label.pack(pady=10)                   # Создаем плашку сверху с текстом "Установка приложения"
separator_frame = ttk.Frame(window, height=2, relief=tk.SUNKEN)
separator_frame.pack(fill=tk.X)             # Создаем рамку для отделения плашки от основного окна
label_text = tk.Label(window, text="Введите название для кнопки", font=("Arial", 14), fg=SECONDARY_COLOR, bg=PRIMARY_COLOR)
label_text.pack()                           # Создаем надпись над полем ввода текста
button_style = ttk.Style()                  # Создаем стиль для кнопок
button_style.configure("TButton",
                       font=("Arial", 11),
                       foreground="black",
                       padding=6)
entry_style = ttk.Style()                   # Создаем стиль для текстового поля
entry_style.configure("TEntry",
                      font=("Arial", 30, "bold"),
                      foreground="black",
                      padding=8,
                      relief=tk.FLAT)
text_entry = ttk.Entry(window, width=60, style="TEntry")
text_entry.pack(pady=10, padx=10)           # Создаем текстовое поле
text_entry.insert(0, "Настройка прокси")
text_entry.bind("<FocusIn>", clear_placeholder)
text_entry.bind("<FocusOut>", restore_placeholder)
text_entry.bind("<Return>", handle_enter)
button_frame = tk.Frame(window, bg=PRIMARY_COLOR)
button_frame.pack(pady=20)                  # Создаем фрейм для кнопок
continue_button = ttk.Button(button_frame, text="Продолжить", command=continue_button_clicked, style="TButton")
continue_button.pack(side=tk.LEFT, padx=5)
spacer = ttk.Label(button_frame, width=25, background=PRIMARY_COLOR)
spacer.pack(side=tk.LEFT)                   # Создаем пространство между кнопками
cancel_button = ttk.Button(button_frame, text="Отмена", command=window.destroy, style="TButton")
cancel_button.pack(side=tk.LEFT, padx=5)    # Создаем кнопку "Отмена"
window.mainloop()

if index:
    setup()
else:
    cancel()