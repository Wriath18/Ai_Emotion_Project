import speech_recognition as sr
import pyttsx3
from config import api_key, CLIENT_ID, REDIRECT_URI, CLIENT_SECRET
import openai
openai.api_key = api_key
from engine import speak, get_playlist_name
from emotions import happy, sad, greeting_list, response_greet, stop_words, stop_response
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from transformers import pipeline
import random

user_history = []
conversation_history = []
bot_name = "Aura"
sentiment_analyzer = pipeline('sentiment-analysis', model="nlptown/bert-base-multilingual-uncased-sentiment", framework="pt")

class processing:
    def __init__(self, text, option, conversation_history):
        self.conversation_history = conversation_history
        response = " "
        if "last conversation" in text.lower():
            last_conversation = "\n".join(self.conversation_history[-6:])
            response = f"Here's a summary of our last conversation:\n{last_conversation}"
        elif ("your name" in text.lower()) or ("who are you" in text.lower()):
            response = f"I am an Ai bot, {bot_name}"
        elif (any(greet in text.lower() for greet in greeting_list)):
            response += random.choice(response_greet)
        elif (any(stop in text.lower()) for stop in stop_words):
            response += random.choice(stop_response)
            print(response)
            exit()
        else:
            if len(user_history) >= 5:
                string = " ".join(user_history[-5:])
                result = sentiment_analyzer(string)
                label = result[0]['label']
                score = result[0]['score']
                print(f"Sentence: {string}")
                print(f"Sentiment: {label}, Score: {score}\n")
                if (label == "1 star" or label == "2 stars"):
                    mood = "sad"
                elif (label == "3 stars"):
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
        self.conversation_history.append(text)
        user_history.append(text)
        self.conversation_history.append(response)
        print(user_history)

        if option == 1:
            speak(response)
            print(response)
        elif option == 2:
            print(response)


class speech:
    def __init__(self, conversation_history):
        print("Hey there !! How're you ?")
        self.conversation_history = conversation_history
        while True:
            print(f"\n{bot_name}'s Listening ....... ")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.pause_threshold = 0.5
                r.energy_threshold = 4000
                audio = r.listen(source)
                txt = r.recognize_google(audio, language="en-in")
                conversation_history.append(txt)
                print(f"User says {txt}")
                # if txt == "stop":
                #     break
                # speak(txt)
                process = processing(txt,1,conversation_history)


class texting:
    def __init__(self, conversation_history):
        print("Hey there !! How're you ?")
        self.conversation_history = conversation_history
        while True:
            user = input("Prompt : ")
            print(f"User prompt : {user}")
            # if user == "stop" or user == "shut up":
            #     break
            conversation_history.append(user)
            process = processing(user,2,conversation_history)




class user_input:
    def __init__(self, conversation_history):
        chance = 0
        # try:
        print("Have a little conversation with Aura and make sure you converse atleast 5 points\n")
        print("\nSelect the type of input : \n1. Text\n2. Voice\n")
        user_choice = input("Your Choice : ")
        if((user_choice[0]).lower() == "t"):
            t = texting(conversation_history)
        elif((user_choice[0]).lower() == 'v'):
            s = speech(conversation_history)
        else:
            print("Invalid Input")
            chance += 1
            if(chance>3):
                print("No more tries")
                exit()
        # except Exception as e:
        #     print("Invalid Input")

if __name__ == "__main__":
    run = user_input(conversation_history)
    

# import speech_recognition as sr
# import pyttsx3
# from config import api_key, CLIENT_ID, REDIRECT_URI, CLIENT_SECRET, TEL_API
# import openai
# openai.api_key = api_key
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# from engine import speak, get_playlist_name
# from emotions import happy, sad, greeting_list, response_greet, stop_words, stop_response
# import requests
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# from transformers import pipeline
# import random

# user_history = []
# conversation_history = []
# bot_name = "Aura"
# sentiment_analyzer = pipeline('sentiment-analysis', model="nlptown/bert-base-multilingual-uncased-sentiment", framework="pt")


# class YourTelegramBot:
#     def __init__(self, token):
#         self.token = token
#         self.updater = Updater(token=self.token, use_context=True)
#         self.dispatcher = self.updater.dispatcher
#         self.conversation_history = []
#         self.bot_name = "Aura"
#         self.sentiment_analyzer = pipeline('sentiment-analysis', model="nlptown/bert-base-multilingual-uncased-sentiment", framework="pt")

#         self.register_handlers()

#     def start(self, update: Update, context: CallbackContext) -> None:
#         update.message.reply_text("Hey there! How're you?")

#     def text_handler(self, update: Update, context: CallbackContext) -> None:
#         user_input = update.message.text
#         self.process_input(user_input, update)

#     def process_input(self, user_input, update):
#         # Modify your processing logic here
#         # ...
#         response = processing(user_input, 1, self.conversation_history)
#         self.conversation_history.append(user_input)
#         self.conversation_history.append(response)

#         # Send the response back to the user
#         update.message.reply_text(response)

#     def run(self):
#         self.updater.start_polling()
#         self.updater.idle()

#     def register_handlers(self):
#         self.dispatcher.add_handler(CommandHandler("start", self.start))
#         self.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.text_handler))

# if __name__ == "__main__":
#     # Replace 'YOUR_BOT_TOKEN' with your actual bot token
#     bot = YourTelegramBot(token=TEL_API)
#     bot.run()


