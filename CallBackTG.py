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


def return_time():
    dt = datetime.now()
    dt_string = dt.strftime("%d.%m %H:%M")
    return dt_string


def callback_start(bot:telebot.TeleBot, message):
    with open('/mnt/Logs/logs.txt', 'a') as logs:
            logs.write( f"{str(return_time())} - Пользователь: {str(message.from_user.first_name)} - запустил бота\n")
    
    bot.current_states.set_state(message.chat.id, message.chat.id, None)
    bot.current_states.reset_data(message.chat.id, message.chat.id)

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    button = types.KeyboardButton(text='/start')
    markup.add(button) 
    
    bot.send_message(message.chat.id, text='Привет, '+str(message.from_user.first_name), reply_markup=markup)
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    button_print = types.InlineKeyboardButton(text='Печать', callback_data='list_Print')
    button_scan = types.InlineKeyboardButton(text='Сканирование', callback_data='list_Scan')
    print(message.chat.id)
    
    data = bot.current_states.get_data(message.chat.id,message.chat.id )
    if data is not None:
        file_name = data.get("file_name")
        choose_printer = data.get("choose_printer")
        pages_print = data.get("pages_print")
        count_copies = data.get("count_copies")
        copies =  data.get("copies")
        pagess =  data.get("pagess")
    else:
        file_name = None
        choose_printer = None
        pages_print = None
        count_copies = None
        copies = None
        pagess - None

    print(file_name)
    print (choose_printer)
    print(pages_print)
    print(count_copies)
    print(copies)
    print(pagess)
    
     
    if message.chat.id == 815850294:
        admins_button = types.InlineKeyboardButton(text='Администрирование', callback_data='admins')
        keyboard.add(button_print, button_scan, admins_button)
        bot.send_message(message.chat.id, text='Выбирай:', reply_markup=keyboard)
    else:     
        keyboard.add(button_print, button_scan)
        bot.send_message(message.chat.id, text='Выбирай:', reply_markup=keyboard)
    logs.close()    


def admins(bot,call):
    with open("/mnt/Logs/logs.txt") as f:
        for row in deque(f, 7):
            time.sleep(2)
            bot.send_message(call.from_user.id, text=row.strip())
        	#print (row.strip())

    # r = os.system("tail -n 10 /mnt/Logs/logs.txt")
    # for items in r:
    #     bot.send_message(call.from_user.id, text=items)
    #     time.sleep(2)
        

def callback_list_Print_for_scan(bot,call):
    with open('/mnt/Logs/logs.txt', 'a') as logs:
            logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)}  выбрал СКАНИРОВАНИЕ\n")
    keyboard_list_print_for_scan_2520_2530 = types.InlineKeyboardMarkup(row_width=4)
    keyboard_list_print_for_scan_church = types.InlineKeyboardMarkup(row_width=4)
    keyboard_list_print_for_scan_birz = types.InlineKeyboardMarkup(row_width=4)
    #key_print14 = types.InlineKeyboardButton(text='print14', callback_data='print14_scan')
    key_print15 = types.InlineKeyboardButton(text='print15', callback_data='print15_scan')
    key_print16 = types.InlineKeyboardButton(text='print16', callback_data='print16_scan')
    key_print10 = types.InlineKeyboardButton(text='print10', callback_data='print10_scan')
    key_print9 = types.InlineKeyboardButton(text='print9', callback_data='print9_scan')
    key_print13 = types.InlineKeyboardButton(text='print13', callback_data='print13_scan')
    key_print19 = types.InlineKeyboardButton(text='print19', callback_data='print19_scan')
    key_print18 = types.InlineKeyboardButton(text='print18', callback_data='print18_scan')
    key_print7 = types.InlineKeyboardButton(text='print7', callback_data='print7_scan')
    # key_back_scan = types.InlineKeyboardButton(text='Back to choose', callback_data='key_back_print')
    key_print21 = types.InlineKeyboardButton(text='print21', callback_data='print21_scan')
    key_print4318 = types.InlineKeyboardButton(text='print4318', callback_data='print4318_scan')
    key_print22 = types.InlineKeyboardButton(text='print22', callback_data='print22_scan')

    key_print17 = types.InlineKeyboardButton(text='print17', callback_data='print17_scan')
    key_print431 = types.InlineKeyboardButton(text='print431', callback_data='print431_scan')
 

    keyboard_list_print_for_scan_2520_2530.add( key_print15, key_print16,key_print19)
    keyboard_list_print_for_scan_2520_2530.add(key_print10, key_print9, key_print13)
    keyboard_list_print_for_scan_2520_2530.add(key_print22)    # , key_back_scan)
    # bot.send_message(call.from_user.id,"В адресной книге выбери Scan to Telegram BOT и после того, как отсканируешь файл выбери принтер")
    
    bot.send_message(call.from_user.id,
                        text='В адресной книге выбери Scan to Telegram BOT и после того, как отсканируешь файл выбери принтер на котором сканировал\n*Файл будет удален через 5 минут.\nМФУ в 2520/2530',
                        reply_markup=keyboard_list_print_for_scan_2520_2530)

    keyboard_list_print_for_scan_church.add(key_print18,key_print7,key_print21, key_print4318)
    bot.send_message(call.from_user.id,
                        text='МФУ в церкви',
                        reply_markup=keyboard_list_print_for_scan_church)

    keyboard_list_print_for_scan_birz.add(key_print17,key_print431)
    bot.send_message(call.from_user.id,
                        text='МФУ на Биржевой 16/14',
                        reply_markup=keyboard_list_print_for_scan_birz)

    logs.close()

