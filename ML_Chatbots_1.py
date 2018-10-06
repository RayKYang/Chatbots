
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
# add default
# Define variables
name = "Greg"
weather = "cloudy"
# Define a dictionary with the predefined responses
responses = {
  "what's your name?": "my name is {0}".format(name),
  "what's today's weather?": "the weather is {0}".format(weather),
  "default": "default message"
}
# Return the matching response if there is one, default otherwise
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return the matching message
        bot_message = responses[message]
    else:
        # Return the "default" message
        bot_message = responses["default"]
    return bot_message

# 1.b(3) choosing responses randomly:
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

# a fuller example
import random
name = "Greg"
weather = "cloudy"
# Define a dictionary containing a list of responses for each message
responses = {
  "what's your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "what's today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ],
  "default": ["default message"]
}
# Use random.choice() to choose a matching response
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return a random matching response
        bot_message = random.choice(responses[message])
    else:
        # Return a random "default" response
        bot_message = random.choice(responses["default"])
    return bot_message

# 1.b(4) Asking questions
responses = ["tell me more!", "why do you think that?"]
import random
def respond(message):
    return random.choice(responses)
respond("I think you're really great")

# a fuller example
responses = {'question': ["I don't know :(", 'you tell me!'],
 'statement': ['tell me more!',
  'why do you think that?',
  'how long have you felt this way?',
  'I find that extremely interesting',
  'can you back that up?',
  'oh wow!',
  ':)']}
import random
def respond(message):
    # Check for a question mark
    if message.endswith("?"):
        # Return a random question
        return random.choice(responses["question"])
    # Return a random statement
    return random.choice(responses["statement"])


# add delay
import time
time.sleep(0.5)
