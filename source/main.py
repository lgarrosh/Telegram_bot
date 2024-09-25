from config import config
from telegram import Update
from telegram.ext import Application, CommandHandler
from resources import params
from cryptocompare_api import Crypto


async def start(update: Update, context):
    # await update.message.reply_text('Привет! Я твой бот.')
    try:
        await update.message.reply_text(str(type(context)))
        await update.message.reply_text(str(type(update)))
        await update.message.reply_text(str(context.args))
    except Exception as e:
        await update.message.reply_text(str(e))
        exit(1)

async def ton_quotation(update: Update, context):
    crypto = Crypto()
    try:
        response = await crypto.get_price("USD")
        await update.message.reply_text(f"${response}")
    except Exception as e:
        print("Произошла ошибка при запросе цены.", '\n', e)        

def main():
    application = Application.builder().token(config.telegram.token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ton", ton_quotation))
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