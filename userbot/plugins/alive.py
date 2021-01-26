#IMG CREDITS: 
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
ALIVE_IMG = "https://telegra.ph/file/a8cf9812c35f9c04eac27.jpg"
ALIVE_caption = "`TCLUserBot IS:` **ONLINE**\n\n"
ALIVE_caption += "**SYSTEM STATUS**\n\n"
ALIVE_caption += "`TELETHON VERSION:` **6.0.9**\n`Python:` **3.7.4**\n\n"
ALIVE_caption += "`DATABASE STATUS:` **Functional**\n\n"
ALIVE_caption += "**Current Branch** : `master`\n\n"
ALIVE_caption += "**TCL OS** : `3.14`\n\n"
ALIVE_caption += "**Current Sat** : `TCLUserBot Sat-2.95`\n\n"
ALIVE_caption += f"**My Boss** : {DEFAULTUSER} \n\n"
ALIVE_caption += "**Heroku Database** : `AWS - Working Properly`\n\n"
ALIVE_caption += "**Bot Made By @royalswillaspro** \n\n"
ALIVE_caption += "Copyright By [AKHILSIVA](t.me/royalswillaspro)\n\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def Ariana(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete()
    await borg.send_file(alive.chat_id, ALIVE_IMG,caption=ALIVE_caption)

@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def Ariana(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
