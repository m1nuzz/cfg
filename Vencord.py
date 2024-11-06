import os
import requests
import subprocess
import time
import keyboard  # Нужно установить библиотеку: pip install keyboard

# URL для скачивания
url = "https://github.com/Vencord/Installer/releases/latest/download/VencordInstallerCli.exe"
filename = "VencordInstallerCli.exe"

# Скачивание файла
response = requests.get(url)
with open(filename, "wb") as file:
    file.write(response.content)
print(f"Скачан файл: {filename}")

# Запуск exe файла
process = subprocess.Popen([filename])

# Подождем, чтобы процесс запустился
time.sleep(2)

# Эмуляция нажатий клавиш
keyboard.send("down")      # Один раз стрелка вниз
time.sleep(1)
keyboard.send("enter")     # Первый раз Enter
time.sleep(1)
keyboard.send("enter")     # Второй раз Enter
time.sleep(1)
keyboard.send("enter")     # Третий раз Enter

print("Процесс завершен.")
