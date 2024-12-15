import os
import requests
from tqdm import tqdm
import subprocess
import time
import pyautogui

# URL для скачивания
url = "https://github.com/Vencord/Installer/releases/latest/download/VencordInstallerCli.exe"
filename = "VencordInstallerCli.exe"

# Скачивание файла с прогресс-баром
try:
    # Получаем размер файла
    response = requests.get(url, stream=True)
    response.raise_for_status()
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte

    # Создаем прогресс-бар
    progress_bar = tqdm(
        total=total_size, 
        unit='iB', 
        unit_scale=True, 
        desc=filename, 
        colour='green'
    )

    # Скачивание с отображением прогресса
    with open(filename, "wb") as file:
        downloaded_size = 0
        for chunk in response.iter_content(block_size):
            size = file.write(chunk)
            progress_bar.update(size)
            downloaded_size += size

    progress_bar.close()

    # Проверка корректности скачивания
    if total_size != 0 and downloaded_size != total_size:
        print("Ошибка: Файл скачан не полностью")
        exit(1)

    print(f"\nФайл {filename} успешно скачан.")

except requests.exceptions.RequestException as e:
    print(f"Ошибка при скачивании файла: {e}")
    exit(1)

# Запуск exe файла
try:
    subprocess.Popen([filename])
except Exception as e:
    print(f"Ошибка при запуске файла: {e}")
    exit(1)

# Подождем, чтобы процесс запустился
time.sleep(2)

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

# Удаление скачанного файла
try:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Файл {filename} успешно удален.")
except Exception as e:
    print(f"Ошибка при удалении файла: {e}")
