import webbrowser
import pyjokes
import pyttsx3
import pywhatkit
from core.voice import speak
from core.listen import get_input
engine = pyttsx3.init()

def tell_joke():
    return pyjokes.get_joke()

def open_website(command, mode):
    if "youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "google" in command:
        webbrowser.open("https://www.google.com")
    else:
        speak("Which website?")
        site = get_input(mode)
        engine.say(f'Opening {site}')
        webbrowser.open(f"https://{site}.com")

def play_song(command):
    try:
        song = command.split("play")[1].split("song")[0].strip().strip('"')
        speak(f"Playing {song} on Spotify.")
        pywhatkit.playonyt(song + " song spotify")
    except:
        speak("Couldn't find the song name.")
