import asyncio
from datetime import datetime
from pytz import timezone
from pyrogram import Client, filters
from config import api_id, api_hash, admins
from pyrogram.errors import PeerIdInvalid, UserAlreadyParticipant, UserNotParticipant
from pyrogram.raw import functions
# @Sourrce_kade
app = Client("my_new_account", api_id=api_id, api_hash=api_hash)

admin_ids = set(admins)

update_enabled = False
update_bio_enabled = False
always_online_enabled = False
update_emoji_enabled = False
last_minute = None
original_name = None

iran_tz = "Asia/Tehran"

# لیست اموجی‌ها
emoji_list = ["😊", "😂", "😍", "😒", "😭", "😡", "🥺", "😱", "😴", "🤔", "🗿", "🥷", "👑", "💸", "😐", "🦁", "🥺"]

def admin_only(_, __, message):
    return message.from_user.id in admin_ids

async def update_profile():
    global last_minute
    while update_enabled or update_bio_enabled:
        now = datetime.now(timezone(iran_tz))
        minute = now.strftime("%H:%M")
        
        if minute != last_minute:
            last_minute = minute
            if update_enabled:
                new_name = f"{original_name} {minute}"
                await app.update_profile(first_name=new_name)
            if update_bio_enabled:
                await app.update_profile(bio=f"ساعت {minute}")
        
        await asyncio.sleep(30)

async def keep_online():
    while always_online_enabled:
        await app.invoke(functions.account.UpdateStatus(offline=False))
        await asyncio.sleep(10)

async def update_emoji():
    emoji_index = 0
    while update_emoji_enabled:
        new_emoji = emoji_list[emoji_index % len(emoji_list)]
        await app.update_profile(last_name=new_emoji)
        emoji_index += 1
        await asyncio.sleep(60)

