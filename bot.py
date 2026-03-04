import asyncio
import os
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode

BOT_TOKEN = os.getenv("BOT_TOKEN", "8778889794:AAEQzzeRLwXJJ_-p48rPTpRQGZO70787Gm0")
WEB_APP_URL = os.getenv("WEB_APP_URL", "https://daddymoar-lgtm.github.io/uni-guide-webapp/")

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Открыть справочник абитуриента",
                    web_app=WebAppInfo(url=WEB_APP_URL)
                )
            ]
        ]
    )
    await message.answer(
        text=(
            "<b>Справочник абитуриента Беларуси</b>\n\n"
            "Исчерпывающая база данных по университетам, факультетам и специальностям.\n\n"
            "Нажмите кнопку ниже, чтобы открыть приложение."
        ),
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard
    )

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
