from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from bot.databases.database import Workers
from config import URL_SITE


def get_confirm_kb(lang) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardBuilder()
    match lang:
        case 'ENG':
            ikb.add(InlineKeyboardButton(text="✅ Accept the rules", callback_data='back_to_start'))
        case 'RUS':
            ikb.add(InlineKeyboardButton(text="✅ Принять правила", callback_data='back_to_start'))
        case 'UKR':
            ikb.add(InlineKeyboardButton(text="✅ Прийняти правила", callback_data='back_to_start'))

    return ikb.as_markup()


def get_personal_account_kb(user) -> ReplyKeyboardMarkup:
    ikb = ReplyKeyboardBuilder()
    match user.lang:
        case 'ENG':
            ikb.add(KeyboardButton(text='📁 My Account'))
        case 'RUS':
            ikb.add(KeyboardButton(text='📁 Личный кабинет'))
        case 'UKR':
            ikb.add(KeyboardButton(text='📁 Особистий кабінет'))
    return ikb.as_markup(resize_keyboard=True)


def get_choice_lang_kb(code) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardBuilder()
    ikb.row(
        InlineKeyboardButton(text='🇷🇺 Русский', callback_data=f'choice_lang_RUS_{code}'),
        InlineKeyboardButton(text='🇺🇦 Український', callback_data=f'choice_lang_UKR_{code}'),
        InlineKeyboardButton(text='🇺🇸 English', callback_data=f'choice_lang_ENG_{code}'),
        width=2
    )
    return ikb.as_markup()


def get_choice_valute_kb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardBuilder()
    ikb.row(
        InlineKeyboardButton(text='🇺🇦 UAH', callback_data='choice_valute_UAH'),
        InlineKeyboardButton(text='🇱🇷 USD', callback_data='choice_valute_USD'),
    )
    ikb.row(
        InlineKeyboardButton(text='🇪🇺 EUR', callback_data='choice_valute_EUR'),
        InlineKeyboardButton(text='🇵🇱 PLN', callback_data='choice_valute_PLN')
    )
    ikb.row(
        InlineKeyboardButton(text='🇷🇺 RUB', callback_data='choice_valute_RUB'),
        InlineKeyboardButton(text='🇧🇾 BYN', callback_data='choice_valute_BYN'),
    )
    ikb.row(
        InlineKeyboardButton(text='🇨🇿 CZK', callback_data='choice_valute_CZK'),
        InlineKeyboardButton(text='🇬🇧 GBP', callback_data='choice_valute_GBP'),
    )
    return ikb.as_markup()


def get_profile_all(user):
    ikb = InlineKeyboardBuilder()
    match user.lang:
        case 'ENG':
            ikb.row(InlineKeyboardButton(text="💰 Wallet", callback_data='my_balance'))
            ikb.row(InlineKeyboardButton(text="ℹ Information", callback_data='information'))
            ikb.add(InlineKeyboardButton(text="⚙ Settings/support", callback_data='settings'))
            ikb.row(InlineKeyboardButton(text='🌐 Official website 🌐', url=URL_SITE))
        case 'RUS':
            ikb.row(InlineKeyboardButton(text="💰 Кошелёк", callback_data='my_balance'))
            ikb.row(InlineKeyboardButton(text="ℹ Информация", callback_data='information'))
            ikb.add(InlineKeyboardButton(text="⚙ Настройки/поддержка", callback_data='settings'))
            ikb.row(InlineKeyboardButton(text='🌐 Официальный сайт 🌐', url=URL_SITE))
        case 'UKR':
            ikb.row(InlineKeyboardButton(text="💰 Гаманець", callback_data='my_balance'))
            ikb.row(InlineKeyboardButton(text="ℹ Інформація", callback_data='information'))
            ikb.add(InlineKeyboardButton(text="⚙ Налаштування/підтримка", callback_data='settings'))
            ikb.row(InlineKeyboardButton(text='🌐 Офіційний сайт 🌐', url=URL_SITE))

    return ikb


