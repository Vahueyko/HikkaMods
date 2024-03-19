# ---------------------------------------------------------------------------------
# Name: Greetings
# Description: Replies to "Hello"
# Author: Vahueyko
# Commands:
# For what 😍
# ---------------------------------------------------------------------------------

from telethon import events
from .. import loader, utils

@loader.tds
class GreetingMod(loader.Module):
    """Приветствует пользователя"""

    strings = {"name": "Приветствие"}

    async def greetcmd(self, message):
        """Используй .greet, чтобы поприветствовать пользователя"""
        sender = await message.get_sender()
        if sender:
            await utils.answer(message, "Привет, {}!".format(sender.first_name))
        else:
            await utils.answer(message, "Привет!")

    async def client_ready(self, client, db):
        await client.send_message("me", "Я запущен!")

    @loader.unrestricted
    @loader.ratelimit
    async def watcher(self, message):
        sender = await message.get_sender()
        if sender and "привет" in message.text.lower():
            await message.reply("Привет, {}!".format(sender.first_name))
