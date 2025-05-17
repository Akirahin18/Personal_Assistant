import requests
import time
from core.voice import speak

def get_news():
    API_KEY = "YOUR NEW API"  # Replace with your key
    url = f"YOUR NEW API URL"

    try:
        response = requests.get(url)
        news_data = response.json()
        articles = news_data.get("articles", [])
        if not articles:
            speak("Sorry, I couldn't fetch the news.")
            return
        speak("Here are the top news headlines:")
        for i, article in enumerate(articles[:5], 1):
            speak(f"{i}. {article['title']}")
            time.sleep(1)
    except Exception:
        speak("There was an error retrieving the news.")
