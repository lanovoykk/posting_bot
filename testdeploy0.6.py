import telebot
from telebot import types
import requests
import logging
import config
import datetime
import time


bot = telebot.TeleBot(config.TOKEN)

#logger = telebot.logger
#telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.


user_dict = {}

class User:
    def __init__(self, sale_date):
        self.sale_date = sale_date
        self.channel_name = None
        self.channel_link = None

        self.channel_link_check_1 = None
        self.channel_link_check_2 = None
        self.channel_link_check_3 = None
        self.channel_link_check_4 = None
        self.channel_link_check_5 = None
        self.channel_link_check_6 = None
        self.channel_link_check_7 = None
        self.channel_link_check_8 = None
        self.channel_link_check_9 = None
        self.channel_link_check_10 = None
        self.channel_link_check_11 = None
        self.channel_link_check_12 = None
        self.channel_link_check_13 = None
        self.channel_link_check_14 = None
        self.channel_link_check_15 = None

        self.add_or_continue_1 = None
        self.add_or_continue_2 = None
        self.add_or_continue_3 = None
        self.add_or_continue_4 = None
        self.add_or_continue_5 = None
        self.add_or_continue_6 = None

        self.channel_name_2 = None
        self.channel_name_3 = None
        self.channel_name_4 = None
        self.channel_name_5 = None
        self.channel_name_6 = None

        self.channel_link_2 = None
        self.channel_link_3 = None
        self.channel_link_4 = None
        self.channel_link_5 = None
        self.channel_link_6 = None

        self.temat = None
        self.ordinary_price = None
        self.sale_price = None
        self.terms = None
        self.ads_amount = None
        self.comment = None
        self.admin_username = None

        self.date_1 = None
        self.date_2 = None




id_list_subscripted = [594166069, 1277294648]

id_list_3_posts = []

id_list_1_post = []



