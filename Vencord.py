import os
import requests
import subprocess
import time
import pyautogui
import pygetwindow as gw

# URL для скачивания
url = "https://github.com/Vencord/Installer/releases/latest/download/VencordInstallerCli.exe"
filename = "VencordInstallerCli.exe"

# Скачивание файла
try:
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Проверка на успешное выполнение запроса
    with open(filename, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"Скачан файл: {filename}")
except requests.exceptions.RequestException as e:
    print(f"Ошибка при скачивании файла: {e}")
    exit(1)

# Запуск exe файла
try:
    process = subprocess.Popen([filename])
except Exception as e:
    print(f"Ошибка при запуске файла: {e}")
    exit(1)

# Подождем, чтобы процесс запустился
time.sleep(2)

# Получаем все открытые окна и ищем окно, содержащее "py.exe"
windows = [window for window in gw.getAllWindows() if 'py.exe' in window.title]
if windows:
    window = windows[0]
    # Активируем нужное окно
    window.activate()
    time.sleep(1)
    
    # Эмуляция нажатий клавиш
    pyautogui.press('down')      # Один раз стрелка вниз
    time.sleep(1)
    pyautogui.press('enter')     # Первый раз Enter
    time.sleep(1)
    pyautogui.press('enter')     # Второй раз Enter
    time.sleep(1)
    pyautogui.press('enter')     # Третий раз Enter

    print("Процесс завершен.")

    # Удаление скачанного файла
    try:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Файл {filename} успешно удален.")
    except Exception as e:
        print(f"Ошибка при удалении файла: {e}")
else:
    print("Не удалось найти окно с названием, содержащим 'py.exe'.")