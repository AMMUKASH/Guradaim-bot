import os
import asyncio
import threading
from flask import Flask
from pymongo import MongoClient
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# --- EXPRESS/FLASK SERVER FOR RENDER ---
app = Flask(__name__)

@app.route('/')
def home():
    return "GcGuardianXbot is secured and running 24/7!"

def run_server():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# Start Flask server in a separate thread for Render Keep-Alive
threading.Thread(target=run_server, daemon=True).start()

# --- DATABASE SETUP (MONGODB) ---
MONGO_URL = "mongodb+srv://misssqn_db_user:Nova01@cluster0.6xxsrwq.mongodb.net/?retryWrites=true&w=majority"
try:
    mongo_client = MongoClient(MONGO_URL)
    db = mongo_client["GcGuardianXbot_DB"]
    users_col = db["users"]
    print("✨ MongoDB connected successfully!")
except Exception as e:
    print(f"⚠️ MongoDB Connection Error: {e}")
    users_col = None

# --- PYROGRAM TELEGRAM BOT CONFIGURATION ---
API_ID = 38138069
API_HASH = "2ed313ebcc45cbcf65d1fc736ec71681"
BOT_TOKEN = "8370603899:AAEzA-PyQ3T9_lwTQQYfLY3ACPnoRJ5cDrU"

bot = Client(
    "GcGuardianXbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# --- STYLISH STRINGS & TEMPLATES ---
START_TEXT = """
✨ **ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴜʟᴛʀᴀ ɢᴜᴀʀᴅɪᴀɴs ʙᴏᴛ** ✨
━━━━━━━━━━━━━━━━━━━━━━━━
👋 ʜᴇʟʟᴏ! ɪ ᴀᴍ ʏᴏᴜʀ ᴀʟʟ-ɪɴ-ᴏɴᴇ sᴇᴄᴜʀɪᴛʏ & ɢʀᴏᴜᴘ ᴘʀᴏᴛᴇᴄᴛᴏʀ ʙᴏᴛ. ɪ ᴄᴀɴ sᴀᴠᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘs ғʀᴏᴍ sᴘᴀᴍᴍᴇʀs, ᴀʙᴜsɪᴠᴇ ᴜsᴇʀs, ᴀɴᴅ ᴜɴᴡᴀɴᴛᴇᴅ ʟɪɴᴋs.

⚡ **ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs:** ᴀᴄᴛɪᴠᴇ ᴀɴᴅ ʀᴜɴɴɪɴɢ 24/7
👑 **ᴏᴡɴᴇʀ:** @CoderNova
📢 **ᴜᴘᴅᴀᴛᴇs:** [ɴᴏᴠᴀ sᴜᴘᴘᴏʀᴛ](https://t.me/NovaBot_Support)

👇 *ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ᴇxᴘʟᴏʀᴇ ᴍʏ ᴘᴏᴡᴇʀғᴜʟ ᴍᴏᴅᴜʟᴇs:*
"""

HELP_TEXT = """
📚 **ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴘ ᴍᴇɴᴜ**
━━━━━━━━━━━━━━━━━━━━━━━━
ʜᴇʀᴇ ʏᴏᴜ'ʟʟ ғɪɴᴅ ᴅᴇᴛᴀɪʟs ғᴏʀ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴜɢɪɴs ᴀɴᴅ ғᴇᴀᴛᴜʀᴇs. ALL ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋ ɪɴ ʙᴏᴛʜ **ᴘᴜʙʟɪᴄ ɢʀᴏᴜᴘs** ᴀɴᴅ **ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛs**.

👇 *ᴛᴀᴘ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ᴠɪᴇᴡ ʜᴇʟᴘ ғᴏʀ ᴇᴀᴄʜ ᴍᴏᴅᴜʟᴇ:*
"""

GUIDE_TEXT = """
📖 **ᴜʟᴛʀᴀ ɢᴜᴀʀᴅɪᴀɴ ᴜsᴇʀ ɢᴜɪᴅᴇ**
━━━━━━━━━━━━━━━━━━━━━━━━
1️⃣ **ʜᴏᴡ ᴛᴏ ᴜsᴇ ɪɴ ɢʀᴏᴜᴘs:**
   * ᴀᴅᴅ @GcGuardianXbot ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
   * ᴘʀᴏᴍᴏᴛᴇ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀɴ **ᴀᴅᴍɪɴ** ᴡɪᴛʜ ᴀʟʟ ᴘᴇʀᴍɪssɪᴏɴs.
   * ᴛʜᴇ ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ sᴛᴀʀᴛ ᴍᴏɴɪᴛᴏʀɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

2️⃣ **ᴄᴏᴍᴍᴀɴᴅs:**
   * `/start` - ᴏᴘᴇɴ ᴛʜᴇ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇɴᴜ.
   * `/help` - ᴏᴘᴇɴ ᴛʜᴇ ɪɴᴛᴇʀᴀᴄᴛɪᴠᴇ ʜᴇʟᴘ panel.
   * `/guide` - ʀᴇᴀᴅ ᴛʜɪs sᴇᴛᴜᴘ ᴍᴀɴᴜᴀʟ.

🛡️ *ɴᴇᴇᴅ ᴍᴏʀᴇ ʜᴇʟᴘ? ᴄᴏɴᴛᴀᴄᴛ @CoderNova.*
"""

DEFAULT_IMAGE = "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1000"

# --- KEYBOARDS ---
START_KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("📚 ʜᴇʟᴘ ᴍᴇɴᴜ", callback_data="open_help"), InlineKeyboardButton("📖 ᴜsᴇʀ ɢᴜɪᴅᴇ", callback_data="open_guide")],
    [InlineKeyboardButton("👑 ᴏᴡɴᴇʀ", url="https://t.me/CoderNova"), InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/NovaBot_Support")]
])

