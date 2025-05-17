import time
from plyer import notification
from core.voice import speak
import json
import os

REMINDER_FILE = "reminders.json"

def load_reminders():
    global reminders
    if os.path.exists(REMINDER_FILE):
        with open(REMINDER_FILE, "r") as file:
            reminders_data = json.load(file)
            reminders = [tuple(r) for r in reminders_data]  # Convert each list to tuple
    else:
        reminders = []

def save_reminders():
    with open(REMINDER_FILE, "w") as file:
        json.dump(reminders, file)

def init_reminders():
    load_reminders()

def set_reminder(task, delay_sec):
    reminders.append((task, time.time() + delay_sec))
    save_reminders()
    speak(f"Reminder set for {task} in {delay_sec // 60} minutes.")

def check_reminders():
    current = time.time()
    for r in reminders[:]:
        task, alert_time = r
        if current >= alert_time:
            notification.notify(title="Reminder", message=task, timeout=10)
            speak(f"Reminder: {task}")
            reminders.remove(r)
            save_reminders()


# reminders = []

# def init_reminders():
#     global reminders
#     reminders = []

# def set_reminder(task, delay_sec):
#     reminders.append((task, time.time() + delay_sec))
#     speak(f"Reminder set for {task} in {delay_sec // 60} minutes.")

# def check_reminders():
#     current = time.time()
#     for r in reminders[:]:
#         task, alert_time = r
#         if current >= alert_time:
#             notification.notify(title="Reminder", message=task, timeout=10)
#             speak(f"Reminder: {task}")
#             reminders.remove(r)
