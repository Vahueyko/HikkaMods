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

class GreetingMod(loader.Module):
    """Приветствует пользователя"""
    
strings = {"name": "autogreet"}

    def __init__(self):
        self.greet_settings = {}  # Привязка к чату

    async def greetcmd(self, message):
        """Используй .greet, чтобы поприветствовать пользователя"""
        await self._greet(message)

    async def greetoncmd(self, message):
        """Используй .greeton, чтобы включить приветствие"""
        chat_id = message.chat_id
        self.greet_settings[chat_id] = True
        await utils.answer(message, "Приветствие включено в этом чате!")

    async def greetoffcmd(self, message):
        """Используй .greetoff, чтобы выключить приветствие"""
        chat_id = message.chat_id
        self.greet_settings[chat_id] = False
        await utils.answer(message, "Приветствие выключено в этом чате!")

    async def watcher(self, message):
        sender = await message.get_sender()
        if not sender:
            return
        chat_id = message.chat_id
        if self.greet_settings.get(chat_id, False) and sender and any(word in message.text.lower() for word in ["привет", "здаров", "ку", "пр"]):
            await message.reply("Привет, {}!".format(sender.first_name))
