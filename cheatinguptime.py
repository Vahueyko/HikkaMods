# meta developer: @VahueykoMod
# * |           V A H U E Y K O                        
# * |           © 2024 Vahueyko
from hikkatl.types import Message
from .. import loader, utils

@loader.tds
class CheatingUptime(loader.Module):
    """unfair uptime"""
    strings = {"name": "CheatingUptime"}

    async def addumcmd(self, message: Message):
        """.addum <minutes>"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "no args")        
        try:
            args = float(args)
        except (ValueError, TypeError):
            await utils.answer(message, "numbers pls")
        
        utils.init_ts -= args * 60
        await utils.answer(message, "Ready")
        
    async def adduhcmd(self, message: Message):
        """.adduh <hours>"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "no args")        
        try:
            args = float(args)
        except (ValueError, TypeError):
            await utils.answer(message, "numbers pls")
        
        utils.init_ts -= args * 60 * 60
        await utils.answer(message, "Ready")
        
    async def delumcmd(self, message: Message):
        """.delum <minutes>"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "no args ю")        
        try:
            args = float(args)
        except (ValueError, TypeError):
            await utils.answer(message, "numbers pls")
        
        utils.init_ts += args * 60
        await utils.answer(message, "Ready")
        
    async def deluhcmd(self, message: Message):
        """.deluh <hours>"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "no args")        
        try:
            args = float(args)
        except (ValueError, TypeError):
            await utils.answer(message, "numbers pls")
        
        utils.init_ts += args * 60 * 60
        await utils.answer(message, "Ready")
