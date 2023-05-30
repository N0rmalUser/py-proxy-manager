import winreg
import tkinter as tk
from tkinter import messagebox

def set_registry_value(key_path, value_name, value_data):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD, value_data)
        winreg.CloseKey(key)
        print("Значение реестра успешно изменено")
    except Exception as e:
        print("Ошибка при изменении значения реестра:", e)

def show_dialog():
    result = messagebox.askquestion("Диалоговое окно", "Использовать прокси?")
    if result == 'yes':
        set_registry_value("Software\Microsoft\Windows\CurrentVersion\Internet Settings", "ProxyEnable", 1)
    elif result == 'no':
        set_registry_value("Software\Microsoft\Windows\CurrentVersion\Internet Settings", "ProxyEnable", 0)
    else:
        print("Ошибка при изменении значения реестра")

show_dialog()