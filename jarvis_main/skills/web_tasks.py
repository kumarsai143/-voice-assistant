import webbrowser
import pywhatkit
import datetime

def handle_web(command):

    # -------- OPEN WEBSITES --------
    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "open github" in command:
        webbrowser.open("https://github.com")
        return "Opening GitHub"

    elif "open stackoverflow" in command:
        webbrowser.open("https://stackoverflow.com")
        return "Opening Stack Overflow"

    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
        return "Opening LinkedIn"

    # -------- SEARCH GOOGLE --------
    elif "search" in command:
        query = command.replace("search", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching for {query}"

    # -------- PLAY YOUTUBE --------
    elif "play" in command:
        song = command.replace("play", "")
        pywhatkit.playonyt(song)
        return f"Playing {song} on YouTube"

    # -------- YOUTUBE SEARCH --------
    elif "youtube search" in command:
        query = command.replace("youtube search", "")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        return f"Searching YouTube for {query}"

    # -------- SEND WHATSAPP MESSAGE --------
    elif "send whatsapp" in command:
        try:
            # Example: "send whatsapp to 9876543210 hello"
            parts = command.split("to")
            number_and_msg = parts[1].strip()

            number = number_and_msg[:10]
            message = number_and_msg[10:].strip()

            now = datetime.datetime.now()
            hour = now.hour
            minute = now.minute + 2  # send after 2 minutes

            pywhatkit.sendwhatmsg(f"+91{number}", message, hour, minute)
            return "Sending WhatsApp message"
        except:
            return "Failed to send WhatsApp message"

    # -------- OPEN MAPS --------
    elif "open maps" in command:
        webbrowser.open("https://maps.google.com")
        return "Opening Google Maps"

    elif "find location" in command:
        location = command.replace("find location", "")
        webbrowser.open(f"https://www.google.com/maps/search/{location}")
        return f"Showing location of {location}"

    # -------- OPEN EMAIL --------
    elif "open gmail" in command:
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail"

    # -------- NEWS --------
    elif "news" in command:
        webbrowser.open("https://news.google.com")
        return "Opening latest news"

    # -------- WEATHER --------
    elif "weather" in command:
        webbrowser.open("https://www.google.com/search?q=weather")
        return "Showing weather report"

    # -------- DOWNLOAD FROM YOUTUBE --------
    elif "download video" in command:
        return "Sorry, downloading videos is not enabled yet"

    return None