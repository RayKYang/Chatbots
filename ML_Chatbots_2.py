# Understanding Intent and Entities
# NER Named Entity Recognition
# Use Regular Expression to recognize intents and entities
import re
re.search(r"(hello|hey|hi)", "hey there!") is not None
re.search(r"(hello|hey|hi)", "which one?") is not None
re.search(r"\b(hello|hey|hi)\b", "hey there!") is not None
re.search(r"\b(hello|hey|hi)\b", "which one?") is not None

pattern = re.compile('[A-Z]{1}[a-z]*')
message = """
Mary is a fiend of mine, 
she studied at Oxford and
now works at Google"""
pattern.findall(message) # find all capitalized words

# The keywords dictionary for identifying intent
keywords = {'thankyou': ['thank', 'thx'], 'greet': ['hello', 'hi', 'hey'], 'goodbye': ['bye', 'farewell']}
patterns = {}
# Iterate over the keywords dictionary
for intent, keys in keywords.items():
    # Create regular expressions and compile them into pattern objects
    patterns[intent] = re.compile('|'.join(keys))
# Print the patterns
print(patterns)

responses = {'default': 'default message',
             'goodbye': 'goodbye for now',
               'greet': 'Hello you! :)',
            'thankyou': 'you are very welcome'}

# Define a function to find the intent of a message
def match_intent(message):
    matched_intent = None
    for intent, pattern in patterns.items():
        # Check if the pattern occurs in the message
        if pattern.search(message):
            matched_intent = intent
    return matched_intent

# Define a respond function
def respond(message):
    # Call the match_intent function
    intent = match_intent(message)
    # Fall back to the default response
    key = "default"
    if intent in responses:
        key = intent
    return responses[key]

bot_template = "BOT : {0}"
user_template = "USER : {0}"
# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

# Send messages
send_message("hello!")
send_message("bye byeee")
send_message("thanks very much!")