import pyttsx3

engine = pyttsx3.init()

# Flag to check if the engine is currently speaking
is_speaking = False

def speak(text):
    global is_speaking
    if is_speaking:
        return  # Don't speak if the engine is already running
    is_speaking = True

    def on_end(name, completed):
        global is_speaking
        is_speaking = False

    engine.connect('finished-utterance', on_end)
    print("Guts:", text)
    engine.say(text)
    engine.runAndWait()
