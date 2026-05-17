# Rule-Based AI Chatbot

## Overview

This project is a simple rule-based chatbot created for the DecodeLabs Artificial Intelligence Internship. The chatbot does not use any AI APIs or machine learning libraries. It responds by matching user input with predefined rules.

## Objective

The main objective of this project is to understand how a basic chatbot works using Python. It focuses on clean input handling, dictionary-based responses, fallback replies, and a loop that keeps the chatbot running until the user exits.

## Features

- Beginner-friendly Python code
- Predefined chatbot responses
- Greeting and help commands
- Exit commands: `bye`, `exit`, `quit`, and `goodbye`
- Continuous `while` loop
- Input sanitization using `lower().strip()`
- Dictionary/hash-map based responses
- Random response selection for variety
- Fallback response for unknown questions
- More than 10 useful intents

## Concepts Used

- Python functions
- Dictionaries
- Sets
- Conditional statements
- Loops
- User input with `input()`
- String cleaning
- `random.choice()`

## Folder Structure

```text
Project-01-Rule-Based-AI-Chatbot/
├── README.md
├── chatbot.py
├── requirements.txt
├── docs/
│   └── project_explanation.md
├── demo/
│   └── demo_transcript.txt
└── screenshots/
    └── .gitkeep
```

## How to Run

Make sure Python is installed on your system.

```bash
python chatbot.py
```

You can also run it from the root repository folder:

```bash
cd Project-01-Rule-Based-AI-Chatbot
python chatbot.py
```

## Example Conversation

```text
You: hello
DecodeBot: Hello! Welcome to the Rule-Based AI Chatbot.

You: what is ai
DecodeBot: AI means Artificial Intelligence. It is the field of making machines perform tasks that usually need human intelligence.

You: unknown question
DecodeBot: Sorry, I only understand predefined questions right now. Type 'help' for examples.

You: bye
DecodeBot: Goodbye! Thanks for chatting.
```

## What I Learned

Through this project, I learned how to build a basic chatbot using simple Python logic. I practiced using functions, dictionaries, loops, input cleaning, and fallback responses. I also learned why rule-based systems are useful for small and clearly defined tasks.

## Internship Info

- Company: DecodeLabs
- Domain: Artificial Intelligence
- Project: 1
- Batch: 2026