# Handle '/start' command
@bot.message_handler(commands=['start'])
def start_command(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Создать пост')
        markup.add(itembtn1)

        msg = bot.send_message(message.chat.id, 'Здравствуйте, '
        + message.from_user.first_name + '. ' + "Нажмите на кнопку <b>'Создать пост'</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)

    except Exception as e:
        msg = bot.send_message(message.chat.id, 'Упс... Что-то пошло не так')
        msg = bot.send_message(message.chat.id, 'Здравствуйте, '
        + message.from_user.first_name + '. ' + "Нажмите на кнопку <b>'Создать пост'</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)
        bot.register_next_step_handler(start_command)
        return




# Handle '/help' command
@bot.message_handler(commands=['help'])
def help_command(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Создать пост')
        markup.add(itembtn1)

        bot.send_message(message.chat.id, "Этот бот создан для публикации постов в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML')
        bot.send_message(message.chat.id, "Нажмите на кнопку <b>'Создать пост'</b> или введите комманду /start для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)
    except Exception as e:
        msg = bot.send_message(message.chat.id, 'Упс... Что-то пошло не так')
        msg = bot.send_message(message.chat.id, "Этот бот создан для публикации постов в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML')
        msg = bot.send_message(message.chat.id, "Нажмите на кнопку <b>'Создать пост'</b> или введите комманду /start для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)
        bot.register_next_step_handler(msg, help_command)
        return




# Handle 'Создать пост'
@bot.message_handler(content_types=['text'])
def start_conversation(message):
    try:
        if message.text == 'Создать пост':

            markup_cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Отмена')
            markup_cancel.add(itembtn1)

            if message.chat.id in id_list_subscripted:
                msg = bot.send_message(message.chat.id, 'Введите дату вашего горящего места. Можно ввести несколько дат сразу через запятую. Например: 14.07, 15.07', reply_markup=markup_cancel)
                bot.register_next_step_handler(msg, process_sale_date)
            else:
                bot.send_message(message.chat.id, 'У вас нет доступа к функционалу бота. Чтобы оплатить подписку, пишите @teledvizhadm')
                return

        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup.add(itembtn1)

            msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
            msg = bot.send_message(message.chat.id, "Нажмите на кнопку <b>'Создать пост'</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)
            return

    except Exception as e:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Создать пост')
        markup.add(itembtn1)

        msg = bot.reply_to(message, 'Упс... Что-то пошло не так')
        msg = bot.send_message(message.chat.id, "Нажмите на кнопку <b>'Создать пост'</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)
        bot.register_next_step_handler(msg, start_conversation_2)
        return


def process_sale_date(message):

    try:
        chat_id = message.chat.id
        sale_date = message.text
        user = User(sale_date)
        user_dict[chat_id] = user

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        markup.add(itembtn1, itembtn2)

        if message.text == 'Отмена':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>'Создать пост'</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)


        elif message.text == 'Назад':
            msg = bot.send_message(chat_id, 'Введите дату вашего горящего места. Можно ввести несколько дат сразу через запятую. Например: 14.07, 15.07', reply_markup=markup)
            bot.register_next_step_handler(msg, process_sale_date_2)
            return


        else:
            msg = bot.send_message(chat_id, 'Введите название вашего канала', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_name)

    except Exception as e:
        msg = bot.reply_to(message, 'Упс... Что-то пошло не так')
        msg = bot.send_message(chat_id, 'Введите дату вашего горящего места. Можно ввести несколько дат сразу через запятую. Например: 14.07, 15.07')
        bot.register_next_step_handler(msg, process_sale_date)
        return


def process_channel_name(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        channel_name = message.text
        user.channel_name = channel_name

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        markup.add(itembtn1, itembtn2)

        user.date_1 = datetime.date.today()

        if message.text == 'Отмена':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>'Создать пост'</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':
            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Введите дату вашего горящего места. Можно ввести несколько дат сразу через запятую. Например: 14.07, 15.07', reply_markup=markup)
            bot.register_next_step_handler(msg, process_sale_date_2)
            return

        else:
            msg = bot.send_message(chat_id, "Введите ссылку на ваш канал в t.me/ формате. Например: t.me/durov", disable_web_page_preview=True)
            bot.register_next_step_handler(msg, process_channel_link)

    except Exception as e:
        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Введите название вашего канала')
        bot.register_next_step_handler(msg, process_channel_name)
        return




def process_channel_link(message):

    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.channel_link = message.text


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Добавить канал')
    itembtn2 = types.KeyboardButton('Продолжить')
    itembtn3 = types.KeyboardButton('Назад')
    itembtn4 = types.KeyboardButton('Отмена')

    markup.row(itembtn2)
    markup.row(itembtn1)
    markup.row(itembtn3, itembtn4)

    if message.text == 'Отмена':
        markup_add = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Создать пост')
        markup_add.add(itembtn1)

        msg = bot.send_message(chat_id, 'Вы отменили создание поста')
        msg = bot.send_message(chat_id, "Нажмите на кнопку <b>'Создать пост'</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup_add, disable_web_page_preview=True)
        bot.register_next_step_handler(msg, start_conversation_2)

    elif message.text == 'Назад':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        markup.add(itembtn1, itembtn2)

        msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
        msg = bot.send_message(chat_id, 'Введите название вашего канала', reply_markup=markup)
        bot.register_next_step_handler(msg, process_channel_name)
        return

    elif not message.text.startswith(('t.me/', 'https://t.me')):
        msg = bot.reply_to(message, "Ссылка на канал должна содержать t.me/. Например: t.me/durov", disable_web_page_preview=True)
        bot.register_next_step_handler(msg, process_channel_link)
        return



        #Проверка на наличие публикумегого каналa в базе данных (списке), если пользователь создает пост 2-й раз за день

    if user.date_1 != user.date_2:

        user.channel_link = message.text
        msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
        bot.register_next_step_handler(msg, process_add_or_continue_1)

    elif user.date_1 == user.date_2:

        if message.text == user.channel_link_check_1 or message.text == user.channel_link_check_2 or message.text == user.channel_link_check_3 or message.text == user.channel_link_check_4 or message.text == user.channel_link_check_5 or message.text == user.channel_link_check_6 or message.text == user.channel_link_check_7 or message.text == user.channel_link_check_8 or message.text == user.channel_link_check_9 or message.text == user.channel_link_check_10 or message.text == user.channel_link_check_11 or message.text == user.channel_link_check_12 or message.text == user.channel_link_check_13 or message.text == user.channel_link_check_14 or message.text == user.channel_link_check_15:
            msg = bot.send_message(chat_id, 'Вы уже публиковали данный канал сегодня. Запрещено публиковать два одинаковых канала за день, максимум - <b>один</b>. Выберите другой канал для публикации', parse_mode='HTML')
            msg = bot.send_message(chat_id, 'Введите название вашего канала')
            bot.register_next_step_handler(msg, process_channel_name)
            return

        else:
            user.channel_link = message.text
            msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_add_or_continue_1)




def process_add_or_continue_1(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]

        if message.text == 'Продолжить':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')
            markup.add(itembtn1, itembtn2)

            user.add_or_continue_1 = message.text
            msg = bot.send_message(chat_id, 'Введите тематику вашего канала', reply_markup=markup)
            bot.register_next_step_handler(msg, process_temat)


        elif message.text == 'Добавить канал':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')
            markup.add(itembtn1, itembtn2)

            user.add_or_continue_1 = message.text
            msg = bot.send_message(chat_id, 'Введите название вашего <b>второго канала</b>', parse_mode = 'HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_name_2)

        elif message.text == 'Отмена':
            markup_add = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup_add.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>«Создать пост»</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup_add, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')
            markup.add(itembtn1, itembtn2)

            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, "Введите ссылку на ваш канал в t.me/ формате. Например: t.me/durov", disable_web_page_preview=True, reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_link)
            return

        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Добавить канал')
            itembtn2 = types.KeyboardButton('Продолжить')
            itembtn3 = types.KeyboardButton('Назад')
            itembtn4 = types.KeyboardButton('Отмена')

            markup.row(itembtn2)
            markup.row(itembtn1)
            markup.row(itembtn3, itembtn4)

            msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
            msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_add_or_continue_1)
            return

    except Exception as e:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Добавить канал')
        itembtn2 = types.KeyboardButton('Продолжить')
        itembtn3 = types.KeyboardButton('Назад')
        itembtn4 = types.KeyboardButton('Отмена')

        markup.row(itembtn2)
        markup.row(itembtn1)
        markup.row(itembtn3, itembtn4)

        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
        bot.register_next_step_handler(msg, process_add_or_continue_1)
        return


def process_channel_name_2(message):
    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        markup.add(itembtn1, itembtn2)

        if message.text == 'Отмена':
            markup_add = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup_add.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>«Создать пост»</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup_add, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Добавить канал')
            itembtn2 = types.KeyboardButton('Продолжить')
            itembtn3 = types.KeyboardButton('Назад')
            itembtn4 = types.KeyboardButton('Отмена')

            markup.row(itembtn2)
            markup.row(itembtn1)
            markup.row(itembtn3, itembtn4)

            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_add_or_continue_1)
            return

        else:

            user.channel_name_2 = message.text
            msg = bot.send_message(chat_id, 'Введите линк на ваш <b>второй канал</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_link_2)

    except Exception as e:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        markup.add(itembtn1, itembtn2)

        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Введите название вашего <b>второго канала</b>', parse_mode = 'HTML', reply_markup=markup)
        bot.register_next_step_handler(msg, process_channel_name_2)
        return


def process_channel_link_2(message):
    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]

        if message.text == 'Отмена':
            markup_add = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup_add.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>«Создать пост»</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup_add, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')

            markup.row(itembtn1, itembtn2)

            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Введите название вашего <b>второго канала</b>', parse_mode = 'HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_name_2)
            return

        else:

            user.channel_link_2 = message.text

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Добавить канал')
            itembtn2 = types.KeyboardButton('Продолжить')
            itembtn3 = types.KeyboardButton('Назад')
            itembtn4 = types.KeyboardButton('Отмена')

            markup.row(itembtn2)
            markup.row(itembtn1)
            markup.row(itembtn3, itembtn4)

            msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_add_or_continue_2)

    except Exception as e:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        markup.add(itembtn1, itembtn2)

        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Введите линк на ваш <b>второй канал</b>', parse_mode='HTML', reply_markup=markup)
        bot.register_next_step_handler(msg, process_channel_link_2)
        return


def process_add_or_continue_2(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]

        if message.text == 'Продолжить':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')
            markup.add(itembtn1, itembtn2)

            user.add_or_continue_2 = message.text
            msg = bot.send_message(chat_id, 'Введите тематику ваших каналов', reply_markup=markup)
            bot.register_next_step_handler(msg, process_temat)

        elif message.text == 'Добавить канал':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')
            markup.add(itembtn1, itembtn2)

            user.add_or_continue_2 = message.text
            msg = bot.send_message(chat_id, 'Введите название вашего <b>третьего канала</b>', parse_mode = 'HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_name_3)


        elif message.text == 'Отмена':
            markup_add = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup_add.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>«Создать пост»</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup_add, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')
            markup.add(itembtn1, itembtn2)

            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Введите линк на ваш <b>второй канал</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_link_2)
            return

        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Добавить канал')
            itembtn2 = types.KeyboardButton('Продолжить')
            itembtn3 = types.KeyboardButton('Назад')
            itembtn4 = types.KeyboardButton('Отмена')

            markup.row(itembtn2)
            markup.row(itembtn1)
            markup.row(itembtn3, itembtn4)

            msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
            msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_add_or_continue_2)
            return

    except Exception as e:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Добавить канал')
        itembtn2 = types.KeyboardButton('Продолжить')
        itembtn3 = types.KeyboardButton('Назад')
        itembtn4 = types.KeyboardButton('Отмена')

        markup.row(itembtn2)
        markup.row(itembtn1)
        markup.row(itembtn3, itembtn4)

        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
        bot.register_next_step_handler(msg, process_add_or_continue_2)
        return


def process_channel_name_3(message):
    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        markup.add(itembtn1, itembtn2)

        if message.text == 'Отмена':
            markup_add = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup_add.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>«Создать пост»</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup_add, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Добавить канал')
            itembtn2 = types.KeyboardButton('Продолжить')
            itembtn3 = types.KeyboardButton('Назад')
            itembtn4 = types.KeyboardButton('Отмена')

            markup.row(itembtn2)
            markup.row(itembtn1)
            markup.row(itembtn3, itembtn4)

            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_add_or_continue_2)
            return

        else:

            user.channel_name_3 = message.text
            msg = bot.send_message(chat_id, 'Введите линк на ваш <b>третий канал</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_link_3)

    except Exception as e:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        markup.add(itembtn1, itembtn2)

        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Введите название вашего <b>третьего канала</b>', parse_mode = 'HTML', reply_markup=markup)
        bot.register_next_step_handler(msg, process_channel_name_3)
        return


def process_channel_link_3(message):
    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]


        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Добавить канал')
        itembtn2 = types.KeyboardButton('Продолжить')
        itembtn3 = types.KeyboardButton('Назад')
        itembtn4 = types.KeyboardButton('Отмена')
        markup.row(itembtn2)
        markup.row(itembtn1)
        markup.row(itembtn3, itembtn4)

        if message.text == 'Отмена':
            markup_add = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup_add.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>«Создать пост»</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup_add, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')

            markup.row(itembtn1, itembtn2)

            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Введите название вашего <b>третьего канала</b>', parse_mode = 'HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_name_3)
            return

        else:

            user.channel_link_3 = message.text
            msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_add_or_continue_3)

    except Exception as e:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        markup.add(itembtn1, itembtn2)

        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Введите линк на ваш <b>третий канал</b>', parse_mode='HTML', reply_markup=markup)
        bot.register_next_step_handler(msg, process_channel_link_3)
        return


def process_add_or_continue_3(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]

        if message.text == 'Продолжить':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')
            markup.add(itembtn1, itembtn2)

            user.add_or_continue_3 = message.text
            msg = bot.send_message(chat_id, 'Введите тематику ваших каналов', reply_markup=markup)
            bot.register_next_step_handler(msg, process_temat)

        elif message.text == 'Добавить канал':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')
            markup.add(itembtn1, itembtn2)

            user.add_or_continue_3 = message.text
            msg = bot.send_message(chat_id, 'Введите название вашего <b>четвертого канала</b>', parse_mode = 'HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_name_4)


        elif message.text == 'Отмена':
            markup_add = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup_add.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>«Создать пост»</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup_add, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')
            markup.add(itembtn1, itembtn2)

            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Введите линк на ваш <b>третий канал</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_link_3)
            return

        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Добавить канал')
            itembtn2 = types.KeyboardButton('Продолжить')
            itembtn3 = types.KeyboardButton('Назад')
            itembtn4 = types.KeyboardButton('Отмена')

            markup.row(itembtn2)
            markup.row(itembtn1)
            markup.row(itembtn3, itembtn4)

            msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
            msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_add_or_continue_3)
            return

    except Exception as e:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Добавить канал')
        itembtn2 = types.KeyboardButton('Продолжить')
        itembtn3 = types.KeyboardButton('Назад')
        itembtn4 = types.KeyboardButton('Отмена')

        markup.row(itembtn2)
        markup.row(itembtn1)
        markup.row(itembtn3, itembtn4)

        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
        bot.register_next_step_handler(msg, process_add_or_continue_3)
        return


def process_channel_name_4(message):
    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        markup.add(itembtn1, itembtn2)

        if message.text == 'Отмена':
            markup_add = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup_add.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>«Создать пост»</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup_add, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Добавить канал')
            itembtn2 = types.KeyboardButton('Продолжить')
            itembtn3 = types.KeyboardButton('Назад')
            itembtn4 = types.KeyboardButton('Отмена')

            markup.row(itembtn2)
            markup.row(itembtn1)
            markup.row(itembtn3, itembtn4)

            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_add_or_continue_3)
            return

        else:

            user.channel_name_4 = message.text
            msg = bot.send_message(chat_id, 'Введите линк на ваш <b>четвертый канал</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_link_4)

    except Exception as e:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        markup.add(itembtn1, itembtn2)

        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Введите название вашего <b>четвертого канала</b>', parse_mode = 'HTML', reply_markup=markup)
        bot.register_next_step_handler(msg, process_channel_name_4)
        return


def process_channel_link_4(message):
    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]


        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Добавить канал')
        itembtn2 = types.KeyboardButton('Продолжить')
        itembtn3 = types.KeyboardButton('Назад')
        itembtn4 = types.KeyboardButton('Отмена')
        markup.row(itembtn2)
        markup.row(itembtn1)
        markup.row(itembtn3, itembtn4)

        if message.text == 'Отмена':
            markup_add = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup_add.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>«Создать пост»</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup_add, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')

            markup.row(itembtn1, itembtn2)

            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Введите название вашего <b>четвертого канала</b>', parse_mode = 'HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_name_4)
            return

        else:

            user.channel_link_4 = message.text
            msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_add_or_continue_4)

    except Exception as e:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        markup.add(itembtn1, itembtn2)

        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Введите линк на ваш <b>четвертый канал</b>', parse_mode='HTML', reply_markup=markup)
        bot.register_next_step_handler(msg, process_channel_link_4)
        return