def callback_list_Print(bot,call):
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
    
    # key_back_print = types.InlineKeyboardButton(text='Back to choose', callback_data='key_back_print')


    keyboard_list_print_for_print_2520_2530.add(key_print14,key_print10,key_print9,key_print13)
    keyboard_list_print_for_print_2520_2530.add(key_print19, key_print15,key_print16,key_print22)
    #keyboard_list_print_for_print.add(key_print14, key_print15, key_print16)
    #keyboard_list_print_for_print.add(key_print10, key_print9, key_print13)  # , key_back_print)
    #        keyboard_list_print_for_scan.add(key_back_print, row_width=1)
    #return keyboard_list_print_for_print
    bot.send_message(call.from_user.id, text='Выбери принтер для печати.\nПринтеры в 2520/2530',reply_markup=keyboard_list_print_for_print_2520_2530)

    keyboard_list_print_for_print_cerkov.add(key_print18, key_print7,key_print21,key_print4318)
    bot.send_message(call.from_user.id, text='Принтеры в церкви',reply_markup=keyboard_list_print_for_print_cerkov)

    keyboard_list_print_for_print_birz.add(key_print17,key_print431)
    bot.send_message(call.from_user.id, text='Принтеры на Биржевой 16/14',reply_markup=keyboard_list_print_for_print_birz)

def callback_print_scan (bot,call,choose_printer_for_scan):
    with open('/mnt/Logs/logs.txt', 'a') as logs:
            logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - сканировал на принтере {choose_printer_for_scan} " + "\n")
    for root, dirs, files in os.walk("//mnt//Scan//"+choose_printer_for_scan):
        for f in files:
            #if f.find(choose_printer_for_scan) >= 0:
            split_tup = os.path.splitext(f)
            file_extension = split_tup[1]
            if(file_extension == ".pdf"): 
                bot.send_document(call.message.chat.id, open(root + "//" + f, 'rb'))
                os.remove(root + "//" + f)
            

def callback_print13_scan (bot,call,choose_printer_for_scan):
    with open('/mnt/Logs/logs.txt', 'a') as logs:
            logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - сканировал на принтере {choose_printer_for_scan}.metalab.ifmo.ru " + "\n")
    if call.data == "print13_scan":
        for root, dirs, files in os.walk("//mnt//Scan//"):
            for f in files:
                #if f.find("2022") >= 0:
                bot.send_document(call.message.chat.id, open(root + "//" + f, 'rb'))
                os.remove(root + "//" + f)

                
                
                
