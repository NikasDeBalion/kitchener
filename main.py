import telebot
from telebot import types
import strings
import random

bot = telebot.TeleBot(strings.token, parse_mode=None)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.delete_message(message.chat.id, message.message_id)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("🍮 Drinks")
    item2 = types.KeyboardButton("🍰 Desserts")
    item3 = types.KeyboardButton("🍲 Soups")
    item4 = types.KeyboardButton("🍚 Porridge")
    item5 = types.KeyboardButton("🍽 Start 🍽")
    item6 = types.KeyboardButton("🎲 Random 🎲")
    item7 = types.KeyboardButton("")

    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id,
                     "I'm glad to see you, <b>{0.first_name}</b>!\nI'm - <b>{1.first_name}</b>, your personal assistant in the kitchen.  What do you want to cook?".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=["text", "video"])
def handle_text(message):

# Drinks
    if message.text == "🍮 Drinks":
        bot.delete_message(message.chat.id, message.message_id)

        keyboard_drinks = types.InlineKeyboardMarkup(row_width=2)
        drinks_tea = types.InlineKeyboardButton(text="☕️Tea ☕", callback_data="drinks_tea")
        drinks_cappuccino = types.InlineKeyboardButton(text="🥤 Cappuccino 🥤", callback_data="drinks_cappuccino")
        drinks_banana_cocktail = types.InlineKeyboardButton(text="🍹 Banana cocktail 🍹",
                                                            callback_data="drinks_banana_cocktail")
        drinks_ginger_tea = types.InlineKeyboardButton(text="🍯 Ginger tea with lemon 🍯",
                                                       callback_data="drinks_ginger_tea")
        drinks_hot_chocolate = types.InlineKeyboardButton(text="🍫☕ Hot chocolate ☕🍫",
                                                       callback_data="drinks_hot_chocolate")
        drinks_cacao = types.InlineKeyboardButton(text="☕ Cacao with milk ☕",
                                                       callback_data="drinks_cacao")
        drinks_random = types.InlineKeyboardButton(text="🎲 Random 🎲", callback_data="drinks_random")

        keyboard_drinks.add(drinks_tea, drinks_cappuccino, drinks_banana_cocktail, drinks_ginger_tea, drinks_hot_chocolate, drinks_cacao, drinks_random)

        sticker_drinks = open('static/drinks.webp', 'rb')
        bot.send_sticker(message.chat.id, sticker_drinks)
        bot.send_message(message.from_user.id, "<b>{0.first_name}</b>!\nDo you want something to drink?".format(
            message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard_drinks)

# Desserts
    if message.text == "🍰 Desserts":
        bot.delete_message(message.chat.id, message.message_id)

        keyboard_desserts = types.InlineKeyboardMarkup(row_width=2)
        drinks_tea = types.InlineKeyboardButton(text="☕️Tea ☕", callback_data="drinks_tea")
        drinks_cappuccino = types.InlineKeyboardButton(text="🥤 Cappuccino 🥤", callback_data="drinks_cappuccino")
        drinks_banana_cocktail = types.InlineKeyboardButton(text="🍹 Banana cocktail 🍹",
                                                            callback_data="drinks_banana_cocktail")
        drinks_ginger_tea = types.InlineKeyboardButton(text="🍯 Ginger tea with lemon 🍯",
                                                       callback_data="drinks_ginger_tea")
        drinks_random = types.InlineKeyboardButton(text="🎲 Random 🎲", callback_data="drinks_random")

        keyboard_desserts.add(drinks_tea, drinks_cappuccino, drinks_banana_cocktail, drinks_ginger_tea, drinks_random)

        sticker_drinks = open('static/desserts.webp', 'rb')
        bot.send_sticker(message.chat.id, sticker_drinks)
        bot.send_message(message.from_user.id, "<b>{0.first_name}</b>!\nDo you want something to drink?".format(
            message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard_desserts)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

# Drinks
    if call.data == "drinks_tea":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=strings.tea, parse_mode='html')

    if call.data == "drinks_cappuccino":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=strings.cappuccino, parse_mode='html')

    if call.data == "drinks_banana_cocktail":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=strings.banana_cocktail, parse_mode='html')

    if call.data == "drinks_ginger_tea":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=strings.ginger_tea, parse_mode='html')

    if call.data == "drinks_hot_chocolate":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=strings.hot_chocolate, parse_mode='html')

    if call.data == "drinks_cacao":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=strings.cacao, parse_mode='html')

    if call.data == "drinks_random":
        drinks_list = [strings.tea, strings.cappuccino, strings.banana_cocktail, strings.ginger_tea,strings.hot_chocolate,strings.cacao]
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=random.choice(drinks_list), parse_mode='html')

# Desserts




# the mode of continuous processing of information coming from telegram servers
if __name__ == '__main__':
    # bot.infinity_polling()
    bot.polling(none_stop=False, interval=0, timeout=20)
