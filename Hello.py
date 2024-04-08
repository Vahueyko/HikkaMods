# моя мать раняла меня в детстве

from telethon import events
from .. import loader, utils

class GreetingMod(loader.Module):
    """Приветствует пользователя"""
    
    strings = {"name": "GreetMod"}

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
        if chat_id in self.greet_settings:
            del self.greet_settings[chat_id]
            await utils.answer(message, "Приветствие выключено в этом чате!")
        else:
            await utils.answer(message, "Приветствие уже выключено в этом чате!")

    async def watcher(self, message):
        chat_id = message.chat_id
        if self.greet_settings.get(chat_id, False) and sender and any(word in message.text.lower() for word in ["привет", "здаров", "ку", "пр"]):
            await message.reply("Привет, {}!".format(sender.first_name))
