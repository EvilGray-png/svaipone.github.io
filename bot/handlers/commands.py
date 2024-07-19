from datetime import date

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.databases.database import Users, Workers
from bot.keyboards.keyboards import get_personal_account_kb, get_choice_lang_kb, get_worker_kb
from bot.more.auxiliary_functions import call_profile_menu
from config import *

router = Router()


@router.message(Command("start"))
async def start_message(message: Message):
    if message.chat.type != 'private':
        return

    if len(message.text.split(' ')) == 2:
        code = message.text.split(' ')[-1]
    else:
        code = 'None'

    reg_date = str(date.today())

    if Users.get_or_none(Users.TelegramId == message.chat.id):
        if code == 'worker':
            username = message.chat.first_name if message.chat.username is None else message.chat.username
            Users.create(
                Token=message.from_user.id,
                UserName=username,
                TelegramId=message.from_user.id,
                RegistrationDate=reg_date
            )
            await new_worker(message)
        else:
            user = Users.get(Users.TelegramId == message.from_user.id)
            text = ' '
            match user.lang:
                case 'ENG':
                    text = 'Your personal account 📁'
                case 'RUS':
                    text = 'Ваш личный кабинет 📁'
                case 'UKR':
                    text = 'Ваш особистий кабінет 📁'

            await message.answer(
                text=text,
                reply_markup=get_personal_account_kb(user)
            )
            await call_profile_menu(message, user, message.chat.id)
    else:
        if code == 'worker':
            username = message.chat.first_name if message.chat.username is None else message.chat.username
            Users.create(
                Token=message.from_user.id,
                UserName=username,
                TelegramId=message.from_user.id,
                RegistrationDate=reg_date
            )
            await new_worker(message)
        else:
            text = '''<b>
🌍 Выберите язык:
🌍 Select a language:
🌍 Оберіть мову:
</b>'''
            await message.delete()
            await message.answer(
                text=text,
                reply_markup=get_choice_lang_kb(code),
                parse_mode='HTML'
            )


@router.message(Command(commands=['Worker', 'worker', 'Воркер', 'воркер']))
async def new_worker(message: Message):
    if message.chat.type != 'private':
        return

    if not Workers.get_or_none(Workers.user_id == message.from_user.id):
        Workers.create(user_id=message.from_user.id)

    user = Users.get(Users.TelegramId == message.chat.id)
    text = ' '
    match user.lang:
        case 'ENG':
            text = "<b>👨‍💻You have entered the Worker's menu👨‍💻</b>"
        case 'RUS':
            text = '<b>👨‍💻Вы вошли в меню воркера👨‍💻</b>'
        case 'UKR':
            text = '<b>👨‍💻Ви увійшли в меню воркера👨‍💻</b>'
    await message.answer(
        text=text,
        parse_mode='HTML',
        reply_markup=get_worker_kb(user)
    )
