# from transformers import pipeline

# sentiment_analyzer = pipeline('sentiment-analysis', model="nlptown/bert-base-multilingual-uncased-sentiment", framework="pt")


# sentences = {
#     "i had a rough day My boss scolded me",
#     "my day was okaishh",
#     "i won a prize today"
# }

# for i in sentences:
#     result = sentiment_analyzer(i)
#     label = result[0]['label']
#     score = result[0]['score']
#     print(f"Sentence: {i}")
#     print(f"Sentiment: {label}, Score: {score}\n")
import telebot
from config import TEL_API
import random
from emotions import greeting_list
# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = TEL_API

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello, I'm your simple Telegram bot!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    res = random.choice(greeting_list)
    bot.reply_to(message, res)

bot.polling()

