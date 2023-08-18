# import speech_recognition as sr
# import pyttsx3
# from config import api_key, CLIENT_ID, REDIRECT_URI, CLIENT_SECRET, TEL_API
# import openai
# openai.api_key = api_key
# from engine import speak, get_playlist_name
# from emotions import happy, sad, greeting_list, response_greet, stop_words, stop_response
# import requests
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# from transformers import pipeline
# import random
# import telebot



# user_history = []
# conversation_history = []
# bot_name = "Aura"
# sentiment_analyzer = pipeline('sentiment-analysis', model="nlptown/bert-base-multilingual-uncased-sentiment", framework="pt")

# # Replace 'YOUR_TOKEN' with your actual bot token
# TOKEN = TEL_API

# bot = telebot.TeleBot(TOKEN)
# global response
# response = " "

# class processing:
#     def __init__(self, text, conversation_history, message):
#         self.conversation_history = conversation_history
#         response = " "  # Initialize response here
#         if "last conversation" in text.lower():
#             last_conversation = "\n".join(self.conversation_history[-6:])
#             response = f"Here's a summary of our last conversation:\n{last_conversation}"
#         elif ("your name" in text.lower()) or ("who are you" in text.lower()):
#             response = f"\nI am {bot_name}, made by Saaniidhya"
#         elif any(greet in text.lower() for greet in greeting_list):
#             response += random.choice(response_greet)
#         # elif (any(stop in text.lower()) for stop in stop_words):
#         #     response += random.choice(stop_response)
#         else:
#             if len(user_history) >= 5:
#                 string = " ".join(user_history[-5:])
#                 result = sentiment_analyzer(string)
#                 label = result[0]['label']
#                 score = result[0]['score']
#                 print(f"Sentence: {string}")
#                 print(f"Sentiment: {label}, Score: {score}\n")
#                 if label == "1 star" or label == "2 stars":
#                     mood = "sad"
#                 elif label == "3 stars":
#                     mood = "neutral"
#                 else:
#                     mood = "happy"
#                 response += "\nHere's a playlist that might match your mood:\n"
#                 response += get_playlist_name(mood)
#             else:
#                 response = openai.Completion.create(
#                     model="text-davinci-003",
#                     prompt=text,
#                     max_tokens=900,
#                     top_p=1,
#                     temperature=0.7,
#                     frequency_penalty=0,
#                     presence_penalty=0
#                 )
#                 response = response.choices[0].text.strip()
#         self.conversation_history.append(text)
#         user_history.append(text)
#         self.conversation_history.append(response)
#         self.send_telegram_message(message, response)

#     def send_telegram_message(self, message, response):
#         bot.reply_to(message, response)



# class texting:
#     def __init__(self, conversation_history):
#         @bot.message_handler(commands=['start'])
#         def start(message):
#             bot.reply_to(message, "Hello, I'm your simple Telegram bot!")
#         # print("Hey there !! How're you ?")
#         self.conversation_history = conversation_history
#         while True:
#             user = input("Prompt : ")
#             print(f"User prompt : {user}")
#             @bot.message_handler(func=lambda message: True)
#             def echo(message):
#                 bot.reply_to(message, "Hello, World!")
#             # if user == "stop" or user == "shut up":
#             #     break
#             conversation_history.append(user)
#             process = processing(user,2,conversation_history)



# @bot.message_handler(commands=['start'])
# def start(message):
#     response = " "
#     response += random.choice(response_greet)
#     bot.reply_to(message, response)

# @bot.message_handler(func=lambda message: True)
# def message_handler(message):
#     user_message = message.text
#     conversation_history.append(user_history)
#     process = processing(user_message, conversation_history, message)

# if __name__ == "__main__":
#     bot.polling()
###################################################################################################################

# import speech_recognition as sr
# import pyttsx3
# from config import api_key, CLIENT_ID, REDIRECT_URI, CLIENT_SECRET, TEL_API
# import openai
# openai.api_key = api_key
# from engine import speak, get_playlist_name
# from emotions import happy, sad, greeting_list, response_greet, stop_words, stop_response
# import requests
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# from transformers import pipeline
# import random
# import telebot
# import uuid

# user_history = []
# conversation_history = {}
# user_id_collection = []
# bot_name = "Aura"
# sentiment_analyzer = pipeline('sentiment-analysis', model="nlptown/bert-base-multilingual-uncased-sentiment", framework="pt")

# # Replace 'YOUR_TOKEN' with your actual bot token
# TOKEN = TEL_API

# bot = telebot.TeleBot(TOKEN)
# global response
# response = " "

