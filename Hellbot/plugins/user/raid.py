import os
import sys
import asyncio
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message

from Hellbot.core.data import *


@Client.on_message(filters.command(["raid", "r"], ".") & (filters.me | filters.user(SUDO_USER)))
async def raid(app: Client, m: Message):  
      Hellbot = "".join(m.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Hellbot) == 2:
        counts = int(Hellbot[0])
        username = Hellbot[1]
        if not counts:
          await m.reply_text(f"RAID LIMIT NOT FOUND PLEASE GIVE COUNT!")
          return       
        if not username:
          await m.reply_text("you need to specify an user! Reply to any user or gime id/username")
          return
        try:
           user = await app.get_users(Hellbot[1])
        except:
           await m.reply_text("**Error:** User not found or may be deleted!")
           return
      elif m.reply_to_message:
        counts = int(Hellbot[0])
        try:
           user = await app.get_users(m.reply_to_message.from_user.id)
        except:
           user = m.reply_to_message.from_user 
      else:
        await m.reply_text("Usage: .raid count username or reply")
        return
      if int(m.chat.id) in GROUP:
         await m.reply_text("**Sorry !! i Can't Spam Here.**")
         return
      if int(user.id) in VERIFIED_USERS:
         await m.reply_text("I can't raid on my developer")
         return
      if int(user.id) in SUDO_USER:
         await m.reply_text("This guy is a sudo users.")
         return
      mention = user.mention
      for _ in range(counts): 
         r = f"{mention} {choice(RAID)}"
         await app.send_message(m.chat.id, r)
         await asyncio.sleep(0.3)


@Client.on_message(filters.command(["dmraid", "dmr"], ".") & (filters.me | filters.user(SUDO_USER)))
async def draid(app: Client, m: Message):  
      Hellbot = "".join(m.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Hellbot) == 2:
        counts = int(Hellbot[0])
        username = Hellbot[1]
        if not counts:
          await m.reply_text(f"RAID LIMIT NOT FOUND PLEASE GIVE COUNT!")
          return       
        if not username:
          await m.reply_text("you need to specify an user! Reply to any user or gime id/username")
          return
        try:
           user = await app.get_users(Hellbot[1])
        except:
           await m.reply_text("**Error:** User not found or may be deleted!")
           return
      elif m.reply_to_message:
        counts = int(Hellbot[0])
        try:
           user = await app.get_users(m.reply_to_message.from_user.id)
        except:
           user = m.reply_to_message.from_user 
      else:
        await m.reply_text("Usage: .dmraid count username or reply")
        return
      if int(user.id) in VERIFIED_USERS:
         await m.reply_text("I can't raid on my developer")
         return
      if int(user.id) in SUDO_USER:
         await m.reply_text("This guy is a sudo users.")
         return
      mention = user.mention
      await m.reply_text("Dm Raid started..")
      for _ in range(counts): 
         r = f"{choice(RAID)}"
         await app.send_message(user.id, r)
         await asyncio.sleep(0.3)
        
