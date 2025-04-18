import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# তোমার বটের টোকেন
TOKEN = "7784967189:AAEmjp6czEFkveSeFoXAoGpibg1uM_n-4d0"

# নামকে স্টাইলিশ বানায়
def stylish_name(name):
    prefix = "ᶦƬˢ⃝🎀"
    suffix = "﷽"

    if len(name) == 0:
        return ""

    first_char = name[0]
    if 'A' <= first_char.upper() <= 'Z':
        regional = chr(0x1F1E6 + ord(first_char.upper()) - ord('A')) + '\u200C'
    else:
        regional = first_char

    rest = name[1:]

    small_caps = {
        'A': 'ᴀ', 'B': 'ʙ', 'C': 'ᴄ', 'D': 'ᴅ', 'E': 'ᴇ', 'F': 'ғ', 'G': 'ɢ',
        'H': 'ʜ', 'I': 'ɪ', 'J': 'ᴊ', 'K': 'ᴋ', 'L': 'ʟ', 'M': 'ᴍ', 'N': 'ɴ',
        'O': 'ᴏ', 'P': 'ᴘ', 'Q': 'ǫ', 'R': 'ʀ', 'S': 's', 'T': 'ᴛ', 'U': 'ᴜ',
        'V': 'ᴠ', 'W': 'ᴡ', 'X': 'x', 'Y': 'ʏ', 'Z': 'ᴢ'
    }

    rest_styled = ''.join([small_caps.get(c.upper(), c) for c in rest])
    styled = prefix + regional + rest_styled + suffix

    return styled

# ইউজারের মেসেজ পেলে বট যেটা করবে
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text
    styled = stylish_name(name)
    await update.message.reply_text(styled)

# বট চালানোর মূল অংশ
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

    print("Bot is running...")
    await app.run_polling()

# Pydroid3 এর জন্য লাগবে
nest_asyncio.apply()
asyncio.run(main())
