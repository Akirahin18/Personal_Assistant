from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import os

# Optional: Remove database file to retrain from scratch
if not os.path.exists("db.sqlite3"):
    print("Training from scratch...")

# Create the chatbot
chatbot = ChatBot(
    "Guts",
    read_only=True,  # Set to False if you want it to learn in runtime
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        }
    ],
    database_uri='sqlite:///db.sqlite3'
)

# Train if not already trained
def train_bot():
    corpus_trainer = ChatterBotCorpusTrainer(chatbot)
    corpus_trainer.train("chatterbot.corpus.english")

    list_trainer = ListTrainer(chatbot)

    # Custom conversations
    custom_conversations = [
        [
            "Hi",
            "Hello! How can I help you today?"
        ],
        [
            "What is your name?",
            "I am Guts, your personal assistant."
        ],
        [
            "What can you do?",
            "I can tell time, give weather updates, set reminders, and more!"
        ],
        [
            "Tell me a joke",
            "Why don't robots get tired? Because they recharge!"
        ],
        [
            "Bye",
            "Goodbye! Have a great day!"
        ]
    ]

    for conv in custom_conversations:
        list_trainer.train(conv)

# Respond to a user message
def respond(text: str) -> str:
    try:
        response = chatbot.get_response(text)
        return str(response)
    except Exception as e:
        return "Oops, I had trouble understanding that."

# Train the bot once (if needed)
if not os.path.exists("db.sqlite3"):
    train_bot()