def callback_list_Print(bot,call):
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
    
    # key_back_print = types.InlineKeyboardButton(text='Back to choose', callback_data='key_back_print')


    keyboard_list_print_for_print_2520_2530.add(key_print14,key_print10,key_print9,key_print13)
    keyboard_list_print_for_print_2520_2530.add(key_print19, key_print15,key_print16,key_print22)
    #keyboard_list_print_for_print.add(key_print14, key_print15, key_print16)
    #keyboard_list_print_for_print.add(key_print10, key_print9, key_print13)  # , key_back_print)
    #        keyboard_list_print_for_scan.add(key_back_print, row_width=1)
    #return keyboard_list_print_for_print
    bot.send_message(call.from_user.id, text='Выбери принтер для печати.\nПринтеры в 2520/2530',reply_markup=keyboard_list_print_for_print_2520_2530)

    keyboard_list_print_for_print_cerkov.add(key_print18, key_print7,key_print21,key_print4318)
    bot.send_message(call.from_user.id, text='Принтеры в церкви',reply_markup=keyboard_list_print_for_print_cerkov)

    keyboard_list_print_for_print_birz.add(key_print17,key_print431)
    bot.send_message(call.from_user.id, text='Принтеры на Биржевой 16/14',reply_markup=keyboard_list_print_for_print_birz)

          
      
def cansel_buttons (bot, call):
    data = bot.current_states.get_data(call.message.chat.id, call.message.chat.id )
    if data is not None:
        file_name = data.get("file_name")
        choose_printer = data.get("choose_printer")
        pages_print = data.get("pages_print")
    else:
        file_name = None
        choose_printer = None
        pages_print = None
    if file_name is not None:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
        button_start  = types.KeyboardButton(text='/start')
        markup.add(button_start) 
        bot.send_message(call.message.chat.id, text="Отмена режима постраничной печати", reply_markup=markup)
        bot.send_message(call.message.chat.id, f"Файл: {file_name} \nПринтер: {choose_printer}", reply_markup=pre_printing())
    else:
        bot.send_message(call.message.chat.id,"ПРоизошла неизвестная ошибка, нажми на кнопку start")
      
      
      
def pre_printing():
    keyboard_print_or_addition = types.InlineKeyboardMarkup(row_width=3)
    prints = types.InlineKeyboardButton(text='Печать', callback_data='Printing')
    addition = types.InlineKeyboardButton(text='Дополнительно', callback_data='Additionally')
    keyboard_print_or_addition.add(prints, addition)

    return keyboard_print_or_addition


def callback_print(bot:telebot.TeleBot,call:telebot.types.CallbackQuery,choose_printer):
    try :
        bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "choose_printer", choose_printer)
    except:
        # bot.current_states.set_state(call.message.chat.id, call.message.chat.id, None)
        # bot.current_states.reset_data(call.message.chat.id, call.message.chat.id)
        # bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "choose_printer", choose_printer)
        bot.send_message(call.message.chat.id,"ПРоизошла неизвестная ошибка, нажми на кнопку start")

    data = bot.current_states.get_data(call.message.chat.id, call.message.chat.id )
    if data is not None:
        file_name = data.get("file_name")
    else:
        file_name = None
    
    if file_name is not None:
        #chose_printer = choose_printer
        bot.send_message(call.message.chat.id, f"Файл: {file_name} \nВыбран принтер {choose_printer}. \nФормат файла А4(по умолчанию)",  reply_markup=pre_printing())
        #print(f"Пользователь {str(call.from_user.first_name)} выбрал принтер {chose_printer}")
    else:
        #chose_printer = choose_printer
        #print(f"Пользователь {str(call.from_user.first_name)} выбрал принтер {chose_printer}")
        bot.send_message(call.message.chat.id, f"Выбран принтер {choose_printer}. \nЗагрузи файл который нужно распечатать: \nФормат файла А4(по умолчанию)")
    with open('/mnt/Logs/logs.txt', 'a') as logs:
        logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - выбрал {choose_printer}  " + "\n")
    logs.close()


