import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
import json
import os

# ================= LOG =================
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ================= TOKEN VA ADMIN =================
BOT_TOKEN = "8476556604:AAFtOOKEuc3bwX25afbkQwrr5b6NH8pAW2k"  # @BotFather dan token
ADMIN_ID = 8064752412  # Sizning ID (raqamlarni o'zgartiring!)

# ================= VIDEO DARSLIKLAR =================
# Bu yerga hamma darsliklaringizni qo'shing!

# ================= FOYDALANUVCHILAR FAYLI =================
LESSONS = {
    "ita7k3q": {
        "file_id": "BAACAgIAAxkBAAMNaUC18lAFtW10FYLigUmdcBVJqZYAAo9RAAKw9ulJqfUkASiriyE2BA",
        "title": "Kompyuter savotxonligi 1-dars video✅\n(Kompyuter va uning turlari) "
    },
    "it9m2f8": {
        "file_id": "BQACAgIAAxkBAAMRaUC18gWm0Yu6_fA6e9Sx9EHL0FIAApVRAAKw9ulJlhDNfB9nnJQ2BA",
        "title": "Kompyuter savotxonligi 1-dars test✅\n(Homework Test)"
    },
    "itx4r6b": {
        "file_id": "BAACAgIAAxkBAAIBIGlBQmKXei2BjxVxUtb9j3FpzuWvAAKcUQACsPbpSQqyoIMuOzasNgQ",  # Bu yerga FILE_ID qo'shing
        "title": "Kompyuter savotxonligi 2-dars video✅\n(Dasturiy taminot)"
    },
    "it5qz9a": {
        "file_id": "BAACAgIAAxkBAAIBNGlBSNjtMq5ZFv3rdGuDDlR2jN9HAAKjUQACsPbpSYaY9q-xR6k1NgQ",  # Bu yerga FILE_ID qo'shing
        "title": "Kompyuter savotxonligi 3-dars video✅\n(Tezkor tugmalar)"
    },
    "ith8n2c": {
        "file_id": "BQACAgIAAxkBAAIBImlBRlh_UWFFZsZ1RRdUJuWEkR1rAAKoUQACsPbpSRmn1qKJKmQmNgQ",  # Bu yerga FILE_ID qo'shing
        "title": "Kompyuter savotxonligi 2-3-dars test✅\n(2-3-dars Homework Test)"
    },
    "it7d4p9": {
        "file_id": "BAACAgIAAxkBAAIBN2lBTMwOxvagR0h3eoNX7UNmaUzhAAKuUQACsPbpSW3gUbPEO7KaNgQ",  # Bu yerga FILE_ID qo'shing
        "title": "Kompyuter savotxonligi 4-dars video✅\n(Word kirish)"
    },
    "itl3a6x": {
        "file_id": "BQACAgIAAxkBAAIBO2lBUcysM4K6LsLMXpzazAABTyhjYgACv1EAArD26Unr5T35FiNOQTYE",  # Bu yerga FILE_ID qo'shing
        "title": "Kompyuter savotxonligi 4-dars Amaliyot\n(Homework Word)"
    },
    "it2fj8m": {
        "file_id": "BQACAgIAAxkBAAIBPWlBUncFjRdJWuHMRHEKKij1B1fgAALBUQACsPbpSbm42Z_Kj2K5NgQ",  # Bu yerga FILE_ID qo'shing
        "title": "Kompyuter savotxonligi 4-dars Word Test\n(Homework Test)"
    },
    "itc9k5r": {
        "file_id": "BAACAgIAAxkBAAIBP2lBUstBAyfQaafM1I6f762n0tEAA8lRAAKw9ulJFtxq3FRMZjU2BA",  # Bu yerga FILE_ID qo'shing
        "title": "Kompyuter savotxonligi 5-dars video✅ \n(Brauvzerlar, Word)"
    },
    "itp6x7d": {
        "file_id": "BQACAgIAAxkBAAIBQWlBUuWwZBN9wHpKxjUVLmCDQ0iJAALQUQACsPbpSQrK0Oz5KxUbNgQ",  # Bu yerga FILE_ID qo'shing
        "title": "Kompyuter savotxonligi 5-dars Test\n(Homework Test)"
    },
    "it8a2zq": {
        "file_id": "BAACAgIAAxkBAAIBQ2lBVcKZcMgMceycRWuPnvfn2hAQAALnUQACsPbpSUVhwORmsPioNgQ",  # Bu yerga FILE_ID qo'shing
        "title": "Kompyuter savotxonligi 6-dars video✅\n( Word rasmlar bilan ishlash)"
    },
    "itm5r9h": {
        "file_id": "BQACAgIAAxkBAAIBRWlBVieryuUes5B0JfRLOlROO1f7AALtUQACsPbpSVPr2lovbATONgQ",  # Bu yerga FILE_ID qo'shing
        "title": "Kompyuter savotxonligi 6-dars Test✅\n(Homework Test)"
    },
    "it4c7fj": {
        "file_id": "BAACAgIAAxkBAAIBTWlB94amyRW_4JKBsDrxhw-bmilvAALyUQACsPbpSTi5iTcHyMM1NgQ",# Bu yerga FILE_ID qo'shing
        "title": "Kompyuter savotxonligi 7-dars video✅\n(Word amaliyot)"
    },
    "itqx6a3": {
        "file_id": "BQACAgIAAxkBAAIBT2lB-DjsWeHqAnsB5JA8jP8SO9HZAAL4UQACsPbpSQarHbGcuUnCNgQ",
        "title": "Kompyuter savotxonligi 7-dars Test✅\n(Homework Test)"
    },
    "it9p2n8": {
        "file_id": "BAACAgIAAxkBAAIBUWlB-EKs7l7x2_XdFlNOoRuZ7yL1AAIBUgACsPbpSX4hp723JwV8NgQ",
        "title": "Kompyuter savotxonligi 8-dars video✅\n Word(Jadvallar bilan ishlash)"
    },
    "itd7m5k": {
        "file_id": "BQACAgIAAxkBAAIBU2lB-E9wRVRNSfA0aNGcpnFkfuD6AAIOUgACsPbpSaKOMLsZ5YsZNgQ",
        "title": "Kompyuter savotxonligi 8-dars Test✅\n(Homework Test)"
    },
    "ita8r4x": {
        "file_id": "BAACAgIAAxkBAAIBVWlB-Fdbgz0QzcaKyRVW7xlxokIjAAITUgACsPbpSV1fwqeEe5aaNgQ",
        "title": "Kompyuter savotxonligi 9-dars video✅\n(Word amaliyot)"
    },
    "it6jq9c": {
        "file_id": "BQACAgIAAxkBAAIBV2lB-IRV49mYWeSe6B60ziqtjbwiAAIaUgACsPbpSc8C4UsIn7pqNgQ",
        "title": "Kompyuter savotxonligi 9-dars Amaliyot✅\n(Homework Amaliyot)"
    },
    "itf2h7p": {
        "file_id": "BAACAgIAAxkBAAIBWWlB-r_b0L2YSftqzVXvDmt2yP6zAAIrUgACsPbpSZcLRgl2yCPkNgQ",
        "title": "Kompyuter savotxonligi 10-dars video✅\n(1-qism)"
    },
    "itx5m3a": {
        "file_id": "BAACAgIAAxkBAAIBW2lB-xFjY_VvPtxJ64kTgbkmrDI3AAIvUgACsPbpSficv9hA1zbkNgQ",
        "title": "Kompyuter savotxonligi 10-dars video\n(2-qism)"
    },
    "it7q9d8": {
        "file_id": "BQACAgIAAxkBAAIBXWlB-xrUJhg1OClgR97rQ9602tkfAAIxUgACsPbpSQ2tQlSkNXJJNgQ",
        "title": "Kompyuter savotxonligi 10-dars Homework✅\n(1-2-qism Homework)"
    },
    "itn4a6k": {
        "file_id": "BAACAgIAAxkBAAIBX2lB_NETgFw1K3uCZzLj2n3ZUwo8AAI2UgACsPbpScSCoJJebqyoNgQ",
        "title": "Kompyuter savotxonligi 11-dars video✅\n(Word mavzusidan)"
    },
    "itp2xh5": {
        "file_id": "BQACAgIAAxkBAAIBZWlB_RTjlNmCAvXYmxXq2SSC0SuiAAI8UgACsPbpSYF6TYv0GWSyNgQ",
        "title": "Kompyuter savotxonligi 11-dars Homework✅\n(Word Homework)"
    },
    "itc8m7r": {
        "file_id": "BAACAgIAAxkBAAIBYWlB_NYxbUJEPzc4WCUeBhJmCndZAAI4UgACsPbpSRsAATDi6_7znzYE",
        "title": "Kompyuter savotxonligi 12-dars video✅\n(Word mavzusi Tugadi.)"
    },
    "it9fjq4": {
        "file_id": "BQACAgIAAxkBAAIBY2lB_P40GUoUHDgx50OJOZQ4jPeVAAI7UgACsPbpSdi6BYf8yrBKNgQ",
        "title": "Kompyuter savotxonligi 12-dars Test✅\n(11-12-darslarg oid Testlar)"
    },
    "ita5d2x": {
        "file_id": "BAACAgIAAxkBAAIBZ2lB_k2RSHEL_S89aGqxoHF4gxLxAAJKUgACsPbpSdr27QZd-UssNgQ",
        "title": "Kompyuter savotxonligi 13-dars video✅\n(Excel kirish)"
    },
    "it6h8p9": {
        "file_id": "BQACAgIAAxkBAAIBaWlB_l0qe8aAK5Zx0-aEP375HUtRAAJPUgACsPbpSVHyUcffzW5ANgQ",
        "title": "Kompyuter savotxonligi 13-dars Test✅\n(Homework Test)"
    },
    "itr7cqm": {
        "file_id": "BAACAgIAAxkBAAIBa2lB_mRBxELAgCsY1FFQoCu6W1teAAJZUgACsPbpSdy30yN0d5dHNgQ",
        "title": "Kompyuter savotxonligi 14-dars video✅\nExel(sonlar,formatlash)"
    },
    "itx3a4f": {
        "file_id": "BQACAgIAAxkBAAIBbWlB_mshV2r1zv2CmN6IVtnj4CAjAAJdUgACsPbpSfNxJyJ4LgIBNgQ",
        "title": "Kompyuter savotxonligi 14-dars Test✅\n(Homework Test)"
    },
    "itk9n5j": {
        "file_id": "BAACAgIAAxkBAAIBb2lB_nBflW7uHb6MzerTkE6QW3jBAAJgUgACsPbpSQmwBlHCrqbtNgQ",
        "title": "Kompyuter savotxonligi 15-dars video✅\n(Excel diagramma)"
    },
    "it4n8x2a": {
        "file_id": "BQACAgIAAxkBAAIBcWlB_nq6mq3v3WIkY6g1JSA4AAFrgAACZFIAArD26UlVUtTUp3vXMTYE",
        "title": "Kompyuter savotxonligi 15-dars Test✅\n(Homework Test)"
    },
    "itq7m5k9": {
        "file_id": "BAACAgIAAxkBAAIBc2lB_odBH7uHArbJdKH2OaGqOijRAAJqUgACsPbpSYFI9j9zv4I_NgQ",
        "title": "Kompyuter savotxonligi 16-dars video✅\nExcel (matematik funksiyalar)"
    },
    "it3f6rpa": {
        "file_id": "BQACAgIAAxkBAAIBdWlB_pAmPEol9WDbXJ1Vvj-8yPI0AAJvUgACsPbpSUg7nNw8oSxlNgQ",
        "title": "Kompyuter savotxonligi 16-dars Test✅\n(Homework Test)"
    },
    "it8c2hxm": {
        "file_id": "BAACAgIAAxkBAAIBd2lB_paQ1ozK_Ux7s54CkBEV3OplAAJzUgACsPbpSShFN0PlGslNNgQ",
        "title": "Kompyuter savotxonligi 17-dars video✅\nExcel(matnli funksiyalar)"
    },
    "it9a4d7q": {
        "file_id": "BQACAgIAAxkBAAIBeWlB_pzBihyfKg_e7N9_Y1A-UvzBAAJ2UgACsPbpSTyQTdeoJP9mNgQ",
        "title": "Kompyuter savotxonligi 17-dars Test✅\n(Homework Test)"
    },
    "itk5x3n8": {
        "file_id": "BQACAgIAAxkBAAIBeWlB_pzBihyfKg_e7N9_Y1A-UvzBAAJ2UgACsPbpSTyQTdeoJP9mNgQ",
        "title": "Kompyuter savotxonligi 18-dars video✅\nExcel(mantiqiy funksiyalar)"
    },
    "it2m9p6f": {
        "file_id": "BQACAgIAAxkBAAIBfWlB_rntk53hvAr_gj7UpCdVH9lBAAJ9UgACsPbpSaN07wx8ztFsNgQ",
        "title": "Kompyuter savotxonligi 18-dars Test✅\n(Homework Test)"
    },
    "itr8a5c4": {
        "file_id": "BAACAgIAAxkBAAIBf2lB_sID_LimyPndyt9GT4bPrQW8AAJdUgACyMUQSo8y8lc3eccjNgQ",
        "title": "Kompyuter savotxonligi 19-dars video✅\n Excel (havolalar va nomlash)"
    },
    "it7xkq2m": {
        "file_id": "BQACAgIAAxkBAAIBgWlB_sy0j17GB_4ili46WqElCTENAAJhUgACyMUQSqFAgBOQK_TGNgQ",
        "title": "Kompyuter savotxonligi 19-dars Test✅\n(Homework Test)"
    },
    "it6n4a9h": {
        "file_id": "BAACAgIAAxkBAAIBg2lB_tdtMV-fH4AqFEjMcCZwHLPwAAJlUgACyMUQStHlj48wjd07NgQ",
        "title": "Kompyuter savotxonligi 20-dars video✅\nExcel (VPR, INDEX, Faol jadval) Excel oxirgi dasr❗"
    },
    "itp3m8x5": {
        "file_id": "BQACAgIAAxkBAAIBhWlB_t0AAXdo-BsM_7H-DWN-n8c-8QACaFIAAsjFEEr1bA8i1C01EDYE",
        "title": "Kompyuter savotxonligi 20-dars Test✅\nExcel (Homework Test) oxirgi dasr Test❗"
    },
    "it4qk7n2": {
        "file_id": "BQACAgIAAxkBAAIBh2lB_un-34KuUeegQ5hyZz7KBJ1zAAJpUgACyMUQSi9JR44Po8C3NgQ",
        "title": "Kompyuter savotxonligi 20-dars Funksiyalar to\'plami✅\n(Excel barcha funksiyalar to'liq.)"
    },
    "it9x5cma": {
        "file_id": "BAACAgIAAxkBAAIBmmlCBm3qOlYzE8GlRfjAw8Fxn-3nAAJrUgACyMUQSqzUOw3-UUWKNgQ",
        "title": "Kompyuter savotxonligi 21-dars video✅\nPowerPoint (Kirish)"
    },
    "it2a8r6k": {
        "file_id": "BQACAgIAAxkBAAIBnGlCBnrrSOM13-qhY0HfETWFYVwIAAJvUgACyMUQSkBiu7fg8OYGNgQ",
        "title": "Kompyuter savotxonligi 21-dars Test✅\n(Homework Test)"
    },
    "itd7p4m9": {
        "file_id": "BAACAgIAAxkBAAIBnmlCBn8UWZY1lvNZOczpzsvAbTMbAAJxUgACyMUQSuoRrV4ezzlyNgQ",
        "title": "Kompyuter savotxonligi 22-dars video✅\nPowerPoint (Animatsiya, Grafika)"
    },
    "it5n2q8x": {
        "file_id": "BQACAgIAAxkBAAIBoGlCBonvaJC0AeYxhpQcMqDBLaV-AAJ4UgACyMUQSjFdYnykIk36NgQ",
        "title": "Kompyuter savotxonligi 22-dars Test✅\n(Homework Test)"
    },
    "itk9a3f7": {
        "file_id": "BAACAgIAAxkBAAIBpmlCBqCN-dN5X_wden1qP5ZxfVwzAAJ8UgACyMUQSvC1qlvsrKfSNgQ",
        "title": "Kompyuter savotxonligi 23-dars video✅\n(Google,Printer)"
    },
    "it6m4xcp": {
        "file_id": "BQACAgIAAxkBAAIBqGlCBrYfA4ouqLT3andQvZwV0y41AAJ-UgACyMUQSuKOR-Xpl5ZHNgQ",
        "title": "Kompyuter savotxonligi 23-dars Test✅\n(Homework Test)"
    },
    "it8q2n5a": {
        "file_id": "BQACAgIAAxkBAAIBqmlCBt2dXwux0mb20YvvmYbX48KwAAKAUgACyMUQSlNOrswYNuhENgQ",
        "title": "Kompyuter savotxonliginig❗\n\nYakuniy imtihoni✅\n\nHurmatli o'quvchi haridingiz uchun raxmat🤝😊\n"
                 "darslarimiz sizga yoqgan bo'lsa hursandmiz😊✅"
    },
    "itks": {
        "file_id": "______",
        "title": "Kompyuter savotxonligi -dars ____✅\n(______)"
    }






    # Yangi darsliklarni shu yerga qo'shing...
}
USERS_FILE = "allowed_users.json"


