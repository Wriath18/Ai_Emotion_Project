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


# import speech_recognition as sr
# import pyttsx3
from config import api_key, CLIENT_ID, REDIRECT_URI, CLIENT_SECRET, TEL_API, API_TOKEN
import openai
openai.api_key = api_key
from engine import get_playlist_name
from emotions import happy, sad, greeting_list, response_greet, stop_response, stop_words, song_refr
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from transformers import pipeline
import random
import telebot
import traceback
import requests


# API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
# headers = {"Authorization": f"Bearer {API_TOKEN}"}
# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()["generated_text"]
# # Dictionary to store user conversation history
conversation_history = {}
user_id_collection = []

user_history_key = 'user_history'
user_id_key = 'user_id'

bot_name = "Aura"
sentiment_analyzer = pipeline('sentiment-analysis', model="nlptown/bert-base-multilingual-uncased-sentiment", framework="pt")
welcome_message = "PLEASE READ BEFORE STARTING\n\nHey there !! This is Aura, an Ai Emotion based song recommendation system.🎶\n\nThings to know\n\n1️⃣ Your chat is always engrypted🔒\n\n2️⃣ Do not share any personal information in the chat🚫\n\n3️⃣ Aura needs atleast 5 statements/Inputs from you to analyse your mood\n\n4️⃣ When you type /stop, the chat gets deleted and refreshed\n\n 5️⃣ No more rules, Enjoyyy😎\n"
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
            response = f"\nI am {bot_name}, made by Sanidhya"
        # elif (any(greet in text.lower()) for greet in greeting_list):
        #     response += random.choice(response_greet)
        # elif (any(stop in text.lower()) for stop in stop_words):
        #     response += random.choice(stop_response)
        elif any(statement in text for statement in song_refr):
            self.song_recommend(message, user_id, response)
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

    def song_recommend(self, message, user_id, response):
        bot.reply_to(message, "Sure, Let's get straight to the business")
        user_history = self.conversation_history[user_id][user_history_key]
        if len(user_history) >= 3:
            string = " ".join(user_history[-3:])
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
            bot.reply_to(message, "Sure, let's get straight to the business.")
            bot.send_message(user_id, "To recommend a song, I'll need to know a bit more about your mood and song preferences.")
            bot.send_message(user_id, "Could you please tell me how you're feeling right now? For example, happy, sad, or neutral.")
            bot.register_next_step_handler(message, self.get_mood)

    def get_mood(self, message):
        mood = message.text.lower()
        bot.send_message(message.chat.id, f"Got it, you're feeling {mood}.")
        bot.send_message(message.chat.id, "Next, could you let me know the type of song you'd like? For example, upbeat, relaxing, energetic, etc.")
        bot.register_next_step_handler(message, self.get_song_type, mood)

    def get_song_type(self, message, mood):
        song_type = message.text
        bot.send_message(message.chat.id, f"Thank you! You're looking for a {song_type} song.")
        # Now you can call the get_playlist_name function with the mood and song_type
        playlist_name = get_playlist_name(mood)  # You need to modify this to use the actual function
        bot.send_message(message.chat.id, f"Based on your mood and preference, I recommend the playlist: {playlist_name}")


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    user_id_collection.append(user_id)  # Add user ID to the collection
    try:
        conversation_history[user_id] = {
            user_history_key: [],
            user_id_key: user_id,
        }
        response = f"\n Id: {user_id} \n"
        response += random.choice(response_greet)
        bot.send_message(user_id, welcome_message)
        bot.reply_to(message, response)

    except Exception as e:
        print(f"An error occured {e}")
        bot.send_message(user_id, "Sorry, Something went wrong !! \n\nPlease write /stop and then /start to continue with new session")

@bot.message_handler(commands=['stop'])
def start(message):
    user_id = message.chat.id
    try:
        response = f"\n Id: {user_id} \n"
        response += random.choice(stop_response)
        bot.reply_to(message, response)
        if user_id in conversation_history:
            del conversation_history[user_id]
    
    except Exception as e:
        print(f"An error occured {e}")
        bot.send_message(user_id, "Sorry, Something went wrong !! \n\nPlease write /stop and then /start to continue with new session")

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    user_message = message.text
    user_id = message.chat.id
    try:
        if user_id not in user_id_collection:
            # New user, start fresh history
            start(message)
        user_history = conversation_history[user_id][user_history_key]
        process = processing(user_message, conversation_history, message, user_id)
    except Exception as e:
        print(f"An error occured {e}")
        bot.send_message(user_id, "Sorry, Something went wrong !! \n\nPlease write /stop and then /start to continue with new session")

@bot.message_handler(commands=['feedback'])
def feedback(message):
    user_id = message.chat.id
    bot.reply_to(user_id, "Please provide your feedback:")
    bot.register_next_step_handler(message, process_feedback)

def process_feedback(message):
    user_id = message.chat.id
    feedback_text = message.text
    # Send the feedback to a designated channel or user (replace CHAT_ID with the actual ID)
    feedback_channel_id = 'aura_feedbacks'  # Replace with your channel ID
    bot.send_message(feedback_channel_id, f"Feedback from user {user_id}:\n{feedback_text}")
    
    # Notify the user that their feedback has been received
    bot.send_message(user_id, "Thank you for your feedback!")
    if user_id in conversation_history:
        del conversation_history[user_id]


if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"An error occurred while polling: {e}")
        traceback.print_exc()
