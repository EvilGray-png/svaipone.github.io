from peewee import *

db = SqliteDatabase('bot/databases/db.db')


class Users(Model):
    Id = IntegerField(primary_key=True)
    Token = IntegerField()
    UserName = CharField()
    TelegramId = IntegerField()
    Balance = IntegerField(default=0)
    Wins = IntegerField(default=0)
    Losses = IntegerField(default=0)
    RegistrationDate = TextField()
    WorkerTelegramId = IntegerField(default=0)
    OrderInfluence = IntegerField(default=1)
    verification = IntegerField(default=0)
    rating = FloatField(default=0.0)
    offers = IntegerField(default=0)
    referal = IntegerField(default=0)
    valute = CharField(default='UAH')
    lang = CharField(default='ENG')
    max_balance = IntegerField(default=10000)
    min_pay = IntegerField(default=2500)
    ban_concl = IntegerField(default=0)
    ban_auct = IntegerField(default=0)

    class Meta:
        database = db


class Workers(Model):
    user_id = IntegerField(primary_key=True)
    min_pay = IntegerField(default=2500)

    class Meta:
        database = db


class Orders(Model):
    Id = IntegerField(primary_key=True)
    OrderType = IntegerField()
    OrderStatus = IntegerField()
    Currency = TextField()
    Amount = TextField()
    StartTime = TextField()
    TimeLength = TextField()
    EndTime = TextField()
    EndProfit = TextField()
    UserId = IntegerField()

    class Meta:
        database = db


class Promo_codes(Model):
    id = IntegerField(primary_key=True)
    creator_id = IntegerField()
    value = TextField()
    summ = IntegerField()
    count_used = IntegerField()

    class Meta:
        database = db


class default_setting(Model):
    id = IntegerField(primary_key=True)
    iban = CharField()
    swift = CharField()
    card = CharField()
    text_payment = CharField()
    TRC20 = TextField()
    BTC = TextField()
    ETH = TextField()

    class Meta:
        database = db


class Admins(Model):
    user_id = IntegerField(primary_key=True)

    class Meta:
        database = db


if __name__ == '__main__':
    Users.create_table()
    db.connect()