def load_users():
    """Ruxsat etilgan foydalanuvchilarni yuklash"""
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r') as f:
                return set(json.load(f))
        except:
            pass
    # Faqat admin boshida
    return {ADMIN_ID}


def save_users(users):
    """Foydalanuvchilarni saqlash"""
    with open(USERS_FILE, 'w') as f:
        json.dump(list(users), f, indent=2)


# Global o'zgaruvchilar
ALLOWED_USERS = load_users()
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# ================= TELEGRAM ORQALI RUXSAT BERISH =================

@dp.message(Command("add"))
async def add_user(message: Message):
    """Foydalanuvchi qo'shish (faqat admin)"""
    if message.from_user.id != ADMIN_ID:
        return

    try:
        parts = message.text.split()
        if len(parts) < 2:
            await message.reply(
                "❌ <b>To'g'ri emas!</b>\n\n"
                "Format: <code>/add 123456789</code>",
                parse_mode="HTML"
            )
            return

        user_id = int(parts[1])

        if user_id in ALLOWED_USERS:
            await message.reply(
                "⚠️ Bu foydalanuvchi allaqachon ro'yxatda!",
                parse_mode="HTML"
            )
            return

        ALLOWED_USERS.add(user_id)
        save_users(ALLOWED_USERS)

        await message.reply(
            f"✅ <b>Ruxsat berildi!</b>\n\n"
            f"👤 Foydalanuvchi: <code>{user_id}</code>\n"
            f"📊 Jami: {len(ALLOWED_USERS)} ta",
            parse_mode="HTML"
        )

        # Foydalanuvchiga xabar yuborish
        try:
            await bot.send_message(
                user_id,
                "🎉 <b>Tabriklaymiz!</b>\n\n"
                "Sizga botdan foydalanish uchun ruxsat berildi.\n\n"
                "📘 Darslik kodlarini yuboring va o'rganing!",
                parse_mode="HTML"
            )
        except:
            await message.reply("⚠️ Foydalanuvchiga xabar yubora olmadim (botni boshlamagan)")

    except ValueError:
        await message.reply("❌ ID raqam bo'lishi kerak!")
    except Exception as e:
        await message.reply(f"❌ Xatolik: {e}")


