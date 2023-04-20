import pyrogram
import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
import asyncio
from info import ADMINS

@Client.on_message(filters.media & filters.private & filters.incoming)
async def channel_tag(bot, message):
    try:
        reference_id = True
        chat_id = message.chat.id
        forward_msg = await message.copy(ADMINS)
        await message.delete()
        await asyncio.sleep(1)
#        await forward_msg.delete()
        await bot.send_cached_media(
            chat_id =(ADMINS)
            chat_id=int(reference_id),
            from_chat_id=message.chat.id,
            message_id=message.id,
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton('🎁𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬🎁', url="http://t.me/nasrani_bot?startgroup=true")
                        ],
                        [
                            InlineKeyboardButton('📩𝐑𝐄𝐐𝐔𝐀𝐒𝐓 𝐆𝐑𝐎𝐔𝐏📩', url="https://t.me/NasraniMovies"),
                            InlineKeyboardButton('☘𝐍𝐄𝐖 𝐌𝐎𝐕𝐈𝐄𝐒☘', url="https://t.me/HDAZmovies")
                        ]                            
                    ]
                )
             )        
        
        
    except:
        await message.reply_text("Oops , Recheck My Admin Permissions & Try Again")
