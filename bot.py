import telegram
bot = telegram.Bot("telegram bot Token")

import openai
openai.api_key = "API"

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text('Hi! I am Keli. Ask me any question!')

def answer(update, context):

    question = update.message.text

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1.5,
    )

    response_text = response['choices'][0]['text']

    update.message.reply_text(response_text)

def main():


    updater = Updater("Telegram bot token", use_context=True)


    dp = updater.dispatcher


    dp.add_handler(CommandHandler("start", start))


    dp.add_handler(MessageHandler(Filters.text, answer))

    # Start the Bot
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
