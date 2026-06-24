from core.listener import listen
from core.speaker import speak
from skills.system_control import handle_system
from skills.web_tasks import handle_web
from skills.ai_chat import handle_ai

def process_command(command):

    # System tasks
    result = handle_system(command)
    if result:
        return result

    # Web tasks
    result = handle_web(command)
    if result:
        return result

    # AI fallback
    return handle_ai(command)


def run():
    speak("Jarvis activated")

    while True:
        command = listen()
        print("Heard:", command)

        if command == "":
            continue

        # 🔥 DIRECT COMMAND PROCESSING (NO WAKE WORD NEEDED)
        response = process_command(command)

        print("Response:", response)

        if response:
            speak(response)
        else:
            speak("I didn't understand that")


if __name__ == "__main__":
    run()