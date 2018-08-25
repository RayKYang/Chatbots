
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

# 1.b Small talk
responses = {
    "what's your name?": "my name is EchoBot",
    "what's the weather today?": "it's sunny!"
}

def respond(message):
    if message in responses:
        return responses[message]

respond("what's your name?")





import time
time.sleep(0.5)
