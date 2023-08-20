# import speech_recognition as sr
# import pyttsx3
# from config import api_key
# import openai
# openai.api_key = api_key


# # class speech:
# #     def __init(self, txt):
# #         while txt != "stop":
# #             print("\nListening ....... ")
# #             r = sr.Recognizer()
# #             with sr.Microphone() as source:
# #                 r.pause_threshold = 0.5
# #                 audio = r.listen(source)
# #                 txt = r.recognize_google(audio, language="en-in")
# #                 print(f"User says {txt}")

# #             speak(txt)
    
# # def speak(string,voice_id = 1):
# #     engine = pyttsx3.init()
# #     voices = engine.getProperty('voices')
# #     engine.setProperty('voice', voices[voice_id].id)
# #     engine.setProperty('rate', 190) # adjust the speaking rate
# #     engine.setProperty('volume', 0.9) # adjust the speaking volume
# #     engine.say(string)
# #     engine.runAndWait()


# # class user_input:
# #     def __init__(self):
# #         chance = 0
# #         try:
# #             print("\nSelect the type of input : \n1. Text\n2. Voice\n")
# #             user_choice = input("Your Choice : ")
# #             if((user_choice[0]).lower() == "t"):
# #                 print("text os chosen")
# #             elif((user_choice[0]).lower() == 'v'):
# #                 s = speak("start")
# #             else:
# #                 print("INvalid INput")
# #                 chance += 1
# #                 if(chance>3):
# #                     print("No more tries")
# #                     exit()
# #         except Exception as e:
# #             print("INvalid INput")

# class processing:
#     def __init__(self,text, option):
#         response = openai.Completion.create(
#             model = "text-curie-001",
#             # engine="davinci",
#             prompt=text,
#             max_tokens=200,
#             top_p = 1,
#             # n=1,
#             # stop=None,
#             temperature=0.7,
#             frequency_penalty = 0,
#             presence_penalty = 0
#         )   
#         output = response.choices[0].text.strip()
        
#         if(option == 1):
#             speak(output)
#         elif(option == 2):
#             print(output)
#             print(output)        
        
# class speech:
#     def __init__(self):
#         while True:
#             print("\nListening ....... ")
#             r = sr.Recognizer()
#             with sr.Microphone() as source:
#                 r.pause_threshold = 0.5
#                 r.energy_threshold = 4000
#                 audio = r.listen(source)
#                 txt = r.recognize_google(audio, language="en-in")
#                 print(f"User says {txt}")
#                 if txt == "stop":
#                     break
#                 # speak(txt)
#                 process = processing(txt,1)


# class texting:
#     def __init__(self):
#         while True:
#             user = input("Prompt : ")
#             print(f"User prompt : {user}")
#             if user == "stop" or user == "shut up":
#                 break
#             process = processing(user,2)


# def speak(string, voice_id=1):
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[voice_id].id)
#     engine.setProperty('rate', 190) # adjust the speaking rate
#     engine.setProperty('volume', 0.9) # adjust the speaking volume
#     engine.say(string)
#     engine.runAndWait()

# class user_input:
#     def __init__(self):
#         chance = 0
#         try:
#             print("\nSelect the type of input : \n1. Text\n2. Voice\n")
#             user_choice = input("Your Choice : ")
#             if((user_choice[0]).lower() == "t"):
#                 t = texting()
#             elif((user_choice[0]).lower() == 'v'):
#                 s = speech()
#             else:
#                 print("Invalid Input")
#                 chance += 1
#                 if(chance>3):
#                     print("No more tries")
#                     exit()
#         except Exception as e:
#             print("Invalid Input")



# # def speak(string, voice_id=1):
# #     engine = pyttsx3.init()
# #     voices = engine.getProperty('voices')
# #     engine.setProperty('voice', voices[voice_id].id)
# #     engine.setProperty('rate', 190) # adjust the speaking rate
# #     engine.setProperty('volume', 0.9) # adjust the speaking volume
# #     engine.say(string)
# #     engine.runAndWait()



# # def takecommand():
# #     r = sr.Recognizer()
# #     with sr.Microphone() as source:
# #         r.pause_threshold = 0.5
# #         audio = r.listen(source)
# #         txt = r.recognize_google(audio, language="en-in")
# #         print(f"Uer says {txt}")
# #         return txt

# # def process_speech():
# #     text = takecommand()
# #     response = openai.Completion.create(
# #         model = "text-curie-001",
# #         # engine="davinci",
# #         prompt=text,
# #         max_tokens=200,
# #         top_p = 1,
# #         # n=1,
# #         # stop=None,
# #         temperature=0.7,
# #         frequency_penalty = 0,
# #         presence_penalty = 0
# #     )
# #     output = response.choices[0].text.strip()
# #     print(output)
# #     speak(output)


# # class processing:
# #     def __init__(self, text, option, conversation_history):
# #         self.conversation_history = conversation_history
# #         if "last conversation" in text.lower():
# #             last_conversation = "\n".join(self.conversation_history[-6:])
# #             response = f"Here's a summary of our last conversation:\n{last_conversation}"
        
# #         elif ("your name" in text.lower()) or ("who are you" in text.lower()):
# #             response = f"I am {bot_name}, made by Saaniidhya"
# #         # elif any(word in text.lower() for word in happy):
# #         #     response = "It sounds like you're feeling happy! 😄"
# #         # elif any(word in text.lower() for word in sad):
# #         #     response = "I'm sorry to hear that you're feeling sad. 😔"
# #         else:
# #             if len(user_history) >= 3:
# #                 string = " ".join(user_history[-3:])
# #                 result = sentiment_analyzer(string)
# #                 label = result[0]['label']
# #                 score = result[0]['score']
# #                 print(f"Sentence: {string}")
# #                 print(f"Sentiment: {label}, Score: {score}\n")
# #                 if (label == "1 Star" or label == "2 Star"):
# #                     mood = "sad"
# #                 elif (label == "3 Star"):
# #                     mood = "neutral"
# #                 else:
# #                     mood = "happy"
# #                 response = ""
# #                 response += "\nHere's a playlist that might match your mood:\n"
# #                 response += get_playlist_name(mood)
                
# #             response = openai.Completion.create(
# #                 model="text-davinci-003",
# #                 prompt=text,
# #                 max_tokens=900,
# #                 top_p=1,
# #                 temperature=0.7,
# #                 frequency_penalty=0,
# #                 presence_penalty=0
# #             )
# #             response = response.choices[0].text.strip()

# #         # Append the user input here
# #         self.conversation_history.append(text)
# #         user_history.append(text)
# #         # Append the bot's response
# #         self.conversation_history.append(response)
# #         print(user_history)

# #         if option == 1:
# #             speak(response)
# #             print(response)
# #         elif option == 2:
# #             print(response)


# if __name__ == "__main__":
#     run = user_input()

# # process_speech()
# # speak("Hello Sir , I am Aura", voice_id=1)
# strings = ["hello", "heaven", "hero"]
# matched_strings = ""
# for chars in zip(*strings):
#     if all(c == chars[0] for c in chars):
#         matched_strings += chars[0]
#     else:
#         print("No match for characters:", chars)

# print(matched_strings)
