import asyncio
import logging
import time
import json

REFRESH_DELAY = 3600  # SECONDS

logger = logging.getLogger(__name__)
loop = asyncio.get_event_loop()

ru = {}
en = {}
uz = {}

try:
    ru: dict = json.load(open("locales/ru/messages.json"))
    en: dict = json.load(open("locales/en/messages.json"))
    uz: dict = json.load(open("locales/uz/messages.json"))
except (FileNotFoundError, TypeError):
    logger.error("Locales was not downloaded")

ASK_LANG_TEXT_STR = "Tilni tanlang. Выберите язык. Choose language:"


def get_var_for_lang(key, lang: str = 'ru', default="...") -> str or dict:
    if lang is None:
        lang = 'ru'

    try:
        if key == "langChoose":
            return ASK_LANG_TEXT_STR

        elif lang == "en":
            return en.get(key, default)

        elif lang == "ru":
            return ru.get(key, default)

        elif lang == "uz":
            return uz.get(key, default)

    except (IOError, BlockingIOError, Exception) as error:
        time.sleep(0.01)
        logger.error(error)
        return get_var_for_lang(key, lang, default)


async def value_refresher():
    await asyncio.sleep(REFRESH_DELAY)
    try:
        global ru, en, uz
        ru = json.load(open("locales/ru/messages.json"))
        en = json.load(open("locales/en/messages.json"))
        uz = json.load(open("locales/uz/messages.json"))
    except FileNotFoundError:
        logger.error("Locales was not downloaded")


loop.create_task(value_refresher())