def callback_additional(bot,call):
    with open('/mnt/Logs/logs.txt', 'a') as logs:
        logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - выбирает дополнительные функции.  " + "\n")
    #print("Additional")
    keyboard_additional = types.InlineKeyboardMarkup(row_width=6)
    count_copies = types.InlineKeyboardButton(text='Количество копий', callback_data='count_Copies')
    duplex_print = types.InlineKeyboardButton(text='Двухсторонняя печать', callback_data='duplex_print')
    pages = types.InlineKeyboardButton(text='Страницы', callback_data='pages')

    data = bot.current_states.get_data(call.message.chat.id, call.message.chat.id )
    if data is not None:
        choose_printer = data.get("choose_printer")
    else:
        choose_printer = None    

    #if UploadTG.file_extension in  [".jpg", ".png", ".jpeg"]:
    if choose_printer=="print13.metalab.ifmo.ru":
        keyboard_additional = types.InlineKeyboardMarkup(row_width=6)
        a3_print = types.InlineKeyboardButton(text='A3', callback_data='a3_print')
        a5_print = types.InlineKeyboardButton(text='A5', callback_data='a5_print')
        a4_print = types.InlineKeyboardButton(text='A4', callback_data='a4_print')
        keyboard_additional.add(a3_print, a5_print, a4_print)
    else:    
        keyboard_additional = types.InlineKeyboardMarkup(row_width=5)
        a5_print = types.InlineKeyboardButton(text='A5', callback_data='a5_print')
        a4_print = types.InlineKeyboardButton(text='A4', callback_data='a4_print')
        keyboard_additional.add(a5_print, a4_print)
        

    keyboard_additional.add(count_copies, duplex_print, pages)
    bot.send_message(call.from_user.id, text='Выбери дополнительные функции: ',reply_markup=keyboard_additional)
    logs.close()


def callback_pages(bot:telebot.TeleBot,call:telebot.types.CallbackQuery,pagess):
    try :
        bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "pagess", pagess)
    except:
        # bot.current_states.set_state(call.message.chat.id, call.message.chat.id, None)
        # bot.current_states.reset_data(call.message.chat.id, call.message.chat.id)
        # bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "choose_printer", choose_printer)
        bot.send_message(call.message.chat.id,"ПРоизошла неизвестная ошибка, нажми на кнопку start")
    
    data = bot.current_states.get_data(call.message.chat.id,call.message.chat.id )
    if data is not None:
        file_name = data.get("file_name")
        choose_printer = data.get("choose_printer")
        pages_print = data.get("pages_print")
        pagess= data.get("pages_print")
    else:
        file_name = None
        choose_printer = None
        pages_print = None
        pagess = None
    #global printing, count_copies, duplex_print, pages_print,full_text,size_paper, userTG, current_datetime
    
    with open('/mnt/Logs/logs.txt', 'a') as logs:
        logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - выбирает страницы для печати\n")
    print(pages_print)
    
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    cansel_buuton = types.KeyboardButton(text='/cansel')
    markup.add(cansel_buuton) 
    #bot.send_message(message.chat.id, text='Привет, '+str(message.from_user.first_name), reply_markup=markup)
    #bot.send_message(call.message.chat.id, "с-по, пример 1,3-5,16\nДля отмены нажми на кнопку cansel", reply_markup=markup)
    keyboard_cancel = types.InlineKeyboardMarkup(row_width=1)
    cancel = types.InlineKeyboardButton(text='Cancel', callback_data='cancel')
    keyboard_cancel.add(cancel)
    bot.send_message(call.message.chat.id, "с-по, пример 1,3-5,16\nДля отмены нажми на кнопку cancel", reply_markup=keyboard_cancel)

def callback_duplex_print(bot,call):
    try :
        duplex_print=" -o sides=two-sided-long-edge"
        bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "duplex_print", duplex_print)
        #bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "choose_printer", choose_printer)        
    except:
        bot.send_message(call.message.chat.id,"ПРоизошла неизвестная ошибка, нажми на кнопку start")    


    data = bot.current_states.get_data(call.message.chat.id, call.message.chat.id )

    if data is not None:
        file_name = data.get("file_name")
        choose_printer = data.get("choose_printer")
        full_text = data.get("full_text")
    else:
        file_name = None 
        choose_printer = None  
        full_text = None        
        
    with open('/mnt/Logs/logs.txt', 'a') as logs:
        logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - включил режим  двухсторонней печати." + "\n")
    full_text = f"Файл: {file_name} \nПринтер: {choose_printer} \nВключен режим двухсторонней печати"

    bot.send_message(call.message.chat.id, full_text , reply_markup=pre_printing())
      