@dp.message(Command("remove"))
async def remove_user(message: Message):
    """Foydalanuvchini o'chirish (faqat admin)"""
    if message.from_user.id != ADMIN_ID:
        return

    try:
        parts = message.text.split()
        if len(parts) < 2:
            await message.reply(
                "❌ <b>To'g'ri emas!</b>\n\n"
                "Format: <code>/remove 123456789</code>",
                parse_mode="HTML"
            )
            return

        user_id = int(parts[1])

        if user_id == ADMIN_ID:
            await message.reply("❌ O'zingizni o'chira olmaysiz!")
            return

        if user_id not in ALLOWED_USERS:
            await message.reply("⚠️ Bu foydalanuvchi ro'yxatda yo'q!")
            return

        ALLOWED_USERS.discard(user_id)
        save_users(ALLOWED_USERS)

        await message.reply(
            f"✅ <b>Ruxsat bekor qilindi!</b>\n\n"
            f"👤 Foydalanuvchi: <code>{user_id}</code>\n"
            f"📊 Qoldi: {len(ALLOWED_USERS)} ta",
            parse_mode="HTML"
        )

        # Foydalanuvchiga xabar
        try:
            await bot.send_message(
                user_id,
                "⚠️ <b>Diqqat!</b>\n\n"
                "Sizning ruxsatingiz bekor qilindi.\n"
                "Agar bu xato bo'lsa, admin bilan bog'laning⤵️\n\nAdmin:@Online_ITadmin",
                parse_mode="HTML"
            )
        except:
            pass

    except ValueError:
        await message.reply("❌ ID raqam bo'lishi kerak!")
    except Exception as e:
        await message.reply(f"❌ Xatolik: {e}")


