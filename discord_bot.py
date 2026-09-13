import discord
from discord.ext import commands
import requests
import os

# التوكن السري الخاص بكِ مدمج هنا للتشغيل التلقائي
TOKEN = 'MTU0ODQ4NDcyMDgyNzAzOTg1NQ.GWJ7Wo.Py2QgWBzip8_sXnRJMNJETXiGfI8-lT29HLibc'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'🔥 تم تشغيل البوت بنجاح باسم: {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    user_url = message.content

    if "gateway.platoboost" in user_url or "platoboost" in user_url.lower():
        status_msg = await message.reply("⏳ جاري فك التشفير وتخطي نظام الحماية الخاص بـ Delta... انتظر ثوانٍ...")
        
        try:
            # الاتصال بخادم التخطي المفتوح
            api_endpoint = f"https://bypass.vip{user_url}"
            response = requests.get(api_endpoint).json()
            
            if response.get("status") == "success" or "result" in response:
                final_key = response.get("result", "لم يتم العثور على المفتاح")
                
                success_text = (
                    f"🎉 **تم تخطي الرابط بنجاح يا {message.author.mention}!**\n\n"
                    f"🔑 **المفتاح الخاص بك هو:**\n`{final_key}`\n\n"
                    "قم بنسخه ووضعه داخل اللعبة الآن! 🚀"
                )
                await status_msg.edit(content=success_text)
            else:
                await status_msg.edit(content="❌ فشل التخطي. قد يكون الرابط منتهي الصلاحية أو غير صحيح.")
        except Exception as e:
            await status_msg.edit(content="⚠️ حدث خطأ في الاتصال بخادم التخطي، يرجى المحاولة لاحقاً.")
            
    await bot.process_commands(message)

bot.run(TOKEN)
