from config import config
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from cryptocompare_api import Crypto
import logging

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def bot_close(context, e=None):
    if e:
        logger.error("Ошибка при запуске бота: %s", e)
    context.application.stop_running()
    

async def start(update: Update, context):
    logger.info("Пользователь %s запустил бота.", update.effective_user.username)
    try:
        await update.message.reply_text("Hello world")
    except Exception as e:
        bot_close(context, e=e)

async def ton_quotation(update: Update, context):
    logger.info("Пользователь %s запросил котировку.", update.effective_user.username)
    try:
        response = await Crypto().get_price("USD")
        await update.message.reply_text(f"${response}")
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
    application.add_handler(CommandHandler("ton", ton_quotation))
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