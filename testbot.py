from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
#######################################  Bot  #####################################################
def start(bot, update):
    update.message.reply_text(main_menu_message(),
                              reply_markup = main_menu_keyboard())

def main_menu(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id = query.message.chat_id,
                          message_id = query.message.message_id,
                          text = main_menu_message(),
                          reply_markup = main_menu_keyboard())

def opt1(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id = query.message.chat_id,
                          message_id = query.message.message_id,
                          text = opt1_message(),
                          reply_markup = opt1_keyboard())

def opt2(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id = query.message.chat_id,
                          message_id = query.message.message_id,
                          text = opt2_message(),
                          reply_markup = opt2_keyboard())
def opt3(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id = query.message.chat_id,
                          message_id = query.message.message_id,
                          text = opt3_message(),
                          reply_markup = opt3_keyboard())
def opt1_1(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id = query.message.chat_id,
                          message_id = query.message.message_id,
                          text = opt1_1_message(),
                          reply_markup = back_in_main_keyboard())

def opt1_2(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id = query.message.chat_id,
                          message_id = query.message.message_id,
                          text = opt1_1_message(),
                          reply_markup = back_in_main_keyboard())

#######################################  KeyBoards  ###############################################
def main_menu_keyboard():
    keyboards = [
        [InlineKeyboardButton('opt1', callback_data = 'opt1')],
        [InlineKeyboardButton('opt2', callback_data = 'opt2')],
        [InlineKeyboardButton('opt3', callback_data = 'opt3')]
    ]
    return InlineKeyboardMarkup(keyboards)

def opt1_keyboard():
    keyboards = [
        [InlineKeyboardButton('opt1_1', callback_data='opt1_1')],
        [InlineKeyboardButton('opt1_2', callback_data='opt1_2')],
        [InlineKeyboardButton('main menu', callback_data='main')]
    ]
    return InlineKeyboardMarkup(keyboards)

def opt2_keyboard():
    keyboards = [
        [InlineKeyboardButton('opt2_1', callback_data = 'opt2_1')],
        [InlineKeyboardButton('opt2_2', callback_data = 'opt2_2')],
        [InlineKeyboardButton('main menu', callback_data = 'main')]
    ]
    return InlineKeyboardMarkup(keyboards)

def opt3_keyboard():
    keyboards = [
        [InlineKeyboardButton('opt3_1', callback_data = 'opt3_1')],
        [InlineKeyboardButton('opt3_2', callback_data = 'opt3_2')],
        [InlineKeyboardButton('main menu', callback_data = 'main')]
    ]
    return InlineKeyboardMarkup(keyboards)

def back_in_main_keyboard():
    keyboards = [
        [InlineKeyboardButton('main menu', callback_data = 'main')]
    ]
    return InlineKeyboardMarkup(keyboards)
#######################################  Messages  ################################################
def main_menu_message():
    return 'The main menu, choose one command: '
def opt1_message():
    return 'The Option 1, choose one command:'
def opt2_message():
    return 'The Option 2, choose one command: '
def opt3_message():
    return 'The Option 3, choose one command: '
def opt1_1_message():
    return 'Opt1_1'
def opt1_2_message():
    return 'Opt1_2'

#######################################  Hendler  #################################################
token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
# request_kwargs = {
#     'proxy_url':'socks5h://207.97.174.134:1080'
# }
updater = Updater(token)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern = 'main'))
updater.dispatcher.add_handler(CallbackQueryHandler(opt1, pattern = 'opt1'))
updater.dispatcher.add_handler(CallbackQueryHandler(opt2, pattern = 'opt2'))
updater.dispatcher.add_handler(CallbackQueryHandler(opt3, pattern = 'opt3'))
updater.dispatcher.add_handler(CallbackQueryHandler(opt1_1, pattern = 'opt1_1'))
updater.dispatcher.add_handler(CallbackQueryHandler(opt1_2, pattern = 'opt1_2'))
updater.start_polling()


#######################################  Logger  ##################################################
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)