# class processing:
#     def __init__(self, text, option, conversation_history):
#         self.conversation_history = conversation_history
#         response = " "
#         if "last conversation" in text.lower():
#             last_conversation = "\n".join(self.conversation_history[-6:])
#             response = f"Here's a summary of our last conversation:\n{last_conversation}"
#         elif ("your name" in text.lower()) or ("who are you" in text.lower()):
#             response = f"I am {bot_name}, made by Saaniidhya"
#         elif (any(greet in text.lower() for greet in greeting_list)):
#             response += random.choice(response_greet)
#         # elif (any(stop in text.lower()) for stop in stop_words):
#         #     response += random.choice(stop_response)
#         #     print(response)
#         #     exit()
#         else:
#             if len(user_history) >= 5:
#                 string = " ".join(user_history[-5:])
#                 result = sentiment_analyzer(string)
#                 label = result[0]['label']
#                 score = result[0]['score']
#                 print(f"Sentence: {string}")
#                 print(f"Sentiment: {label}, Score: {score}\n")
#                 if (label == "1 star" or label == "2 stars"):
#                     mood = "sad"
#                 elif (label == "3 stars"):
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
#         print(user_history)

#         if option == 1:
#             speak(response)
#             print(response)
#         elif option == 2:
#             print(response)


# class speech:
#     def __init__(self, conversation_history):
#         print("Hey there !! How're you ?")
#         self.conversation_history = conversation_history
#         while True:
#             print(f"\n{bot_name}'s Listening ....... ")
#             r = sr.Recognizer()
#             with sr.Microphone() as source:
#                 r.pause_threshold = 0.5
#                 r.energy_threshold = 4000
#                 audio = r.listen(source)
#                 txt = r.recognize_google(audio, language="en-in")
#                 conversation_history.append(txt)
#                 print(f"User says {txt}")
#                 # if txt == "stop":
#                 #     break
#                 # speak(txt)
#                 process = processing(txt,1,conversation_history)


# class texting:
#     def __init__(self, conversation_history):
#         print("Hey there !! How're you ?")
#         self.conversation_history = conversation_history
#         while True:
#             user = input("Prompt : ")
#             print(f"User prompt : {user}")
#             # if user == "stop" or user == "shut up":
#             #     break
#             conversation_history.append(user)
#             process = processing(user,2,conversation_history)




# class user_input:
#     def __init__(self, conversation_history):
#         chance = 0
#         # try:
#         print("\nSelect the type of input : \n1. Text\n2. Voice\n")
#         user_choice = input("Your Choice : ")
#         if((user_choice[0]).lower() == "t"):
#             t = texting(conversation_history)
#         elif((user_choice[0]).lower() == 'v'):
#             s = speech(conversation_history)
#         else:
#             print("Invalid Input")
#             chance += 1
#             if(chance>3):
#                 print("No more tries")
#                 exit()
#         # except Exception as e:
#         #     print("Invalid Input")

# if __name__ == "__main__":
#     run = user_input(conversation_history)
    

# import speech_recognition as sr
# import pyttsx3
# from config import api_key, CLIENT_ID, REDIRECT_URI, CLIENT_SECRET
# import openai
# openai.api_key = api_key
# from engine import speak, get_playlist_name
# from emotions import happy, sad, greeting_list, response_greet, stop_words, stop_response
# import requests
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# from transformers import pipeline
# import random

# user_history = []
# conversation_history = []
# bot_name = "Aura"
# sentiment_analyzer = pipeline('sentiment-analysis', model="nlptown/bert-base-multilingual-uncased-sentiment", framework="pt")

# class processing:
#     def __init__(self, text, option, conversation_history):
#         self.conversation_history = conversation_history
#         response = " "
#         if "last conversation" in text.lower():
#             last_conversation = "\n".join(self.conversation_history[-6:])
#             response = f"Here's a summary of our last conversation:\n{last_conversation}"
#         elif ("your name" in text.lower()) or ("who are you" in text.lower()):
#             response = f"I am {bot_name}, made by Saaniidhya"
#         elif (any(greet in text.lower() for greet in greeting_list)):
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
#                 if (label == "1 star" or label == "2 stars"):
#                     mood = "sad"
#                 elif (label == "3 stars"):
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
#         print(user_history)

#         if option == 1:
#             speak(response)
#             print(response)
#         elif option == 2:
#             print(response)


# class speech:
#     def __init__(self, conversation_history):
#         print("Hey there !! How're you ?")
#         self.conversation_history = conversation_history
#         while True:
#             print(f"\n{bot_name}'s Listening ....... ")
#             r = sr.Recognizer()
#             with sr.Microphone() as source:
#                 r.pause_threshold = 0.5
#                 r.energy_threshold = 4000
#                 audio = r.listen(source)
#                 txt = r.recognize_google(audio, language="en-in")
#                 conversation_history.append(txt)
#                 print(f"User says {txt}")
#                 # if txt == "stop":
#                 #     break
#                 # speak(txt)
#                 process = processing(txt,1,conversation_history)


# class texting:
#     def __init__(self, conversation_history):
#         print("Hey there !! How're you ?")
#         self.conversation_history = conversation_history
#         while True:
#             user = input("Prompt : ")
#             print(f"User prompt : {user}")
#             # if user == "stop" or user == "shut up":
#             #     break
#             conversation_history.append(user)
#             process = processing(user,2,conversation_history)




# class user_input:
#     def __init__(self, conversation_history):
#         chance = 0
#         # try:
#         print("\nSelect the type of input : \n1. Text\n2. Voice\n")
#         user_choice = input("Your Choice : ")
#         if((user_choice[0]).lower() == "t"):
#             t = texting(conversation_history)
#         elif((user_choice[0]).lower() == 'v'):
#             s = speech(conversation_history)
#         else:
#             print("Invalid Input")
#             chance += 1
#             if(chance>3):
#                 print("No more tries")
#                 exit()
#         # except Exception as e:
#         #     print("Invalid Input")

# if __name__ == "__main__":
#     run = user_input(conversation_history)
    


