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
    ]
    await bot.set_my_commands(commands)
async def check_sub_channels (channels, user_id):
    for channel in channels:
        chat_member = await bot.get_chat_member (chat_id=channel[1], user_id=user_id)
        if chat_member['status'] == 'left':
            return False
    return True
@dp.message_handler(commands=['start'], user_id=ALLOWED_USERS)
async def cmd_start(message: types.Message):
    photo = 'https://t.me/cxzczxczxccsascsvasascssbsvacasv/73'
    if await check_sub_channels(cfg.CHANNELS,message.from_user.id):
        await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.keyboard1)   
    else:
        await bot.send_message(message.from_user.id, cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())

@dp.message_handler(commands=['start','del','week'])
async def cmd_star(message: types.Message):
    await message.answer("Запретили доступ , иди нахуй")

@dp.callback_query_handler(text="subchanneldone", user_id=ALLOWED_USERS)
async def subchanneldone (message: types.Message):
    photo = 'https://t.me/cxzczxczxccsascsvasascssbsvacasv/73'
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if await check_sub_channels (cfg.CHANNELS, message.from_user.id):
        await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.keyboard1)
    else:
        await bot.send_message(message.from_user.id, cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())

@dp.message_handler(commands=['del'], user_id=ALLOWED_USERS)
async def cmd_del(message: types.Message):
    if await check_sub_channels(cfg.CHANNELS, message.from_user.id):
        message_id = message.message_id
        if message.reply_to_message:
            message_id = message.reply_to_message.message_id
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(chat_id=message.chat.id, message_id=message_id)
    else:
        await bot.send_message(message.from_user.id, cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())
@dp.message_handler(text=["Какая сейчас неделя?"])
async def get_week(message: types.Message):
    try:
        today = datetime.datetime.now()
        start_date = datetime.datetime(today.year, 9, 1)
        week_num = (today - start_date).days // 7 + 1
        week_type = "Чисельником" if week_num % 2 == 1 else "Знаменником"
        await message.answer(f"Зараз неділя за {week_type}.")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")

@dp.message_handler(text=["week"], user_id=ALLOWED_USERS)
async def get_week(message: types.Message):
    try:
        today = datetime.datetime.now()
        start_date = datetime.datetime(today.year, 9, 1)
        week_num = (today - start_date).days // 7 + 1
        week_type = "Чисельником" if week_num % 2 == 1 else "Знаменником"
        await message.answer(f"Зараз неділя за {week_type}.")
    except Exception as e:
        # отправка сообщения об ошибке
        await message.answer(f"Произошла ошибка: {e}")
reply_options = [
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/42',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/45',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/46',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/47',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/48',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/49',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/50',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/51',
                ]
reply_options1 = [
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/53',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/54',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/55',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/56',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/57',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/58',
                'https://t.me/cxzczxczxccsascsvasascssbsvacasv/59',
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
    if await check_sub_channels(cfg.CHANNELS,message.from_user.id):
        await message.reply('Вернулись к выбору недели',reply_markup=nav.keyboard1)   
    else:
        await bot.send_message(message.from_user.id, cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())

@dp.message_handler(text=['Чисельник'], user_id=ALLOWED_USERS)
async def handle_friday_click(message: types.Message):
    if await check_sub_channels(cfg.CHANNELS,message.from_user.id):
        await bot.send_message(message.from_user.id,"Выберите день недели:", reply_markup=nav.keyboard2)
    else:
        await bot.send_message(message.from_user.id,cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())
@dp.message_handler(text=['Понедельник💼'], user_id=ALLOWED_USERS)
async def handle_monday_click(message: types.Message):
    video = random.choice(reply_options1)
    if await check_sub_channels(cfg.CHANNELS,message.from_user.id):
        await message.answer_video(video=video, caption='‎ ', reply_markup=nav.sub_keyboard)
    else:
        await bot.send_message(message.from_user.id,cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())
@dp.message_handler(text=['Вторник🌤️'], user_id=ALLOWED_USERS)
async def handle_tuesday_click(message: types.Message):
    photo = random.choice(reply_options)
    if await check_sub_channels(cfg.CHANNELS,message.from_user.id):
        await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.sub_keyboard_1)
    else:
        await bot.send_message(message.from_user.id,cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())