MAIN_HELP_KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("🚫 Abuse", callback_data="help_abuse"), InlineKeyboardButton("✅ Approvals", callback_data="help_approvals"), InlineKeyboardButton("💬 MsgDelete", callback_data="help_msgdelete")],
    [InlineKeyboardButton("🛡️ BioMode", callback_data="help_biomode"), InlineKeyboardButton("📝 Edit", callback_data="help_edit"), InlineKeyboardButton("🔗 Links", callback_data="help_links")],
    [InlineKeyboardButton("✒️ LongMode", callback_data="help_longmode"), InlineKeyboardButton("🎬 Media", callback_data="help_media"), InlineKeyboardButton("🤖 Bot Promo", callback_data="help_botpromo")],
    [InlineKeyboardButton("📩 Forward", callback_data="help_forward"), InlineKeyboardButton("# Hashtags", callback_data="help_hashtags"), InlineKeyboardButton("📞 Phone", callback_data="help_phone")],
    [InlineKeyboardButton("🏠 ʙᴀᴄᴋ ʜᴏᴍᴇ", callback_data="back_to_start"), InlineKeyboardButton("➡️ ɴᴇxᴛ", callback_data="action_next_page")]
])

BACK_TO_MENU_KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("🔙 ʙᴀᴄᴋ ᴛᴏ ʜᴇʟᴘ", callback_data="open_help")]
])

BACK_TO_START_KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("🔙 ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="back_to_start")]
])

# --- COMMAND HANDLERS ---
@bot.on_message(filters.command("start"))
async def start_command(client, message):
    try:
        if users_col:
            user_id = message.from_user.id
            if not users_col.find_one({"user_id": user_id}):
                users_col.insert_one({"user_id": user_id, "username": message.from_user.username})
            
        await message.reply_photo(
            photo=DEFAULT_IMAGE,
            caption=START_TEXT,
            reply_markup=START_KEYBOARD
        )
    except Exception as e:
        print(f"Error in start command: {e}")

@bot.on_message(filters.command("help"))
async def help_command(client, message):
    try:
        await message.reply_photo(
            photo=DEFAULT_IMAGE,
            caption=HELP_TEXT,
            reply_markup=MAIN_HELP_KEYBOARD
        )
    except Exception as e:
        print(f"Error in help command: {e}")

@bot.on_message(filters.command("guide"))
async def guide_command(client, message):
    try:
        await message.reply_photo(
            photo=DEFAULT_IMAGE,
            caption=GUIDE_TEXT,
            reply_markup=BACK_TO_START_KEYBOARD
        )
    except Exception as e:
        print(f"Error in guide command: {e}")