def get_profile_kb(user, user_id) -> InlineKeyboardMarkup:
    ikb = get_profile_all(user)
    if Workers.get_or_none(Workers.user_id == user_id):
        match user.lang:
            case 'ENG':
                ikb.row(InlineKeyboardButton(text='🐘 Warker Panel', callback_data='worker_panel'))
            case 'RUS':
                ikb.row(InlineKeyboardButton(text='🐘 Панель воркера', callback_data='worker_panel'))
            case 'UKR':
                ikb.row(InlineKeyboardButton(text='🐘 Панель воркера', callback_data='worker_panel'))
    return ikb.as_markup()


def get_worker_kb(user) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardBuilder()
    match user.lang:
        case 'ENG':
            ikb.row(InlineKeyboardButton(text="📣 Mailing 📣", callback_data='worker_mailing'))
            ikb.row(InlineKeyboardButton(text="🐘 List of mammoths 🐘", callback_data='page_1'))
            ikb.row(InlineKeyboardButton(text="💸 Promotional code", callback_data='promo'))
            ikb.row(InlineKeyboardButton(text="💵 Minimum replenishment for all mammoths", callback_data='min_dep_all'))
            ikb.row(InlineKeyboardButton(text="🐘 Add mammoth by ID", callback_data='new_mamont_id'))
            ikb.row(InlineKeyboardButton(text="🗑 Delete all mammoths 🗑", callback_data='delete_all_mamonts_one'))
            ikb.row(InlineKeyboardButton(text="🔙 Back", callback_data='back_to_start'))
        case 'RUS':
            ikb.row(InlineKeyboardButton(text="📣 Рассылка 📣", callback_data='worker_mailing'))
            ikb.row(InlineKeyboardButton(text="🐘 Список мамонтов 🐘", callback_data='page_1'))
            ikb.row(InlineKeyboardButton(text="💸 Промокод", callback_data='promo'))
            ikb.row(InlineKeyboardButton(text="💵 Минимальное пополнение всем мамонтам", callback_data='min_dep_all'))
            ikb.row(InlineKeyboardButton(text="🐘 Добавить мамонта по ID", callback_data='new_mamont_id'))
            ikb.row(InlineKeyboardButton(text="🗑 Удалить всех мамонтов 🗑", callback_data='delete_all_mamonts_one'))
            ikb.row(InlineKeyboardButton(text="🔙 Назад", callback_data='back_to_start'))
        case 'UKR':
            ikb.row(InlineKeyboardButton(text="📣 Розсилка 📣", callback_data='worker_mailing'))
            ikb.row(InlineKeyboardButton(text="🐘 Список мамонтів 🐘", callback_data='page_1'))
            ikb.row(InlineKeyboardButton(text="💸 Промокод", callback_data='promo'))
            ikb.row(InlineKeyboardButton(text="💵 Мінімальне поповнення всім мамонтам", callback_data='min_dep_all'))
            ikb.row(InlineKeyboardButton(text="🐘 Додати мамонта за ID", callback_data='new_mamont_id'))
            ikb.row(InlineKeyboardButton(text="🗑 Видалити всіх мамонтів 🗑", callback_data='delete_all_mamonts_one'))
            ikb.row(InlineKeyboardButton(text="🔙 Назад", callback_data='back_to_start'))

    return ikb.as_markup()


def get_accept_lisences_kb(user_id, user) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardBuilder()
    match user.lang:
        case 'ENG':
            ikb.row(InlineKeyboardButton(text='Manage Referral', callback_data=f'mamont_id_{user_id}_1'))
        case 'RUS':
            ikb.row(InlineKeyboardButton(text='Управление рефералом', callback_data=f'mamont_id_{user_id}_1'))
        case 'UKR':
            ikb.row(InlineKeyboardButton(text='Керування рефералом', callback_data=f'mamont_id_{user_id}_1'))
    return ikb.as_markup()