def callback_count_copies(bot,call):
    global printing, userTG, current_datetime
    with open('/mnt/Logs/logs.txt', 'a') as logs:
        logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - Выбирает количество копий \n")
    printing = ""
    keyboard_count_Copies = types.InlineKeyboardMarkup(row_width=3)
    count_one = types.InlineKeyboardButton(text='1', callback_data='count_one')
    count_two = types.InlineKeyboardButton(text='2', callback_data='count_two')
    count_three = types.InlineKeyboardButton(text='3', callback_data='count_three')
    count_four = types.InlineKeyboardButton(text='4', callback_data='count_four')
    count_copies_n = types.InlineKeyboardButton(text='n', callback_data='count_copies_n')
    keyboard_count_Copies.add(count_one, count_two, count_three,count_four,count_copies_n)
    bot.send_message(call.from_user.id, text='Сколько копий?',
                        reply_markup=keyboard_count_Copies)
    logs.close()

def callback_count_one(bot,call):
    try :
        count_copies = " -n 1"
        bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "count_copies", count_copies)
        #bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "choose_printer", choose_printer)        
    except:
        bot.send_message(call.message.chat.id,"ПРоизошла неизвестная ошибка, нажми на кнопку start")

    data = bot.current_states.get_data(call.message.chat.id, call.message.chat.id )

    if data is not None:
        file_name = data.get("file_name")
        choose_printer = data.get("choose_printer")
        full_text = data.get("full_text")
        count_copies = data.get("count_copies")
    else:
        file_name = None 
        choose_printer = None  
        full_text = None    
        count_copies = None

    with open('/mnt/Logs/logs.txt', 'a') as logs:
         logs.write(  f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - Выбирает количество копий 2 \n")

    
    count_copies = " -n 1"
    full_text = f"Файл: {file_name} \nПринтер: {choose_printer} \nКоличество копий: 1 "
    bot.send_message(call.message.chat.id, full_text , reply_markup=pre_printing())

def callback_count_two(bot,call):
    try :
        count_copies = " -n 2"
        bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "count_copies", count_copies)
        #bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "choose_printer", choose_printer)        
    except:
        bot.send_message(call.message.chat.id,"ПРоизошла неизвестная ошибка, нажми на кнопку start")

    data = bot.current_states.get_data(call.message.chat.id, call.message.chat.id )

    if data is not None:
        file_name = data.get("file_name")
        choose_printer = data.get("choose_printer")
        full_text = data.get("full_text")
        count_copies = data.get("count_copies")
    else:
        file_name = None 
        choose_printer = None  
        full_text = None    
        count_copies = None

    with open('/mnt/Logs/logs.txt', 'a') as logs:
         logs.write(  f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - Выбирает количество копий 2 \n")

    
    
    full_text = f"Файл: {file_name} \nПринтер: {choose_printer} \nКоличество копий: 2 "
    bot.send_message(call.message.chat.id, full_text , reply_markup=pre_printing())

def callback_count_three(bot,call):
    try :
        count_copies=" -n 3"
        bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "count_copies", count_copies)
        #bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "choose_printer", choose_printer)        
    except:
        bot.send_message(call.message.chat.id,"ПРоизошла неизвестная ошибка, нажми на кнопку start")

    data = bot.current_states.get_data(call.message.chat.id, call.message.chat.id )

    if data is not None:
        file_name = data.get("file_name")
        choose_printer = data.get("choose_printer")
        full_text = data.get("full_text")
        count_copies = data.get("count_copies")
    else:
        file_name = None 
        choose_printer = None  
        full_text = None    
        count_copies = None

    with open('/mnt/Logs/logs.txt', 'a') as logs:
         logs.write(  f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - Выбирает количество копий 3 \n")

    full_text = f"Файл: {file_name} \nПринтер: {choose_printer} \nКоличество копий: 3 "
    bot.send_message(call.message.chat.id, full_text , reply_markup=pre_printing())

def callback_count_four(bot,call):
    try :
        count_copies=" -n 4"
        bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "count_copies", count_copies)
        #bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "choose_printer", choose_printer)        
    except:
        bot.send_message(call.message.chat.id,"ПРоизошла неизвестная ошибка, нажми на кнопку start")

    data = bot.current_states.get_data(call.message.chat.id, call.message.chat.id )

    if data is not None:
        file_name = data.get("file_name")
        choose_printer = data.get("choose_printer")
        full_text = data.get("full_text")
        count_copies = data.get("count_copies")
    else:
        file_name = None 
        choose_printer = None  
        full_text = None    
        count_copies = None

    with open('/mnt/Logs/logs.txt', 'a') as logs:
         logs.write(  f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - Выбирает количество копий 4 \n")

    full_text = f"Файл: {file_name} \nПринтер: {choose_printer} \nКоличество копий: 4 "
    bot.send_message(call.message.chat.id, full_text , reply_markup=pre_printing())


def count_copies_n (bot,message):    
    try:
        copies =message.text
        #count_copies = count_n
        bot.current_states.set_data(message.chat.id, message.chat.id, "copies", copies)
        #pass
    except:
         bot.send_message(message.chat.id,"ПРоизошла неизвестная ошибка, нажми на кнопку start")
    
    data = bot.current_states.get_data(message.chat.id, message.chat.id )

    if data is not None:
        file_name = data.get("file_name")
        choose_printer = data.get("choose_printer")
        full_text = data.get("full_text")
        copies = data.get("copies")
    else:
        file_name = None 
        choose_printer = None  
        full_text = None    
        copies = None

    count_copies = copies
    #with open('/mnt/Logs/logs.txt', 'a') as logs:
    #    logs.write(  f"{str(return_time())} - Пользователь: {str(from_user.first_name)} - Выбирает количество копий {count_copies} \n")

    full_text = f"Файл: {file_name} \nПринтер: {choose_printer} \nКоличество копий: {count_copies} "
    bot.send_message(message.chat.id, full_text , reply_markup=pre_printing())


def counts (bot,call, copies):
    try :
        bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "copies", copies)
    except:
    # bot.current_states.set_state(call.message.chat.id, call.message.chat.id, None)
    # bot.current_states.reset_data(call.message.chat.id, call.message.chat.id)
    # bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "choose_printer", choose_printer)
        bot.send_message(call.message.chat.id,"ПРоизошла неизвестная ошибка, нажми на кнопку start")
    
    data = bot.current_states.get_data(call.message.chat.id,call.message.chat.id )
    if data is not None:
        file_name = data.get("file_name")
        choose_printer = data.get("choose_printer")
        pages_print = data.get("pages_print")
        count_copies = data.get("count_copies")
        copies =  data.get("copies")
    else:
        file_name = None
        choose_printer = None
        pages_print = None
        count_copies = None
        copies = None
    #global printing, count_copies, duplex_print, pages_print,full_text,size_paper, userTG, current_datetime
    
    # with open('/mnt/Logs/logs.txt', 'a') as logs:
    #     logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - выбирает страницы для печати\n")
    print(pages_print)

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    cansel_buuton = types.KeyboardButton(text='/cansel')
    markup.add(cansel_buuton) 
    #bot.send_message(message.chat.id, text='Привет, '+str(message.from_user.first_name), reply_markup=markup)
    #bot.send_message(call.message.chat.id, "с-по, пример 1,3-5,16\nДля отмены нажми на кнопку cansel", reply_markup=markup)
    keyboard_cancel = types.InlineKeyboardMarkup(row_width=1)
    cancel = types.InlineKeyboardButton(text='Cancel', callback_data='cancel')
    keyboard_cancel.add(cancel)
    bot.send_message(call.message.chat.id, "Введи необходимое количество копий!\nВводить нужно толькл цифры!!!", reply_markup=keyboard_cancel)



