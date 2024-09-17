import subprocess

def start_ngrok():
    try:
        # Запускаем ngrok с нужными параметрами
        subprocess.run(["ngrok", "http", "11434", "--host-header=localhost:11434"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске ngrok: {e}")

if __name__ == "__main__":
    start_ngrok()
