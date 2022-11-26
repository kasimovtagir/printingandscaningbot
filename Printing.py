from glob import glob
from socket import PF_RDS
import os 
from datetime import datetime
import telebot
from telebot import types
from PyPDF2 import PdfFileReader
import string
from datetime import datetime
import time
from collections import deque
#import UploadTG
import CallBackTG


def return_time():
    dt = datetime.now()
    dt_string = dt.strftime("%d.%m %H:%M")
    return dt_string

def List_Print(bot,call):
    with open('/mnt/Logs/logs.txt', 'a') as logs:
            logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - выбрал ПЕЧАТЬ  " + "\n")
    keyboard_list_print_for_print_2520_2530 = types.InlineKeyboardMarkup(row_width=4)
    #keyboard_list_print_for_print_2530 = types.InlineKeyboardMarkup(row_width=2)
    keyboard_list_print_for_print_cerkov = types.InlineKeyboardMarkup(row_width=4)
    keyboard_list_print_for_print_birz = types.InlineKeyboardMarkup(row_width=4)
    
    key_print14 = types.InlineKeyboardButton(text='print14', callback_data='print14_print')
    key_print15 = types.InlineKeyboardButton(text='print15', callback_data='print15_print')
    key_print16 = types.InlineKeyboardButton(text='print16', callback_data='print16_print')
    key_print10 = types.InlineKeyboardButton(text='print10', callback_data='print10_print')
    key_print9 = types.InlineKeyboardButton(text='print9', callback_data='print9_print')
    key_print13 = types.InlineKeyboardButton(text='print13', callback_data='print13_print')
    key_print19 = types.InlineKeyboardButton(text='print19', callback_data='print19_print')
    key_print18 = types.InlineKeyboardButton(text='print18', callback_data='print18_print')
    key_print7 = types.InlineKeyboardButton(text='print7', callback_data='print7_print')
    key_print21 = types.InlineKeyboardButton(text='print21', callback_data='print21_print')
    key_print4318 = types.InlineKeyboardButton(text='print4318', callback_data='print4318_print')
    key_print22 = types.InlineKeyboardButton(text='print22', callback_data='print22_print')
    key_print17 = types.InlineKeyboardButton(text='print17', callback_data='print17_print')
    key_print431 = types.InlineKeyboardButton(text='print431', callback_data='print431_print')

    keyboard_list_print_for_print_2520_2530.add(key_print14,key_print10,key_print9,key_print13)
    keyboard_list_print_for_print_2520_2530.add(key_print19, key_print15,key_print16,key_print22)
    bot.send_message(call.from_user.id, text='Выбери принтер для печати.\nПринтеры в 2520/2530',reply_markup=keyboard_list_print_for_print_2520_2530)

    keyboard_list_print_for_print_cerkov.add(key_print18, key_print7,key_print21,key_print4318)
    bot.send_message(call.from_user.id, text='Принтеры в церкви',reply_markup=keyboard_list_print_for_print_cerkov)

    keyboard_list_print_for_print_birz.add(key_print17,key_print431)
    bot.send_message(call.from_user.id, text='Принтеры на Биржевой 16/14',reply_markup=keyboard_list_print_for_print_birz)




def Show_Information (bot:telebot.TeleBot,call:telebot.types.CallbackQuery,choose_printer):
    try :
        bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "choose_printer", choose_printer)
    except Exception as ex:
        # bot.current_states.set_state(call.message.chat.id, call.message.chat.id, None)
        # bot.current_states.reset_data(call.message.chat.id, call.message.chat.id)
        # bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "choose_printer", choose_printer)
        bot.send_message(call.message.chat.id,f"{ex}\nПроизошла неизвестная ошибка, нажми на кнопку start")

    data = bot.current_states.get_data(call.message.chat.id, call.message.chat.id )
    if data is not None:
        file_name = data.get("file_name")
    else:
        file_name = None
    
    if file_name is not None:
        #chose_printer = choose_printer
        bot.send_message(call.message.chat.id, f"Файл: {file_name} \nВыбран принтер {choose_printer}. \nФормат файла А4(по умолчанию)",  reply_markup=CallBackTG.pre_printing())
        #print(f"Пользователь {str(call.from_user.first_name)} выбрал принтер {chose_printer}")
    else:
        #chose_printer = choose_printer
        #print(f"Пользователь {str(call.from_user.first_name)} выбрал принтер {chose_printer}")
        bot.send_message(call.message.chat.id, f"Выбран принтер {choose_printer}. \nЗагрузи файл который нужно распечатать: \nФормат файла А4(по умолчанию)")
    with open('logs.txt', 'a') as logs:
        logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - выбрал {choose_printer}  " + "\n")
    logs.close()

# def pre_printing():
#     keyboard_print_or_addition = types.InlineKeyboardMarkup(row_width=3)
#     prints = types.InlineKeyboardButton(text='Печать', callback_data='Printing')
#     addition = types.InlineKeyboardButton(text='Дополнительно', callback_data='Additionally')
#     keyboard_print_or_addition.add(prints, addition)

#     return keyboard_print_or_addition