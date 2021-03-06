from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_USERNAME


@Client.on_message(filters.command(["start", "start@MemoriesMusicBot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**Hello ππ» {}!**\n\nI **Can Play Music In Voice Chats of Telegram Groups.**I Have A **lot of cool feature that will amaze You!**\n\n**Click /cmdlist For More Help On My Usage β€**".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("β π°π³π³ ππΎ ππΎππ πΆππΎππΏ β", url="https://t.me/MemoriesMusicBot?startgroup=true")
            ],[
            InlineKeyboardButton("π¬ πΆππΎππΏ", url="https://t.me/Team_Memories_Support"),
            InlineKeyboardButton("π£ π²π·π°π½π½π΄π»", url=f"https://t.me/Team_Memories") 
            ],[
            InlineKeyboardButton("π π³π΄ππ΄π»πΎπΏπ΄π ", url="https://t.me/Memory_XY")
            ]]
        ),
        disable_web_page_preview=True
    )
        
@Client.on_message(filters.command(["start", "start@MemoriesMusicBot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="**πΌπ΄πΌπΎππΈπ΄π πΌπππΈπ² π±πΎπ πΈπ πΎπ½π»πΈπ½π΄ β**",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text="ποΈ Support Group ποΈ", url="https://t.me/Team_Memories_Support")
            ]]
        )
    )


@Client.on_message(filters.command(["cmdlist", "start@MemoriesMusicBot"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**πΌπ΄πΌπΎππΈπ΄π πΌπππΈπ² π±πΎπ : π·π΄π»πΏ πΌπ΄π½π**

__Γ π΅πΈπππ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ..
Γ πΏππΎπΌπΎππ΄ πΌπ΄ π°π π°π³πΌπΈπ½ πΈπ½ ππΎππ πΆππΎππΏ ππΈππ· π°π»π» πΏπ΄ππΌπΈπππΈπΎπ½..__

**π· ππ¨π¦π¦π¨π§ ππ¨π¦π¦ππ§ππ¬.**

β’ `/play` <song name> - play song you requested
β’ `/playlist` - Show now playing list
β’ `/current` - Show now playing
β’ `/song` <song name> - download songs you want quickly
β’ `/search` <query> - search videos on youtube with details
β’ `/vid` <song name> - download videos you want quickly

**π· ππ«π¨π?π© πππ¦π’π§ ππ¨π¦π¦ππ§ππ¬.**

β’ `/player` - open music player settings panel
β’ `/pause` - pause song play
β’ `/resume` - resume song play
β’ `/skip` - play next song
β’ `/end` - stop music play
β’ `/userbotjoin` - invite assistant to your chat
β’ `/userbotleave` - remove assistant from your chat
β’ `/reload` - Refresh admin list
 : __https:/t.me/Team_Memories__""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="ποΈ Support Group ποΈ", url="https://t.me/Team_Memories_Support")
              ]]
          )
      )
