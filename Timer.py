import subprocess
import os
import psutil  # Make sure to install psutil using: pip install psutil

def set_timer_resolution(resolution):
    command = f'start /B cmd /c C:\\SetTimerResolution.exe --resolution {resolution} --no-console'
    subprocess.run(command, shell=True)

def turn_off_timer_resolution():
    for process in psutil.process_iter(['pid', 'name']):
        if 'SetTimerResolution.exe' in process.info['name']:
            os.system(f'TASKKILL /F /PID {process.info["pid"]}')

def main():
    initial_resolution = 5000
    set_timer_resolution(initial_resolution)

    while True:
        print(f'Change Resolution: Current Resolution is set to {initial_resolution}')
        new_resolution = int(input('Enter the new resolution (or enter 0 to exit): '))

        if new_resolution == 0:
            break  # Exit the loop if the user enters 0

        # Turn off SetTimerResolution if running
        turn_off_timer_resolution()

        # Set new resolution
        set_timer_resolution(new_resolution)
        print(f'SetTimerResolution.exe is now running with resolution {new_resolution}')

if __name__ == "__main__":
    main()