@dp.message(Command("list"))
async def list_users(message: Message):
    """Barcha foydalanuvchilar ro'yxati (faqat admin)"""
    if message.from_user.id != ADMIN_ID:
        return

    if len(ALLOWED_USERS) == 1:
        await message.reply("📋 Hozircha faqat siz (admin) bor.")
        return

    users_text = "👥 <b>Ruxsat etilgan foydalanuvchilar:</b>\n\n"

    for idx, user_id in enumerate(sorted(ALLOWED_USERS), 1):
        try:
            user = await bot.get_chat(user_id)
            name = user.full_name
            username = f"@{user.username}" if user.username else "❌"
        except:
            name = "Noma'lum"
            username = "❌"

        admin_mark = "👑" if user_id == ADMIN_ID else "👤"
        users_text += f"{idx}. {admin_mark} <b>{name}</b>\n"
        users_text += f"   ├ ID: <code>{user_id}</code>\n"
        users_text += f"   └ Username: {username}\n\n"

    users_text += f"📊 <b>Jami:</b> {len(ALLOWED_USERS)} ta"

    await message.reply(users_text, parse_mode="HTML")


@dp.message(Command("admin"))
async def admin_help(message: Message):
    """Admin buyruqlari ro'yxati"""
    if message.from_user.id != ADMIN_ID:
        return

    await message.reply(
        "🔐 <b>ADMIN BUYRUQLARI</b>\n\n"
        "👥 <b>Foydalanuvchilar:</b>\n"
        "├ /add [ID] - Ruxsat berish\n"
        "├ /remove [ID] - Ruxsatni olish\n"
        "├ /list - Barcha foydalanuvchilar\n"
        "└ /info [ID] - Foydalanuvchi ma'lumoti\n\n"
        "📊 <b>Statistika:</b>\n"
        "└ /stats - Bot statistikasi\n\n"
        "💡 <b>Maslahat:</b>\n"
        "Kimdir botga yozsa, sizga xabar keladi va\n"
        "unga ruxsat berish uchun ID ni olasiz.",
        parse_mode="HTML"
    )


