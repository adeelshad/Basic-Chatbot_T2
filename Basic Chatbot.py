import nltk
import random
import string
import re

# Download NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Preprocessing functions
def preprocess_input(user_input):
    # Lowercase the input
    user_input = user_input.lower()
    # Remove punctuation
    user_input = re.sub(f'[{string.punctuation}]', '', user_input)
    return user_input

# Define a simple set of responses
responses = {
    "hello": ["Hi there!", "Hello!", "Greetings!", "How can I help you?"],
    "how are you": ["I'm just a computer program, but thanks for asking!", "Doing well, how about you?", "I'm here to assist you!"],
    "what is your name": ["I'm a chatbot created to assist you.", "You can call me Chatbot.", "I'm just a simple chatbot."],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
}

# Function to get a response
def get_response(user_input):
    user_input = preprocess_input(user_input)
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    return "I'm sorry, I don't understand that."

# Main loop for the chatbot
def chat():
    print("Chatbot: Hello! How can I assist you today? (Type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
if __name__ == "__main__":
    chat()