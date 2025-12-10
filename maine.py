import os
import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def anonymous_forward(message: types.Message):

    # Texto
    if message.text:
        await bot.send_message(
            ADMIN_CHAT_ID,
            f"📩 *Nuevo reporte anónimo:*\n\n{message.text}",
            parse_mode="Markdown"
        )

    # Fotos
    if message.photo:
        await bot.send_photo(
            ADMIN_CHAT_ID,
            message.photo[-1].file_id,
            caption="📸 Imagen enviada anónimamente"
        )

    # Documentos
    if message.document:
        await bot.send_document(
            ADMIN_CHAT_ID,
            message.document.file_id,
            caption="📎 Archivo enviado anónimamente"
        )

    # Audio
    if message.audio:
        await bot.send_audio(
            ADMIN_CHAT_ID,
            message.audio.file_id,
            caption="🎵 Audio enviado anónimamente"
        )

    # Notas de voz
    if message.voice:
        await bot.send_voice(
            ADMIN_CHAT_ID,
            message.voice.file_id,
            caption="🎤 Nota de voz enviada anónimamente"
        )

    # Videos
    if message.video:
        await bot.send_video(
            ADMIN_CHAT_ID,
            message.video.file_id,
            caption="🎥 Video enviado anónimamente"
        )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
