import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    START_TXT = """<i><b>🎃 Helo {}, I'm <a href=https://telegram.me/{}>{}</a></i></b> \n\n<i><b>🎗I Can Provide You Any Movies, Web-Series, Anime, K-Dramas, Animation, etc.,</i></b>"""
    HELP_TXT = """<b>🔥 <u>Download & Watch Any Movie, Series, Anime etc., For Free 🤩</u> \n\n🎗[Group]: https://t.me/+lYD3tuR0P9szYzk9 \n\n🔆 Join The Above Group & Type The Movie/Series Name You Want👆</b>"""
    ABOUT_TXT = """<i><b>🥁 Follow These Steps To Connect Me To Your Group👇</b>

1. Click on "</i><i><b>Click Here To Add Me</b>" 
2. Select Your Group
3. Make Me Admin in Your Group
4. Send /connect in Your Group</i>"""    
    
    STATUS_TXT = """<b>🎗️ My Statistics 📲</b>
◉ <b>Total Files :</b> {}
◉ <b>Total Users :</b> {}
◉ <b>Total Chats :</b> {}
◉ <b>Used Storage :</b> {} 
◉ <b>Free Storage :</b> {}"""

    LOG_TEXT_G = """<b>#NewGroup</b>
<b>● Group »</b> {} 
<b>● ID »</b> <code>{}</code>
<b>● Total Members »</b> {}
<b>● Added By »</b> {}
"""
    LOG_TEXT_P = """<b>#NewUser</b>
◉ ID - <code>{}</code>
◉ Name - {}
"""
