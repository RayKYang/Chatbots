
# 1.a the simplest bot
bot_template = "BOT : {0}"
user_template = "USER : {0}"

def respond(message):
    return "I can hear you! you said: {}".format(message)

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

# Send a message to the bot
send_message("hello")

## 1.b(1) Small talk
responses = {
    "what's your name?": "my name is EchoBot",
    "what's the weather today?": "it's sunny!"
}

def respond(message):
    if message in responses:
        return responses[message]

respond("what's your name?")

# 1.b(2) including variables
responses = {
    "what's today's weather?": "it's {} today"
}

weather_today = "cloudy"

def respond(message):
    if message in responses:
        return responses[message].format(weather_today)

# 1.b(3) choosing responses:
responses = {
    "what's your name?": [
        "my name is EchoBot",
        "they call me EchoBot",
        "the name's Bot, Echo Bot"
    ]
}
import random
def respond(message):
    if message in responses:
        return random.choice(responses[message])

respond("what's your name?")

# 1.b(4) Asking questions
responses = ["tell me more!", "why do you think that?"]
import random
def respond(message):
    return random.choice(responses)

respond("I think you're really great")

import time
time.sleep(0.5)
