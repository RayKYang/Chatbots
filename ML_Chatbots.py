
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

# text munging with regular expressions
rules = {'I want (.*)': ['What would it mean if you got {0}',
  'Why do you want {0}',
  "What's stopping you from getting {0}"],
 'do you remember (.*)': ['Did you think I would forget {0}',
  "Why haven't you been able to forget {0}",
  'What about {0}',
  'Yes .. and?'],
 'do you think (.*)': ['if {0}? Absolutely.', 'No chance'],
 'if (.*)': ["Do you really think it's likely that {0}",
  'Do you wish that {0}',
  'What do you think about {0}',
  'Really--if {0}']}
import re # regular expression 
def match_rule(rules, message):
    response, phrase = "default", None
    
    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    return response, phrase

# Test match_rule
print(match_rule(rules, "do you remember your last birthday"))

# Define replace_pronouns()
def replace_pronouns(message):
    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub("me", "you", message)
    if 'my' in message:
        return re.sub("my", "your", message)
    if 'your' in message:
        return re.sub("your", "my", message)
    if 'you' in message:
        return re.sub("you", "me", message)
    return message

print(replace_pronouns("my last birthday"))
print(replace_pronouns("when you went to Florida"))
print(replace_pronouns("I had my own castle"))

# response by integrating match_rule(), send_message(), replace_pronouns()
# Define respond()
def respond(message):
    # Call match_rule
    response, phrase = match_rule(rules, message)
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    return response

# Send the messages
send_message("do you remember your last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")

# add delay
import time
time.sleep(0.5)