def process_add_or_continue_4(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]

        if message.text == 'Продолжить':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')
            markup.add(itembtn1, itembtn2)

            user.add_or_continue_4 = message.text
            msg = bot.send_message(chat_id, 'Введите тематику ваших каналов', reply_markup=markup)
            bot.register_next_step_handler(msg, process_temat)


        elif message.text == 'Добавить канал':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')
            markup.add(itembtn1, itembtn2)

            user.add_or_continue_4 = message.text
            msg = bot.send_message(chat_id, 'Введите название вашего <b>пятого канала</b>', parse_mode = 'HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_name_5)


        elif message.text == 'Отмена':
            markup_add = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup_add.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>«Создать пост»</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup_add, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')
            markup.add(itembtn1, itembtn2)

            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Введите линк на ваш <b>четвертый канал</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_link_4)
            return

        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Добавить канал')
            itembtn2 = types.KeyboardButton('Продолжить')
            itembtn3 = types.KeyboardButton('Назад')
            itembtn4 = types.KeyboardButton('Отмена')

            markup.row(itembtn2)
            markup.row(itembtn1)
            markup.row(itembtn3, itembtn4)

            msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
            msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_add_or_continue_4)
            return

    except Exception as e:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Добавить канал')
        itembtn2 = types.KeyboardButton('Продолжить')
        itembtn3 = types.KeyboardButton('Назад')
        itembtn4 = types.KeyboardButton('Отмена')

        markup.row(itembtn2)
        markup.row(itembtn1)
        markup.row(itembtn3, itembtn4)

        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
        bot.register_next_step_handler(msg, process_add_or_continue_4)
        return


def process_channel_name_5(message):
    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]


        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        markup.add(itembtn1, itembtn2)

        if message.text == 'Отмена':
            markup_add = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup_add.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>«Создать пост»</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup_add, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Добавить канал')
            itembtn2 = types.KeyboardButton('Продолжить')
            itembtn3 = types.KeyboardButton('Назад')
            itembtn4 = types.KeyboardButton('Отмена')

            markup.row(itembtn2)
            markup.row(itembtn1)
            markup.row(itembtn3, itembtn4)

            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_add_or_continue_4)
            return

        else:

            user.channel_name_5 = message.text
            msg = bot.send_message(chat_id, 'Введите линк на ваш <b>пятый канал</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_link_5)

    except Exception as e:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        markup.add(itembtn1, itembtn2)

        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Введите название вашего <b>пятого канала</b>', parse_mode = 'HTML', reply_markup=markup)
        bot.register_next_step_handler(msg, process_channel_name_5)
        return


def process_channel_link_5(message):
    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]


        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Добавить канал')
        itembtn2 = types.KeyboardButton('Продолжить')
        itembtn3 = types.KeyboardButton('Назад')
        itembtn4 = types.KeyboardButton('Отмена')
        markup.row(itembtn2)
        markup.row(itembtn1)
        markup.row(itembtn3, itembtn4)

        if message.text == 'Отмена':
            markup_add = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup_add.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>«Создать пост»</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup_add, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')

            markup.row(itembtn1, itembtn2)

            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Введите название вашего <b>пятого канала</b>', parse_mode = 'HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_name_5)
            return

        else:

            user.channel_link_5 = message.text
            msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_add_or_continue_5)

    except Exception as e:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        markup.add(itembtn1, itembtn2)

        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Введите линк на ваш <b>пятый канал</b>', parse_mode='HTML', reply_markup=markup)
        bot.register_next_step_handler(msg, process_channel_link_5)
        return


