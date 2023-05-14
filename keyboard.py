from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import CHANNELS
button01=KeyboardButton(text='Чисельник',callback_data='1')
button02=KeyboardButton(text='Знаменник',callback_data='2')
button03=KeyboardButton(text='Какая сейчас неделя?',callback_data='12')
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False)
keyboard1 .add(button01,button02)
keyboard1.add(button03)
button1 = KeyboardButton(text='Понедельник💼',callback_data='3')
button2 = KeyboardButton(text='Вторник🌤️',callback_data='4')
button3 = KeyboardButton(text='Среда🌧️',callback_data='5')
button4 = KeyboardButton(text='Четверг🌥️',callback_data='6')
button5 = KeyboardButton(text='Пятница🌤️💼',callback_data='7')
button6 = KeyboardButton(text='Уголок разраба👨‍💻💻',callback_data='8')
button7 = KeyboardButton(text="Назад",callback_data='9')
keyboard = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False)
keyboard .add(button1, button2) 
keyboard .add(button3, button4) 
keyboard .add(button5)
keyboard .add(button6,button7)
button1 = KeyboardButton(text='Понедельник🌤️💼',callback_data='3')
button2 = KeyboardButton(text='Вторник🌥️',callback_data='4')
button3 = KeyboardButton(text='Среда👨‍💻',callback_data='5')
button4 = KeyboardButton(text='Четверг🌤️',callback_data='6')
button5 = KeyboardButton(text='Пятница💼',callback_data='7')
button6 = KeyboardButton(text='Уголок разраба🌧️💻',callback_data='8')
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False)
keyboard2 .add(button1, button2) 
keyboard2 .add(button3, button4) 
keyboard2 .add(button5)
keyboard2 .add(button6,button7)
sub_button01 = KeyboardButton('Удалить клавиатуру',callback_data='01')
#Понедельник
sub_button1 = KeyboardButton(text='Іноземна мова (практ.)|Ажогіна Н.В',url='https://zoom.us/j/94696604295?pwd=NTBkeFo2WmhzSk1aVFd3QnBRekpydz09',callback_data='a')
sub_button2 = KeyboardButton(text='Диференціаль-ні рівняння (пр)|ас. Субота С.Л.',url='https://lu-se.zoom.us/j/7830191951',callback_data='b')
sub_button3 = KeyboardButton(text='Математичний аналіз (пр)|ас. Субота С.Л.',url='https://join.skype.com/G4qXe3LgdZLL',callback_data='c')
#Вторник
sub_button4 = KeyboardButton(text='Іноземна мова (практ.)|Ажогіна Н.В',url='https://zoom.us/j/94696604295?pwd=NTBkeFo2WmhzSk1aVFd3QnBRekpydz09')
sub_button5 = KeyboardButton(text='Іноземна мова (практ.)|Ажогіна Н.В',url='https://zoom.us/j/94696604295?pwd=NTBkeFo2WmhzSk1aVFd3QnBRekpydz09')
sub_button6 = KeyboardButton(text='Молекулярна фізика(пр)|доц. Кудря В.Ю.',url='https://join.skype.com/zjFW2d9yTNfz')
sub_button6_1 = KeyboardButton(text='Лінійна алгебра (пр)|ас. Теслик О.М.',url='https://us02web.zoom.us/j/4388908145?pwd=NE1BTlcwcTlDTXVYTkFnQ2FNTFcxZz09')
#Среда
sub_button7 = KeyboardButton(text='260,261 лаб. Практикум з мол.фіз.',url='https://join.skype.com/zjFW2d9yTNfz')
sub_button8 = KeyboardButton(text='Практикум з молекулярної фізики',url='https://join.skype.com/zjFW2d9yTNfz')
#По знаменнику
sub_button9 = KeyboardButton(text='Молекулярна фізика (пр)',url='https://join.skype.com/zjFW2d9yTNfz')
#Четверг
sub_button10 = KeyboardButton(text='Вступ до університетських студій (лекція)|проф. Горбань Т.Ю., проф. Івченко В.М.',url='https://us05web.zoom.us/j/86455322786?pwd=TXk4aDJjYkZ5a3NlNU9weUtLRkVqQT09')
sub_button11 = KeyboardButton(text='Математичний аналіз (лекція)|доц. Майко Н.В.',url='https://lu-se.zoom.us/j/7830191951')
sub_button12 = KeyboardButton(text='Лінійна алгебра та аналітична геометрія (лекція)|проф. Вільчинський С.Й., ас. Приходько О.О.',url='https://knu-ua.zoom.us/j/87693487975?pwd=VUhpTE85MFk4TFJIUWJWNjFGSi9GQT09')
#Пятница
sub_button13 = KeyboardButton(text='Диференціальні рівняння (лекція)|доц. Романенко О.В.',url='https://classroom.google.com/c/NTgzOTE2MTc4MzM4?cjc=dkk6xqf')
sub_button13_1 = KeyboardButton(text='Молекулярна фізика (лекція)|проф. Гаврюшенко  Д.А.',url='https://meet.google.com/rjx-efcr-ofn ')
#По знаменникам
sub_button13_2 = KeyboardButton(text='Молекулярна фізика Тг канал|проф. Гаврюшенко  Д.А.',url='https://t.me/+zeInJhg4zxA2NTYy')
#####################################################################################################################################################
sub_button14 = KeyboardButton(text='Математичний аналіз (пр)|ас. Субота С.Л.',url='https://join.skype.com/G4qXe3LgdZLL')

sub_keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(sub_button1, sub_button2, sub_button3,sub_button01)
sub_keyboard_1 = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(sub_button4, sub_button5, sub_button6,sub_button01)

sub_keyboard_1_1 = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(sub_button4, sub_button5, sub_button6_1,sub_button01)

sub_keyboard_2 = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(sub_button7, sub_button8,sub_button01)
sub_keyboard_3 = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(sub_button10, sub_button11, sub_button12,sub_button01)
sub_keyboard_4= InlineKeyboardMarkup(resize_keyboard=True,)
sub_keyboard_4.add(sub_button13)
sub_keyboard_4.add(sub_button14)
sub_keyboard_4.add(sub_button01)

sub_keyboard_4_1 = InlineKeyboardMarkup(resize_keyboard=True)
sub_keyboard_4_1.add(sub_button13_1,sub_button13_2)
sub_keyboard_4_1.add(sub_button13_1,sub_button13_2)
sub_keyboard_4_1.add(sub_button14)
sub_keyboard_4_1.add(sub_button01)
def showChannels():
    keyboard1 = InlineKeyboardMarkup(row_width=1)
    for channel in CHANNELS:
        btn = InlineKeyboardButton(text=channel[0], url=channel[2])
        keyboard1.insert(btn)
    btnDoneSub = InlineKeyboardButton(text="Я подписАлся", callback_data="subchanneldone")
    keyboard1.insert(btnDoneSub)
    return keyboard1
