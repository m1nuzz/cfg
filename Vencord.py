import os
import requests
from tqdm import tqdm
import subprocess
import time
import pyautogui
import ctypes
import win32gui
import win32con

# URL для скачивания
url = "https://github.com/Vencord/Installer/releases/latest/download/VencordInstallerCli.exe"
filename = "VencordInstallerCli.exe"

# Скачивание файла с прогресс-баром
try:
    response = requests.get(url, stream=True)
    response.raise_for_status()
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte

    progress_bar = tqdm(
        total=total_size, 
        unit='iB', 
        unit_scale=True, 
        desc=filename, 
        colour='green'
    )

    with open(filename, "wb") as file:
        for chunk in response.iter_content(block_size):
            size = file.write(chunk)
            progress_bar.update(size)

    progress_bar.close()

    if total_size != 0 and progress_bar.n != total_size:
        print("Ошибка: Файл скачан не полностью")
        exit(1)

    print(f"\nФайл {filename} успешно скачан.")

except requests.exceptions.RequestException as e:
    print(f"Ошибка при скачивании файла: {e}")
    exit(1)

# Запуск exe файла в новом окне
try:
    process = subprocess.Popen(["start", filename], shell=True)  # Открытие в новом окне
    print("Установщик запущен в новом окне.")
except Exception as e:
    print(f"Ошибка при запуске файла: {e}")
    exit(1)

# Подождем, чтобы процесс запустился
time.sleep(2)

# Функция для поиска окна по названию
def find_window_by_name(name_part):
    def enum_windows(hwnd, lparam):
        window_title = win32gui.GetWindowText(hwnd)
        if name_part in window_title:
            ctypes.windll.user32.SetForegroundWindow(hwnd)
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # Восстановить окно, если оно свернуто
    win32gui.EnumWindows(enum_windows, None)

# Принудительное выставление окна установщика на передний план
find_window_by_name("VencordInstallerCli.exe")

# Эмуляция навигации в установщике
try:
    pyautogui.press('down')  # Один раз стрелка вниз
    time.sleep(1)
    pyautogui.press('enter')  # Первый раз Enter
    time.sleep(1)
    pyautogui.press('enter')  # Второй раз Enter
    time.sleep(1)
    pyautogui.press('enter')  # Третий раз Enter
    
    print("Процесс установки завершен.")
except Exception as e:
    print(f"Ошибка при автоматизации: {e}")

# Ожидание завершения процесса установки
try:
    process.wait()  # Ждем завершения процесса
    print("Установщик завершил работу.")
except Exception as e:
    print(f"Ошибка при ожидании завершения процесса: {e}")

# Удаление скачанного файла
try:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Файл {filename} успешно удален.")
except Exception as e:
    print(f"Ошибка при удалении файла: {e}")