def setup_commands():

    @app.on_message(filters.command("time") & filters.create(admin_only) & filters.regex(r"^/time on$"))
    async def enable_time_update(client, message):
        global update_enabled, original_name, last_minute
        update_enabled = True
        last_minute = None 
        user = await app.get_me()
        original_name = user.first_name
        await message.reply_text("Automatic time update enabled.")
        asyncio.ensure_future(update_profile())

    @app.on_message(filters.command("time") & filters.create(admin_only) & filters.regex(r"^/time off$"))
    async def disable_time_update(client, message):
        global update_enabled
        update_enabled = False
        await message.reply_text("Automatic time update disabled.")

    @app.on_message(filters.command("time") & filters.create(admin_only) & filters.regex(r"^/time bio on$"))
    async def enable_bio_update(client, message):
        global update_bio_enabled, last_minute
        update_bio_enabled = True
        last_minute = None 
        await message.reply_text("Automatic bio update enabled.")
        asyncio.ensure_future(update_profile())

    @app.on_message(filters.command("time") & filters.create(admin_only) & filters.regex(r"^/time bio off$"))
    async def disable_bio_update(client, message):
        global update_bio_enabled
        update_bio_enabled = False
        await message.reply_text("Automatic bio update disabled.")

    @app.on_message(filters.command("resat") & filters.create(admin_only))
    async def disable_all_updates(client, message):
        global update_enabled, update_bio_enabled, update_emoji_enabled
        update_enabled = False
        update_bio_enabled = False
        update_emoji_enabled = False
        await message.reply_text("Automatic updates disabled.")

    @app.on_message(filters.command("ping") & filters.create(admin_only))
    async def ping(client, message):
        await message.reply_text("Krals Online.")

    @app.on_message(filters.command("set") & filters.create(admin_only) & filters.regex(r"^/set name (.+)$"))
    async def set_name(client, message):
        new_name = message.text.split("/set name ", 1)[1].strip()
        global original_name
        original_name = new_name
        await app.update_profile(first_name=new_name)
        await message.reply_text(f"Name updated to: {new_name}")

    @app.on_message(filters.command("clone") & filters.create(admin_only) & filters.reply)
    async def clone_profile(client, message):
        replied_user = message.reply_to_message.from_user
        if replied_user:
        
            await app.update_profile(first_name=replied_user.first_name, last_name=replied_user.last_name)
            global original_name
            original_name = replied_user.first_name

            user_details = await app.get_chat(replied_user.id)
            await app.update_profile(bio=user_details.bio or "")

            async for photo in app.get_chat_photos(replied_user.id):
                photo_file_id = photo.file_id
                photo = await app.download_media(photo_file_id)
                await app.set_profile_photo(photo=photo)
                break 

            await message.reply_text(f"Profile cloned from {replied_user.first_name}.")
        else:
            await message.reply_text("Please reply to a user's message to clone their profile.")

    @app.on_message(filters.command("online") & filters.create(admin_only) & filters.regex(r"^/online mode on$"))
    async def enable_online_mode(client, message):
        global always_online_enabled
        always_online_enabled = True
        await message.reply_text("Always online mode enabled.")
        asyncio.ensure_future(keep_online())

    @app.on_message(filters.command("online") & filters.create(admin_only) & filters.regex(r"^/online mode off$"))
    async def disable_online_mode(client, message):
        global always_online_enabled
        always_online_enabled = False
        await message.reply_text("Always online mode disabled.")

    @app.on_message(filters.command("emoji") & filters.create(admin_only) & filters.regex(r"^/emoji on$"))
    async def enable_emoji_update(client, message):
        global update_emoji_enabled
        update_emoji_enabled = True
        await message.reply_text("Automatic emoji update enabled.")
        asyncio.ensure_future(update_emoji())  # فراخوانی تابع برای آغاز به‌روزرسانی

    @app.on_message(filters.command("emoji") & filters.create(admin_only) & filters.regex(r"^/emoji off$"))
    async def disable_emoji_update(client, message):
        global update_emoji_enabled
        update_emoji_enabled = False
        await message.reply_text("Automatic emoji update disabled.")

    @app.on_message(filters.command("message") & filters.create(admin_only) & filters.regex(r"^/message (.+) @(\w+)$"))
    async def send_message(client, message):
        text = message.matches[0].group(1)
        username = message.matches[0].group(2)
        try:
            user = await client.get_users(username)
            await client.send_message(user.id, text)
            await message.reply_text(f"Message sent to {username}.")
        except PeerIdInvalid:
            await message.reply_text(f"User @{username} not found.")
        except Exception as e:
            await message.reply_text(f"Failed to send message to @{username}: {e}")

    # تعریف دستور help
    @app.on_message(filters.command("help") & filters.create(admin_only))
    async def show_help(client, message):
        help_text = (
            "راهنمای سلف:\n"
            "/time on - ساعت رو اسم\n"
            "/time off - غیرفعال کردن ساعت رو اسم\n"
            "/time bio on - ساعت رو بیوگرافی\n"
            "/time bio off - غیرفعال کردن ساعت در بیو\n"
            "/addadmin id - افزودن ادمین به سلف\n"
            "/removeadmin id - حذف ادمین افزوده شده\n"
            "/ping - اطمینان از آنلاین بودن\n"
            "/resat - غیرفعال کردن کلی عملکرد و بروزرسانی\n"
            "/set name --- - تغییر نام اکانت\n"
            "/join @username - عضویت در کانال\n"
            "/left @username - ترک کانال\n"
            "/clone - کپی کردن پروفایل کاربر ریپلی شده\n"
            "/online mode on - فعال کردن حالت همیشه آنلاین\n"
            "/online mode off - غیرفعال کردن حالت همیشه آنلاین\n"
            "/emoji on - فعال کردن تغییر خودکار اموجی\n"
            "/emoji off - غیرفعال کردن تغییر خودکار اموجی\n"
            "/message متن @username - ارسال پیام به کاربر مشخص"
        )
        await message.reply_text(help_text)

    @app.on_message(filters.command("addadmin") & filters.create(admin_only) & filters.regex(r"^/addadmin (\d+)$"))
    async def add_admin(client, message):
        new_admin_id = int(message.matches[0].group(1))
        admin_ids.add(new_admin_id)
        await message.reply_text(f"User {new_admin_id} added as admin.")

    @app.on_message(filters.command("removeadmin") & filters.create(admin_only) & filters.regex(r"^/removeadmin (\d+)$"))
    async def remove_admin(client, message):
        remove_admin_id = int(message.matches[0].group(1))
        if remove_admin_id in admin_ids:
            admin_ids.remove(remove_admin_id)
            await message.reply_text(f"User {remove_admin_id} removed from admin.")
        else:
            await message.reply_text(f"User {remove_admin_id} is not an admin.")

    @app.on_message(filters.command("join") & filters.create(admin_only) & filters.regex(r"^/join @(\w+)$"))
    async def join_channel(client, message):
        channel_username = message.matches[0].group(1)
        try:
            await client.join_chat(f"@{channel_username}")
            await message.reply_text(f"Successfully joined @{channel_username}.")
        except PeerIdInvalid:
            await message.reply_text(f"Channel @{channel_username} not found.")
        except UserAlreadyParticipant:
            await message.reply_text(f"Already a member of @{channel_username}.")
        except Exception as e:
            await message.reply_text(f"Failed to join @{channel_username}: {e}")

    @app.on_message(filters.command("left") & filters.create(admin_only) & filters.regex(r"^/left @(\w+)$"))
    async def leave_channel(client, message):
        channel_username = message.matches[0].group(1)
        try:
            await client.leave_chat(f"@{channel_username}")
            await message.reply_text(f"Successfully left @{channel_username}.")
        except PeerIdInvalid:
            await message.reply_text(f"Channel @{channel_username} not found.")
        except UserNotParticipant:
            await message.reply_text(f"Not a member of @{channel_username}.")
        except Exception as e:
            await message.reply_text(f"Failed to leave @{channel_username}: {e}")

setup_commands()
