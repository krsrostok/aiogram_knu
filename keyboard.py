from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
button01=KeyboardButton('Чисельник')
button02=KeyboardButton('Знаменник')
button03=KeyboardButton('Какая сейчас неделя?')
button6 = KeyboardButton('Назад')

button1 = KeyboardButton(
    text='Понедельник💼')
button2 = KeyboardButton(
    text='Вторник🌤️')
button3 = KeyboardButton(
    text='Среда🌧️')
button4 = KeyboardButton(
    text='Четверг🌥️')
button5 = KeyboardButton(
    text='Пятница🌤️💼')
button001 = KeyboardButton(
    text='Понедельник🌤️💼')
button002 = KeyboardButton(
    text='Вторник🌥️')
button003 = KeyboardButton(
    text='Среда👨‍💻')
button004 = KeyboardButton(
    text='Четверг🌤️')
button005 = KeyboardButton(
    text='Пятница💼')
keyboard = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True,row_width=3).add(button1,button2,button3,button4,button5)
keyboard.add(button6)
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True,row_width=2).add(button01,button02,button03)
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True,row_width=3).add(button001,button002,button003,button004,button005)
keyboard2.add(button6)

#Понедельник
sub_button0 = KeyboardButton('❌',callback_data='01')
sub_button1 = KeyboardButton('1 Іноземна мова (практ.)|Ажогіна Н.В',url='https://zoom.us/j/94696604295?pwd=NTBkeFo2WmhzSk1aVFd3QnBRekpydz09')
sub_button2 = KeyboardButton('2 Диференціаль-ні рівняння (пр)|ас. Субота С.Л.',url='https://lu-se.zoom.us/j/7830191951')
sub_button3 = KeyboardButton('3 Математичний аналіз (пр)|ас. Субота С.Л.',url='https://join.skype.com/G4qXe3LgdZLL')
#Вторник
sub_button4 = KeyboardButton('1 Іноземна мова (практ.)|Ажогіна Н.В',url='https://zoom.us/j/94696604295?pwd=NTBkeFo2WmhzSk1aVFd3QnBRekpydz09')
sub_button5 = KeyboardButton('2 Іноземна мова (практ.)|Ажогіна Н.В',url='https://zoom.us/j/94696604295?pwd=NTBkeFo2WmhzSk1aVFd3QnBRekpydz09')
sub_button6 = KeyboardButton('3 Молекулярна фізика(пр)|доц. Кудря В.Ю.',url='https://join.skype.com/zjFW2d9yTNfz')
sub_button6_1 = KeyboardButton('3 Лінійна алгебра (пр)|ас. Теслик О.М.',url='https://us02web.zoom.us/j/4388908145?pwd=NE1BTlcwcTlDTXVYTkFnQ2FNTFcxZz09')
#Среда
sub_button7 = KeyboardButton('1 260,261 лаб. Практикум з мол.фіз.',url='https://join.skype.com/zjFW2d9yTNfz')
sub_button8 = KeyboardButton('2 Практикум з молекулярної фізики',url='https://join.skype.com/zjFW2d9yTNfz')
sub_button9 = KeyboardButton('3 Молекулярна фізика (пр)',url='https://join.skype.com/zjFW2d9yTNfz')
#Четверг
sub_button10 = KeyboardButton('1 Вступ до університетських студій (лекція)|проф. Горбань Т.Ю., проф. Івченко В.М.',url='https://us05web.zoom.us/j/86455322786?pwd=TXk4aDJjYkZ5a3NlNU9weUtLRkVqQT09')
sub_button11 = KeyboardButton('2 Математичний аналіз (лекція)|доц. Майко Н.В.',url='https://lu-se.zoom.us/j/7830191951')
sub_button12 = KeyboardButton('3 Лінійна алгебра та аналітична геометрія (лекція)|проф. Вільчинський С.Й., ас. Приходько О.О.',url='https://knu-ua.zoom.us/j/87693487975?pwd=VUhpTE85MFk4TFJIUWJWNjFGSi9GQT09')
#Пятница
sub_button13 = KeyboardButton('1 Диференціальні рівняння (лекція)|доц. Романенко О.В.',url='https://classroom.google.com/c/NTgzOTE2MTc4MzM4?cjc=dkk6xqf')
sub_button13_2 = KeyboardButton('1 Молекулярна фізика (лекція)|проф. Гаврюшенко  Д.А.',url='https://meet.google.com/rjx-efcr-ofn ')
sub_button13_1 = KeyboardButton('2 Молекулярна фізика (лекція)|проф. Гаврюшенко  Д.А.',url='https://meet.google.com/rjx-efcr-ofn ')
sub_button14 = KeyboardButton('3 Математичний аналіз (пр)|ас. Субота С.Л.',url='https://join.skype.com/G4qXe3LgdZLL')

sub_keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(sub_button1, sub_button2, sub_button3,sub_button0)
sub_keyboard_1 = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(sub_button4, sub_button5, sub_button6,sub_button0)
#По знаменнику#
sub_keyboard_1_1 = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(sub_button4, sub_button5, sub_button6_1,sub_button0)
###############
#По Чисельнику#
sub_keyboard_2 = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(sub_button8,sub_button9,sub_button0)
###############
sub_keyboard_2_1 = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(sub_button7, sub_button8,sub_button9,sub_button0)
sub_keyboard_3 = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(sub_button10, sub_button11, sub_button12,sub_button0)
#По знаменнику#
sub_keyboard_4= InlineKeyboardMarkup(resize_keyboard=True,row_width=1).add(sub_button13,sub_button14,sub_button0)
#По Чисельнику#
sub_keyboard_4_1 = InlineKeyboardMarkup(resize_keyboard=True,row_width=1).add(sub_button13_2,sub_button13_1,sub_button14)
sub_keyboard_4_1.add(sub_button0)