@dp.message(Command("info"))
async def user_info(message: Message):
    """Foydalanuvchi haqida ma'lumot"""
    if message.from_user.id != ADMIN_ID:
        return

    try:
        parts = message.text.split()
        if len(parts) < 2:
            await message.reply("❌ Format: <code>/info 123456789</code>", parse_mode="HTML")
            return

        user_id = int(parts[1])
        user = await bot.get_chat(user_id)

        info_text = "👤 <b>FOYDALANUVCHI MA'LUMOTI</b>\n\n"
        info_text += f"🆔 ID: <code>{user_id}</code>\n"
        info_text += f"👤 Ism: {user.full_name}\n"
        username_display = f"@{user.username}" if user.username else "yo'q"
        info_text += f"📱 Username: {username_display}\n"
        info_text += f"🔐 Ruxsat: {'✅ Bor' if user_id in ALLOWED_USERS else '❌ Yoq'}\n"
        info_text += f"👑 Admin: {'Ha' if user_id == ADMIN_ID else 'Yoq'}"

        await message.reply(info_text, parse_mode="HTML")

    except ValueError:
        await message.reply("❌ ID raqam bo'lishi kerak!")
    except Exception as e:
        await message.reply(f"❌ Foydalanuvchi topilmadi: {e}")


@dp.message(Command("stats"))
async def bot_stats(message: Message):
    """Bot statistikasi"""
    if message.from_user.id != ADMIN_ID:
        return

    active_lessons = sum(1 for l in LESSONS.values() if l.get('file_id'))

    stats_text = "📊 <b>BOT STATISTIKASI</b>\n\n"
    stats_text += f"👥 Foydalanuvchilar: {len(ALLOWED_USERS)}\n"
    stats_text += f"📚 Jami darsliklar: {len(LESSONS)}\n"
    stats_text += f"✅ Tayyor: {active_lessons}\n"
    stats_text += f"⚠️ Tayyor emas: {len(LESSONS) - active_lessons}"

    await message.reply(stats_text, parse_mode="HTML")


