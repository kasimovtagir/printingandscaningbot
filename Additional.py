
import CallBackTG
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

def Button_Additional(bot,call):
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

def Button_Duplex_Print(bot,call):
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

    bot.send_message(call.message.chat.id, full_text , reply_markup=CallBackTG.pre_printing())
      
def Button_Choose_Count_Copies(bot,call):
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


def Button_Count_Copies(bot,call, counts):
    try :
        count_copies = f" -n {counts}"
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
         logs.write(  f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - Выбирает количество копий {counts} \n")

    print(count_copies)
    count_copies = f" -n {counts}"
    full_text = f"Файл: {file_name} \nПринтер: {choose_printer} \nКоличество копий: {counts} "
    bot.send_message(call.message.chat.id, full_text , reply_markup=CallBackTG.pre_printing())    


def button_N_Copies(bot, call ):
    try :
        count_copies = "n "
        bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "count_copies", count_copies)
        #bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "choose_printer", choose_printer)        
    except:
        bot.send_message(call.message.chat.id,"ПРоизошла неизвестная ошибка, нажми на кнопку start")
    count_copies = "n "
    with open('logs.txt', 'a') as logs:
        logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - выбирает страницы для печати\n")    
    
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    cansel_buuton = types.KeyboardButton(text='/cansel')
    markup.add(cansel_buuton) 
    keyboard_cancel = types.InlineKeyboardMarkup(row_width=1)
    cancel = types.InlineKeyboardButton(text='Cancel', callback_data='cancel')
    keyboard_cancel.add(cancel)
    bot.send_message(call.message.chat.id, "Введите необходимое количество копий.\nДля отмены нажми на кнопку cancel", reply_markup=keyboard_cancel)


def Button_Count_Copies_N (bot,message):    
    copies =message.text
    count_copies = f" -n {copies}"
    try:
        bot.current_states.set_data(message.chat.id, message.chat.id, "count_copies", count_copies)
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

    
    #with open('/mnt/Logs/logs.txt', 'a') as logs:
    #    logs.write(  f"{str(return_time())} - Пользователь: {str(from_user.first_name)} - Выбирает количество копий {count_copies} \n")
    countss = count_copies.replace("-n","")
    full_text = f"Файл: {file_name} \nПринтер: {choose_printer} \nКоличество копий: {countss} "
    count_copies = f" -n {copies}"
    bot.send_message(message.chat.id, full_text , reply_markup=CallBackTG.pre_printing())
    

def Button_Size_Papes(bot,call,size):
    try :
        size_paper = f" -o media=A{size}"
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
        logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - Выбирал формат файла А{size} \n")

    full_text = f"Файл: {file_name} \nПринтер: {choose_printer} \nКоличество копий: {count_copies} \nФормат бумаги А{size}"

    bot.send_message(call.message.chat.id, full_text, reply_markup=CallBackTG.pre_printing())


def Button_Choose_print_Pages(bot,call):
    try :
        pagess="p"
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
    pagess = "p"
    with open('/mnt/Logs/logs.txt', 'a') as logs:
        logs.write( f"{str(return_time())} - Пользователь: {str(call.from_user.first_name)} - выбирает страницы для печати\n")
    print(pagess)
    
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    cansel_buuton = types.KeyboardButton(text='/cansel')
    markup.add(cansel_buuton) 
    #bot.send_message(message.chat.id, text='Привет, '+str(message.from_user.first_name), reply_markup=markup)
    #bot.send_message(call.message.chat.id, "с-по, пример 1,3-5,16\nДля отмены нажми на кнопку cansel", reply_markup=markup)
    keyboard_cancel = types.InlineKeyboardMarkup(row_width=1)
    cancel = types.InlineKeyboardButton(text='Cancel', callback_data='cancel')
    keyboard_cancel.add(cancel)
    bot.send_message(call.message.chat.id, "с-по, пример 1,3-5,16\nДля отмены нажми на кнопку cancel", reply_markup=keyboard_cancel)
    # pagess = ""
    # bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "pagess", pagess)


def Pages_Print(bot,message):
    try :
        pages_print =message.text
        bot.current_states.set_data(message.chat.id, message.chat.id, "pages_print", pages_print)
        #bot.current_states.set_data(call.message.chat.id, call.message.chat.id, "choose_printer", choose_printer)        
    except:
        bot.send_message(message.chat.id,"ПРоизошла неизвестная ошибка, нажми на кнопку start")

    data = bot.current_states.get_data(message.chat.id, message.chat.id )

    if data is not None:
        file_name = data.get("file_name")
        choose_printer = data.get("choose_printer")
        pages_print = data.get("pages_print")
        pagess = data.get("pagess")
    else:
        file_name = None 
        choose_printer = None
        pages_print = None
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
                bot.send_message(message.chat.id, "Введенное количество страниц не соответствует количеству стрниц которое в документе!\nКоличество страниц в документе = "+str(txt)+" страниц"+"\nВведи правильное количество страниц. Пример 1,3-5,16",reply_markup=CallBackTG.pre_printing()) 
            else: 
                bot.send_message(message.chat.id, f"Выбран: {choose_printer} \nВыбранные страницы: {counts}", reply_markup=CallBackTG.pre_printing()) 
            
            # for x in res:
            #     if int(x) > int(txt):
                        
                        
            #     if int(x) < int(txt):
            #         #bot.send_message(message.chat.id, f"Выбран: {choose_printer} \nВыбранные страницы: {counts}", reply_markup=pre_printing()) 
            #         #continue
            #         break
            
                        
    except Exception as ex:
        print(ex)
        bot.send_message(message.chat.id, "В файле отсутствуют страницы.", reply_markup=CallBackTG.pre_printing()) 

