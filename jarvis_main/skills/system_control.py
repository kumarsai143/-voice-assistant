import os

def handle_system(command):
    if "shutdown" in command:
        os.system("shutdown /s /t 1")
        return "Shutting down"

    elif "restart" in command:
        os.system("shutdown /r /t 1")
        return "Restarting"

    return None