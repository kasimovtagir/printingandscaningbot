from cgitb import text
from email import message
from platform import python_branch
import requests
from hashlib import sha1
import telebot
from telebot import types
from PyPDF2 import PdfFileReader
import re
import time
from datetime import datetime
import os
import os.path, time
import string
import subprocess
#from PIL import Imagex  
import user
from user import  NoTidError, BadRoleError, ServerError
from requests.exceptions import Timeout

import CallBackTG
import UploadTG
import Printing
import Scanning
# import list_printer
# import list_scaner
import Additional

#os.system ("service cups restart")

def return_time():
    dt = datetime.now()
    dt_string = dt.strftime("%d.%m %H:%M")
    return dt_string

  
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup #States

from telebot.storage import StateMemoryStorage

state_storage = StateMemoryStorage() 




ADMINS = os.environ["ADMINS"]

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

RESTAPI_ACCESS_TOKEN = os.environ["REST_API_TOKEN"]

USER_API = user.UserAPI(token=RESTAPI_ACCESS_TOKEN)


bot  = telebot.TeleBot(BOT_TOKEN,state_storage=state_storage)



@bot.message_handler(func=lambda message: not filter_Tg( bot, message.chat.id ))
def Send_instruction(message):
   bot.send_document(message.chat.id ,open("instruction.jpg", 'rb'))

    
@bot.message_handler(content_types=["photo"]) 
def sends_photo(message):
     bot.send_message(message.chat.id, "Файл нужно отправить без сжатия.")

@bot.message_handler(commands=['start'])
def start_message(message):
    CallBackTG.callback_start(bot, message)

#Доступ через сайт      
def filter_Tg(bot, tg_id):
    print(tg_id)
    try:
        try:
            user = USER_API.get_user_by_tid(tg_id)
            #print (user.roles)
            return True
        except (Timeout, ServerError) as e:
            bot.send_message(tg_id, f"1.Чтобы получить доступ к телеграм боту вам необходимо добавить ваш TG ID в личный кабинет на сайте physics.itmo.ru.\nВаш TG ID - {tg_id}\n")
            #print(e)
        except (BadRoleError, NoTidError) as e:
            bot.send_message(tg_id, f"2.Чтобы получить доступ к телеграм боту вам необходимо добавить ваш TG ID в личный кабинет на сайте physics.itmo.ru.\nВаш TG ID - {tg_id}\n")
            #print(e)
        except Exception as e:
            bot.send_message(tg_id, f"3.Чтобы получить доступ к телеграм боту вам необходимо добавить ваш TG ID в личный кабинет на сайте physics.itmo.ru.\nВаш TG ID - {tg_id}\n")
            #print(e)
        return False 
    except :
         bot.send_message(tg_id,f"4.Чтобы получить доступ к телеграм боту вам необходимо добавить ваш TG ID в личный кабинет на сайте physics.itmo.ru.\nВаш TG ID - {tg_id}\n")

#Загрузка файлов      
@bot.message_handler(content_types=['document'])
def documents(message):
    UploadTG.Upload_files(bot,message)            
      
#
@bot.callback_query_handler(func=lambda call: True)
def Actions (call):
#-------------------------------------------------------------------------------------
   
    #show list scaner
    if call.data== "list_Scan":
        CallBackTG.callback_list_Print_for_scan(bot,call)

    if call.data== "print21_scan":
        CallBackTG.callback_print_scan(bot,call, "print21")

    if call.data == "print4318_scan":
        CallBackTG.callback_print(bot,call, "print4318")         

    if call.data== "print17_scan":
        CallBackTG.callback_print_scan(bot,call, "print17")

    if call.data== "print431_scan":
        CallBackTG.callback_print_scan(bot,call, "print431")             

    if call.data== "print7_scan":
        CallBackTG.callback_print_scan(bot,call, "print7")
 
    if call.data== "print18_scan":
        bot.send_message(message.chat.id, text='В разработке.')

    if call.data== "print19_scan":
        CallBackTG.callback_print_scan(bot,call, "print19")

    if call.data== "print14_scan":
        bot.send_message(message.chat.id, text='В разработке.')

    if call.data== "print15_scan":
        CallBackTG.callback_print_scan(bot,call, "print15")

    if call.data== "print16_scan":
        CallBackTG.callback_print_scan(bot,call, "print16")

    if call.data== "print10_scan":
        CallBackTG.callback_print_scan(bot,call, "print10")

    if call.data== "print9_scan":
        CallBackTG.callback_print_scan(bot,call, "print9")
        
    if call.data== "print22_scan":
        CallBackTG.callback_print_scan(bot,call, "print22")        

    if call.data== "print13_scan":
        CallBackTG.callback_print_scan(bot,call, "print13")
