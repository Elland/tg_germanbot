from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import User
from Config import token
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token=token)
dispatcher = updater.dispatcher
print("running")


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="hi")


def joinAlert(bot, update):
    for member in update.message.new_chat_members:
        greeting(bot, update)

def greeting(bot, update):
    with open('greeting', 'r', encoding='utf-8') as greeting_file:
        greeting = greeting_file.read()
        bot.send_message(update.message.chat_id, text=greeting)

        
def rules(bot, update):
    with open('rules','r', encoding='utf-8') as rules_file:
        rules = rules_file.read()
        bot.send_message(update.message.chat_id, text=rules)


def report(bot, update):
    for entity in update.message.entities:
        if entity.type == 'mention':
           offset = entity.offset
           length = entity.length

           username = update.message.text[offset:offset+length]
           bot.send_message(update.message.chat_id, text=username + " ist in die Hölle geschickt worden!")


dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, joinAlert))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('rules', rules))
dispatcher.add_handler(CommandHandler('regel', rules))
dispatcher.add_handler(CommandHandler('greeting', greeting))
dispatcher.add_handler(CommandHandler('report', report))

updater.start_polling()