def Pages_to_print(bot,message):
    try :
        pagess =message.text
        pagesz = "p"+pages_print
        bot.current_states.set_data(message.chat.id, message.chat.id, "pagess", pagess)
        #bot.current_states.set_data(message.chat.id, message.chat.id, "pagess", pagess)
        
        #bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "choose_printer", choose_printer)        
    except:
        bot.send_message(message.chat.id,"ПРоизошла неизвестная ошибка, нажми на кнопку start")

    data = bot.current_states.get_data(message.chat.id, message.chat.id )

    if data is not None:
        file_name = data.get("file_name")
        choose_printer = data.get("choose_printer")
        pagess =  data.get("pagess")
    else:
        file_name = None 
        choose_printer - None
        pagess = None

    try:
        if file_name =="":
            bot.send_message(message.chat.id, "Я поламался :-(.\nНажми на кнопку START ")
        else:
            full_path_file_name = "/mnt/File/"+file_name
            with open(full_path_file_name, 'rb') as f:
                pdf = PdfFileReader(f)
                information = pdf.getDocumentInfo()
                number_of_pages = pdf.getNumPages()

            txt = number_of_pages
            tab = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
            counts = pages_print.replace('p', '')
            res = counts.translate(tab).split()
            count_pages = counts
            max_page = max(res)
            with open('/mnt/Logs/logs.txt', 'a') as logs:
                logs.write( f"{str(return_time())} - Пользователь: {str(message.from_user.first_name)} - печатает {txt} страниц/ы \n")
            #pages_print = f" -o page-ranges={pages_print} "
            #str_page_print = 
            #print(str(len( res)))
            pagess = None
            if int(max_page) >int(txt):
                bot.send_message(message.chat.id, "Введенное количество страниц не соответствует количеству стрниц которое в документе!\nКоличество страниц в документе = "+str(txt)+" страниц"+"\nВведи правильное количество страниц. Пример 1,3-5,16",reply_markup=pre_printing()) 
            else: 
                bot.send_message(message.chat.id, f"Выбран: {choose_printer} \nВыбранные страницы: {counts}", reply_markup=pre_printing()) 
            
            # for x in res:
            #     if int(x) > int(txt):
                        
                        
            #     if int(x) < int(txt):
            #         #bot.send_message(message.chat.id, f"Выбран: {choose_printer} \nВыбранные страницы: {counts}", reply_markup=pre_printing()) 
            #         #continue
            #         break
            
                        
    except Exception as ex:
        print(ex)
        bot.send_message(message.chat.id, "В файле отсутствуют страницы.", reply_markup=pre_printing()) 



