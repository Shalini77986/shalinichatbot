from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
import os
import re


API_ID = os.environ.get("API_ID", "none") 
API_HASH = os.environ.get("API_HASH", "none") 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "none") 
MONGO_URL = os.environ.get("MONGO_URL", "none")
BOT_IMAGE = os.environ.get("BOT_IMAGE", "none")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "none")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "none")
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "none")
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "none")


bot = Client(
    "V_Chat_Bot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]


@bot.on_message(filters.command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""**━━━━━━━━━━Ꮥʜꫝʟɪɴɪ━━━━━━━━━━━
💥 нєℓℓο τнιѕ ιѕ α αι ϲнατ ϐοτ 🌷.\n\n📌 Mʏ Nᴀᴍᴇ Is Ꮥʜꫝʟɪɴɪ cɦαƭ ɓσƭ🌟 𓂀 𝔹𝕦𝕥 𝕐𝕠𝕦 ℂ𝕒𝕟 ℂ𝕒𝕝𝕝 𝕄𝕖 𝕊𝕙𝕒𝕝𝕦 💖 \n\n🌷 I'ᴍ ᴀ Aʀᴛɪғɪᴄɪᴀʟ ɪɴᴛᴇʟʟɪɢᴇɴᴄᴇ ʙᴏᴛ 🌷\n\n /chatbot - [on|off] τнιѕ ϲοммαи∂ ιѕ οиℓγ ƒοя gяουρѕ
💞 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 » 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝
𝐄𝐧𝐣𝐨𝐲 𝐒𝐮𝐩𝐞𝐫 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 ❥︎𝐂𝐡𝐚𝐭.
━━━━━━━━━━Ꮥʜꫝʟɪɴɪ━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],
                [
                    InlineKeyboardButton(
                        "ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/ShaliniMusicBotSh"),
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/MUSIC_WORLD_SH")
                ],
                [
                    InlineKeyboardButton(
                        "💞ᴍᴀɪɴᴛᴀɪɴᴇʀ💞", url=f"https://t.me/shalini_shalu_69")
                ],
                
           ]
        ),
    )
    
    
@bot.on_message(filters.command(["/start", f"start@{BOT_USERNAME}", "/alive", ".alive", "#bikash", "#aditya"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""💥нєℓℓο τнιѕ ιѕ α αι ϲнατ ϐοτ  🌷.\n\n📌 Mʏ Nᴀᴍᴇ Is Ꮥʜꫝʟɪɴɪ cɦαƭ ɓσƭ🌟🇮🇳 \n\n🌷 I'ᴍ ᴀ Aʀᴛɪғɪᴄɪᴀʟ ɪɴᴛᴇʟʟɪɢᴇɴᴄᴇ ʙᴏᴛ 🌷\n\n🇦 🇳 🇾  🇵 🇷 🇴 🇧 🇱 🇪 🇲 ? [ᎡᎬᏢϴᎡͲ](https://t.me/{SUPPORT_GROUP})  🥀\n\n[ႮᏢᎠᎪͲᎬՏ](https://t.me/{UPDATES_CHANNEL}) 🌷\n\n /chatbot - [on|off]""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 💥 𝙳𝚘𝚗'𝚝 𝙾𝚙𝚎𝚗", url=f"https://t.me/music_world_sh")
                ]
            ]
        ),
    )



@bot.on_message(
    filters.command("chatbot off", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    vdb = MongoClient(MONGO_URL)    
    v = vdb["vDb"]["v"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                "💥 нєγ γου αяє иοτ α α∂мιи 💥"
            )
    is_v = v.find_one({"chat_id": message.chat.id})
    if not is_v:
        v.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"🌷 Ꮥʜꫝʟɪɴɪ ᏟᎻᎪͲ BOT ᎠᏆՏᎪᏴᏞᎬᎠ  🥀!\n\nᎪΝᎽ ᏢᎡϴᏴᏞᎬᎷ [Rᴇᴘᴏʀᴛ](https://t.me/{SUPPORT_GROUP})  🥀\n\n[ᴜᴘᴅᴀᴛᴇs](https://t.me/{UPDATES_CHANNEL}) 🌷")
    if is_v:
        await message.reply_text(f"🌷  Ꮥʜꫝʟɪɴɪ ᏟᎻᎪͲ ᏴϴͲ ᏆՏ ᎪᏞᎡᎬᎪᎠᎽ ᎠᏆՏᎪᏴᏞᎬᎠ  🥀!\n\nᎪΝᎽ ᏢᎡϴᏴᏞᎬᎷ [Rᴇᴘᴏʀᴛ](https://t.me/{SUPPORT_GROUP})  🥀\n\n[ᴜᴘᴅᴀᴛᴇs](https://t.me/{UPDATES_CHANNEL}) 🌷")
    

@bot.on_message(
    filters.command("chatbot on", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    vdb = MongoClient(MONGO_URL)    
    v = vdb["vDb"]["v"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_v = v.find_one({"chat_id": message.chat.id})
    if not is_v:           
        await message.reply_text(f"💥 Ꮥʜꫝʟɪɴɪ CʜᴀᴛBᴏᴛ Is Aʟʀᴇᴀᴅʏ Eɴᴀʙʟᴇᴅ 🌷!\n\nᎪΝᎽ ᏢᎡϴᏴᏞᎬᎷ [Rᴇᴘᴏʀᴛ](https://t.me/{SUPPORT_GROUP})  🥀\n\n[ᴜᴘᴅᴀᴛᴇs](https://t.me/{UPDATES_CHANNEL}) 🌷")
    if is_v:
        v.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"💥 Ꮥʜꫝʟɪɴɪ ᏟᎻᎪͲᏴϴͲ ᎬΝᎪᏴᏞᎬᎠ  🌷!\n\nᎪΝᎽ ᏢᎡϴᏴᏞᎬᎷ [Rᴇᴘᴏʀᴛ](https://t.me/{SUPPORT_GROUP})  🥀\n\n[ᴜᴘᴅᴀᴛᴇs](https://t.me/{UPDATES_CHANNEL}) 🌷")
    

@bot.on_message(
    filters.command("chatbot", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"** 𝐔𝐬𝐚𝐠𝐞 🌷 :**\n/chatbot [on|off] 𝐎𝐧𝐥𝐲 𝐆𝐫𝐨𝐮𝐩 🇮🇳 !\n\nᎪΝᎽ ᏢᎡϴᏴᏞᎬᎷ [Rᴇᴘᴏʀᴛ](https://t.me/{SUPPORT_GROUP})  🥀\n\n[ᴜᴘᴅᴀᴛᴇs](https://t.me/{UPDATES_CHANNEL}) 🌷")


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def vai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})
       if not is_v:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_v:                   
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def vstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})
       if not is_v:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_v:                    
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def vprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def vprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")
       
bot.run()
