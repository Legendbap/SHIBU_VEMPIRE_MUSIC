from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
❥ ωєℓ¢σмє тσ тєαм ɾιყα 

❥ ʀᴇᴘᴏ ᴄʜᴀᴀʜɪʏʀ ᴛᴏ ʙᴏᴛ ᴋᴏ 

❥ 3 ɢᴄ ᴍᴀɪ ᴀᴅᴅ ᴋᴀʀ ᴋᴇ 

❥ ᴀᴅᴍɪɴ ʙᴀɴᴏ ᴀᴜʀ sᴄʀᴇᴇɴsʜᴏᴛ 
     
❥ ᴏᴡɴᴇʀ ᴋᴏ ᴅᴏ ғɪʀ ʀᴇᴘᴏ ᴍɪʟ sᴀᴋᴛɪ ʜᴀɪ 

"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("♡ α∂∂ иσω ♡", url=f"https://t.me/NIKKI_MUSIC_ROBOT?startgroup=true")
        ],
        [
          InlineKeyboardButton("ѕυρρσɾƚ", url="https://t.me/SAIM_WORLD"),
          InlineKeyboardButton("⌯꯭ 𝐬͟ ꯭⋏꯭ ꯭𝖎 ꯭ ꯭ᴍ͟🥂꯭ 𝗫꯭ ꯭ᴅ ꯭꯭-//꯭- ִֶָ ꯭꯭꯭݁🥀꯭ ", url="https://t.me/DADDY_SAIM"),
          ],
               [
                InlineKeyboardButton("ᴏᴛʜᴇʀ ʙᴏᴛs", url=f"https://t.me/xyz_own_world"),
],
[
InlineKeyboardButton("ᴄʜᴇᴄᴋ", url=f"https://t.me/NIKKI_MUSIC_ROBOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/ltwmch.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