def callback_size_papes_a3(bot,call):
    try :
        size_paper = " -o media=A3"
        bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "size_paper", size_paper)
        #bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "choose_printer", choose_printer)        
    except:
        bot.send_message(call.message.chat.id,"ПРоизошла неизвестная ошибка, нажми на кнопку start")

    data = bot.current_states.get_data(call.message.chat.id, call.message.chat.id )

    if data is not None:
        file_name = data.get("file_name")
        choose_printer = data.get("choose_printer")
        full_text = data.get("full_text")
        count_copies = data.get("count_copies")
    else:
        file_name = None 
        choose_printer = None  
        full_text = None    
        count_copies = None

    with open('/mnt/Logs/logs.txt', 'a') as logs:
        logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - Выбирал формат файла А3 \n")

    full_text = f"Файл: {file_name} \nПринтер: {choose_printer} \nКоличество копий: {count_copies} \nФормат бумаги А3"

    bot.send_message(call.message.chat.id, full_text, reply_markup=pre_printing())


def callback_size_papes_a4(bot,call):
    try :
        size_paper = " -o media=A4"
        bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "size_paper", size_paper)
        #bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "choose_printer", choose_printer)        
    except:
        bot.send_message(call.message.chat.id,"ПРоизошла неизвестная ошибка, нажми на кнопку start")

    data = bot.current_states.get_data(call.message.chat.id, call.message.chat.id )

    if data is not None:
        file_name = data.get("file_name")
        choose_printer = data.get("choose_printer")
        full_text = data.get("full_text")
        count_copies = data.get("count_copies")
    else:
        file_name = None 
        choose_printer = None  
        full_text = None    
        count_copies = None

    with open('/mnt/Logs/logs.txt', 'a') as logs:
        logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - Выбирал формат файла А4 \n")

    full_text = f"Файл: {file_name} \nПринтер: {choose_printer} \nКоличество копий: {count_copies} \nФормат бумаги А4"

    bot.send_message(call.message.chat.id, full_text, reply_markup=pre_printing())


def callback_size_papes_a5(bot,call):
    try :
        size_paper = " -o media=A5"
        bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "size_paper", size_paper)
        #bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "choose_printer", choose_printer)        
    except:
        bot.send_message(call.message.chat.id,"ПРоизошла неизвестная ошибка, нажми на кнопку start")

    data = bot.current_states.get_data(call.message.chat.id, call.message.chat.id )

    if data is not None:
        file_name = data.get("file_name")
        choose_printer = data.get("choose_printer")
        full_text = data.get("full_text")
        count_copies = data.get("count_copies")
    else:
        file_name = None 
        choose_printer = None  
        full_text = None    
        count_copies = None

    with open('/mnt/Logs/logs.txt', 'a') as logs:
        logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - Выбирал формат файла А5 \n")

    full_text = f"Файл: {file_name} \nПринтер: {choose_printer} \nКоличество копий: {count_copies} \nФормат бумаги А5"

    bot.send_message(call.message.chat.id, full_text, reply_markup=pre_printing())