def process_add_or_continue_5(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]

        if message.text == 'Продолжить':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')
            markup.add(itembtn1, itembtn2)

            user.add_or_continue_5 = message.text
            msg = bot.send_message(chat_id, 'Введите тематику ваших каналов', reply_markup=markup)
            bot.register_next_step_handler(msg, process_temat)


        elif message.text == 'Добавить канал':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')
            markup.add(itembtn1, itembtn2)

            user.add_or_continue_5 = message.text
            msg = bot.send_message(chat_id, 'Введите название вашего <b>шестого канала</b>', parse_mode = 'HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_name_6)


        elif message.text == 'Отмена':
            markup_add = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup_add.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>«Создать пост»</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup_add, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')
            markup.add(itembtn1, itembtn2)

            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Введите линк на ваш <b>пятый канал</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_link_5)
            return

        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Добавить канал')
            itembtn2 = types.KeyboardButton('Продолжить')
            itembtn3 = types.KeyboardButton('Назад')
            itembtn4 = types.KeyboardButton('Отмена')

            markup.row(itembtn2)
            markup.row(itembtn1)
            markup.row(itembtn3, itembtn4)

            msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
            msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_add_or_continue_5)
            return

    except Exception as e:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Добавить канал')
        itembtn2 = types.KeyboardButton('Продолжить')
        itembtn3 = types.KeyboardButton('Назад')
        itembtn4 = types.KeyboardButton('Отмена')

        markup.row(itembtn2)
        markup.row(itembtn1)
        markup.row(itembtn3, itembtn4)

        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
        bot.register_next_step_handler(msg, process_add_or_continue_5)
        return


def process_channel_name_6(message):
    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]


        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        markup.add(itembtn1, itembtn2)

        if message.text == 'Отмена':
            markup_add = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup_add.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>«Создать пост»</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup_add, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Добавить канал')
            itembtn2 = types.KeyboardButton('Продолжить')
            itembtn3 = types.KeyboardButton('Назад')
            itembtn4 = types.KeyboardButton('Отмена')

            markup.row(itembtn2)
            markup.row(itembtn1)
            markup.row(itembtn3, itembtn4)

            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_add_or_continue_5)
            return

        else:

            user.channel_name_6 = message.text
            msg = bot.send_message(chat_id, 'Введите линк на ваш <b>шестой канал</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_link_6)

    except Exception as e:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        markup.add(itembtn1, itembtn2)

        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Введите название вашего <b>шестого канала</b>', parse_mode = 'HTML', reply_markup=markup)
        bot.register_next_step_handler(msg, process_channel_name_6)
        return


def process_channel_link_6(message):
    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]


        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        itembtn3 = types.KeyboardButton('Продолжить')
        markup.row(itembtn3)
        markup.row(itembtn1, itembtn2)

        if message.text == 'Отмена':
            markup_add = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup_add.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>«Создать пост»</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup_add, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')

            markup.row(itembtn1, itembtn2)

            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Введите название вашего <b>шестого канала</b>', parse_mode = 'HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_name_6)
            return

        else:

            user.channel_link_6 = message.text
            msg = bot.send_message(chat_id, 'Вы добавили максимальное количество каналов (6) в один пост. Нажмите на кнопку <b>«Продолжить»</b>, для продолжения заполнения поста', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_add_or_continue_6)

    except Exception as e:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        itembtn2 = types.KeyboardButton('Отмена')
        markup.add(itembtn1, itembtn2)

        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Введите линк на ваш <b>шестой канал</b>', parse_mode='HTML', reply_markup=markup)
        bot.register_next_step_handler(msg, process_channel_link_6)
        return


def process_add_or_continue_6(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]

        if message.text == 'Продолжить':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')
            markup.add(itembtn1, itembtn2)

            user.add_or_continue_6 = message.text
            msg = bot.send_message(chat_id, 'Введите тематику ваших каналов', reply_markup=markup)
            bot.register_next_step_handler(msg, process_temat)


        elif message.text == 'Отмена':
            markup_add = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup_add.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>«Создать пост»</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup_add, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')
            markup.add(itembtn1, itembtn2)

            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Введите линк на ваш <b>шестой канал</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_link_6)
            return

        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Продолжить')
            itembtn2 = types.KeyboardButton('Назад')
            itembtn3 = types.KeyboardButton('Отмена')

            markup.row(itembtn1)
            markup.row(itembtn2, itembtn3)

            msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
            msg = bot.send_message(chat_id, 'Вы добавили максимальное количество каналов (6) в один пост. Нажмите на кнопку <b>«Продолжить»</b>, для продолжения заполнения поста', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_add_or_continue_6)
            return

    except Exception as e:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Продолжить')
        itembtn2 = types.KeyboardButton('Назад')
        itembtn3 = types.KeyboardButton('Отмена')

        markup.row(itembtn1)
        markup.row(itembtn2, itembtn3)


        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Вы добавили максимальное количество каналов (6) в один пост. Нажмите на кнопку <b>«Продолжить»</b>, для продолжения заполнения поста', parse_mode='HTML', reply_markup=markup)
        bot.register_next_step_handler(msg, process_add_or_continue_6)
        return


def process_temat(message):
    try:
        chat_id = message.chat.id
        temat = message.text
        user = user_dict[chat_id]
        user.temat = temat
        if message.text == 'Отмена':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>'Создать пост'</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Добавить канал')
            itembtn2 = types.KeyboardButton('Продолжить')
            itembtn3 = types.KeyboardButton('Назад')
            itembtn4 = types.KeyboardButton('Отмена')

            markup.row(itembtn2)
            markup.row(itembtn1)
            markup.row(itembtn3, itembtn4)

            msg = bot.send_message(chat_id, 'Если хотите добавить еще один канал к <b>этому же посту</b>, нажмите на кнопку - <b>«Добавить канал»</b>\n\nЕсли хотите продолжить создание поста, нажмите на кнопку - <b>«Продолжить»</b>', parse_mode='HTML', reply_markup=markup)
            bot.register_next_step_handler(msg, process_add_or_continue_1)
            return

        else:

            msg = bot.send_message(chat_id, 'Введите <b>стандартную стоимость</b> рекаламного поста в вашем канале (в рублях)', parse_mode='HTML')
            bot.register_next_step_handler(msg, process_ordinary_price)
    except Exception as e:
        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Введите тематику вашего канала')
        bot.register_next_step_handler(msg, process_temat)
        return


def process_ordinary_price(message):
    try:
        chat_id = message.chat.id
        ordinary_price = message.text

        if message.text == 'Отмена':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>'Создать пост'</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':
            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Введите тематику вашего канала')
            bot.register_next_step_handler(msg, process_temat)
            return

        else:

            if not ordinary_price.isdigit():
                msg = bot.reply_to(message, 'Стоимость должна быть в <b>числовом формате</b>. Напрмер: 1200', parse_mode='HTML')
                bot.register_next_step_handler(msg, process_ordinary_price)
                return
            else:
                user = user_dict[chat_id]
                user.ordinary_price = ordinary_price
                msg = bot.send_message(chat_id, 'Введите стоимость рекаламного поста в вашем канале <b>с учетом скидки</b> (стоимость горящего места)', parse_mode='HTML')
                bot.register_next_step_handler(msg, process_sale_price)
    except Exception as e:
        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Введите <b>стандартную стоимость</b> рекаламного поста в вашем канале (в рублях)', parse_mode='HTML')
        bot.register_next_step_handler(msg, process_ordinary_price)
        return


def process_sale_price(message):
    try:
        chat_id = message.chat.id
        sale_price = message.text

        if message.text == 'Отмена':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>'Создать пост'</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':
            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Введите <b>стандартную стоимость</b> рекаламного поста в вашем канале (в рублях)', parse_mode='HTML')
            bot.register_next_step_handler(msg, process_ordinary_price)
            return

        else:

            if not sale_price.isdigit():
                msg = bot.reply_to(message, 'Стоимость должна быть в <b>числовом формате</b>. Напрмер: 1200', parse_mode='HTML')
                bot.register_next_step_handler(msg, process_sale_price)
                return
            else:
                user = user_dict[chat_id]
                user.sale_price = sale_price
                msg = bot.send_message(chat_id, 'Введите условия размещения рекламного поста. Например: 2/24')
                bot.register_next_step_handler(msg, process_terms)
    except Exception as e:
        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Введите стоимость рекаламного поста в вашем канале <b>с учетом скидки</b> (стоимость горящего места)', parse_mode='HTML')
        bot.register_next_step_handler(msg, process_sale_price)
        return


