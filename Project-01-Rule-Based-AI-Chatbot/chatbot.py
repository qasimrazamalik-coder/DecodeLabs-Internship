"""A simple rule-based chatbot for the DecodeLabs AI Internship."""

import difflib
import random


EXIT_COMMANDS = {"bye", "exit", "quit", "goodbye"}

RESPONSES = {
    "hello": [
        "Hello! Welcome to the Rule-Based AI Chatbot.",
        "Hi there! How can I help you today?",
        "Hey! Type 'help' to see what I can answer.",
    ],
    "hi": [
        "Hi! I am ready to chat.",
        "Hello! Ask me something about AI, Python, or this internship project.",
    ],
    "hey": [
        "Hey! Nice to meet you.",
        "Hey there! What would you like to know?",
    ],
    "what is your name": [
        "My name is DecodeBot.",
        "I am DecodeBot, a simple rule-based chatbot.",
    ],
    "your name": [
        "You can call me DecodeBot.",
        "I am DecodeBot.",
    ],
    "who are you": [
        "I am a beginner-friendly rule-based chatbot built in Python.",
        "I am a simple chatbot created for Project 1 of the DecodeLabs AI Internship.",
    ],
    "how are you": [
        "I am doing great and ready to answer your questions.",
        "I am running smoothly. Thanks for asking!",
    ],
    "what can you do": [
        "I can answer predefined questions about AI, Python, and this internship project.",
        "I can respond to simple commands using rules and dictionary lookups.",
    ],
    "what is ai": [
        "AI means Artificial Intelligence. It is the field of making machines perform tasks that usually need human intelligence.",
        "Artificial Intelligence is about building systems that can reason, learn, or make decisions in useful ways.",
    ],
    "what is artificial intelligence": [
        "Artificial Intelligence is a branch of computer science focused on creating smart systems.",
        "AI helps computers solve problems, understand data, and make decisions.",
    ],
    "what is python": [
        "Python is a popular programming language known for simple syntax and readability.",
        "Python is beginner-friendly and is widely used in AI, data science, automation, and web development.",
    ],
    "internship help": [
        "This internship has 4 tasks in total. Right now, Project 1 is the rule-based chatbot.",
        "For the DecodeLabs internship, complete each assigned project carefully and keep your repository clean.",
    ],
    "project help": [
        "Project 1 is about creating a simple rule-based chatbot with predefined responses.",
        "For this project, focus on input cleaning, dictionary-based responses, a loop, exit commands, and fallback handling.",
    ],
    "thanks": [
        "You're welcome!",
        "No problem. Happy to help!",
    ],
    "thank you": [
        "You're welcome!",
        "Glad I could help.",
    ],
    "help": [
        "menu",
    ],
    "menu": [
        "menu",
    ],
}

FALLBACK_RESPONSES = [
    "I do not have a response for that yet. Try typing 'help' to see my options.",
    "Sorry, I only understand predefined questions right now. Type 'help' for examples.",
    "I am still a simple rule-based bot. Please try another question from the menu.",
]

KEYWORD_SUGGESTIONS = {
    "ai": "Try asking: what is ai",
    "artificial": "Try asking: what is ai",
    "python": "Try asking: what is python",
    "internship": "Try asking: internship help",
    "task": "Try asking: project help",
    "project": "Try asking: project help",
    "name": "Try asking: what is your name",
}


def clean_text(text):
    """Clean user input so matching becomes easier."""
    return text.lower().strip()


def show_help():
    """Display example commands for the user."""
    print("\nYou can try these commands:")
    print("- hello")
    print("- what is your name")
    print("- who are you")
    print("- how are you")
    print("- what can you do")
    print("- what is ai")
    print("- what is python")
    print("- internship help")
    print("- project help")
    print("- thanks")
    print("- bye / exit / quit / goodbye")


def get_fallback_response(user_message):
    """Give a helpful fallback response with a suggested command."""
    possible_commands = list(RESPONSES.keys()) + list(EXIT_COMMANDS)
    close_matches = difflib.get_close_matches(
        user_message,
        possible_commands,
        n=1,
        cutoff=0.6,
    )

    if close_matches:
        return f"I did not understand that exactly. Did you mean '{close_matches[0]}'?"

    for keyword, suggestion in KEYWORD_SUGGESTIONS.items():
        if keyword in user_message:
            return f"I am not sure how to answer that exact question. {suggestion}."

    return f"{random.choice(FALLBACK_RESPONSES)} Example: 'what is ai' or 'help'."


def get_response(user_message):
    """Return a chatbot response based on predefined rules."""
    if user_message in RESPONSES:
        response = random.choice(RESPONSES[user_message])

        if response == "menu":
            show_help()
            return "Choose any command from the list above."

        return response

    return get_fallback_response(user_message)


def main():
    """Run the chatbot until the user enters an exit command."""
    print("Welcome to DecodeBot!")
    print("This is a simple rule-based AI chatbot.")
    print("Type 'help' to see example commands or 'bye' to exit.")

    while True:
        user_input = input("\nYou: ")
        user_message = clean_text(user_input)

        if not user_message:
            print("DecodeBot: Please type something so I can respond.")
            continue

        if user_message in EXIT_COMMANDS:
            print("DecodeBot: Goodbye! Thanks for chatting.")
            break

        bot_response = get_response(user_message)
        print(f"DecodeBot: {bot_response}")


if __name__ == "__main__":
    main()
