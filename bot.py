import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN
from utils.faqloader import load_faq_from_json
from handlers.main import register_handlers

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

faq = load_faq_from_json("faq.json")

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())

register_handlers(dp, faq)


async def set_commands():
    commands = [
        BotCommand(command="/start", description="Start the bot"),
        BotCommand(command="/help", description="How it works"),
    ]
    await bot.set_my_commands(commands)

if __name__ == "__main__":
    import asyncio

    async def main():
        logging.info("Bot is starting...")
        await set_commands()
        await dp.start_polling(bot)

    asyncio.run(main())
