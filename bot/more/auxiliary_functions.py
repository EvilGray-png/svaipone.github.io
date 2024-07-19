import random

import requests
from bot.databases.database import Users, Admins, Orders
from bot.keyboards.keyboards import *
from bot.texts.texts import PROFILE_TEXT
from config import *
from misc import bot


def my_profile(call=None, message=None):
    name = message.chat if call is None else call.from_user
    user = Users.get(Users.TelegramId == name.id)
    username = name.first_name
    reg_date = user.RegistrationDate.split(' ')[0]
    verif = '❌' if user.verification == 0 else '✅'
    referal = user.referal
    text = PROFILE_TEXT[user.lang].replace(
        '{username}', username
    ).replace(
        '{reg_date}', reg_date
    ).replace(
        '{verif}', verif
    ).replace(
        '{referal}', str(referal)
    ).replace(
        '{BOT_NAME}', BOT_NAME
    ).replace(
        '{name.id}', str(name.id)
    )
    return text


async def call_profile_menu(message, user, user_id):
    text = my_profile(message=message)
    await message.answer_photo(
        PROFILE_PHOTO,
        text,
        parse_mode='html',
        reply_markup=get_profile_kb(user, user_id)
    )
