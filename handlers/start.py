from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USERNAME


@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**Hello 👋🏻 {}!**\n\nI **Can Play Music In Voice Chats of Telegram Groups.**I Have A **lot of cool feature that will amaze You!**\n\n**Click /cmdlist For More Help On My Usage ❤**".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("⚜ 𝐎𝐖𝐍𝐄𝐑 ⚜", url="https://t.me/OFFICIAL_SAMBODHIRAJ")
            ],[
            InlineKeyboardButton("🔱 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🔱", url="https://t.me/TEAM_HEARTLESS_POLICE_OP"),
            InlineKeyboardButton("🔱 𝐂𝐎-𝐎𝐖𝐍𝐄𝐑 🔱", url="https://t.me/HELLL_BOYYYY")
            ],[
            InlineKeyboardButton("♫︎ 𝐕𝐂 𝐏𝐋𝐀𝐘𝐄𝐑 ♫︎", url="https://t.me/TEAMHEARTLESSVCPLAYER")
            ]]
        ),
        disable_web_page_preview=True
    )
        
@Client.on_message(filters.command(["start", "start@TEAMHERTLESPMUSICBOT"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="**ZINDA HU BE 🙄**",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text="🔱 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏 🔱", url="https://t.me/TEAM_HEARTLESS_POLICE_OP")
            ]]
        )
    )


@Client.on_message(filters.command(["cmdlist", "start@TEAMHERTLESPMUSICBOT"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**Group Music Bot : Help Menu**

__× First Add Me To Your Group..
× Promote Me As Admin In Your Group With All Permission..__

**🏷 Common Commands.**

• `/play` - Song Name : __Plays Via Youtube__
• `/dplay` - Song Name : __Play Via Deezer__
• `/splay` - Song Name : __Play Via Jio Saavn__
• `/playlist` - __Show now playing list__
• `/current` - __Show now playing__

• `/song` - Song Name : __Get The Song From YouTube__
• `/vid` - Video Name : __Get The Video From YouTube__
• `/deezer` - song name : __download songs you want quickly via deezer__
• `/saavn` - song name : __download songs you want quickly via saavn__
• `/search` - YouTube Title : __(Get YouTube Search Query)__

**🏷 Group Admin Commands.**

• `/skip` : __Skips Music__
• `/pause` : __Pause Playing Music__
• `/resume` : __Resume Playing Music__
• `/end` : __Stops playing Music__
• `/reload` : __Reloads Admin List__
• `/userbotjoin` : __Assistant Joins The Group__
• `/userbotleave` : __Assistant Leaves From The Group.__""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🔱 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏 🔱", url="https://t.me/TEAM_HEARTLESS_POLICE_OP")
              ]]
          )
      )
