import os
from dotenv import load_dotenv
import telebot
from telebot import types


load_dotenv('.env')
TOKEN = os.getenv("TOKEN")
CHAT_C = os.getenv("CHAT_C")
CHAT_R = os.getenv("CHAT_R")
administradores = [int(x) for x in os.getenv("ADMINS").split('-')]

max_links = 20

chats = {
    "c" : {
        "name": "clientes",
        "id" : CHAT_C
    },
    "r" : {
        "name": "revendedores",
        "id" : CHAT_R
    }

}

bot = telebot.TeleBot(TOKEN)

def generateLinks(type, num):
    links = []
    try:
        chat_id = chats[type]['id']
        for i in range(1, num + 1):
            link = bot.create_chat_invite_link(chat_id=chat_id, member_limit=1).invite_link
            links.append(f'{i} - `{link}`')
        return "\n".join(links)
    except KeyError:
        return "El tipo de chat no existe."

def generateKeyboardChat(num ):
    markup = types.InlineKeyboardMarkup()

    for chat_type, chat_info in chats.items():
        item = types.InlineKeyboardButton(text=chat_info["name"].capitalize(), callback_data=f'chat-{chat_type}-{num}')
        markup.add(item)

    markup.add(types.InlineKeyboardButton(text="Atras 🔙", callback_data='atras'))

    return markup

def generateKeyboard(prefix, start, end):
    markup = types.InlineKeyboardMarkup()

    for i in range(start, end + 1):
        item = types.InlineKeyboardButton(str(i), callback_data=f'{prefix}-{i}')
        markup.add(item)
    
    return markup


@bot.message_handler(func=lambda message: message.text == 'gen' and message.from_user.id in administradores)
def start(message):
    print(message)
    keyboard = generateKeyboard("gen", 1, max_links)
    bot.send_message(
                    message.chat.id, "❇️ Selecciona un número ❇️\nObs:*El numero sera el numeros de link a generar!*",
                    reply_markup=keyboard,
                    parse_mode="Markdown"
                    )


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.message:
        if call.data.startswith('gen'):
            num = int(call.data.split('-')[1])
            keyboard = generateKeyboardChat(num)
            bot.edit_message_text(text=f'♾️ Elige a que chat vas a generar {num} link/s: ♾️', chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=keyboard  )

        if call.data=="atras":
            keyboard = generateKeyboard("gen", 1, max_links)
            bot.edit_message_text(text="❇️ Selecciona un número ❇️", chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=keyboard  )
            
        if call.data.startswith('chat'):
            keyboard = generateKeyboard("gen", 1, max_links)
            bot.edit_message_text(text="❇️ Selecciona un número ❇️", chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=keyboard  )

            info=call.data.split('-')
            
            message = f'Tus enlaces de invitacion validos para *1 persona* ✅ :\n{generateLinks(type=info[1],num=int(info[2]),)}'

            bot.send_message(chat_id=call.message.chat.id, text=message, parse_mode='Markdown' )
            
            

if __name__ == "__main__":
    print("BOT LIVE!")
    bot.polling(none_stop=True)
