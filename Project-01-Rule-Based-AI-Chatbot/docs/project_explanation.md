# Project Explanation

## What Is a Rule-Based Chatbot?

A rule-based chatbot is a chatbot that gives answers based on fixed rules. It does not learn from data like a machine learning model. Instead, the developer writes possible user inputs and connects them to predefined responses.

For example, if the user types `hello`, the chatbot can reply with a greeting. If the user types `what is ai`, the chatbot can return a short explanation about Artificial Intelligence.

## Input Sanitization With `lower().strip()`

Input sanitization means cleaning the user's message before using it in the program. In this project, the chatbot uses:

```python
text.lower().strip()
```

`lower()` converts the message to lowercase, so `Hello`, `HELLO`, and `hello` can be treated the same way. `strip()` removes extra spaces from the start and end of the message.

This makes the chatbot easier to use because the user does not have to type every command perfectly.

## Dictionary-Based Responses

The chatbot stores responses in a Python dictionary. A dictionary stores data as key-value pairs. In this project, the key is the user message and the value is a list of possible responses.

This makes it easy to find a response:

```python
RESPONSES["hello"]
```

The chatbot also uses `random.choice()` so it can choose one response from a list and feel less repetitive.

## Why Dictionary Lookup Is Cleaner Than a Long `if-elif` Ladder

A chatbot can be written with many `if`, `elif`, and `else` conditions, but that becomes hard to read when the number of intents increases.

Using a dictionary is cleaner because all predefined messages are stored in one place. It is easier to add a new intent by adding another key and response list. The main response function also stays short and simple.

## Continuous Loop

The chatbot uses a `while True` loop so it keeps running after each user message. This allows the user to have a conversation instead of running the program again for every question.

The loop continues until the user enters an exit command.

## Exit Strategy

The chatbot has clear exit commands:

- `bye`
- `exit`
- `quit`
- `goodbye`

When the cleaned user message matches one of these commands, the chatbot prints a goodbye message and uses `break` to stop the loop.

## Fallback Response

A fallback response is used when the chatbot does not understand the user's message. Instead of crashing or staying silent, it politely tells the user to try a supported command.

In this project, the fallback method is a little more helpful than a simple random message. If the user types something close to a supported command, the chatbot suggests the closest command. If the message contains a useful keyword like `ai`, `python`, `internship`, or `project`, the chatbot suggests a related command.

This makes the chatbot more user-friendly and keeps the program stable.
