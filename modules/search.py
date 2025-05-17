import wikipedia
import pywhatkit
from core.voice import speak

def detailed_search(query):
    try:
        result = wikipedia.summary(query, sentences=3)
        speak(result)
    except:
        speak("Couldn't find a detailed answer. Searching the web...")
        pywhatkit.search(query)