#-------------------------------------------------------------------------------------
    
    #show list printers
    if call.data == "list_Print":
        Printing.List_Print(bot, call)

    #action with printers
    if call.data == "print22_print":
        Printing.Show_Information(bot,call, "print22.metalab.ifmo.ru")

    if call.data == "print19_print":
        Printing.Show_Information(bot,call, "print19.metalab.ifmo.ru")

    if call.data == "print10_print":
        Printing.Show_Information(bot,call, "print10.metalab.ifmo.ru")

    if call.data == "print13_print":
        Printing.Show_Information(bot,call, "print13.metalab.ifmo.ru")

    if call.data == "print9_print":
        Printing.Show_Information(bot,call, "print9.metalab.ifmo.ru")

    if call.data == "print14_print":
        Printing.Show_Information(bot,call, "print14.metalab.ifmo.ru")
                
    if call.data == "print15_print":
        Printing.Show_Information(bot,call, "print15.metalab.ifmo.ru")

    if call.data == "print16_print":
        Printing.Show_Information(bot,call, "print16.metalab.ifmo.ru")

    if call.data == "print18_print":
         Printing.Show_Information(bot,call, "print18.metalab.ifmo.ru")

    if call.data == "print7_print":
        Printing.Show_Information(bot,call, "print7.metalab.ifmo.ru")     

    if call.data == "print21_print":
        Printing.Show_Information(bot,call, "print21.metalab.ifmo.ru") 
        
    if call.data == "print4318_print":
        Printing.Show_Information(bot,call, "print4318.metalab.ifmo.ru")         

    if call.data == "print17_print":
        Printing.Show_Information(bot,call, "print17.metalab.ifmo.ru") 
    
    if call.data == "print431_print":
        Printing.Show_Information(bot,call, "print431.metalab.ifmo.ru")
#-------------------------------------------------------------------------------------

    #show access additionals 
    if call.data == "Additionally":
        Additional.Button_Additional(bot,call)

    if call.data == "duplex_print" :
        Additional.Button_Duplex_Print(bot,call)

    if call.data == "count_Copies" :
        Additional.Button_Choose_Count_Copies(bot, call)  

    if call.data == "count_one":
        Additional.Button_Count_Copies(bot,call,"1")

    if call.data == "count_two":
        Additional.Button_Count_Copies(bot,call,"2")

    if call.data == "count_three":
        Additional.Button_Count_Copies(bot,call,"3")

    if call.data == "count_four":
        Additional.Button_Count_Copies(bot,call,"4")  
    
    if call.data == "count_copies_n":  
        Additional.button_N_Copies(bot,call)


    if call.data == "pages" :
        Additional.Button_Choose_print_Pages(bot,call)



    if call.data == "a3_print":
        Additional.Button_Size_Papes(bot,call,"3")

    if call.data == "a4_print":
        Additional.Button_Size_Papes(bot,call,"4")

    if call.data == "a5_print":
        Additional.Button_Size_Papes(bot,call,"5")

    if call.data == "cancel":
        CallBackTG.cansel_buttons(bot, call)

    if call.data == "call_yes":
        CallBackTG.call_yes(bot, call)

    if call.data == "call_no":
        CallBackTG.call_no(bot, call)      




#-----------------------------------------------------------START PRINTING--------------------------------
    if call.data=="Printing":
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
            #os.system(printing)
            bot.current_states.set_state(call.message.chat.id, call.message.chat.id, None)
            bot.current_states.reset_data(call.message.chat.id, call.message.chat.id)

      
          
@bot.message_handler(content_types=['text'])
def repeat_all_message(message):
    data = bot.current_states.get_data(message.chat.id, message.chat.id )

    if data is not None:
        file_name = data.get("file_name")
        choose_printer = data.get("choose_printer")
        pagess =  data.get("pagess")
        count_copies = data.get("count_copies")

    else:
        file_name = None 
        choose_printer - None
        pagess = None
        count_copies = None

    print (count_copies)
    print(pagess)
    if pagess is not None:
        print("печать страниц")
        Additional.Pages_Print(bot, message)
        try :
            pagess = None
            bot.current_states.set_data(message.chat.id, message.chat.id, "pagess", pagess)
        except:
            bot.send_message(message.chat.id,"ПРоизошла неизвестная ошибка, нажми на кнопку start")

        print(pagess)
    else:
        print("Произошла ошибка") 
            
    if count_copies is not None:
        print("печать количества страниц")
        Additional.Button_Count_Copies_N(bot, message)
        print(count_copies)
    else:
        print("Произошла ошибка") 

          

try:
    bot.polling(none_stop=True, interval=0)
except Exception as ex:  
    print (ex)
    os.system("python3 Main.py")