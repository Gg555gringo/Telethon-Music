from telethon import events, Button
from Zaid import Zaid
from Zaid.status import *
from Config import Config
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

@Zaid.on(events.callbackquery.CallbackQuery(data="admin"))
async def _(event):

    await event.edit(ADMIN_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])

@Zaid.on(events.callbackquery.CallbackQuery(data="play"))
async def _(event):

    await event.edit(PLAY_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])


ADMIN_TEXT = """
**✘Um módulo do qual os administradores do chat podem usar!**

‣ `?end` - Para terminar a transmissão de música.
‣ `?skip` - Para pular musicas acontecendo.
‣ `?pause` - Para pausar a transmissão.
‣ `?resume` - para retomar a transmissão.
‣ `?leavevc` - force o Userbot a sair do chat de voz (Às vezes entrou). 
‣ `?playlist` - para verificar as listas de reprodução. 
"""

PLAY_TEXT = """
**✘ Um módulo do qual os usuários do chat podem usar!**

‣ `?play` - To Play Audio from Else Responda ao arquivo de áudio. 
‣ `?vplay` - Para transmitir vídeos  (HEROKU_MODE > Doesn't support).
"""
