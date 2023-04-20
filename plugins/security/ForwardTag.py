import pyrogram
import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
import asyncio
from info import ADMINS

@Client.on_message(filters.media & filters.private & filters.incoming)
async def channel_tag(bot, message):
    try:
        chat_id = message.chat.id
        forward_msg = await message.copy(ADMINS)
        await message.delete()
        await asyncio.sleep(1)
#        await forward_msg.delete()
        
    except:
        await message.reply_text("Oops , Recheck My Admin Permissions & Try Again")