@dp.message_handler(text=['Среда🌧️'], user_id=ALLOWED_USERS)
async def handle_wednesday_click(message: types.Message):
    photo = random.choice(reply_options)
    if await check_sub_channels(cfg.CHANNELS,message.from_user.id):
        await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.sub_keyboard_2)
    else:
        await bot.send_message(message.from_user.id,cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())
@dp.message_handler(text=['Четверг🌥️'], user_id=ALLOWED_USERS)
async def handle_thursday_click(message: types.Message):
    photo = random.choice(reply_options)
    if await check_sub_channels(cfg.CHANNELS,message.from_user.id):
        await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.sub_keyboard_3)
    else:
        await bot.send_message(message.from_user.id,cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())
@dp.message_handler(text=['Пятница🌤️💼'], user_id=ALLOWED_USERS)
async def handle_friday_click(message: types.Message):
    photo = random.choice(reply_options)
    if await check_sub_channels(cfg.CHANNELS,message.from_user.id):
        await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.sub_keyboard_4)
    else:
        await bot.send_message(message.from_user.id,cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())
@dp.message_handler(text=['Знаменник'], user_id=ALLOWED_USERS)
async def handle_friday_click(message: types.Message):
    if await check_sub_channels(cfg.CHANNELS,message.from_user.id):
        await bot.send_message(message.from_user.id,"Выберите день недели:", reply_markup=nav.keyboard2)
    else:
        await bot.send_message(message.from_user.id,cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())
@dp.message_handler(text=['Понедельник🌤️💼'], user_id=ALLOWED_USERS)
async def handle_monday_click(message: types.Message):
    video = random.choice(reply_options1)
    if await check_sub_channels(cfg.CHANNELS,message.from_user.id):
        await message.answer_video(video=video, caption='‎ ', reply_markup=nav.sub_keyboard)
    else:
        await bot.send_message(message.from_user.id,cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())
@dp.message_handler(text=['Вторник🌥️'], user_id=ALLOWED_USERS)
async def handle_tuesday_click(message: types.Message):
    photo = random.choice(reply_options)
    if await check_sub_channels(cfg.CHANNELS,message.from_user.id):
        await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.sub_keyboard_1_1)
    else:
        await bot.send_message(message.from_user.id,cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())
@dp.message_handler(text=['Среда👨‍💻'], user_id=ALLOWED_USERS)
async def handle_wednesday_click(message: types.Message):
    photo = random.choice(reply_options)
    if await check_sub_channels(cfg.CHANNELS,message.from_user.id):
        await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.sub_keyboard_2)
    else:
        await bot.send_message(message.from_user.id,cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())
@dp.message_handler(text=['Четверг🌤️'], user_id=ALLOWED_USERS)
async def handle_thursday_click(message: types.Message):
    photo = random.choice(reply_options)
    if await check_sub_channels(cfg.CHANNELS,message.from_user.id):
        await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.sub_keyboard_3)
    else:
        await bot.send_message(message.from_user.id,cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())
@dp.message_handler(text=['Пятница💼'], user_id=ALLOWED_USERS)
async def handle_friday_click(message: types.Message):
    photo = random.choice(reply_options)
    if await check_sub_channels(cfg.CHANNELS,message.from_user.id):
        await message.answer_photo(photo=photo, caption='‎ ', reply_markup=nav.sub_keyboard_4_1)
    else:
        await bot.send_message(message.from_user.id,cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())





if __name__ == '__main__':
    loop = get_event_loop()
    loop.run_until_complete(set_commands())
    executor.start_polling(dp, skip_updates=True)
