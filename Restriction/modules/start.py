from pyrogram import filters
from Restriction import app
from Restriction.core import script
from Restriction.core.func import subscribe
from Restriction.modules.callbacks import buttons
from Restriction.core.multi_func import *
from Restriction.core.more_func import reffer_verified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


@app.on_message(filters.command("start") & filters.private)
async def start(_, message):
    joined = await subscribe(_, message)
    if joined == 1:
        return

    if message.text.startswith("/start Verify"):
        await verification_accepter(_, message)
        return 

    if message.text.startswith("/start Referral"):
        reffer_id = message.text.split("_")[1]
        await reffer_verified(_, message, int(reffer_id))
        return 
    else:
        # 🎨 Custom UI Buttons for Better User Interaction
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("💻 ADMIN PANEL 💻", callback_data="admin_panel")],
            [InlineKeyboardButton("🙎‍♂️ ADMIN 🙎‍♂️", callback_data="admin"), 
             InlineKeyboardButton("❤️ TUTORIAL ❤️", callback_data="tutorial")],
            [InlineKeyboardButton("📄 FEATURES 📄", callback_data="features"),
             InlineKeyboardButton("🚀 ABOUT BOT 🚀", callback_data="about")],
            [InlineKeyboardButton("❌ CLOSE ❌", callback_data="close")]
        ])

        await message.reply_photo(
            photo="https://i.imghippo.com/files/TvnJ4931gM.jpg",
            caption=script.START_TXT.format(message.from_user.first_name),
            reply_markup=keyboard
        )

# ✅ Handling Button Clicks from Users
@app.on_callback_query()
async def button(client, callback_query):
    data = callback_query.data

    if data == "admin_panel":
        await callback_query.message.edit_text("⚙️ **Admin Panel:**\nManage bot settings here.", reply_markup=None)
    elif data == "admin":
        await callback_query.message.edit_text("👤 **Admin Contact:**\nReach out to the admin for support.")
    elif data == "tutorial":
        await callback_query.message.edit_text("📖 **Tutorial:**\nHere’s how to use this bot effectively.")
    elif data == "features":
        await callback_query.message.edit_text("📋 **Features:**\n1️⃣ Save Media\n2️⃣ Restrict Users\n3️⃣ Auto Forward")
    elif data == "about":
        await callback_query.message.edit_text("🤖 **About Bot:**\nThis bot is created for saving restricted media.")
    elif data == "close":
        await callback_query.message.delete()  # Deletes the message when closed

# ✅ Run the Bot
app.run()
