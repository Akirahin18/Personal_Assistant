from core.voice import speak
from core.listen import get_input
from modules import calculator, time_date, weather, location, news, reminder, search, entertainment
from modules import ai_chat
# from modules.ai_chat import respond
import json
import os

history_file = "command_history.json"

# Initialize the history list by loading from the file if it exists
def load_history():
    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            return json.load(file)
    return []

# Function to log the command to the JSON file
def log_command(command):
    history.append(command)
    with open(history_file, "w") as file:
        json.dump(history, file)

# Initialize the history variable
history = load_history()

mode = "voice"  # Default to voice mode

def main():
    global mode
    speak("Hello! I'm Guts! How can I help you today?")
    reminder.init_reminders()

    while True:
        reminder.check_reminders()
        command = get_input(mode=mode)

        if not command:
            continue

        command = command.lower()

        if "text" in command:
            mode = "text"
            speak("Switched to text mode. You can type your commands now.")
            continue

        elif "voice mode" in command:
            mode = "voice"
            speak("Switched to voice mode. You can speak your commands now.")
            continue

        elif "time" in command:
            speak(f"The time is {time_date.get_time()}")

        elif "date" in command:
            speak(f"Today's date is {time_date.get_date()}")

        elif "weather" in command:
            speak("Which city?")
            city = get_input(mode)
            if city:
                report = weather.get_weather(city)
                speak(report)
            else:
                speak("Sorry, I didn't catch the city name.")

        elif "location" in command:
            speak(location.get_location())

        elif "news" in command or 'headlines' in command:
            news.get_news()

        elif "remind me" in command:
            speak("What should I remind you about?")
            task = get_input(mode)
            speak("In how many minutes?")
            try:
                minutes = int(get_input(mode))
                reminder.set_reminder(task, minutes * 60)
            except (ValueError, TypeError):
                speak("Sorry, I couldn't set the reminder. Please provide a valid number.")

        elif "search" in command or "wikipedia" in command:
            topic = command.replace("wikipedia", "").replace("search", "").strip()
            if not topic:
                speak("What do you want to search?")
                topic = get_input(mode)
            search.detailed_search(topic)

        elif "joke" in command:
            speak(entertainment.tell_joke())

        elif "play" in command:
            entertainment.play_song(command)

        elif "open" in command:
            entertainment.open_website(command,mode)

        elif "calculate" in command or "calculation" in command:
            calculator.handle_calculation(mode)

        elif "exit" in command or "stop" in command:
            speak("Thanks for using me, Have a nice day! Goodbye!")
            break
        
        elif "chat" in command or "talk" in command:
            speak("I am ready to chat with you!")
            while True:
                user_input = get_input(mode)
                if user_input.lower() in ["exit", "stop", "quit"]:
                    speak("Ending chat. Let me know if you need anything else.")
                    break
                print("You said:", user_input)  # Debug
                response = ai_chat.respond(user_input)
                print("Gut says:", response)    # Debug
                speak(response)

        else:
            speak("Searching or trying to understand...")
            search.detailed_search(command)

        log_command(command)
        
if __name__ == "__main__":
    main()
