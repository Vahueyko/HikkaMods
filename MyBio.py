#made by Vahueyko

from telethon import events
from .. import loader, utils

class MyBioMod(loader.Module):
    """Отправляет пользователю вашу биографию, которую вы сами напишете(.cfg)"""
    
    strings = {"name": "MyBio"}
        
    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "Биография1",
                None,
                lambda: "Напишите свое Био",
            ),
            loader.ConfigValue(
                "banner_url1",
                "https://i.yapx.cc/XQUzA.png",
                lambda: self.strings("_cfg_banner"),
                validator=loader.validators.Link(),
            ),
            loader.ConfigValue(
                "banner_url2",
                "https://i.yapx.cc/XQUzA.png",
                lambda: self.strings("_cfg_banner"),
                validator=loader.validators.Link(),
            ),
            loader.ConfigValue(
                "Биография2",
                None,
                lambda: "Напишите свое Био",
            ),
        )
        
           
    
    async def mbio1cmd(self, message):
        """Используй, чтобы прислать свою  первую биографию"""
        (
                    {"photo": self.config["banner_url1"]}
                    if self.config["banner_url1"]
                    else {}
                ),
        await utils.answer_file(
                message,
                self.config["banner_url1"],
                self.config["Биография1"],
            ),
    async def mbio2cmd(self, message):
        """Используй, чтобы прислать свою  вторую биографию"""
        (
                    {"photo": self.config["banner_url2"]}
                    if self.config["banner_url2"]
                    else {}
                ),
        await utils.answer_file(
                message,
                self.config["banner_url2"],
                self.config["Биография2"],
            ),
       
       