def callback_printing(bot:telebot.TeleBot,call):     
    data = bot.current_states.get_data(call.message.chat.id, call.message.chat.id )
    if data is not None:
        file_name = data.get("file_name")
        choose_printer = data.get ("choose_printer")
        duplex_print = data.get("duplex_print")
        count_copies = data.get("count_copies")
        pages_print = data.get ("pages_print")
        size_paper = data.get ("size_paper")
        pagess = data.get ("pagess")

    else:
        file_name = None
        choose_printer = None
        duplex_print = None
        count_copies= None
        pages_print = None
        size_paper = None
        pagess = None
    
    count_copies = pagess.replace('n', '') 
    with open('/mnt/Logs/logs.txt', 'a') as logs:
        logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - отправил на печеть файл: {format(str(file_name))} На принтер {choose_printer} \n")

    if file_name == None:
        bot.send_message(call.message.chat.id,f"Зафиксировано повторное нажатие. \nНажми на кнопку START")       
    else:
        bot.send_message(call.message.chat.id,f"Идет печать файла: {format(str(file_name))} \nНа принтере: {choose_printer}\n")
        if pages_print==None:
            pages_print =""
        else: 
            pages_print=f" -o page-ranges={pages_print}"
        
        if duplex_print==None:
            duplex_print=""
        if count_copies == None:
            count_copies= ""    
        if size_paper==None:
            size_paper=""
            printing =  f"lp -d {choose_printer} /mnt/File/{file_name} -o media=A4 {duplex_print} {count_copies} {pages_print} {size_paper}"

        else: printing =  f"lp -d {choose_printer} /mnt/File/{file_name} {size_paper} {duplex_print} {count_copies} {pages_print}"
        
        print(printing)
        os.system(printing)
        bot.current_states.set_state(call.message.chat.id, call.message.chat.id, None)
        bot.current_states.reset_data(call.message.chat.id, call.message.chat.id)


def callback_question (bot, call, count_pages):
    global file_name
    keyboard_list_print_for_print = types.InlineKeyboardMarkup(row_width=3)
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='call_yes')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='call_no')
    keyboard_list_print_for_print.add(key_yes, key_no)
    bot.send_message(call.from_user.id, f'В файле {file_name} - {count_pages} страниц\ы.\nОтправить на печать ? ',reply_markup=keyboard_list_print_for_print)

def call_yes(bot,call):
    global file_name,chose_printer,printing, count_copies, duplex_print, pages_print,full_text,size_paper, userTG, current_datetime, count_pages
    with open('/mnt/Logs/logs.txt', 'a') as logs:
            logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - отправил на печеть файл: {format(str(file_name))}\nНа принтер {chose_printer} ")
    bot.send_message(call.message.chat.id,f"Идет печать файла: {format(str(file_name))} \nНа принтере: {chose_printer}\n")
    if printing=="":
        printing = f"lp -d {chose_printer} /mnt/File/{file_name} -o media=A4 "
        printZ(printing)
        #os.system(printing)
        print(printing)
    else:
        print(printing)
        logs.close()
        printZ(printing)
        #os.system(printing)
        file_name = ""
        chose_printer = ""
        printing = ""
        duplex_print = ""
        pages_print = ""
        count_copies=""
        size_paper= ""
        userTG = ""  

def call_no(bot,call):
    global file_name,chose_printer,printing, count_copies, duplex_print, pages_print,full_text,size_paper, userTG, current_datetime, count_pages
    file_name = ""
    chose_printer = ""
    printing = ""
    duplex_print = ""
    pages_print = ""
    count_copies=""
    size_paper= ""
    userTG = ""
    bot.send_message(call.message.chat.id, text='Нажми на кнопку START')

def printZ (printing):
    print(printing)
    #os.system(printing)