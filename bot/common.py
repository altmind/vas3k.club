from collections import namedtuple

import telegram
from django.conf import settings
from django.template import loader
from telegram import ParseMode

from bot.bot import bot, log

Chat = namedtuple("Chat", ["id"])

ADMIN_CHAT = Chat(id=settings.TELEGRAM_ADMIN_CHAT_ID)
CLUB_CHAT = Chat(id=settings.TELEGRAM_CLUB_CHAT_ID)
CLUB_CHANNEL = Chat(id=settings.TELEGRAM_CLUB_CHANNEL_ID)


def send_telegram_message(
    chat: Chat,
    text: str,
    parse_mode: ParseMode = telegram.ParseMode.HTML,
    disable_preview: bool = True,
    **kwargs
):
    if not bot:
        log.warning("No telegram token. Skipping")
        return

    log.info(f"Telegram: sending the message: {text}")

    return bot.send_message(
        chat_id=chat.id,
        text=text,
        parse_mode=parse_mode,
        disable_web_page_preview=disable_preview,
        **kwargs
    )


def send_telegram_image(
    chat: Chat,
    image_url: str,
    text: str,
    parse_mode: ParseMode = telegram.ParseMode.MARKDOWN,
    **kwargs
):
    if not bot:
        log.warning("No telegram token. Skipping")
        return

    log.info(f"Telegram: sending the image: {image_url} {text}")

    return bot.send_photo(
        chat_id=chat.id,
        photo=image_url,
        caption=text[:1024],
        parse_mode=parse_mode,
        **kwargs
    )


def remove_action_buttons(chat: Chat, message_id: str, **kwargs):
    try:
        return bot.edit_message_reply_markup(
            chat_id=chat.id,
            message_id=message_id,
            reply_markup=None,
            **kwargs
        )
    except telegram.error.BadRequest:
        log.info("Buttons are already removed. Skipping")
        return None


def render_html_message(template, **data):
    template = loader.get_template(f"telegram/{template}")
    return template.render({
        **data,
        "settings": settings
    })
