import keyboard
import time

# Функция для выполнения команды
def execute_command(command):
    print("Выполняю команду:", command)
    # Ваш код для выполнения команды здесь
    # Например, вы можете использовать subprocess для запуска консольной команды
    keyboard.write(command)  # Вводим команду
    keyboard.send("enter")  # Нажимаем клавишу Enter

# Список с названиями навыков и соответствующими командами
skills = [
    "campaign.set_skill_main_hero Athletics | 300",
    "campaign.set_skill_main_hero Bow | 300",
    "campaign.set_skill_main_hero Charm | 300",
    "campaign.set_skill_main_hero Crossbow | 300",
    "campaign.set_skill_main_hero Engineering | 300",
    "campaign.set_skill_main_hero Leadership | 300",
    "campaign.set_skill_main_hero Medicine | 300",
    "campaign.set_skill_main_hero OneHanded | 300",
    "campaign.set_skill_main_hero Polearm | 300",
    "campaign.set_skill_main_hero Riding | 300",
    "campaign.set_skill_main_hero Roguery | 300",
    "campaign.set_skill_main_hero Scouting | 300",
    "campaign.set_skill_main_hero Smithing | 300",
    "campaign.set_skill_main_hero Steward | 300",
    "campaign.set_skill_main_hero Tactics | 300",
    "campaign.set_skill_main_hero Throwing | 300",
    "campaign.set_skill_main_hero Trade | 300",
    "campaign.set_skill_main_hero TwoHanded | 300"
]

# Функция для обработки нажатия клавиши Enter
def on_key_press(event):
    if event.name == 'enter':  # Проверяем, была ли нажата клавиша Enter
        time.sleep(1)  # Подождать 1 секунду перед началом ввода команд
        for command in skills:
            execute_command(command)
            time.sleep(0.5)  # Подождать полсекунды между выполнением команд

# Назначаем обработчик событий для нажатия клавиш
keyboard.on_press(on_key_press)

# Ожидаем нажатия Enter перед началом выполнения скрипта
print("Нажмите Enter для запуска скрипта...")
keyboard.wait("enter")

# Запускаем бесконечный цикл для обработки событий клавиатуры
keyboard.wait('esc')  # Ждем нажатия клавиши Esc для выхода из программы
