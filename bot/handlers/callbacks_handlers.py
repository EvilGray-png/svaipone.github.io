import asyncio
from datetime import date

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.databases.database import Users, Workers
from bot.keyboards.keyboards import get_accept_lisences_kb, get_choice_valute_kb, get_confirm_kb, get_profile_kb
from bot.more.auxiliary_functions import my_profile
from bot.texts.texts import ACCEPT_LICENSE_TEXT
from config import PROFILE_PHOTO
from misc import bot

router = Router()


@router.callback_query(F.data.startswith('choice_lang_'))
async def choice_lang(call: CallbackQuery):
    reg_date = str(date.today())

    username = call.from_user.first_name if call.from_user.username is None else call.from_user.username

    Users.create(
        Token=call.from_user.id,
        UserName=username,
        TelegramId=call.from_user.id,
        RegistrationDate=reg_date
    )

    accept_lisence_code = call.data.split('_')[-1]

    if accept_lisence_code != 'None':
        name = call.from_user.first_name

        if Workers.get_or_none(Workers.user_id == accept_lisence_code):
            user = Users.get(Users.TelegramId == call.from_user.id)
            worker = Workers.get(Workers.user_id == accept_lisence_code)
            user.WorkerTelegramId = accept_lisence_code
            user.min_pay = worker.min_pay
            user.save()
            worker = Users.get(Users.TelegramId == accept_lisence_code)
            worker.referal += 1
            worker.save()
            text1 = ' '
            match user.lang:
                case 'ENG':
                    text1 = f'<b>💞 You have a new mammoth! @{call.from_user.username} | {call.from_user.first_name} {call.from_user.last_name} | {call.from_user.id}</b>'
                case 'RUS':
                    text1 = f'<b>💞 У вас новый мамонт! @{call.from_user.username} | {call.from_user.first_name} {call.from_user.last_name} | {call.from_user.id}</b>'
                case 'UKR':
                    text1 = f'<b>💞 У вас новий мамонт! @{call.from_user.username} | {call.from_user.first_name} {call.from_user.last_name} | {call.from_user.id}</b>'

            await bot.send_message(
                accept_lisence_code,
                text1,
                parse_mode='HTML',
                reply_markup=get_accept_lisences_kb(call.from_user.id, user)
            )
        else:
            user = Users.get(Users.TelegramId == accept_lisence_code)
            user.referal += 1
            user.save()
            user = Users.get(Users.TelegramId == call.from_user.id)
            text2 = ' '
            match user.lang:
                case 'ENG':
                    text2 = f'<b>🎉 You have a new referral! {name}</b>'
                case 'RUS':
                    text2 = f'<b>🎉 У вас новый реферал! {name}</b>'
                case 'UKR':
                    text2 = f'<b>🎉 У вас новий реферал! {name}</b>'

            await bot.send_message(
                accept_lisence_code,
                text2,
                parse_mode='HTML'
            )

    lang = call.data.split('_')[-2]
    user = Users.get(Users.TelegramId == call.from_user.id)
    user.lang = lang
    user.save()

    text = ' '
    match lang:
        case 'ENG':
            await call.answer('The language has been successfully chosen!')
            text = 'Select your currency'
        case 'RUS':
            await call.answer('Язык был успешно выбран!')
            text = 'Выберите вашу валюту'
        case 'UKR':
            await call.answer('Мову обрано вдало!')
            text = 'Виберіть вашу валюту'

    await call.message.delete()
    await call.message.answer(
        text=text,
        reply_markup=get_choice_valute_kb(),
        parse_mode='HTML'
    )


@router.callback_query(F.data.startswith('choice_valute_'))
async def accept_lisence(call: CallbackQuery):
    valute = call.data.split('_')[-1]
    user = Users.get(Users.TelegramId == call.from_user.id)
    user.valute = valute
    user.save()
    s = {'UAH': '🇺🇦', 'USD': '🇱🇷', 'EUR': '🇪🇺', 'PLN': '🇵🇱', 'RUB': '🇷🇺', 'BYN': '🇧🇾', 'CZK': '🇨🇿', 'GBP': '🇬🇧'}
    match user.lang:
        case 'ENG':
            await call.answer(f'The {s[valute]} {valute} currency has been successfully selected!')
        case 'RUS':
            await call.answer(f'Валюта {s[valute]} {valute} успешно выбрана!')
        case 'UKR':
            await call.answer(f'Валюта {s[valute]} {valute} успішно обрана!')

    await call.message.delete()
    await call.message.answer(
        text=ACCEPT_LICENSE_TEXT[user.lang],
        reply_markup=get_confirm_kb(user.lang),
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'back_to_start')
async def back_to_start(call: CallbackQuery):
    text = my_profile(call=call)

    try:
        await call.message.delete()
    except Exception as ex:
        print(ex)
    user = Users.get(Users.TelegramId == call.from_user.id)
    await call.message.answer_photo(
        PROFILE_PHOTO,
        text,
        reply_markup=get_profile_kb(user, call.from_user.id),
        parse_mode='HTML'
    )