# class processing:
#     def __init__(self, text, conversation_history, message, user_id):
#         self.conversation_history = conversation_history
#         response = " "  # Initialize response here
#         if "last conversation" in text.lower():
#             last_conversation = "\n".join(self.conversation_history[-6:])
#             response = f"Here's a summary of our last conversation:\n{last_conversation}"
#         elif ("your name" in text.lower()) or ("who are you" in text.lower()):
#             response = f"\nI am {bot_name}, made by Saaniidhya"
#         elif any(greet in text.lower() for greet in greeting_list):
#             response += random.choice(response_greet)
#         # elif (any(stop in text.lower()) for stop in stop_words):
#         #     response += random.choice(stop_response)
#         else:
#             if len(user_history) >= 5:
#                 string = " ".join(user_history[-5:])
#                 result = sentiment_analyzer(string)
#                 label = result[0]['label']
#                 score = result[0]['score']
#                 print(f"Sentence: {string}")
#                 print(f"Sentiment: {label}, Score: {score}\n")
#                 if label == "1 star" or label == "2 stars":
#                     mood = "sad"
#                 elif label == "3 stars":
#                     mood = "neutral"
#                 else:
#                     mood = "happy"
#                 response += "\nHere's a playlist that might match your mood:\n"
#                 response += get_playlist_name(mood)
#             else:
#                 response = openai.Completion.create(
#                     model="text-davinci-003",
#                     prompt=text,
#                     max_tokens=900,
#                     top_p=1,
#                     temperature=0.7,
#                     frequency_penalty=0,
#                     presence_penalty=0
#                 )
#                 response = response.choices[0].text.strip()
#         conversation_history[user_id] += f"\n {text}\n"
#         user_history.append(text)
#         # self.conversation_history.append(response)
#         self.send_telegram_message(message, response)

#     def send_telegram_message(self, message, response):
#         bot.reply_to(message, response)


# @bot.message_handler(commands=['start'])
# def start(message):
#     user_id = message.chat.id
#     response = f"\n Id: {user_id} \n"
#     response += random.choice(response_greet)
#     bot.reply_to(message, response)

# @bot.message_handler(commands=['stop'])
# def start(message):
#     user_id = message.chat.id
#     response = f"\n Id: {user_id} \n"
#     response += random.choice(stop_response)
#     bot.reply_to(message, response)
#     exit()

# @bot.message_handler(func=lambda message: True)
# def message_handler(message):
#     user_message = message.text
#     user_id = message.chat.id
#     if user_id not in user_id_collection:
#         user_id_collection.append(user_id)
#         conversation_history[user_id] = user_message
#         user_history.clear()
#         process = processing(user_message, conversation_history, message, user_id)
#     else:
#         process = processing(user_message, conversation_history, message, user_id)

# if __name__ == "__main__":
#     bot.polling()


import speech_recognition as sr
import pyttsx3
from config import api_key, CLIENT_ID, REDIRECT_URI, CLIENT_SECRET, TEL_API
import openai
openai.api_key = api_key
from engine import speak, get_playlist_name
from emotions import happy, sad, greeting_list, response_greet, stop_words, stop_response
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from transformers import pipeline
import random
import telebot
import uuid

# Dictionary to store user conversation history
conversation_history = {}
user_id_collection = []

user_history_key = 'user_history'
user_id_key = 'user_id'

bot_name = "Aura"
sentiment_analyzer = pipeline('sentiment-analysis', model="nlptown/bert-base-multilingual-uncased-sentiment", framework="pt")

# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = TEL_API

bot = telebot.TeleBot(TOKEN)
global response
response = " "

class processing:
    def __init__(self, text, conversation_history, message, user_id):
        self.conversation_history = conversation_history
        response = " "  # Initialize response here
        if "last conversation" in text.lower():
            last_conversation = "\n".join(self.conversation_history[user_id][user_history_key][-6:])
            response = f"Here's a summary of our last conversation:\n{last_conversation}"
        elif ("your name" in text.lower()) or ("who are you" in text.lower()):
            response = f"\nI am {bot_name}, made by Saaniidhya"
        elif any(greet in text.lower() for greet in greeting_list):
            response += random.choice(response_greet)
        # elif (any(stop in text.lower()) for stop in stop_words):
        #     response += random.choice(stop_response)
        else:
            user_history = self.conversation_history[user_id][user_history_key]
            if len(user_history) >= 5:
                string = " ".join(user_history[-5:])
                result = sentiment_analyzer(string)
                label = result[0]['label']
                score = result[0]['score']
                print(f"Sentence: {string}")
                print(f"Sentiment: {label}, Score: {score}\n")
                if label == "1 star" or label == "2 stars":
                    mood = "sad"
                elif label == "3 stars":
                    mood = "neutral"
                else:
                    mood = "happy"
                response += "\nHere's a playlist that might match your mood:\n"
                response += get_playlist_name(mood)
            else:
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=text,
                    max_tokens=900,
                    top_p=1,
                    temperature=0.7,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                response = response.choices[0].text.strip()
        self.conversation_history[user_id][user_history_key].append(text)
        self.send_telegram_message(message, response)

    def send_telegram_message(self, message, response):
        bot.reply_to(message, response)


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    user_id_collection.append(user_id)  # Add user ID to the collection
    conversation_history[user_id] = {
        user_history_key: [],
        user_id_key: user_id,
    }
    response = f"\n Id: {user_id} \n"
    response += random.choice(response_greet)
    bot.reply_to(message, response)

@bot.message_handler(commands=['stop'])
def start(message):
    user_id = message.chat.id
    response = f"\n Id: {user_id} \n"
    response += random.choice(stop_response)
    bot.reply_to(message, response)
    exit()

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    user_message = message.text
    user_id = message.chat.id
    if user_id not in user_id_collection:
        # New user, start fresh history
        start(message)
    user_history = conversation_history[user_id][user_history_key]
    process = processing(user_message, conversation_history, message, user_id)

if __name__ == "__main__":
    bot.polling()
