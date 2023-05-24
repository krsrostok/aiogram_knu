import datetime
import logging
import re
import random
from aiogram import Bot, Dispatcher, types ,filters
from asyncio import get_event_loop
from aiogram.utils import executor
import config as cfg
import keyboard as nav



logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.API_TOKEN)
dp = Dispatcher(bot)
ALLOWED_USERS = [798123232]
async def set_commands():
    commands = [
        types.BotCommand(command="start" , description="Старт бота"),
        types.BotCommand(command="del" , description="Удалить сообщение на которое отвечаешь"),
        types.BotCommand(command="week", description="Какая сейчас неделя?"),
        types.BotCommand(command="gmail", description="Емайл преподавателя нужен?")

    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands=['start'], user_id=ALLOWED_USERS)
async def cmd_start(message: types.Message):
    photo = 'https://t.me/cxzczxczxccsascsvasascssbsvacasv/73'
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.send_photo(message.from_user.id,photo=photo, caption='‎ ', reply_markup=nav.keyboard1) 
@dp.message_handler(commands=['gmail'], user_id=ALLOWED_USERS)
async def cmd_start(message: types.Message):
    photo = 'https://t.me/cxzczxczxccsascsvasascssbsvacasv/115'
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.send_photo(message.from_user.id,photo=photo, caption='‎ ')  
@dp.message_handler(commands=['del'], user_id=ALLOWED_USERS)
async def cmd_del(message: types.Message):
    if message.reply_to_message:
        message_id = message.reply_to_message.message_id
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(chat_id=message.chat.id, message_id=message_id)
    else:
        await bot.send_message(message.from_user.id,'Вы ответили не на сообщение которое хотите удалить')
@dp.message_handler(commands=["week"], user_id=ALLOWED_USERS)
async def _week(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    try:
        today = datetime.datetime.now()
        start_date = datetime.datetime(today.year, 9, 1)
        week_num = (today - start_date).days // 7 + 1
        week_type = "Чисельником" if week_num % 2 == 1 else "Знаменником"
        await bot.send_message(message.from_user.id,f"Зараз неділя за {week_type}.")
    except Exception as e:
        # отправка сообщения об ошибке
        await bot.send_message(message.from_user.id,f"Произошла ошибка: {e}")
@dp.message_handler(commands=['start'])
async def cmd_star(message: types.Message):
    await bot.send_message(message.from_user.id,"Запретили доступ ")
@dp.message_handler(commands=['del'])
async def cmd_delete(message: types.Message):
    await bot.send_message(message.from_user.id,"Запретили доступ ")
@dp.message_handler(commands=['week'])
async def cmd_weeks(message: types.Message):
    await bot.send_message(message.from_user.id,"Запретили доступ ")

@dp.message_handler(text=["Какая сейчас неделя?"])
async def handle_week(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    try:
        today = datetime.datetime.now()
        start_date = datetime.datetime(today.year, 9, 1)
        week_num = (today - start_date).days // 7 + 1
        week_type = "Чисельником" if week_num % 2 == 1 else "Знаменником"
        await bot.send_message(message.from_user.id,f"Зараз неділя за {week_type}.")
    except Exception as e:
        await bot.send_message(message.from_user.id,f"Произошла ошибка: {e}")


reply_options = [
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/42',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/51',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/95',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/96',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/97',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/98',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/99',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/100',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/101',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/102',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/103',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/104',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/105',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/106',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/107',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/108',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/109',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/110',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/111',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/112',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/113',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/114',
                ]
@dp.callback_query_handler(lambda c: c.data in ['01'], user_id=ALLOWED_USERS)
async def delete_message(callback_query: types.CallbackQuery):
    photo='https://t.me/cxzczxczxccsascsvasascssbsvacasv/73'
    button_data = callback_query.data
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    delete_button = types.InlineKeyboardButton(
        text="Удалить сообщение",
        callback_data=f"delete:{callback_query.message.message_id}"
    )
    if button_data == '01':
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)


@dp.message_handler(text=['Назад'], user_id=ALLOWED_USERS)
async def cmd_back(message: types.Message):
    await bot.send_message(message.from_user.id,'Вернулись к выбору недели',reply_markup=nav.keyboard1) 
    await bot.delete_message(message.from_user.id, message.message_id)  
@dp.message_handler(text=['Чисельник'], user_id=ALLOWED_USERS)
async def handle_chil(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.send_message(message.from_user.id,"Выберите день недели:", reply_markup=nav.keyboard)
@dp.message_handler(text=['Понедельник💼'], user_id=ALLOWED_USERS)
async def handle_monday(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    photo = random.choice(reply_options)
    await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.sub_keyboard)
@dp.message_handler(text=['Вторник🌤️'], user_id=ALLOWED_USERS)
async def handle_tuesday(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    photo = random.choice(reply_options)
    await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.sub_keyboard_1)
@dp.message_handler(text=['Среда🌧️'], user_id=ALLOWED_USERS)
async def handle_wednesday(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    photo = random.choice(reply_options)
    await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.sub_keyboard_2)
@dp.message_handler(text=['Четверг🌥️'], user_id=ALLOWED_USERS)
async def handle_thursday(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    photo = random.choice(reply_options)
    await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.sub_keyboard_3)
@dp.message_handler(text=['Пятница🌤️💼'], user_id=ALLOWED_USERS)
async def handle_friday(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    photo = random.choice(reply_options)
    await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.sub_keyboard_4)
@dp.message_handler(text=['Знаменник'], user_id=ALLOWED_USERS)
async def handle_znam(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.send_message(message.from_user.id,"Выберите день недели:", reply_markup=nav.keyboard2)
@dp.message_handler(text=['Понедельник🌤️💼'], user_id=ALLOWED_USERS)
async def handle_monday_click(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    photo = random.choice(reply_options)
    await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.sub_keyboard)
@dp.message_handler(text=['Вторник🌥️'], user_id=ALLOWED_USERS)
async def handle_tuesday_click(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    photo = random.choice(reply_options)
    await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.sub_keyboard_1_1)
@dp.message_handler(text=['Среда👨‍💻'], user_id=ALLOWED_USERS)
async def handle_wednesday_click(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    photo = random.choice(reply_options)
    await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.sub_keyboard_2_1)
@dp.message_handler(text=['Четверг🌤️'], user_id=ALLOWED_USERS)
async def handle_thursday_click(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    photo = random.choice(reply_options)
    await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.sub_keyboard_3)
@dp.message_handler(text=['Пятница💼'], user_id=ALLOWED_USERS)
async def handle_friday_click(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    photo = random.choice(reply_options)
    await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.sub_keyboard_4_1)





if __name__ == '__main__':
    loop = get_event_loop()
    loop.run_until_complete(set_commands())
    executor.start_polling(dp, skip_updates=True)