# ================= /start =================

@dp.message(Command("start"))
async def start_handler(message: Message):
    """Start buyrug'i"""
    user_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name

    # Agar ruxsat yo'q bo'lsa
    if user_id not in ALLOWED_USERS:
        username_display = f"@{username}" if username else "yo'q"
        # Adminga yangi foydalanuvchi haqida xabar
        try:
            await bot.send_message(
                ADMIN_ID,
                f"⚠️ <b>YANGI FOYDALANUVCHI</b>\n\n"
                f"👤 Ism: {full_name}\n"
                f"📱 Username: {username_display}\n"
                f"🆔 ID: <code>{user_id}</code>\n\n"
                f"<b>Ruxsat berish uchun:</b>\n"
                f"<code>/add {user_id}</code>",
                parse_mode="HTML"
            )
        except Exception as e:
            logging.error(f"Adminга xabar yuborishda xatolik: {e}")

        # Foydalanuvchiga javob
        await message.reply(
            "❌ <b>Kechirasiz!</b>\n\n"
            "Sizda botdan foydalanish uchun ruxsat yo'q.\n\n"
            "📞 Admin bilan bog'laning va ruxsat so'rang⤵️\n\nAdmin:@Online_ITadmin✅",
            parse_mode="HTML"
        )
        return

    # Agar ruxsat bo'lsa
    if user_id == ADMIN_ID:
        # Admin uchun
        await message.reply(
            "👋 <b>Salom Admin!</b>\n\n"
            "🔐 Admin panel: /admin\n"
            "👥 Foydalanuvchilar: /list\n"
            "📊 Statistika: /stats",
            parse_mode="HTML"
        )
    else:
        # Oddiy foydalanuvchi uchun
        await message.reply(
            "👋 <b>Xush kelibsiz!</b>\n\n"
            "📘 <b>IT ni online o'rganamiz 💻🌐</b>\n\n"
            "Video darslik olish uchun kod yuboring ⤵️\n\n",
            parse_mode="HTML"
        )


