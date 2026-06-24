import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.energy_threshold = 400
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        try:
            command = r.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except:
            return ""

    except sr.WaitTimeoutError:
        return ""

    except Exception as e:
        print("Mic Error:", e)
        return ""