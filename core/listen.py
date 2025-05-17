import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, phrase_time_limit=5)
        try:
            query = recognizer.recognize_google(audio)
            print("You:", query)
            return query.lower()
        except sr.UnknownValueError:
            from core.voice import speak
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            from core.voice import speak
            speak("Network issue.")
            return ""

def get_input(mode="voice"):
    if mode == "voice":
        return listen()
    else:
        return input("Enter your command: ").lower()