def process_terms(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        terms = message.text

        if message.text == 'Отмена':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>'Создать пост'</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':
            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Введите стоимость рекаламного поста в вашем канале <b>с учетом скидки</b> (стоимость горящего места)', parse_mode='HTML')
            bot.register_next_step_handler(msg, process_sale_price)
            return

        else:

            if not '/' in terms:
                msg = bot.reply_to(message, "Условия размещения должны быть в формате 'часов в топе / часов в ленте'. Например: 1/24, 2/24 и т.д.")
                bot.register_next_step_handler(msg, process_terms)
                return
            else:
                user.terms = terms
                msg = bot.send_message(chat_id, 'Введите кол-во рекламных постов в сутки на вашем канале')
                bot.register_next_step_handler(msg, process_ads_amount)
    except Exception as e:
        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Введите условия размещения рекламного поста. Например: 2/24')
        bot.register_next_step_handler(msg, process_terms)
        return


def process_ads_amount(message):
    try:
        chat_id = message.chat.id
        ads_amount = message.text

        if message.text == 'Отмена':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>'Создать пост'</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':
            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Введите условия размещения рекламного поста. Например: 2/24')
            bot.register_next_step_handler(msg, process_terms)
            return

        else:

            if not ads_amount.isdigit():
                msg = bot.reply_to(message, 'Kол-во рекламных постов в сутки должно быть в <b>числовом формате</b>', parse_mode='HTML')
                bot.register_next_step_handler(msg, process_ads_amount)
                return
            else:
                user = user_dict[chat_id]
                user.ads_amount = ads_amount
                msg = bot.send_message(chat_id, 'Введите комментарий')
                bot.register_next_step_handler(msg, process_comment)
    except Exception as e:
        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Введите кол-во рекламных постов в сутки на вашем канале')
        bot.register_next_step_handler(msg, process_ads_amount)
        return


def process_comment(message):
    try:
        chat_id = message.chat.id
        comment = message.text

        if message.text == 'Отмена':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>'Создать пост'</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':
            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Введите кол-во рекламных постов в сутки на вашем канале')
            bot.register_next_step_handler(msg, process_ads_amount)
            return

        else:

            user = user_dict[chat_id]
            user.comment = comment
            msg = bot.send_message(chat_id, "Введите юзернейм в t.me/ формате для связи с админом или менеджером данного телеграм-канала")
            bot.register_next_step_handler(msg, process_admin_username)
    except Exception as e:
        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(chat_id, 'Введите комментарий')
        bot.register_next_step_handler(msg, process_comment)
        return


def process_admin_username(message):
    try:
        chat_id = message.chat.id
        admin_username = message.text

        if message.text == 'Отмена':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>'Создать пост'</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':
            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Введите комментарий')
            bot.register_next_step_handler(msg, process_comment)
            return

        elif not admin_username.startswith('t.me/'):
            msg = bot.reply_to(message, "Юзернейм должен содержать t.me/. Например: t.me/durov", disable_web_page_preview=True)
            bot.register_next_step_handler(msg, process_admin_username)
            return

        else:
            user = user_dict[chat_id]
            user.admin_username = admin_username

            markup_inline = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton('Написать админу', url = user.admin_username)
            markup_inline.add(item1)

            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item2 = types.KeyboardButton('Опубликовать')
            item3 = types.KeyboardButton('Отмена')
            item4 = types.KeyboardButton('Назад')
            markup_reply.row(item2)
            markup_reply.row(item4, item3)


            msg = bot.send_message(chat_id, "Ваш пост готов к публикации в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>.\nНажмите на кнопку <b>'Опубликовать'</b> для публикации поста", parse_mode='HTML', disable_web_page_preview=True, reply_markup=markup_reply)

            if 'Продолжить' in user.add_or_continue_1:
                msg = bot.send_message(chat_id,
                '<b>Горит на </b>' + f'<b>{user.sale_date}</b>' + '\n\n' +
                '• Канал: ' + f'<a href="{user.channel_link}">{user.channel_name}</a>' + '\n\n' +
                '• Тематика: ' + f'<b>{user.temat}</b>' + '\n\n' +
                '• Стандартная цена: ' + f'<s>{user.ordinary_price}</s>' + '<s> p</s>' + '\n\n' +
                '• Цена со скидкой: ' + f'<b>{user.sale_price}</b>' + '<b> p</b>' + '\n\n' +
                '• Условия: ' + user.terms + '\n\n' +
                '• Рекламных постов в сутки: ' + user.ads_amount + '\n\n' +
                '• Комментарий: ' + user.comment + '\n\n' +
                '• Связь: ' + user.admin_username + '\n\n' +
                '<i>Чтобы купить горящее, перешли этот пост админу указанному выше и скажи, что хочешь купить горящее. Помни, горящие места разлетаются очень быстро</i>',
                parse_mode='HTML', disable_web_page_preview=True, reply_markup=markup_inline)
                bot.register_next_step_handler(msg, publication)

            elif 'Продолжить' in user.add_or_continue_2:
                msg = bot.send_message(chat_id,
                '<b>Горит на </b>' + f'<b>{user.sale_date}</b>' + '\n\n' +
                '• Канал: ' + f'<a href="{user.channel_link}">{user.channel_name}</a>' + ' + ' +  f'<a href="{user.channel_link_2}">{user.channel_name_2}</a>' + '\n\n' +
                '• Тематика: ' + f'<b>{user.temat}</b>' + '\n\n' +
                '• Стандартная цена: ' + f'<s>{user.ordinary_price}</s>' + '<s> p</s>' + '\n\n' +
                '• Цена со скидкой: ' + f'<b>{user.sale_price}</b>' + '<b> p</b>' + '\n\n' +
                '• Условия: ' + user.terms + '\n\n' +
                '• Рекламных постов в сутки: ' + user.ads_amount + '\n\n' +
                '• Комментарий: ' + user.comment + '\n\n' +
                '• Связь: ' + user.admin_username + '\n\n' +
                '<i>Чтобы купить горящее, перешли этот пост админу указанному выше и скажи, что хочешь купить горящее. Помни, горящие места разлетаются очень быстро</i>',
                parse_mode='HTML', disable_web_page_preview=True, reply_markup=markup_inline)
                bot.register_next_step_handler(msg, publication)

            elif 'Продолжить' in user.add_or_continue_3:
                msg = bot.send_message(chat_id,
                '<b>Горит на </b>' + f'<b>{user.sale_date}</b>' + '\n\n' +
                '• Канал: ' + f'<a href="{user.channel_link}">{user.channel_name}</a>' + ' + ' + f'<a href="{user.channel_link_2}">{user.channel_name_2}</a>' + ' + ' + f'<a href="{user.channel_link_3}">{user.channel_name_3}</a>' + '\n\n' +
                '• Тематика: ' + f'<b>{user.temat}</b>' + '\n\n' +
                '• Стандартная цена: ' + f'<s>{user.ordinary_price}</s>' + '<s> p</s>' + '\n\n' +
                '• Цена со скидкой: ' + f'<b>{user.sale_price}</b>' + '<b> p</b>' + '\n\n' +
                '• Условия: ' + user.terms + '\n\n' +
                '• Рекламных постов в сутки: ' + user.ads_amount + '\n\n' +
                '• Комментарий: ' + user.comment + '\n\n' +
                '• Связь: ' + user.admin_username + '\n\n' +
                '<i>Чтобы купить горящее, перешли этот пост админу указанному выше и скажи, что хочешь купить горящее. Помни, горящие места разлетаются очень быстро</i>',
                parse_mode='HTML', disable_web_page_preview=True, reply_markup=markup_inline)
                bot.register_next_step_handler(msg, publication)

            elif 'Продолжить' in user.add_or_continue_4:
                msg = bot.send_message(chat_id,
                '<b>Горит на </b>' + f'<b>{user.sale_date}</b>' + '\n\n' +
                '• Канал: ' + f'<a href="{user.channel_link}">{user.channel_name}</a>' + ' + ' + f'<a href="{user.channel_link_2}">{user.channel_name_2}</a>' + ' + ' + f'<a href="{user.channel_link_3}">{user.channel_name_3}</a>' + ' + ' + f'<a href="{user.channel_link_4}">{user.channel_name_4}</a>' + '\n\n' +
                '• Тематика: ' + f'<b>{user.temat}</b>' + '\n\n' +
                '• Стандартная цена: ' + f'<s>{user.ordinary_price}</s>' + '<s> p</s>' + '\n\n' +
                '• Цена со скидкой: ' + f'<b>{user.sale_price}</b>' + '<b> p</b>' + '\n\n' +
                '• Условия: ' + user.terms + '\n\n' +
                '• Рекламных постов в сутки: ' + user.ads_amount + '\n\n' +
                '• Комментарий: ' + user.comment + '\n\n' +
                '• Связь: ' + user.admin_username + '\n\n' +
                '<i>Чтобы купить горящее, перешли этот пост админу указанному выше и скажи, что хочешь купить горящее. Помни, горящие места разлетаются очень быстро</i>',
                parse_mode='HTML', disable_web_page_preview=True, reply_markup=markup_inline)
                bot.register_next_step_handler(msg, publication)

            elif 'Продолжить' in user.add_or_continue_5:
                msg = bot.send_message(chat_id,
                '<b>Горит на </b>' + f'<b>{user.sale_date}</b>' + '\n\n' +
                '• Канал: ' + f'<a href="{user.channel_link}">{user.channel_name}</a>' + ' + ' + f'<a href="{user.channel_link_2}">{user.channel_name_2}</a>' + ' + ' + f'<a href="{user.channel_link_3}">{user.channel_name_3}</a>' + ' + ' + f'<a href="{user.channel_link_4}">{user.channel_name_4}</a>' + ' + ' + f'<a href="{user.channel_link_5}">{user.channel_name_5}</a>' + '\n\n' +
                '• Тематика: ' + f'<b>{user.temat}</b>' + '\n\n' +
                '• Стандартная цена: ' + f'<s>{user.ordinary_price}</s>' + '<s> p</s>' + '\n\n' +
                '• Цена со скидкой: ' + f'<b>{user.sale_price}</b>' + '<b> p</b>' + '\n\n' +
                '• Условия: ' + user.terms + '\n\n' +
                '• Рекламных постов в сутки: ' + user.ads_amount + '\n\n' +
                '• Комментарий: ' + user.comment + '\n\n' +
                '• Связь: ' + user.admin_username + '\n\n' +
                '<i>Чтобы купить горящее, перешли этот пост админу указанному выше и скажи, что хочешь купить горящее. Помни, горящие места разлетаются очень быстро</i>',
                parse_mode='HTML', disable_web_page_preview=True, reply_markup=markup_inline)
                bot.register_next_step_handler(msg, publication)


            elif 'Продолжить' in user.add_or_continue_6:
                msg = bot.send_message(chat_id,
                '<b>Горит на </b>' + f'<b>{user.sale_date}</b>' + '\n\n' +
                '• Канал: ' + f'<a href="{user.channel_link}">{user.channel_name}</a>' + ' + ' + f'<a href="{user.channel_link_2}">{user.channel_name_2}</a>' + ' + ' + f'<a href="{user.channel_link_3}">{user.channel_name_3}</a>' + ' + ' + f'<a href="{user.channel_link_4}">{user.channel_name_4}</a>' + ' + ' + f'<a href="{user.channel_link_5}">{user.channel_name_5}</a>' + ' + ' + f'<a href="{user.channel_link_6}">{user.channel_name_6}</a>' + '\n\n' +
                '• Тематика: ' + f'<b>{user.temat}</b>' + '\n\n' +
                '• Стандартная цена: ' + f'<s>{user.ordinary_price}</s>' + '<s> p</s>' + '\n\n' +
                '• Цена со скидкой: ' + f'<b>{user.sale_price}</b>' + '<b> p</b>' + '\n\n' +
                '• Условия: ' + user.terms + '\n\n' +
                '• Рекламных постов в сутки: ' + user.ads_amount + '\n\n' +
                '• Комментарий: ' + user.comment + '\n\n' +
                '• Связь: ' + user.admin_username + '\n\n' +
                '<i>Чтобы купить горящее, перешли этот пост админу указанному выше и скажи, что хочешь купить горящее. Помни, горящие места разлетаются очень быстро</i>',
                parse_mode='HTML', disable_web_page_preview=True, reply_markup=markup_inline)
                bot.register_next_step_handler(msg, publication)

            else:

                msg = bot.send_message(chat_id, 'Упс... Что-то пошло не так при формировании поста')
                msg = bot.send_message(chat_id, "Введите юзернейм в t.me/ формате для связи с админом или менеджером данного телеграм-канала")
                bot.register_next_step_handler(msg, process_admin_username)
                return


    except Exception as e:
        msg = bot.send_message(chat_id, 'Упс... Что-то пошло не так')
        msg = bot.send_message(chat_id, "Введите юзернейм в t.me/ формате для связи с админом или менеджером данного телеграм-канала")
        bot.register_next_step_handler(msg, process_admin_username)
        return


def publication(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]


        if message.text == 'Отмена':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>'Создать пост'</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':
            msg = bot.send_message(chat_id, 'Вы вернулись на шаг назад')
            msg = bot.send_message(chat_id, 'Введите юзернейм в t.me/ формате для связи с админом или менеджером данного телеграм-канала', disable_web_page_preview=True)
            bot.register_next_step_handler(msg, process_admin_username)
            return

        elif message.text == 'Опубликовать':

            user.date_2 = datetime.date.today()

            channel_id = '-1001205836941'

            markup_inline = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton('Написать админу', url = user.admin_username)
            markup_inline.add(item1)

            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup_reply.add(itembtn1)


            if 'Продолжить' in user.add_or_continue_1:
                msg = bot.send_message(channel_id,
                '<b>Горит на </b>' + f'<b>{user.sale_date}</b>' + '\n\n' +
                '• Канал: ' + f'<a href="{user.channel_link}">{user.channel_name}</a>' + '\n\n' +
                '• Тематика: ' + f'<b>{user.temat}</b>' + '\n\n' +
                '• Стандартная цена: ' + f'<s>{user.ordinary_price}</s>' + '<s> p</s>' + '\n\n' +
                '• Цена со скидкой: ' + f'<b>{user.sale_price}</b>' + '<b> p</b>' + '\n\n' +
                '• Условия: ' + user.terms + '\n\n' +
                '• Рекламных постов в сутки: ' + user.ads_amount + '\n\n' +
                '• Комментарий: ' + user.comment + '\n\n' +
                '• Связь: ' + user.admin_username + '\n\n' +
                '<i>Чтобы купить горящее, перешли этот пост админу указанному выше и скажи, что хочешь купить горящее. Помни, горящие места разлетаются очень быстро</i>',
                parse_mode='HTML', disable_web_page_preview=True, reply_markup=markup_inline)
                msg = bot.send_message(chat_id, 'Пост опубликован!', parse_mode='HTML')
                msg = bot.send_message(chat_id, "Для создания нового поста, нажми на кнопку <b>'Создать пост'</b>.", parse_mode='HTML', reply_markup=markup_reply)

                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                else:
                    bot.register_next_step_handler(msg, start_conversation_2)

            elif 'Продолжить' in user.add_or_continue_2:
                msg = bot.send_message(channel_id,
                '<b>Горит на </b>' + f'<b>{user.sale_date}</b>' + '\n\n' +
                '• Канал: ' + f'<a href="{user.channel_link}">{user.channel_name}</a>' + ' + ' +  f'<a href="{user.channel_link_2}">{user.channel_name_2}</a>' + '\n\n' +
                '• Тематика: ' + f'<b>{user.temat}</b>' + '\n\n' +
                '• Стандартная цена: ' + f'<s>{user.ordinary_price}</s>' + '<s> p</s>' + '\n\n' +
                '• Цена со скидкой: ' + f'<b>{user.sale_price}</b>' + '<b> p</b>' + '\n\n' +
                '• Условия: ' + user.terms + '\n\n' +
                '• Рекламных постов в сутки: ' + user.ads_amount + '\n\n' +
                '• Комментарий: ' + user.comment + '\n\n' +
                '• Связь: ' + user.admin_username + '\n\n' +
                '<i>Чтобы купить горящее, перешли этот пост админу указанному выше и скажи, что хочешь купить горящее. Помни, горящие места разлетаются очень быстро</i>',
                parse_mode='HTML', disable_web_page_preview=True, reply_markup=markup_inline)
                msg = bot.send_message(chat_id, 'Пост опубликован!', parse_mode='HTML')
                msg = bot.send_message(chat_id, "Для создания нового поста, нажми на кнопку <b>'Создать пост'</b>.", parse_mode='HTML', reply_markup=markup_reply)
                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                else:
                    bot.register_next_step_handler(msg, start_conversation_2)

                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                else:
                    bot.register_next_step_handler(msg, start_conversation_2)

            elif 'Продолжить' in user.add_or_continue_3:
                msg = bot.send_message(channel_id,
                '<b>Горит на </b>' + f'<b>{user.sale_date}</b>' + '\n\n' +
                '• Канал: ' + f'<a href="{user.channel_link}">{user.channel_name}</a>' + ' + ' + f'<a href="{user.channel_link_2}">{user.channel_name_2}</a>' + ' + ' + f'<a href="{user.channel_link_3}">{user.channel_name_3}</a>' + '\n\n' +
                '• Тематика: ' + f'<b>{user.temat}</b>' + '\n\n' +
                '• Стандартная цена: ' + f'<s>{user.ordinary_price}</s>' + '<s> p</s>' + '\n\n' +
                '• Цена со скидкой: ' + f'<b>{user.sale_price}</b>' + '<b> p</b>' + '\n\n' +
                '• Условия: ' + user.terms + '\n\n' +
                '• Рекламных постов в сутки: ' + user.ads_amount + '\n\n' +
                '• Комментарий: ' + user.comment + '\n\n' +
                '• Связь: ' + user.admin_username + '\n\n' +
                '<i>Чтобы купить горящее, перешли этот пост админу указанному выше и скажи, что хочешь купить горящее. Помни, горящие места разлетаются очень быстро</i>',
                parse_mode='HTML', disable_web_page_preview=True, reply_markup=markup_inline)
                msg = bot.send_message(chat_id, 'Пост опубликован!', parse_mode='HTML')
                msg = bot.send_message(chat_id, "Для создания нового поста, нажми на кнопку <b>'Создать пост'</b>.", parse_mode='HTML', reply_markup=markup_reply)
                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)

                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                else:
                    bot.register_next_step_handler(msg, start_conversation_2)

                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                else:
                    bot.register_next_step_handler(msg, start_conversation_2)


            elif 'Продолжить' in user.add_or_continue_4:
                msg = bot.send_message(channel_id,
                '<b>Горит на </b>' + f'<b>{user.sale_date}</b>' + '\n\n' +
                '• Канал: ' + f'<a href="{user.channel_link}">{user.channel_name}</a>' + ' + ' + f'<a href="{user.channel_link_2}">{user.channel_name_2}</a>' + ' + ' + f'<a href="{user.channel_link_3}">{user.channel_name_3}</a>' + ' + ' + f'<a href="{user.channel_link_4}">{user.channel_name_4}</a>' + '\n\n' +
                '• Тематика: ' + f'<b>{user.temat}</b>' + '\n\n' +
                '• Стандартная цена: ' + f'<s>{user.ordinary_price}</s>' + '<s> p</s>' + '\n\n' +
                '• Цена со скидкой: ' + f'<b>{user.sale_price}</b>' + '<b> p</b>' + '\n\n' +
                '• Условия: ' + user.terms + '\n\n' +
                '• Рекламных постов в сутки: ' + user.ads_amount + '\n\n' +
                '• Комментарий: ' + user.comment + '\n\n' +
                '• Связь: ' + user.admin_username + '\n\n' +
                '<i>Чтобы купить горящее, перешли этот пост админу указанному выше и скажи, что хочешь купить горящее. Помни, горящие места разлетаются очень быстро</i>',
                parse_mode='HTML', disable_web_page_preview=True, reply_markup=markup_inline)
                msg = bot.send_message(chat_id, 'Пост опубликован!', parse_mode='HTML')
                msg = bot.send_message(chat_id, "Для создания нового поста, нажми на кнопку <b>'Создать пост'</b>.", parse_mode='HTML', reply_markup=markup_reply)
                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)

                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                else:
                    bot.register_next_step_handler(msg, start_conversation_2)

                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                else:
                    bot.register_next_step_handler(msg, start_conversation_2)

                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                else:
                    bot.register_next_step_handler(msg, start_conversation_2)



            elif 'Продолжить' in user.add_or_continue_5:
                msg = bot.send_message(channel_id,
                '<b>Горит на </b>' + f'<b>{user.sale_date}</b>' + '\n\n' +
                '• Канал: ' + f'<a href="{user.channel_link}">{user.channel_name}</a>' + ' + ' + f'<a href="{user.channel_link_2}">{user.channel_name_2}</a>' + ' + ' + f'<a href="{user.channel_link_3}">{user.channel_name_3}</a>' + ' + ' + f'<a href="{user.channel_link_4}">{user.channel_name_4}</a>' + ' + ' + f'<a href="{user.channel_link_5}">{user.channel_name_5}</a>' + '\n\n' +
                '• Тематика: ' + f'<b>{user.temat}</b>' + '\n\n' +
                '• Стандартная цена: ' + f'<s>{user.ordinary_price}</s>' + '<s> p</s>' + '\n\n' +
                '• Цена со скидкой: ' + f'<b>{user.sale_price}</b>' + '<b> p</b>' + '\n\n' +
                '• Условия: ' + user.terms + '\n\n' +
                '• Рекламных постов в сутки: ' + user.ads_amount + '\n\n' +
                '• Комментарий: ' + user.comment + '\n\n' +
                '• Связь: ' + user.admin_username + '\n\n' +
                '<i>Чтобы купить горящее, перешли этот пост админу указанному выше и скажи, что хочешь купить горящее. Помни, горящие места разлетаются очень быстро</i>',
                parse_mode='HTML', disable_web_page_preview=True, reply_markup=markup_inline)
                msg = bot.send_message(chat_id, 'Пост опубликован!', parse_mode='HTML')
                msg = bot.send_message(chat_id, "Для создания нового поста, нажми на кнопку <b>'Создать пост'</b>.", parse_mode='HTML', reply_markup=markup_reply)
                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)

                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                else:
                    bot.register_next_step_handler(msg, start_conversation_2)

                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                else:
                    bot.register_next_step_handler(msg, start_conversation_2)

                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                else:
                    bot.register_next_step_handler(msg, start_conversation_2)

                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                else:
                    bot.register_next_step_handler(msg, start_conversation_2)


            elif 'Продолжить' in user.add_or_continue_6:
                msg = bot.send_message(channel_id,
                '<b>Горит на </b>' + f'<b>{user.sale_date}</b>' + '\n\n' +
                '• Канал: ' + f'<a href="{user.channel_link}">{user.channel_name}</a>' + ' + ' + f'<a href="{user.channel_link_2}">{user.channel_name_2}</a>' + ' + ' + f'<a href="{user.channel_link_3}">{user.channel_name_3}</a>' + ' + ' + f'<a href="{user.channel_link_4}">{user.channel_name_4}</a>' + ' + ' + f'<a href="{user.channel_link_5}">{user.channel_name_5}</a>' + ' + ' + f'<a href="{user.channel_link_6}">{user.channel_name_6}</a>' + '\n\n' +
                '• Тематика: ' + f'<b>{user.temat}</b>' + '\n\n' +
                '• Стандартная цена: ' + f'<s>{user.ordinary_price}</s>' + '<s> p</s>' + '\n\n' +
                '• Цена со скидкой: ' + f'<b>{user.sale_price}</b>' + '<b> p</b>' + '\n\n' +
                '• Условия: ' + user.terms + '\n\n' +
                '• Рекламных постов в сутки: ' + user.ads_amount + '\n\n' +
                '• Комментарий: ' + user.comment + '\n\n' +
                '• Связь: ' + user.admin_username + '\n\n' +
                '<i>Чтобы купить горящее, перешли этот пост админу указанному выше и скажи, что хочешь купить горящее. Помни, горящие места разлетаются очень быстро</i>',
                parse_mode='HTML', disable_web_page_preview=True, reply_markup=markup_inline)
                msg = bot.send_message(chat_id, 'Пост опубликован!', parse_mode='HTML')
                msg = bot.send_message(chat_id, "Для создания нового поста, нажми на кнопку <b>'Создать пост'</b>.", parse_mode='HTML', reply_markup=markup_reply)
                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link
                    bot.register_next_step_handler(msg, start_conversation_2)

                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link_2
                    bot.register_next_step_handler(msg, start_conversation_2)
                else:
                    bot.register_next_step_handler(msg, start_conversation_2)

                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link_3
                    bot.register_next_step_handler(msg, start_conversation_2)
                else:
                    bot.register_next_step_handler(msg, start_conversation_2)

                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link_4
                    bot.register_next_step_handler(msg, start_conversation_2)
                else:
                    bot.register_next_step_handler(msg, start_conversation_2)

                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link_5
                    bot.register_next_step_handler(msg, start_conversation_2)
                else:
                    bot.register_next_step_handler(msg, start_conversation_2)


                if user.channel_link_check_1 == None:
                    user.channel_link_check_1 = user.channel_link_6
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_2 == None:
                    user.channel_link_check_2 = user.channel_link_6
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_3 == None:
                    user.channel_link_check_3 = user.channel_link_6
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_4 == None:
                    user.channel_link_check_4 = user.channel_link_6
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_5 == None:
                    user.channel_link_check_5 = user.channel_link_6
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_6 == None:
                    user.channel_link_check_6 = user.channel_link_6
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_7 == None:
                    user.channel_link_check_7 = user.channel_link_6
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_8 == None:
                    user.channel_link_check_8 = user.channel_link_6
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_9 == None:
                    user.channel_link_check_9 = user.channel_link_6
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_10 == None:
                    user.channel_link_check_10 = user.channel_link_6
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_11 == None:
                    user.channel_link_check_11 = user.channel_link_6
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_12 == None:
                    user.channel_link_check_12 = user.channel_link_6
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_13 == None:
                    user.channel_link_check_13 = user.channel_link_6
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_14 == None:
                    user.channel_link_check_14 = user.channel_link_6
                    bot.register_next_step_handler(msg, start_conversation_2)
                elif user.channel_link_check_15 == None:
                    user.channel_link_check_15 = user.channel_link_6
                    bot.register_next_step_handler(msg, start_conversation_2)
                else:
                    bot.register_next_step_handler(msg, start_conversation_2)


            else:
                markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item2 = types.KeyboardButton('Опубликовать')
                item3 = types.KeyboardButton('Назад')
                item4 = types.KeyboardButton('Отмена')
                markup_reply.row(item2)
                markup_reply.row(item3, item4)

                msg = bot.reply_to(message, 'Вы ввели что-то невнятное')
                msg = bot.send_message(chat_id, "Ваш пост готов к публикации в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>. Нажмите на кнопку <b>'Опубликовать'</b> для публикации поста", parse_mode='HTML', disable_web_page_preview=True, reply_markup=markup_reply)
                bot.register_next_step_handler(msg, publication)
                return

    except Exception as e:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton('Опубликовать')
        item3 = types.KeyboardButton('Отмена')
        item4 = types.KeyboardButton('Назад')
        markup_reply.row(item2)
        markup_reply.row(item4, item3)

        msg = bot.send_message(chat_id, 'Упс... Что-то пошло не так при публикации поста')
        msg = bot.send_message(chat_id, "Ваш пост готов к публикации в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>.\nНажмите на кнопку <b>'Опубликовать'</b> для публикации поста", parse_mode='HTML', disable_web_page_preview=True, reply_markup=markup_reply)
        bot.register_next_step_handler(msg, publication)



