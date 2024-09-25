from config import config
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from cryptocompare_api import Crypto
from utils import *


# command /start
async def start(update: Update, context):
    logger.info("Пользователь %s запустил бота.", update.effective_user.username)
    try:
        await update.message.reply_text("Hello world")
    except Exception as e:
        bot_close(context, e=e)


# command /price
async def price(update: Update, context):
    logger.info("Пользователь %s запустил бота.", update.effective_user.username)
    try:
        response = await Crypto().get_price_multi()
        if not response:
            await update.message.reply_text("response is empty")
        elif "Response" in response:
            await update.message.reply_text(f"Error: {response["Message"]}")
            return
        else:
            await update.message.reply_text(print_dict_multi_price(response))
    except Exception as e:
        bot_close(context, e=e)


# command /quotation
async def quotation(update: Update, context):
    logger.info("Пользователь %s запросил котировку %s.", update.effective_user.username, context.args[0] if context.args else '')
    try:
        if context.args:
            response = await Crypto().get_price(context.args[0])
            if not response:
                await update.message.reply_text("response is empty")
            elif "Response" in response:
                await update.message.reply_text(f"Error: {response["Message"]}")
                return
            elif "USD" in response or "RUB" in response:
                await update.message.reply_text('\n'.join(f"{"{:,.2f}".format(value).replace(',',' ')} {key}" \
                                                          for key, value in response.items()))
            else:
                await update.message.reply_text(response)
                logger.error("Ответ %s неожидаемый.", response)
        else:
            await update.message.reply_text("Укажите монету, котировку которой хотите узнать \
                                            \nФормат ввода '/quotation (coin)'")
    except Exception as e:
        bot_close(context, e=e)


async def message_handler_text(update: Update, context):
    logger.info("Пользователь %s отправил текстовае сообщение.", update.effective_user.username)
    await update.message.reply_text("Вы отправили текст")

async def message_handler_photo(update: Update, context):
    logger.info("Пользователь %s отправил фото.", update.effective_user.username)
    await update.message.reply_text("Вы отправили фото")

async def message_handler_video(update: Update, context):
    logger.info("Пользователь %s отправил видео.", update.effective_user.username)
    await update.message.reply_text("Вы отправили видео")

async def message_handler_audio(update: Update, context):
    logger.info("Пользователь %s отправил аудио сообщение.", update.effective_user.username)
    await update.message.reply_text("Вы отправили аудио сообщение")

def main():
    application = Application.builder().token(config.telegram.token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("quotation", quotation))
    application.add_handler(CommandHandler("price", price))
    application.add_handler(MessageHandler(filters.TEXT, message_handler_text))
    application.add_handler(MessageHandler(filters.PHOTO, message_handler_photo))
    application.add_handler(MessageHandler(filters.VIDEO, message_handler_video))
    application.add_handler(MessageHandler(filters.AUDIO, message_handler_audio))
    application.run_polling()

# async def main_test():
#     crypto = Crypto()
#     try:
#         response = await crypto.get_price("USD")
#         print(response)
#     except Exception as e:
#         print("Произошла ошибка при запросе цены.", '\n', e)   

if __name__ == '__main__':
    # asyncio.run(main_test())
    main()