# ================= VIDEO YUBORISH (Admin uchun FILE_ID olish) =================

@dp.message(F.video | F.photo | F.document)
async def admin_file_handler(message: Message):
    """Admin file yuborsa - FILE_ID ko'rsatish"""
    if message.from_user.id != ADMIN_ID:
        return

    file_id = None
    file_type = None

    if message.video:
        file_id = message.video.file_id
        file_type = "video"
    elif message.photo:
        file_id = message.photo[-1].file_id
        file_type = "photo"
    elif message.document:
        file_id = message.document.file_id
        file_type = "document"

    if file_id:
        await message.reply(
            f"✅ <b>FILE_ID ({file_type}):</b>\n\n"
            f"<code>{file_id}</code>\n\n"
            f"📝 Kodga qo'shish:\n\n"
            f'"kod": {{\n'
            f'    "file_id": "{file_id}",\n'
            f'    "title": "Darslik nomi"\n'
            f'}}',
            parse_mode="HTML"
        )


# ================= KOD QABUL QILISH VA DARSLIK BERISH =================

@dp.message(F.text)
async def handle_lesson_code(message: Message):
    """Foydalanuvchi kod yuborsa - darslik yuborish"""
    user_id = message.from_user.id

    # Ruxsat tekshirish
    if user_id not in ALLOWED_USERS:
        return

    code = message.text.strip().lower()

    # Agar darslik mavjud bo'lsa
    if code in LESSONS:
        lesson = LESSONS[code]

        if lesson.get("file_id"):
            try:
                # VIDEO YUBORISH (HIMOYALANGAN)
                await message.reply_video(
                    video=lesson["file_id"],
                    caption=f"📘 {lesson['title']}",
                    protect_content=True  # ❗ Bu juda muhim!
                )

                # Adminга statistika (admin o'zi yozsa xabar yo'q)
                if user_id != ADMIN_ID:
                    try:
                        user = await bot.get_chat(user_id)
                        await bot.send_message(
                            ADMIN_ID,
                            f"📊 <b>Darslik ko'rildi</b>\n\n"
                            f"👤 {user.full_name}\n"
                            f"🆔 <code>{user_id}</code>\n"
                            f"🔑 Kod: <code>{code}</code>\n"
                            f"📝 {lesson['title']}",
                            parse_mode="HTML"
                        )
                    except:
                        pass

            except Exception as e:
                await message.reply("❌ Video yuborishda xatolik yuz berdi!")
                logging.error(f"Video yuborishda xatolik: {e}")
        else:
            await message.reply(
                "⚠️ <b>Bu darslik hali tayyor emas.</b>\n\n"
                "🕐 Tez orada qo'shiladi.",
                parse_mode="HTML"
            )
    else:
        await message.reply(
            "❌ <b>Bu kod topilmadi!</b>\n\n"
            "🔍 Iltimos, to'g'ri kodni kiriting.",
            parse_mode="HTML"
        )


# ================= MAIN =================

async def main():
    """Botni ishga tushirish"""
    print("=" * 50)
    print("✅ Bot muvaffaqiyatli ishga tushdi!")
    print(f"👑 Admin ID: {ADMIN_ID}")
    print(f"👥 Ruxsat etilganlar: {len(ALLOWED_USERS)} ta")
    print(f"📚 Darsliklar: {len(LESSONS)} ta")
    print(f"✅ Tayyor darsliklar: {sum(1 for l in LESSONS.values() if l.get('file_id'))} ta")
    print("=" * 50)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())