# --- CALLBACK HANDLERS FOR INTERACTIVE BUTTONS ---
MODULES_DATA = {
    "help_abuse": ("ᴀɴᴛɪ-ᴀʙᴜsᴇ", "⛔ **ᴀɴᴛɪ-ᴀʙᴜsᴇ sʏsᴛᴇᴍ**\n\nAutomated scanner that blocks profanity, toxic slurs, and bad words. Sends warnings or automatically mutes violators to maintain clean conversations."),
    "help_approvals": ("ᴀᴘᴘʀᴏᴠᴀʟs", "✅ **ᴍᴇᴍʙᴇʀ ᴀᴘᴘʀᴏᴠᴀʟs**\n\nAllows admins to whitelist special members. Approved accounts can completely bypass spam triggers, strict link filters, and restrictions."),
    "help_msgdelete": ("ᴍsɢ ᴅᴇʟᴇᴛᴇ", "💬 **ᴍᴇssᴀɢᴇ ᴘᴜʀɢᴇ / ᴅᴇʟᴇᴛᴇ**\n\nFast administrative tool to wipe target spam messages or instantly clear recent chat history in massive bursts."),
    "help_biomode": ("ʙɪᴏ ᴍᴏᴅᴇ", "🛡️ **ʙɪᴏ-ᴍᴏᴅᴇ sᴄᴀɴɴᴇʀ**\n\nAutomatically checks profiles of new incoming members. Instantly kicks or bans users carrying advertising tokens or malicious links in their bio."),
    "help_edit": ("ᴀɴᴛɪ-ᴇᴅɪᴛ", "📝 **ᴀɴᴛɪ-ᴍᴇssᴀɢᴇ ᴇᴅɪᴛ**\n\nLogs or prevents users from editing messages to sneak past chat filters or bad-word logs after posting."),
    "help_links": ("ʟɪɴᴋ ʙʟᴏᴄᴋᴇʀ", "🔗 **ɪɴsᴛᴀɴᴛ ʟɪɴᴋ ғɪʟᴛᴇʀ**\n\nStrictly terminates and blocks external links, social handles, and invite links shared by regular members."),
    "help_longmode": ("ʟᴏɴɢ ᴍᴏᴅᴇ", "✒️ **ʟᴏɴɢ ᴛᴇxᴛ ᴅᴇᴛᴇᴄᴛᴏʀ**\n\nIdentifies and purges large paragraphs or walls-of-text intended to crash Telegram viewports or freeze group scrolls."),
    "help_media": ("ᴍᴇᴅɪᴀ ᴄᴏɴᴛʀᴏʟ", "🎬 **ᴍᴇᴅɪᴀ ʀᴇsᴛʀɪᴄᴛɪᴏɴs**\n\nAllows lock downs on dedicated attachments like voice logs, video stickers, high-capacity animations, or massive files dynamically."),
    "help_botpromo": ("ʙᴏᴛ ᴘʀᴏᴍᴏ", "🤖 **ʙᴏᴛ ᴘʀᴏᴍᴏᴛɪᴏɴ sᴇᴛᴛɪɴɢs**\n\nAllows the owner (@CoderNova) to schedule operational announcements or promotional links inside targeted chats."),
    "help_forward": ("ᴀɴᴛɪ-ғᴏʀᴡᴀʀᴅ", "📩 **ᴀɴᴛɪ-ғᴏʀᴡᴀʀᴅ ғɪʟᴛᴇʀ**\n\nDeletes materials or media posts forwarded straight from unrelated or external telegram channels."),
    "help_hashtags": ("ʜᴀsʜᴛᴀɢs", "#️⃣ **ʜᴀsʜᴛᴀɢ ᴍᴏɴɪᴛᴏʀ**\n\nCleans out trending tag spams, bulk metadata hashtags, and commercial promotion tag strings."),
    "help_phone": ("ᴘʜᴏɴᴇ ғɪʟᴛᴇʀ", "📞 **ᴘʀɪᴠᴀᴄʏ / ᴘʜᴏɴᴇ sʜɪᴇʟᴅ**\n\nInstantly intercepts and deletes phone contact numbers, private info, or vCards leaked in the chat room.")
}

@bot.on_callback_query()
async def handle_callbacks(client, callback_query: CallbackQuery):
    data = callback_query.data
    
    if data in MODULES_DATA:
        title, desc = MODULES_DATA[data]
        await callback_query.answer()
        await callback_query.edit_message_caption(
            caption=desc,
            reply_markup=BACK_TO_MENU_KEYBOARD
        )
        
    elif data == "open_help":
        await callback_query.answer()
        await callback_query.edit_message_caption(
            caption=HELP_TEXT,
            reply_markup=MAIN_HELP_KEYBOARD
        )
        
    elif data == "open_guide":
        await callback_query.answer()
        await callback_query.edit_message_caption(
            caption=GUIDE_TEXT,
            reply_markup=BACK_TO_START_KEYBOARD
        )
        
    elif data == "back_to_start":
        await callback_query.answer()
        await callback_query.edit_message_caption(
            caption=START_TEXT,
            reply_markup=START_KEYBOARD
        )
        
    elif data == "action_next_page":
        await callback_query.answer("ᴘᴀɢᴇ 2 ғᴇᴀᴛᴜʀᴇs ᴀʀᴇ ᴄᴜʀʀᴇɴᴛʟʏ ᴜɴᴅᴇʀ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ!", show_alert=True)

# --- ASYNC BOT LAUNCHER TO FIX RUNTIME LOOPS ---
async def main():
    print("🚀 GcGuardianXbot is firing up...")
    await bot.start()
    print("✨ Bot is fully online and monitoring!")
    # Keeps loop active until stop event
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
