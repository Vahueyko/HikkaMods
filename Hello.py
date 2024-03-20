# ---------------------------------------------------------------------------------
# Name: Greetings
# Description: Replies to "Hello"
# Author: Vahueyko
# Commands:
#  greeton
#  greetoff
# ---------------------------------------------------------------------------------

from telethon import events
from .. import loader, utils

valuegreet = False  # Устанавливаем значение переменной в начале

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

    async def greetoncmd(self, message):
        """Используй .greeton, чтобы включить приветствие"""
        global valuegreet
        valuegreet = True
        await utils.answer(message, "Приветствие включено!")

    async def greetoffcmd(self, message):
        """Используй .greetoff, чтобы выключить приветствие"""
        global valuegreet
        valuegreet = False
        await utils.answer(message, "Приветствие выключено!")

    async def client_ready(self, client, db):
        await client.send_message("me", "Я запущен!")

    @loader.unrestricted
    @loader.ratelimit
    async def watcher(self, message):
        global valuegreet  # Используем глобальную переменную
        sender = await message.get_sender()
        if valuegreet and sender and any(word in message.text.lower() for word in ["привет", "здаров", "ку"]):  # Проверяем значение переменной и текст сообщения
            await message.reply("Привет, {}!".format(sender.first_name))
