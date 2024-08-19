#made by Vahueyko

from telethon import events
from .. import loader, utils

class loggermod(loader.Module):
    """Поможет вам в нужной ситуации😘"""

    strings = {"name": "LoggerMod"}

    def __init__(self):
        self.logvalue = {}
      
    async def logstartcmd(self, message):
        """Используй, чтобы включить отслеживание сообщений в этом чате"""
        chat_id = message.chat_id
        self.logvalue[chat_id] = True
        await message.delete()

    async def logstopcmd(self, message):
        """Используй, чтобы выключить отслеживание сообщений в этом чате"""
        chat_id = message.chat_id
        self.logvalue[chat_id] = False
        await message.delete()

    async def watcher(self, message):
        chat_id = message.chat_id
        if self.logvalue.get(chat_id, False):  # Проверка
                # Пересылка
            await message.forward_to("me")
