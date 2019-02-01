#!/usr/bin/env/ python3

import telebot
import sys
from secrets import *
from twtools import api_init, get_url, get_id
from datetime import datetime

# Starting telegram api
bot = telebot.TeleBot(bot_token)

# Starting twitter api
ttapi = api_init()

# Default messages
messages = {
    'start' : ('Welcome to tweetToMp4, use /help for instructions about usage,'
                + ' /about for information about this project, or just send me'
                + ' a tweet url already.'),
    'help' : ('Send me a video tweet url, like https://twitter.com/foo/status/XXXXXX,'
                + ' and I\'ll reply you with it\'s media, so you can download it. Use'
                + ' /about for information about this project, or /donate to donate.'),
    'about' : ('tweetToMp4 was developed by v0idpwn (https://v0idpwn.github.io) and Junior Bona'
                + ' take a look at our repo: https://github.com/v0idpwn/tweetToMp4'),
    'donate' : ('Buy me a coffe! https://ko-fi.com/v0idpwn')
}

# Logger
def write_to_log(username, status):
    log = open(sys.path[0]+"/logfile.txt", "a+")
    log.write((str(datetime.now()) + " - " + username + ' ' + status + '\n'))
    log.close()


# Command handlers
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, messages['start'])

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, messages['help'])

@bot.message_handler(commands=['about'])
def send_welcome(message):
    bot.reply_to(message, messages['about'])

@bot.message_handler(commands=['donate'])
def send_welcome(message):
    bot.reply_to(message, messages['donate'])


# Default message handler
@bot.message_handler()
def at_answer(message):
    twid = get_id(message.text)
    response = get_url(ttapi, twid)
    bot.reply_to(message, '{}'.format(response))
    status = 'Success' if response[0:6] != 'Error:' else 'Error'
    write_to_log(message.from_user.username, status)


# Polling, yay!
bot.polling(none_stop=True, interval=0, timeout=20)