def start_conversation_2(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]

        if message.text == 'Создать пост':

            markup_cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Отмена')
            markup_cancel.add(itembtn1)

            msg = bot.send_message(message.chat.id, 'Введите дату вашего горящего места. Можно несколько дат сразу через запятую. Например: 14.07, 15.07', reply_markup=markup_cancel)
            bot.register_next_step_handler(msg, process_sale_date_2)

        else:

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup.add(itembtn1)

            msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
            msg = bot.send_message(message.chat.id, "Нажмите на кнопку <b>'Создать пост'</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)
            return

    except Exception as e:
        markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Создать пост')
        markup_1.add(itembtn1)

        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(message.chat.id, "Нажмите на кнопку <b>'Создать пост'</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup_1, disable_web_page_preview=True)
        bot.register_next_step_handler(msg, start_conversation_2)
        return


def process_sale_date_2(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.sale_date = message.text


        if message.text == 'Отмена':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Создать пост')
            markup.add(itembtn1)

            msg = bot.send_message(chat_id, 'Вы отменили создание поста')
            msg = bot.send_message(chat_id, "Нажмите на кнопку <b>'Создать пост'</b> для создания поста в канал <a href='http://t.me/joinchat/AAAAAEcnQFslPC-TSOdoPg'>Горящие места</a>", parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)
            bot.register_next_step_handler(msg, start_conversation_2)

        elif message.text == 'Назад':

            msg = bot.send_message(chat_id, 'Введите дату вашего горящего места. Можно ввести несколько дат сразу через запятую. Например: 14.07, 15.07')
            bot.register_next_step_handler(msg, process_sale_date_2)
            return

        else:

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itembtn1 = types.KeyboardButton('Назад')
            itembtn2 = types.KeyboardButton('Отмена')
            markup.add(itembtn1, itembtn2)

            msg = bot.send_message(chat_id, 'Введите название вашего канала', reply_markup=markup)
            bot.register_next_step_handler(msg, process_channel_name)
    except Exception as e:
        msg = bot.reply_to(message, 'Вы ввели что-то невнятное.')
        msg = bot.send_message(message.chat.id, 'Введите дату вашего горящего места. Можно несколько дат сразу через запятую. Например: 14.07, 15.07')
        bot.register_next_step_handler(msg, process_sale_date_2)
        return




# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
# bot.load_next_step_handlers()

bot.polling()
