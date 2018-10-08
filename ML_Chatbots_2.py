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

# respond to names
# Define find_name()
def find_name(message):
    name = None
    # Create a pattern for checking if the keywords occur
    name_keyword = re.compile('name|call')
    # Create a pattern for finding capitalized words
    name_pattern = re.compile('[A-Z]{1}[a-z]*')
    if name_keyword.search(message):
        # Get the matching words in the string
        name_words = name_pattern.findall(message)
        if len(name_words) > 0:
            # Return the name if the keywords are present
            name = ' '.join(name_words)
    return name

# Define respond()
def respond(message):
    # Find the name
    name = find_name(message)
    if name is None:
        return "Hi there!"
    else:
        return "Hello, {0}!".format(name)

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
send_message("my name is David Copperfield")
send_message("call me Ishmael")
send_message("People call me Cassandra")

# GloVe algorithm, which is a cousin of word2vec
import spacy
nlp = spacy.load('en')
nlp.vocab.vectors_length
doc = nlp('hello can you help me?')
for token in doc:
    print("{} : {}".format(token, token.vector[:3]))
# similarity:
# direction of vectors matters
# "Distance" between words = angle between the vectors
# Cosine similarity: 1 similar, -1 dissimilar
doc = nlp("cat")
doc.similarity(nlp("can"))
doc.similarity(nlp("dog"))

# e.g. create a 2D array X with as many rows as there are sentences in the dataset, where each row is a vector describing that sentence
sentences = [' i want to fly from boston at 838 am and arrive in denver at 1110 in the morning',
 ' what flights are available from pittsburgh to baltimore on thursday morning',
 ' what is the arrival time in san francisco for the 755 am flight leaving washington']
# Load the spacy model: nlp
nlp = spacy.load('en')
# Calculate the length of sentences
n_sentences = len(sentences)
# Calculate the dimensionality of nlp
embedding_dim = nlp.vocab.vectors_length
# Initialize the array with zeros: X
import numpy as np
X = np.zeros((n_sentences, embedding_dim))
# Iterate over the sentences
for idx, sentence in enumerate(sentences):
    # Pass each each sentence to the nlp object to create a document
    doc = nlp(sentence)
    # Save the document's .vector attribute to the corresponding row in X
    X[idx, :] = doc.vector
