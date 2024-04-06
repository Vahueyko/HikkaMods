#made by Vahueyko
# а смогут ли червячки слизарио, заполсти в очко

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
                "https://i.yapx.cc/XTqIC.png",
                lambda: self.strings("_cfg_banner"),
                validator=loader.validators.Link(),
            ),
            loader.ConfigValue(
                "banner_url2",
                "https://i.yapx.cc/XTqIC.png",
                lambda: self.strings("_cfg_banner"),
                validator=loader.validators.Link(),
            ),
            loader.ConfigValue(
                "Биография2",
                None,
                lambda: "Напишите свое Био",
            ),
            loader.ConfigValue(
                "banner_url3",
                "https://i.yapx.cc/XTqIC.png",
                lambda: self.strings("_cfg_banner"),
                validator=loader.validators.Link(),
            ),
            loader.ConfigValue(
                "Биография3",
                None,
                lambda: "Напишите свое Био",
            ),
            loader.ConfigValue(
                "banner_url4",
                "https://i.yapx.cc/XTqIC.png",
                lambda: self.strings("_cfg_banner"),
                validator=loader.validators.Link(),
            ),
            loader.ConfigValue(
                "Биография4",
                None,
                lambda: "Напишите свое Био",
            ),
        )
        
           
    
    async def mbio1cmd(self, message):
        """Используй, чтобы прислать свою первую биографию"""
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
        """Используй, чтобы прислать свою вторую биографию"""
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
    async def mbio3cmd(self, message):
        """Используй, чтобы прислать свою третью биографию"""
        (
                    {"photo": self.config["banner_url3"]}
                    if self.config["banner_url3"]
                    else {}
                ),
        await utils.answer_file(
                message,
                self.config["banner_url3"],
                self.config["Биография3"],
            ),
    async def mbio4cmd(self, message):
        """Используй, чтобы прислать свою четвёртую биографию"""
        (
                    {"photo": self.config["banner_url4"]}
                    if self.config["banner_url4"]
                    else {}
                ),
        await utils.answer_file(
                message,
                self.config["banner_url4"],
                self.config["Биография24"],
            ),   
# не кто мой код читать не будет, так что я его комментировать могу, как только захочу
# Secure, Contain, Protect — «Обезопасить, Удержать, Сохранить» или Special Containment Procedures — «Особые Условия Содержания») — вымышленная исследовательская организация, являющаяся предметом одноимённого проекта совместного веб-творчества, в русском переводе также известная просто как Фонд или Организация.

#Сегодня поиграю я в майнкрафт!
#С рассвета до глубокой ночи
#Наружу выходить мне лень
#Пусть даже там отличный день
#Сегодня поиграю я в майнкрафт!
#Ммм
#Включаю компьютер, запустилась игра
#Со мной газировка, крипов жарить пора
#Меня им сегодня не одолеть, нет!
#Спешу я свой домик построить
#Пока не появилась передо мной «game over» строка
#Нет никого меня сильней!
#Оу-у, так и есть, да, так и есть, о да, ты мне поверь!
#Сегодня поиграю я в майнкрафт!
#С рассвета до глубокой ночи
#Наружу выходить мне лень
#Пусть даже там отличный день
#Сегодня поиграю я в майнкрафт!
#Только в майнкрафт
#У, у-у, у, у-у, угу-угу-угу
#Только в майнкрафт
#У, у-у, у, у-у, угу-угу-угу
#А завтра накопаю немного бриллиантов
#С железной киркой ты крутой без вариантов
#Вот это прокричу охренеть! (Оу, охренеть!)
#Копну в глубину, много плюшек найду
#И Notch’a я точно не подведу
#Пускай нет шансов встретится с ним
#Но-о, так и есть, да, так и есть, о да, ты мне поверь!
#Сегодня поиграю я в майнкрафт!
#С рассвета до глубокой ночи
#Наружу выходить мне лень
#Пусть даже там отличный день
#Сегодня поиграю я в майнкрафт!
#От счастья не завизжу, восторга не покажу
#Не, не, не, не-не, не, не-не, не
#Пойду приключаться опять, себя только бы не взорвать
#Е, е-е, е-е, е-е-е, е
#Ооо
#Сегодня поиграю я в майнкрафт!
#С рассвета до глубокой ночи
#Наружу выходить мне лень
#Пусть даже там отличный день
#Сегодня поиграю я в майнкрафт!
#Только в майнкрафт
#У, у-у, у, у-у, угу-угу-угу
#Только в майнкрафт
