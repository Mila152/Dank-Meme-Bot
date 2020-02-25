import telebot
import config
import random
from telebot import types
import urllib.request
import json

url = config.URL
#"https://node-meme-api-private.herokuapp.com"
#"https://python-telegram-bot-wceve.run-us-west2.goorm.io"
bot = telebot.TeleBot(config.TOKEN)

#/start
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    #keyboard
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton("Random")
    # item1 = types.KeyboardButton("Dank")
    # item3 = types.KeyboardButton("Normie")
    # markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "BaReV GeGeTsKuXi` <b>{0.first_name}</b>\neS <b>{1.first_name}</b> XoRkUrI gAnDn eM!!!\n\n<i>commands:</i>\n/start return the start page\n/dank return a dank meme\n/normie return a normie meme\n/any return any random meme\n/furry return a furry meme\n<del>/it return an IT related meme |not working|</del>\n/edgy return edgy meme\n/wholesome return a wholesome meme\n/christian return a christian meme\n/art return an art meme\n/history return a history meme\n/anime return anime meme\n/4chan return a 4chan meme\n".format(message.from_user, bot.get_me()), parse_mode='html') #, reply_markup=markup

#/dank
@bot.message_handler(commands=['dank'])
def dank(message):    
    contents = urllib.request.urlopen(url+"/dank").read()
    contents = contents.decode('utf8') #bytes to str
    contents = json.loads(contents) #to JSON
    bot.send_photo(chat_id=message.chat.id, photo=contents["meme"])
    
#/normie
@bot.message_handler(commands=['normie'])
def normie(message):    
    contents = urllib.request.urlopen(url+"/normie").read()
    contents = contents.decode('utf8') #bytes to str
    contents = json.loads(contents) #to JSON
    bot.send_photo(chat_id=message.chat.id, photo=contents["meme"])
        
#/any
@bot.message_handler(commands=['any'])
def moderate(message):    
    contents = urllib.request.urlopen(url+"/moderate").read()
    contents = contents.decode('utf8') #bytes to str
    contents = json.loads(contents) #to JSON
    bot.send_photo(chat_id=message.chat.id, photo=contents["meme"])
    
#/furry
@bot.message_handler(commands=['furry'])
def furry(message):    
    contents = urllib.request.urlopen(url+"/furry").read()
    contents = contents.decode('utf8') #bytes to str
    contents = json.loads(contents) #to JSON
    bot.send_photo(chat_id=message.chat.id, photo=contents["meme"])
    
#/it
@bot.message_handler(commands=['it'])
def it(message):    
    contents = urllib.request.urlopen(url+"/it").read()
    contents = contents.decode('utf8') #bytes to str
    contents = json.loads(contents) #to JSON
    bot.send_photo(chat_id=message.chat.id, photo=contents["meme"])
    
#/edgy
@bot.message_handler(commands=['edgy'])
def edgy(message):    
    contents = urllib.request.urlopen(url+"/edgy").read()
    contents = contents.decode('utf8') #bytes to str
    contents = json.loads(contents) #to JSON
    bot.send_photo(chat_id=message.chat.id, photo=contents["meme"])
    
#/wholesome
@bot.message_handler(commands=['wholesome'])
def wholesome(message):    
    contents = urllib.request.urlopen(url+"/wholesome").read()
    contents = contents.decode('utf8') #bytes to str
    contents = json.loads(contents) #to JSON
    bot.send_photo(chat_id=message.chat.id, photo=contents["meme"])
    
#/christian
@bot.message_handler(commands=['christian'])
def christian(message):    
    contents = urllib.request.urlopen(url+"/christian").read()
    contents = contents.decode('utf8') #bytes to str
    contents = json.loads(contents) #to JSON
    bot.send_photo(chat_id=message.chat.id, photo=contents["meme"])
    
#/art
@bot.message_handler(commands=['art'])
def art(message):    
    contents = urllib.request.urlopen(url+"/art").read()
    contents = contents.decode('utf8') #bytes to str
    contents = json.loads(contents) #to JSON
    bot.send_photo(chat_id=message.chat.id, photo=contents["meme"])
    
#/history
@bot.message_handler(commands=['history'])
def history(message):    
    contents = urllib.request.urlopen(url+"/history").read()
    contents = contents.decode('utf8') #bytes to str
    contents = json.loads(contents) #to JSON
    bot.send_photo(chat_id=message.chat.id, photo=contents["meme"])
    
#/anime
@bot.message_handler(commands=['anime'])
def anime(message):    
    contents = urllib.request.urlopen(url+"/anime").read()
    contents = contents.decode('utf8') #bytes to str
    contents = json.loads(contents) #to JSON
    bot.send_photo(chat_id=message.chat.id, photo=contents["meme"])
    
#/4chan
@bot.message_handler(commands=['4chan'])
def fourchan(message):    
    contents = urllib.request.urlopen(url+"/fourchan").read()
    contents = contents.decode('utf8') #bytes to str
    contents = json.loads(contents) #to JSON
    bot.send_photo(chat_id=message.chat.id, photo=contents["meme"])

#text    
@bot.message_handler(content_types=['text'])
def handlerfunc(message):
    if message.chat.type == 'private':
        if message.text == 'Random':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == 'Fuck you':
            bot.send_message(message.chat.id, "<b>Fuck you {0.first_name}!!!</b>".format(message.from_user, bot.get_me()), parse_mode='html')
        elif message.text == 'I love you':
            bot.send_message(message.chat.id, "".format(message.from_user, bot.get_me()), parse_mode='html')
        else:
            bot.send_message(message.chat.id, message.text)
            
#documents
@bot.message_handler(content_types=['document', 'sticker', 'photo', 'voice', 'video', 'audio'])
def dochandler(message):
    sti = open('static/funny.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "LooooooL".format(message.from_user, bot.get_me()), parse_mode='html')

#RUN
bot.polling(none_stop=True)
