import logging

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def bot_close(context, e=None):
    if e:
        logger.error("Экстренный выход\nError: %s", e)
    context.application.stop_running()

def print_dict_multi_price(d):
    result = ""
    try:
        for key, value in d.items():
            result += f"\n{key}"
            for x, y in value.items():
                result += f"\n    {"{:,.2f}".format(y)} {x}".replace(',', ' ')
            result += '\n'
    except Exception as e:
        logger.error("Ошибка %s в %s", e, __name__)
    return result
        