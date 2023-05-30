import os
import shutil
import winreg

# Параметры
button_name = "Прокси"      # Название кнопки
file_name = "proxy.exe"     # Название файла (если как-то переименовал)
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

current_dir = os.path.dirname(__file__)
source_file = f"{current_dir}\{file_name}"
destination_folder = "C:\Windows\System32"
copy_file(source_file, destination_folder)
key_path = f"Directory\Background\shell\{button_name}\command"
create_registry_key(key_path)
set_default_registry_value(key_path, file_name)
