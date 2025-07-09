from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.enums import ChatType
from utils.helpers import find_answer, is_personal_question
from functools import partial
import logging

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hi! I'm your FAQ bot. Just ask me a question.")


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("You can ask me any question from the Youmint FAQ, and I’ll try to answer.")


async def handle_question(message: Message, faq):
    logging.info(
        f"[DEBUG] Got message in chat {message.chat.id}, type {message.chat.type}, text: {message.text}")

    question = message.text
    answer = find_answer(faq, question)

    if is_personal_question(question) and message.chat.type != ChatType.PRIVATE:
        try:
            await message.answer("I’ve sent you a private message with the answer.")
            await message.bot.send_message(chat_id=message.from_user.id, text=answer)
        except Exception as e:
            logging.error(f"Failed to send private message: {e}")
            await message.answer("Sorry, I couldn’t send you a private message. Please start me in private first.")
    else:
        await message.answer(answer)


def register_handlers(dp, faq):
    router.message.register(partial(handle_question, faq=faq), F.chat.type.in_(
        {ChatType.PRIVATE, ChatType.GROUP, ChatType.SUPERGROUP}))
    dp.include_router(router)
